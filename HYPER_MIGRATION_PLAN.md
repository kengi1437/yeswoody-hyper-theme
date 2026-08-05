# 🎯 Hyper Theme to Horizon Theme Migration Plan

## 📊 Project Overview

**Source**: Hyper Theme Demo (https://hyper-theme-demo.myshopify.com/)
**Target**: Horizon Theme (現在的 master 分支)
**Goal**: 將 Hyper theme 的所有功能移植到 Horizon theme

## 🏗️ Architecture Differences

### Hyper Theme (Traditional)
- 使用傳統的 sections/*.liquid 文件
- Section schemas 在文件內定義
- 直接在 sections 中編寫 HTML/Liquid

### Horizon Theme (Modern Blocks System)
- 使用 blocks/*.liquid 系統
- sections/_blocks.liquid 作為主要渲染引擎
- 更靈活的組件化架構

## 📝 需要移植的 Hyper Theme 功能列表

### 1. **Slideshow / Hero Section** ✅ (Horizon 已有 hero.liquid)
   - 優化：添加更多 transition effects
   - 添加：Autoplay 選項
   - 添加：Ken Burns 效果

### 2. **Collection List Slider** 🔨 (需要新建)
   - 商品系列橫向滾動展示
   - 帶有分類圖片和標題
   - Carousel 導航

### 3. **Collection Tabs** 🔨 (需要新建)
   - 標籤切換式商品系列展示
   - 每個 tab 對應一個 collection
   - 動態切換內容

### 4. **Promotion Banner** 🔨 (需要新建)
   - 促銷橫幅區塊
   - 支持倒數計時器
   - 自定義背景和文字

### 5. **Buttons With Icon** 🔨 (需要新建)
   - 帶圖標的按鈕列表
   - 橫向或縱向排列
   - 自定義圖標

### 6. **Lookbook Slider** 🔨 (需要新建)
   - 時尚產品展示滑動器
   - 點擊熱點顯示產品信息
   - 適合服飾類目

### 7. **Testimonials / Reviews** 🔨 (需要新建)
   - 客戶評價輪播
   - 星級評分顯示
   - 頭像 + 姓名 + 評論

### 8. **Image With Text** ✅ (Horizon 已有類似功能)
   - 檢查並優化現有功能

### 9. **Multicolumn** ✅ (Horizon 已有類似功能)
   - 檢查並優化

### 10. **Scrolling Promotion** 🔨 (需要新建)
   - 無限滾動的促銷文字
   - Marquee 效果
   - 自定義速度和方向

### 11. **Scrolling Gallery** 🔨 (需要新建)
   - 橫向滾動圖片畫廊
   - 自動播放選項

### 12. **Featured Products / Favorite Products** ✅ (Horizon 已有 product-list)
   - 檢查並優化

### 13. **Custom Content Blocks** ✅ (Horizon 已有靈活的 blocks 系統)
   - 利用現有 blocks 系統

## 🎨 需要移植的樣式特性

### CSS Features from Hyper
- **Color Schemes**: Multiple pre-defined schemes
- **Typography**: Instrument Sans 字體系統
- **Animations**: Sophisticated CSS animations
- **Button Styles**: 多種按鈕變體
- **Card Designs**: Product card 樣式

### JavaScript Features
- **Collection Slider**: Swiper.js or similar
- **Tab Switching**: Collection tabs functionality  
- **Countdown Timer**: For promotion banners
- **Infinite Scroll**: For scrolling sections
- **Lightbox**: Product image gallery

## 📅 Implementation Phases

### Phase 1: 分析和準備 (Current)
- [x] 分析兩個 theme 的架構差異
- [x] 列出所有需要移植的功能
- [ ] 創建測試計劃

### Phase 2: 核心 Sections (Priority High)
- [ ] Collection List Slider
- [ ] Collection Tabs
- [ ] Promotion Banner with Countdown
- [ ] Lookbook Slider

### Phase 3: 增強 Sections (Priority Medium)
- [ ] Scrolling Promotion (Marquee)
- [ ] Testimonials Carousel
- [ ] Buttons With Icon List
- [ ] Scrolling Gallery

### Phase 4: 樣式和優化 (Priority Normal)
- [ ] 移植 Hyper 的 color schemes
- [ ] 優化 animations
- [ ] 統一 button styles
- [ ] Product card 樣式優化

### Phase 5: 測試和調整
- [ ] 功能測試
- [ ] 響應式測試
- [ ] 性能優化
- [ ] Browser compatibility

## 🔧 Technical Approach

### Strategy 1: 創建新的 Blocks
為 Hyper 特有的功能創建新的 block 文件：
- `_collection-slider.liquid`
- `_collection-tabs.liquid`
- `_promotion-banner.liquid`
- `_lookbook.liquid`
- `_testimonials.liquid`
- `_scrolling-text.liquid`

### Strategy 2: 創建新的 Sections
創建對應的 section 文件來整合這些 blocks

### Strategy 3: 移植 Assets
- CSS: 提取 Hyper 的樣式到 Horizon
- JS: 移植互動功能的 JavaScript
- Images: 保留 placeholder 圖片結構

## 📁 File Structure Plan

