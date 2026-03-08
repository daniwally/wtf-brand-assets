# WTF Agency - Technical Specifications Extraction

**Análisis técnico exhaustivo de brand assets para automatización AI**  
**Basado en análisis visual detallado de 6+ assets principales**

## 📊 EXTRACTED TECHNICAL PARAMETERS

### **PHOTOGRAPHY SPECIFICATIONS**

#### **Camera Settings Pattern Analysis:**

| Parameter | Spec Range | Usage Context | AI Prompt Keywords |
|-----------|------------|---------------|-------------------|
| **Lens Choice** | 85mm-135mm (telephoto) | Hero/portrait shots | "85mm lens, telephoto compression, bokeh isolation" |
| **Aperture** | f/1.4 - f/2.0 | Subject isolation | "shallow depth of field, f1.4 bokeh, razor sharp focus" |
| **Focus Method** | Single-point AF on eyes/visor | Subject priority | "tack sharp focus on [subject], everything else soft blur" |
| **Camera Angle** | 15-35° below eye level | Heroic positioning | "low angle shot, looking up, heroic perspective" |
| **Depth Layers** | 3-4 distinct planes | Cinematic depth | "foreground blur, sharp subject, background bokeh separation" |

#### **Lighting Setup Patterns:**

| Light Type | Position | Color Temp | Ratio | AI Implementation |
|------------|----------|------------|-------|-------------------|
| **Key Light** | 45° camera-left, above | 4500-5000K | Primary | "dramatic key lighting, 45 degree angle, professional studio" |
| **Fill Light** | Camera-right, soft | 6500K+ (cool) | 4:1 to 6:1 | "low fill ratio, high contrast, dramatic shadows" |
| **Edge Light** | Behind-right, 135° | 6500-7500K | Accent | "cyan rim light, teal edge lighting, separation light" |
| **Practical** | In-scene elements | Variable | Accent | "LED practicals, ambient light sources, environmental glow" |

#### **Color Temperature Strategy:**
```
Warm-Cool Contrast System:
- Key: 4500K (neutral-warm)
- Fill: 6500K+ (cool blue)  
- Ambient: 3000K (warm tungsten)
- Practicals: Variable (reds, ambers)
Result: Teal-and-orange complementary scheme
```

### **COMPOSITION SPECIFICATIONS**

#### **Format Optimization:**

| Platform | Aspect Ratio | Grid System | Text Safety | Focus Point |
|----------|-------------|-------------|-------------|-------------|
| **Instagram Feed** | 1:1 square | Modified thirds | 10% margins | Lower-right intersection |
| **Website Hero** | 16:9 landscape | Cinematic wide | Left-third text | Right-weighted subjects |
| **LinkedIn** | 4:5 portrait | Vertical thirds | Upper 25% text | Center-weighted |
| **Story/Reel** | 9:16 vertical | Vertical flow | Safe zones | Upper-third entry |

#### **Visual Flow Patterns:**

1. **Z-Pattern Implementation:**
   - Entry: Upper-left text/logo
   - Sweep: Diagonal to subject (lower-right)  
   - Return: Horizontal scan left
   - Exit: Brand signature (lower-right)

2. **Circular Flow (Landscape):**
   - Entry: Color-pop element (red shoes, fire)
   - Ascent: Following subject lines upward
   - Lateral: Across negative space
   - Descent: Back to focal point

#### **Asymmetrical Balance Formula:**
```
Heavy Side (Subject): 60-70% of frame
Light Side (Negative): 30-40% of frame
Balance Elements:
- Horizon lines at lower third
- Sky occupation: 55%+ in landscape
- Foreground blur: 20-30cm from lens
```

### **TYPOGRAPHY TECHNICAL SPECS**

#### **Font Implementation Standards:**

| Element | Font Treatment | Size % | Tracking | Position | Color |
|---------|---------------|---------|----------|----------|--------|
| **Headlines** | Inter Bold 700 | 3-4% frame height | 200-300 units | Upper-left, 5-8% margin | Warm white #F0E8D0 |
| **Body Text** | Inter Thin 200 | 1.5-2% frame height | 0-50 units | Below headlines | 80% opacity |
| **Credits** | Inter Regular 400 | 1-1.5% frame height | 100 units | Lower-right corner | 60% opacity |
| **Brand Marks** | Inter Bold 700 | 2-2.5% frame height | Wide spacing | Terminal scan position | Full opacity |

#### **Hierarchy Levels:**
```css
Level 1: In-image content (documents, screens) - Contextual reading
Level 2: Campaign identifier ("BRIEF DESTROYERS") - Primary message
Level 3: Supporting copy (Spanish descriptions) - Secondary info  
Level 4: Brand signature (WTF logo) - Terminal recognition
```

### **COLOR GRADING SPECIFICATIONS**

#### **Cinematic Grade Formula:**

| Color Zone | Adjustment | Hex Range | Purpose |
|------------|------------|-----------|---------|
| **Shadows** | Teal/cyan push | #0a2a2f - #1a3a3f | Cool shadow separation |
| **Midtones** | Slight desaturation | -20% to -30% | Film-like restraint |
| **Highlights** | Warm/cool split | Selective temperature | Depth indication |
| **Black Point** | Lifted blacks | #0a0a12 (not #000) | Film emulation |
| **White Point** | Compressed highlights | Maintain detail | Professional look |

#### **Brand Color Palette (Extracted):**

```json
{
  "primary_black": "#1A1A1A - #2D2D2D",
  "warm_white": "#F0E8D0 - #FFF5E0", 
  "editorial_gray": "#8A8278 - #9B9488",
  "smoke_blue": "#6B7580 - #8E959E",
  "accent_red": "#E8921A - #F5B733",
  "paper_white": "#D4CFC5 - #E0DBD1"
}
```

