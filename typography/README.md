# WTF Agency Typography

## ✅ Inter Variable Fonts Uploaded

**Core Variable Fonts:**
- `Inter-VariableFont_opsz,wght.ttf` ✅ Roman/Regular Variable Font
- `Inter-Italic-VariableFont_opsz,wght.ttf` ✅ Italic Variable Font

## 📋 Technical Specifications

### Variable Axes
- **Weight (wght):** 100-900 (Thin to Black)
- **Optical Size (opsz):** 14-32pt (auto-optimization)

### WTF Agency Standards
- **Headlines:** Inter Bold (700-800) + large optical size
- **Body Text:** Inter Thin (100-200) + small optical size  
- **Impact:** Inter Black (900) + maximum optical size

## 📚 Documentation

- **`INTER-TECHNICAL-GUIDE.md`** ✅ Complete implementation guide
- **`typography-guidelines.md`** ✅ Brand usage guidelines
- **`../scripts/inter-font-generator.py`** ✅ Automated text generation

## 🚀 Automated Integration

**Available in all workflows:**
- ✅ ComfyDeploy AI workflows (text overlays)
- ✅ Legnext/Midjourney banner automation  
- ✅ Presentation templates
- ✅ Social media assets

## ⚙️ CSS Implementation

```css
/* Variable Font Setup */
:root {
  font-family: 'InterVariable', Inter, sans-serif;
  font-feature-settings: 'liga' 1, 'calt' 1, 'ss02' 1;
}

/* WTF Headlines */
.wtf-headline {
  font-variation-settings: 'wght' 700, 'opsz' 24;
}

/* WTF Body */
.wtf-body {
  font-variation-settings: 'wght' 200, 'opsz' 16;
}
```

## 🎯 OpenType Features

- **Ligatures (liga)** - Enhanced character combinations
- **Contextual Alternates (calt)** - Smart punctuation adjustment
- **Stylistic Set 02 (ss02)** - Unambiguous characters
- **Slashed Zero (zero)** - Distinguish 0 from o
- **Tabular Numbers (tnum)** - Data/pricing alignment

## 📱 Size Recommendations

- **11px minimum** - Inter's designed lower limit
- **14-18px** - Body text sweet spot (WTF standard)
- **24-32px** - Headlines and titles
- **48px+** - Display/impact statements

---

**Status:** ✅ PRODUCTION READY  
**Variable Font:** Latest Inter family with full OpenType features  
**WTF Agency Standard:** Editorial + Fashion + Premium aesthetic  
**Last Updated:** 2026-03-08