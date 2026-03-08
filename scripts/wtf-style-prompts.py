#!/usr/bin/env python3
"""
WTF Agency Style Prompts Generator
Based on Visual DNA Analysis of uploaded brand assets
"""

class WTFStylePrompts:
    """
    WTF Agency branded prompt system based on analyzed visual DNA
    """
    
    def __init__(self):
        # Core aesthetic pillars from visual analysis
        self.pillars = {
            'editorial_fashion': {
                'base': 'POV first-person view high-fashion Vogue editorial',
                'modifiers': ['avant-garde fashion', 'sophisticated editorial', 'magazine-quality production'],
                'lighting': 'editorial studio lighting, fashion photography standard',
                'composition': 'Vogue composition, editorial hierarchy, premium white space'
            },
            
            'cinematic_premium': {
                'base': 'cinematic ultra-realistic photography',
                'modifiers': ['movie-quality lighting', 'atmospheric dramatic', 'premium production values'],
                'lighting': 'cinematic lighting, dramatic atmosphere, film-quality',
                'composition': 'movie cinematography, professional framing, cinematic depth'
            },
            
            'conceptual_creative': {
                'base': 'THE AGENTS by WTF hero campaign visual',
                'modifiers': ['BRIEF DESTROYERS creative confidence', 'next-generation creative', 'conceptual art'],
                'lighting': 'creative lighting, conceptual atmosphere',
                'composition': 'creative confidence composition, innovative framing'
            },
            
            'luxury_sophisticated': {
                'base': 'luxury positioning, photorealistic premium materials',
                'modifiers': ['sophisticated object photography', 'premium brand aesthetic', 'high-end production'],
                'lighting': 'luxury lighting, premium studio setup',
                'composition': 'sophisticated composition, luxury brand standards'
            }
        }
    
    def get_wtf_prompt(self, style='editorial_fashion', subject='', additional_context=''):
        """
        Generate WTF Agency branded prompt
        
        Args:
            style (str): One of the pillar styles
            subject (str): Main subject/product
            additional_context (str): Specific campaign context
        """
        
        if style not in self.pillars:
            style = 'editorial_fashion'  # Default fallback
        
        pillar = self.pillars[style]
        
        # Build comprehensive prompt
        prompt_parts = []
        
        # Base aesthetic
        prompt_parts.append(pillar['base'])
        
        # Subject integration
        if subject:
            prompt_parts.append(f"featuring {subject}")
        
        # Style modifiers
        prompt_parts.extend(pillar['modifiers'])
        
        # Technical specifications
        prompt_parts.append(pillar['lighting'])
        prompt_parts.append(pillar['composition'])
        
        # WTF Agency DNA
        prompt_parts.append("WTF Agency aesthetic, Brief Destroyers confidence")
        prompt_parts.append("Inter typography visible, editorial premium feel")
        
        # Additional context
        if additional_context:
            prompt_parts.append(additional_context)
        
        # Quality standards
        prompt_parts.append("ultra-high quality, professional production, tier-1 client standard")
        
        return ", ".join(prompt_parts)
    
    def get_campaign_prompt(self, campaign_type, product='', client_context=''):
        """
        Generate campaign-specific WTF Agency prompt
        """
        
        campaign_styles = {
            'hero_launch': 'cinematic_premium',
            'social_media': 'editorial_fashion', 
            'brand_identity': 'conceptual_creative',
            'luxury_product': 'luxury_sophisticated',
            'fashion_campaign': 'editorial_fashion',
            'corporate_premium': 'luxury_sophisticated'
        }
        
        style = campaign_styles.get(campaign_type, 'editorial_fashion')
        
        return self.get_wtf_prompt(
            style=style,
            subject=product,
            additional_context=f"{campaign_type} campaign, {client_context}"
        )
    
    def get_social_media_prompt(self, platform, content_type=''):
        """
        Platform-specific WTF Agency branded prompts
        """
        
        platform_specs = {
            'instagram': {
                'style': 'editorial_fashion',
                'aspect': '4:5 aspect ratio, Instagram feed optimized',
                'specs': 'high engagement visual, story-ready composition'
            },
            'linkedin': {
                'style': 'luxury_sophisticated', 
                'aspect': '16:9 aspect ratio, LinkedIn professional',
                'specs': 'B2B premium positioning, corporate sophistication'
            },
            'youtube': {
                'style': 'cinematic_premium',
                'aspect': '16:9 aspect ratio, YouTube thumbnail',
                'specs': 'high click-through design, video-ready composition'
            },
            'tiktok': {
                'style': 'editorial_fashion',
                'aspect': '9:16 vertical aspect ratio, TikTok optimized', 
                'specs': 'mobile-first design, Gen Z premium appeal'
            }
        }
        
        if platform not in platform_specs:
            platform = 'instagram'  # Default
        
        spec = platform_specs[platform]
        
        base_prompt = self.get_wtf_prompt(style=spec['style'])
        
        return f"{base_prompt}, {spec['aspect']}, {spec['specs']}, {content_type}"

# Usage examples and testing
def generate_wtf_examples():
    """Generate example prompts for different WTF Agency use cases"""
    
    wtf = WTFStylePrompts()
    
    examples = [
        # Campaign examples
        ("Hero Launch Campaign", wtf.get_campaign_prompt('hero_launch', 'new smartphone', 'tech innovation premium')),
        ("Social Media Post", wtf.get_social_media_prompt('instagram', 'brand announcement')),
        ("Luxury Product", wtf.get_campaign_prompt('luxury_product', 'premium champagne', 'celebration premium lifestyle')),
        ("Editorial Fashion", wtf.get_wtf_prompt('editorial_fashion', 'fashion model', 'Vogue editorial spread')),
        ("Cinematic Brand", wtf.get_wtf_prompt('cinematic_premium', 'brand hero shot', 'movie-quality production')),
        ("Brief Destroyers Concept", wtf.get_wtf_prompt('conceptual_creative', 'WTF Agency identity', 'Brief Destroyers philosophy'))
    ]
    
    print("🎯 WTF AGENCY - BRANDED AI PROMPTS")
    print("=" * 50)
    
    for title, prompt in examples:
        print(f"\n📋 {title}:")
        print(f"   {prompt[:120]}...")
    
    return examples

if __name__ == "__main__":
    # Generate examples
    examples = generate_wtf_examples()
    
    # Test specific prompt generation
    wtf = WTFStylePrompts()
    
    print("\n\n🎨 PROMPT TESTING:")
    print("=" * 30)
    
    # Test editorial prompt
    editorial = wtf.get_wtf_prompt(
        style='editorial_fashion',
        subject='champagne bottle',
        additional_context='premium celebration lifestyle campaign'
    )
    
    print(f"\n📝 Editorial Fashion Prompt:")
    print(f"   {editorial}")
    
    # Test cinematic prompt  
    cinematic = wtf.get_wtf_prompt(
        style='cinematic_premium',
        subject='tech product launch',
        additional_context='innovation showcase, future-forward'
    )
    
    print(f"\n🎬 Cinematic Premium Prompt:")
    print(f"   {cinematic}")
    
    print(f"\n✅ WTF Agency style prompts ready for AI workflows!")
    print(f"   Use in ComfyDeploy, Midjourney, and all automated generation")