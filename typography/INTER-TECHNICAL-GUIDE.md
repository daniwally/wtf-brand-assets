# Inter Variable Font - Technical Implementation Guide

## 📋 Overview

**Inter** es una variable font diseñada específicamente para pantallas, con características avanzadas de OpenType y optimización automática según el tamaño. Es la tipografía principal de WTF Agency.

## 🎯 Files Uploaded

✅ **Inter-VariableFont_opsz,wght.ttf** - Roman/Regular Variable Font  
✅ **Inter-Italic-VariableFont_opsz,wght.ttf** - Italic Variable Font  

## ⚙️ Variable Axes

### Weight (wght)
- **Range:** 100-900
- **Key weights for WTF Agency:**
  - **100-200 (Thin/Extra Light)** → Body text, descriptions
  - **700-800 (Bold/Extra Bold)** → Headlines, titles  
  - **900 (Black)** → Impact statements, brand elements

### Optical Size (opsz) 
- **Range:** 14-32pt
- **Auto-optimization:** Adjusts stroke weight and letter shapes for optimal readability
- **14pt:** Small text, body copy (higher x-height: 1118 UPM)
- **32pt:** Large headlines, display text (lower x-height: 1056 UPM)

## 🔧 CSS Implementation

### Basic Setup
```css
/* Variable Font Implementation */
@font-face {
  font-family: 'InterVariable';
  src: url('./Inter-VariableFont_opsz,wght.ttf') format('truetype-variations');
  font-weight: 100 900;
  font-display: swap;
}

/* Root Configuration */
:root {
  font-family: 'InterVariable', Inter, sans-serif;
  font-feature-settings: 'liga' 1, 'calt' 1, 'ss02' 1;
}

/* Browser Support Fallback */
@supports not (font-variation-settings: normal) {
  :root {
    font-family: Inter, sans-serif;
  }
}
```

### WTF Agency Font Weights
```css
/* Headlines - Editorial Bold */
.wtf-headline {
  font-variation-settings: 'wght' 700, 'opsz' 24;
  font-size: 32px;
  line-height: 1.2;
  letter-spacing: -0.02em;
}

/* Body Text - Sophisticated Thin */
.wtf-body {
  font-variation-settings: 'wght' 200, 'opsz' 16;
  font-size: 16px;
  line-height: 1.5;
  letter-spacing: 0;
}

/* Impact Statements - Maximum Weight */
.wtf-impact {
  font-variation-settings: 'wght' 900, 'opsz' 32;
  font-size: 48px;
  line-height: 1.1;
  letter-spacing: -0.03em;
}
```

## ✨ OpenType Features

### Enabled by Default
```css
font-feature-settings: 
  'liga' 1,    /* Ligatures - Better character combinations */
  'calt' 1,    /* Contextual Alternates - Smart punctuation */
  'ss02' 1;    /* Stylistic Set 02 - Unambiguous characters */
```

### Additional Features Available
- **'zero'** - Slashed zero (0̸) to distinguish from 'o'
- **'tnum'** - Tabular numbers for data/pricing
- **'frac'** - Automatic fractions (1/2 → ½)
- **'case'** - All caps optimized punctuation

## 🎨 WTF Agency Usage Guidelines

### Brand Hierarchy
1. **Headlines (Bold 700-800):** Campaign titles, section headers
2. **Body (Thin 100-200):** Descriptions, copy, supporting text
3. **Impact (Black 900):** "Brief Destroyers", key statements

### Size Recommendations
- **11px minimum** - Inter's designed lower limit
- **14-18px** - Body text sweet spot  
- **24px+** - Headlines and titles
- **48px+** - Display/impact text

### Letter Spacing by Size
- **11-18px:** `letter-spacing: 0` (normal)
- **20-32px:** `letter-spacing: -0.01em` (slight tightening)
- **36px+:** `letter-spacing: -0.02em` to `-0.03em` (editorial tightness)

## 🚀 Workflow Integration

### For Banner Automation (Legnext/Midjourney)
```python
# Text overlay with Inter specifications
text_config = {
    'font_family': 'Inter Variable',
    'headline_weight': 700,
    'body_weight': 200,
    'optical_size': 'auto',  # Let browser optimize
    'features': ['liga', 'calt', 'ss02']
}
```

### For ComfyDeploy AI Workflows
- Use Inter Variable for all text elements
- Maintain weight contrast: Thin (200) + Bold (700)
- Enable contextual alternates for premium feel

### For Social Media Assets
- **Instagram:** 16px body, 24px headlines
- **LinkedIn:** 18px body, 28px headlines  
- **Twitter:** 15px body, 22px headlines

## 🔍 Technical Specifications

- **UPM:** 2048 units
- **Cap Height:** 1490 UPM
- **x-Height:** 1118 UPM (opsz=14) to 1056 UPM (opsz=32)
- **Ascender:** 1984 UPM  
- **Descender:** -494 UPM
- **Classification:** Sans-serif, Grotesk
- **Designed for:** Screen reading, UI/UX, digital applications

## 💡 Best Practices for WTF Agency

### ✅ DO
- Use weight contrast (Thin + Bold) for editorial hierarchy
- Enable ligatures and contextual alternates always
- Let optical size auto-adjust for sizes 14-32pt
- Use negative letter-spacing for large headlines
- Combine with generous white space (magazine style)

### ❌ DON'T  
- Mix multiple weights in same text block
- Use below 11px font size
- Disable contextual alternates ('calt')
- Overcrowd layouts - maintain sophistication
- Use Inter for decorative/script purposes

---

**Reference:** Google Fonts Inter + rsms.me/inter  
**WTF Agency Standard:** Editorial + Fashion + Premium  
**Updated:** 2026-03-08  
**Status:** ✅ PRODUCTION READY