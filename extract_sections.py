#!/usr/bin/env python3
"""Extract each template section from the rendered index.html and save as raw HTML blocks."""

import re
import json
import os

html_path = "/tmp/hyper-theme/pages/index.html"
output_dir = "/tmp/hyper-theme/sections_raw"

os.makedirs(output_dir, exist_ok=True)

with open(html_path, "r") as f:
    html = f.read()

# Find all section boundaries
# Pattern: <section id="shopify-section-template--...__TYPE_HASH" or <div id="shopify-section-template--...__TYPE_HASH"
pattern = r'(<(?:section|div)\s+id="shopify-section-template--[^"]*?__(\w+)_[a-zA-Z0-9]+)"[^>]*>'

matches = list(re.finditer(pattern, html))
print(f"Found {len(matches)} section openings")

sections = []
for i, m in enumerate(matches):
    full_open_tag = m.group(0)
    section_type = m.group(2)
    section_id_match = re.search(r'id="(shopify-section-[^"]+)"', full_open_tag)
    section_id = section_id_match.group(1) if section_id_match else f"unknown_{i}"
    
    # Find the full section - from this match to the next matching closing tag
    start = m.start()
    # Look for corresponding </section> or </div> at same nesting level
    tag_name = 'section' if m.group(0).startswith('<section') else 'div'
    
    # Find the next section start
    if i + 1 < len(matches):
        end = matches[i + 1].start()
    else:
        # Last section - find footer or end
        end = len(html)
    
    # Extract the section block, trim whitespace
    raw_html = html[start:end].strip()
    
    # Clean up: remove closing tags that belong to previous section
    # The raw HTML may start with </section> or </div> from previous section
    if raw_html.startswith('</'):
        closing_end = raw_html.find('>') + 1
        raw_html = raw_html[closing_end:].strip()
    
    sections.append({
        'type': section_type,
        'id': section_id,
        'start': start,
        'end': end,
        'tag': tag_name,
        'raw': raw_html
    })
    print(f"  {i}: type={section_type}, id={section_id}, start={start}, end={end}, len={len(raw_html)}")

# Load the template JSON to map order to type
with open("/tmp/hyper-theme/templates/index.json") as f:
    template = json.load(f)

# Build a map: order_number -> section_type
order_sections = {}
for key, val in template["sections"].items():
    order_sections[key] = val["type"]

# Map section types to HTML blocks
type_to_html = {}
for s in sections:
    t = s['type']
    if t not in type_to_html:
        type_to_html[t] = []
    type_to_html[t].append(s)

# Print what we have
print("\n--- Section types found ---")
for t, blocks in type_to_html.items():
    print(f"  {t}: {len(blocks)} instances")

# Print the template order
print("\n--- Template order ---")
for key in sorted(order_sections.keys(), key=int):
    print(f"  {key}: {order_sections[key]}")

# Save raw HTML blocks for each template section
for key in sorted(order_sections.keys(), key=int):
    section_type = order_sections[key]
    if section_type in type_to_html:
        blocks = type_to_html[section_type]
        # Get the first match (or in order)
        # We need to match by order; the template sections appear in the HTML in the same order
        # Map: 0 -> first instance of that type
        instances_of_type = [i for i, s in enumerate(sections) if s['type'] == section_type]
        
        # Count how many of this type appear before
        used_count = sum(1 for k, v in order_sections.items() if int(k) < int(key) and v == section_type)
        
        if used_count < len(blocks):
            block = blocks[used_count]
            filename = f"{section_type}.html"
            with open(os.path.join(output_dir, filename), "w") as f:
                f.write(block['raw'])
            print(f"Saved {filename} ({len(block['raw'])} chars)")
        else:
            print(f"WARNING: No HTML block for {section_type} (order {key}), used_count={used_count}, available={len(blocks)}")
    else:
        print(f"WARNING: Section type '{section_type}' not found in HTML")

print(f"\nDone. Raw sections saved to {output_dir}")