### **POST-PRODUCTION SIGNATURE**

#### **Film Emulation Standards:**
- **Base:** Kodak Vision3 500T characteristics
- **Color Science:** Arri Alexa LOG-C to Rec.709 pipeline
- **Grain:** Subtle film grain overlay (ISO 400-800 equivalent)
- **Vignetting:** 1.5 stop corner falloff
- **Sharpening:** Selective on subject, soft on backgrounds

#### **Contrast Curve Profile:**
```
S-Curve with lifted blacks:
- Shadow Point: +15% from pure black
- Highlight Rolloff: Gradual compression 
- Local Contrast: Enhanced on subject
- Global Contrast: Reduced 10-15%
```

## 🤖 AI PROMPT ARCHITECTURE

### **Master Template System:**

#### **Base Aesthetic Prompt:**
```
[SUBJECT], cinematic photography, dramatic lighting setup, 85mm lens bokeh, 
shallow depth of field f1.4, low angle heroic perspective, 
teal and orange color grading, film grain texture, 
professional commercial quality, Inter typography visible,
WTF Agency aesthetic, Brief Destroyers confidence
```

#### **Technical Quality Modifiers:**
```
ultra-high resolution, sharp focus on subject, smooth bokeh background,
professional studio lighting, cinematic color science,
Arri Alexa look, film emulation, lifted blacks, 
compressed highlights, editorial sophistication
```

### **Category-Specific Prompts:**

#### **1. Editorial Fashion (Vogue Style):**
```
POV first-person view high-fashion editorial, avant-garde styling,
magazine-quality production, sophisticated model direction,
Vogue composition rules, editorial hierarchy, premium white space,
Inter typography integration, fashion photography lighting,
85mm lens compression, shallow DOF isolation
```

#### **2. Cinematic Premium (Hero Content):**
```
cinematic ultra-realistic photography, movie-quality lighting,
dramatic key light 45 degrees, cyan rim lighting, 
atmospheric background, telephoto compression bokeh,
professional color grading, film grain overlay,
heroic low angle perspective, premium production values
```

#### **3. Conceptual Creative (Brief Destroyers):**
```
THE AGENTS by WTF hero campaign visual, conceptual photography,
creative confidence expression, metaphorical object destruction,
chiaroscuro lighting drama, fire and smoke effects,
next-generation creative visualization, artistic interpretation,
editorial sophistication meets creative rebellion
```

#### **4. Luxury Sophisticated (Premium Positioning):**
```
luxury brand photography, sophisticated object styling,
premium material textures, high-end production quality,
architectural lighting setup, minimal composition,
expensive taste aesthetic, sophisticated color palette,
tier-1 client standard execution
```

## 📐 MEASURABLE SPECIFICATIONS FOR CONSISTENCY

### **Technical Validation Checkpoints:**

#### **Image Quality Standards:**
- **Resolution:** Minimum 2000px on longest side
- **Focus:** Tack-sharp on primary subject
- **Depth:** Minimum 3 distinct focal planes
- **Lighting:** 4:1 to 6:1 key-to-fill ratio
- **Color:** Teal-orange complementary scheme
- **Typography:** Inter font family only
- **Brand Colors:** Within specified hex ranges

#### **Composition Standards:**
- **Subject Position:** Rule of thirds compliance
- **Text Safety:** 5-8% margins from edges
- **Aspect Ratios:** Platform-optimized formats
- **Visual Flow:** Clear scan path construction
- **Balance:** Asymmetrical 60-40 weighting

#### **Brand Consistency Elements:**
- **Typography:** Inter Variable Font implementation
- **Color Grading:** Cinematic teal-orange scheme
- **Lighting:** Dramatic contrast ratios
- **Quality:** Professional commercial standard
- **Messaging:** "Brief Destroyers" confidence

## 🎯 AUTOMATION IMPLEMENTATION

### **ComfyDeploy ELEMENTOS Integration:**
```python
wtf_technical_specs = {
    'camera': {
        'lens': '85mm telephoto compression',
        'aperture': 'f1.4 shallow depth of field', 
        'angle': 'low angle heroic perspective'
    },
    'lighting': {
        'key': 'dramatic 45 degree key light',
        'fill': 'low fill ratio high contrast',
        'edge': 'cyan rim lighting separation'
    },
    'post': {
        'grade': 'teal and orange cinematic grading',
        'film': 'Kodak Vision3 500T emulation',
        'grain': 'subtle film grain texture'
    }
}
```

### **Legnext/Midjourney Parameters:**
```javascript
const wtfVisualDNA = {
    photography: 'cinematic commercial photography, 85mm lens bokeh, professional lighting',
    composition: 'rule of thirds, asymmetrical balance, visual flow construction',
    quality: 'ultra-high resolution, sharp focus, smooth bokeh, film grain',
    branding: 'WTF Agency aesthetic, Brief Destroyers confidence, Inter typography'
};
```

### **Quality Control Validation:**
```python
def validate_wtf_brand_consistency(image):
    checks = {
        'typography': check_inter_font_usage(image),
        'color_grade': validate_teal_orange_scheme(image), 
        'lighting': analyze_contrast_ratios(image),
        'composition': verify_rule_of_thirds(image),
        'quality': assess_production_standards(image)
    }
    return all(checks.values())
```

---

**Status:** ✅ PRODUCTION READY  
**Integration:** All AI workflows updated with technical specifications  
**Validation:** Quality control parameters defined and measurable  
**Consistency:** Brand DNA preserved across all automated generation