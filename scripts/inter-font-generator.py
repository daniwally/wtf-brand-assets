#!/usr/bin/env python3
"""
Inter Variable Font Generator for WTF Agency Workflows
Generates text overlays using Inter Variable Font with proper specifications
"""

from PIL import Image, ImageDraw, ImageFont
import os
from pathlib import Path

class InterFontGenerator:
    def __init__(self, font_dir="./typography/"):
        self.font_dir = Path(font_dir)
        self.regular_font = self.font_dir / "Inter-VariableFont_opsz,wght.ttf"
        self.italic_font = self.font_dir / "Inter-Italic-VariableFont_opsz,wght.ttf"
        
        # WTF Agency font specifications
        self.wtf_specs = {
            'headline': {
                'weight': 700,
                'optical_size': 24,
                'letter_spacing': -0.02,
                'line_height': 1.2
            },
            'body': {
                'weight': 200,  
                'optical_size': 16,
                'letter_spacing': 0,
                'line_height': 1.5
            },
            'impact': {
                'weight': 900,
                'optical_size': 32,
                'letter_spacing': -0.03,
                'line_height': 1.1
            }
        }
    
    def get_inter_font(self, size=16, weight=400, italic=False):
        """
        Get Inter Variable Font with specified parameters
        
        Args:
            size (int): Font size in pixels
            weight (int): Font weight (100-900)
            italic (bool): Use italic version
        """
        try:
            font_path = self.italic_font if italic else self.regular_font
            
            if not font_path.exists():
                raise FileNotFoundError(f"Inter font not found: {font_path}")
            
            # Load variable font with weight
            font = ImageFont.truetype(str(font_path), size)
            
            # Note: PIL doesn't fully support variable font axes yet
            # For production, recommend using web/CSS implementation
            return font
            
        except Exception as e:
            print(f"⚠️  Font loading error: {e}")
            return ImageFont.load_default()
    
    def create_wtf_text_overlay(self, text, style='headline', size=32, color=(0, 0, 0)):
        """
        Create text overlay with WTF Agency Inter specifications
        
        Args:
            text (str): Text to render
            style (str): 'headline', 'body', or 'impact'
            size (int): Font size override
            color (tuple): RGB color tuple
        """
        
        if style not in self.wtf_specs:
            raise ValueError(f"Style must be one of: {list(self.wtf_specs.keys())}")
        
        spec = self.wtf_specs[style]
        font = self.get_inter_font(size=size, weight=spec['weight'])
        
        # Calculate text dimensions
        bbox = font.getbbox(text)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        # Create image with text
        img = Image.new('RGBA', (text_width + 40, text_height + 40), (255, 255, 255, 0))
        draw = ImageDraw.Draw(img)
        
        # Draw text with Inter specs
        draw.text(
            (20, 20),
            text,
            font=font,
            fill=color + (255,),  # Add alpha
        )
        
        return img
    
    def generate_wtf_banner_text(self, headline, body_text=None, output_path="wtf_text_overlay.png"):
        """
        Generate complete WTF Agency banner text overlay
        
        Args:
            headline (str): Main headline text
            body_text (str, optional): Supporting body text
            output_path (str): Output file path
        """
        
        # Calculate sizes based on headline length
        headline_size = max(24, min(48, 600 // len(headline)))
        body_size = max(14, headline_size // 2)
        
        # Create headline
        headline_img = self.create_wtf_text_overlay(
            headline, 
            style='headline',
            size=headline_size,
            color=(0, 0, 0)  # Black for contrast
        )
        
        if body_text:
            # Create body text
            body_img = self.create_wtf_text_overlay(
                body_text,
                style='body', 
                size=body_size,
                color=(64, 64, 64)  # Dark gray
            )
            
            # Combine headline and body
            total_height = headline_img.height + body_img.height + 20
            max_width = max(headline_img.width, body_img.width)
            
            combined = Image.new('RGBA', (max_width, total_height), (255, 255, 255, 0))
            combined.paste(headline_img, (0, 0), headline_img)
            combined.paste(body_img, (0, headline_img.height + 20), body_img)
            
            result = combined
        else:
            result = headline_img
        
        # Save result
        result.save(output_path, 'PNG')
        print(f"✅ WTF text overlay generated: {output_path}")
        print(f"   Headlines: Inter Bold {headline_size}px")
        if body_text:
            print(f"   Body: Inter Thin {body_size}px")
        
        return output_path

def generate_wtf_specimens():
    """Generate Inter font specimens for WTF Agency"""
    
    generator = InterFontGenerator()
    
    specimens = [
        ("Brief Destroyers", "headline", 48),
        ("WTF Agency - Editorial Premium", "headline", 32),
        ("Sophisticated brand communication", "body", 18),
        ("IMPACT STATEMENT", "impact", 40)
    ]
    
    print("🎨 Generating WTF Agency Inter specimens...")
    
    for i, (text, style, size) in enumerate(specimens, 1):
        output_path = f"inter_specimen_{i}_{style}.png"
        img = generator.create_wtf_text_overlay(text, style, size)
        img.save(output_path)
        print(f"   ✅ Generated: {output_path}")

if __name__ == "__main__":
    # Demo usage
    generator = InterFontGenerator()
    
    # Example 1: Simple headline
    generator.generate_wtf_banner_text(
        headline="Brief Destroyers",
        output_path="wtf_headline_demo.png"
    )
    
    # Example 2: Headline + body
    generator.generate_wtf_banner_text(
        headline="WTF Agency",
        body_text="Editorial + Fashion + Premium",
        output_path="wtf_complete_demo.png"
    )
    
    # Generate specimens
    generate_wtf_specimens()
    
    print("\n🎯 Inter Variable Font generator ready for WTF workflows!")
    print("   Use in banner automation, social media, presentations")