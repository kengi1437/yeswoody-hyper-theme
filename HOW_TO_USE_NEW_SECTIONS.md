# 📖 如何使用新的 Sections

## 🔍 找不到新的 Sections？

如果你在 Shopify Theme Editor 看不到新添加的 sections，這是因為你的 Shopify theme 還在使用舊版本。

## ✅ 解決方法

### 選項 1：使用 Shopify CLI（最快）

如果你已經安裝了 Shopify CLI：

```bash
# Pull 最新代碼
shopify theme pull

# Push 到 Shopify
shopify theme push
```

### 選項 2：通過 GitHub 同步

1. 登入 Shopify Admin
2. 進入 **Online Store > Themes**
3. 如果你的 theme 已經連接到 GitHub：
   - 找到你的 theme
   - 點擊 **Actions > Edit code**
   - Git 會自動同步最新版本

4. 如果還沒連接到 GitHub：
   - 點擊 **Add theme**
   - 選擇 **Connect from GitHub**
   - 選擇 `kengi1437/yeswoody-hyper-theme` repository
   - 選擇 `master` 分支
   - 等待安裝完成

### 選項 3：手動上傳文件

1. 在 GitHub 下載這些文件：
   - `sections/collection-slider.liquid`
   - `sections/collection-tabs.liquid`
   - `sections/promotion-banner.liquid`
   - `blocks/_collection-slider-card.liquid`
   - `blocks/_collection-slider-content.liquid`
   - `blocks/_collection-tabs-content.liquid`
   - `blocks/_promotion-banner-content.liquid`
   - `snippets/product-card-simple.liquid`

2. 在 Shopify Admin:
   - 進入 **Online Store > Themes**
   - 點擊你的 theme 的 **Actions > Edit code**
   - 上傳對應的文件到對應的文件夾

## 🎨 如何添加 Sections 到頁面

### 在 Theme Editor 中添加：

1. 進入 **Online Store > Themes**
2. 點擊 **Customize**
3. 選擇要編輯的頁面（如 Homepage）
4. 點擊 **Add section**
5. 在列表中找到：
   - **Collection Slider** - 商品系列滑動展示
   - **Collection Tabs** - 商品系列標籤切換
   - **Promotion Banner** - 促銷橫幅（帶倒數計時）

6. 點擊 section 後配置設定

## ⚙️ Section 設定說明

### Collection Slider
- **Heading**: 標題文字
- **Columns**: 桌面顯示的列數（2-6）
- **Mobile columns**: 手機顯示的列數（1-2）
- **Navigation**: 箭頭導航樣式

**添加商品系列**:
1. 點擊 **Collection Slider Content** block
2. 添加 **Collection Card** blocks
3. 為每個 card 選擇一個 collection

### Collection Tabs
- **Heading**: 標題文字
- **Products per tab**: 每個標籤顯示的產品數量
- **Tab style**: 標籤樣式（pills / underline / buttons）

**添加標籤**:
1. 點擊 **Collection Tabs Content** block
2. 添加 **Collection Tab** blocks
3. 為每個 tab 選擇一個 collection

### Promotion Banner
- **Heading**: 促銷標題
- **Description**: 促銷描述
- **Show countdown timer**: 顯示倒數計時
- **End date**: 結束日期（格式：YYYY-MM-DD）
- **End time**: 結束時間（格式：HH:MM:SS）
- **Button label**: 按鈕文字
- **Button link**: 按鈕連結
- **Background color**: 背景顏色
- **Text color**: 文字顏色

## 🐛 常見問題

### Q: Section 不顯示內容？
A: 確保你已經在 section settings 中添加了內容（collections、products 等）

### Q: 倒數計時器不工作？
A: 檢查日期格式是否正確：
- 日期：YYYY-MM-DD（例如：2026-12-31）
- 時間：HH:MM:SS（例如：23:59:59）

### Q: 樣式看起來不對？
A: 這些 sections 繼承了 Horizon theme 的樣式系統，確保你的 theme 是最新版本

## 📞 需要幫助？

如果遇到問題，檢查：
1. GitHub 上的文件是否最新
2. Shopify theme 是否已同步最新代碼
3. Browser 緩存是否已清除

---

**Repository**: https://github.com/kengi1437/yeswoody-hyper-theme  
**Branch**: master
