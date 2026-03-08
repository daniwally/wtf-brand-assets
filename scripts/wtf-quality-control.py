#!/usr/bin/env python3
"""
WTF Agency Quality Control System
Advanced validation for brand consistency across all generated content
"""

import json
import os
from datetime import datetime
from PIL import Image, ImageStat, ImageFilter
import numpy as np
import cv2

class WTFQualityControl:
    """
    Advanced quality control system for WTF Agency brand consistency
    Validates technical specs, brand compliance, and professional standards
    """
    
    def __init__(self):
        # Technical specifications from analysis
        self.technical_standards = {
            'resolution': {'min_width': 2000, 'min_height': 1200},
            'aspect_ratios': {
                'instagram_feed': (1, 1),
                'website_hero': (16, 9), 
                'linkedin_post': (4, 5),
                'story_vertical': (9, 16)
            },
            'color_ranges': {
                'primary_black': [(26, 26, 26), (45, 45, 45)],  # #1A1A1A - #2D2D2D
                'warm_white': [(240, 232, 208), (255, 245, 224)],  # #F0E8D0 - #FFF5E0
                'editorial_gray': [(138, 130, 120), (155, 148, 136)],  # #8A8278 - #9B9488
                'teal_shadow': [(10, 42, 47), (26, 58, 63)]  # #0a2a2f - #1a3a3f
            },
            'lighting_ratios': {
                'min_contrast': 4.0,  # 4:1 key to fill minimum
                'max_contrast': 8.0,  # 8:1 maximum for dramatic look
                'highlight_compression': 0.85  # Don't blow highlights
            },
            'typography': {
                'font_family': 'Inter Variable Font',
                'headline_size_percent': (3, 4.5),  # 3-4.5% of frame height
                'text_margins': (5, 8)  # 5-8% from edges
            }
        }
        
        # Brand DNA validation criteria
        self.brand_criteria = {
            'aesthetic_pillars': [
                'editorial_fashion',
                'cinematic_premium', 
                'conceptual_creative',
                'luxury_sophisticated'
            ],
            'visual_flow_patterns': [
                'z_pattern',
                'circular_flow',
                'diagonal_sweep'
            ],
            'composition_rules': [
                'rule_of_thirds',
                'asymmetrical_balance',
                'depth_layering'
            ]
        }
    
    def analyze_image_technical_quality(self, image_path):
        """Analyze technical quality of image against WTF standards"""
        
        try:
            img = Image.open(image_path)
            img_array = np.array(img)
            
            analysis = {
                'resolution': self._check_resolution(img),
                'aspect_ratio': self._check_aspect_ratio(img),
                'color_analysis': self._analyze_color_palette(img_array),
                'contrast_analysis': self._analyze_contrast(img_array),
                'composition': self._analyze_composition(img_array),
                'sharpness': self._analyze_sharpness(img_array),
                'noise_grain': self._analyze_noise_characteristics(img_array)
            }
            
            return analysis
            
        except Exception as e:
            return {'error': f"Analysis failed: {str(e)}"}
    
    def _check_resolution(self, img):
        """Check if image meets resolution standards"""
        width, height = img.size
        
        meets_standard = (
            width >= self.technical_standards['resolution']['min_width'] and
            height >= self.technical_standards['resolution']['min_height']
        )
        
        return {
            'width': width,
            'height': height,
            'meets_standard': meets_standard,
            'megapixels': round((width * height) / 1000000, 1)
        }
    
    def _check_aspect_ratio(self, img):
        """Check aspect ratio against platform standards"""
        width, height = img.size
        actual_ratio = width / height
        
        closest_platform = None
        closest_diff = float('inf')
        
        for platform, (w_ratio, h_ratio) in self.technical_standards['aspect_ratios'].items():
            target_ratio = w_ratio / h_ratio
            diff = abs(actual_ratio - target_ratio)
            
            if diff < closest_diff:
                closest_diff = diff
                closest_platform = platform
        
        return {
            'actual_ratio': round(actual_ratio, 3),
            'closest_platform': closest_platform,
            'ratio_difference': round(closest_diff, 3),
            'platform_optimized': closest_diff < 0.1
        }
    
    def _analyze_color_palette(self, img_array):
        """Analyze color palette against brand standards"""
        
        # Convert to RGB if needed
        if len(img_array.shape) == 3 and img_array.shape[2] == 3:
            rgb_array = img_array
        else:
            rgb_array = cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB)
        
        # Calculate dominant colors
        pixels = rgb_array.reshape(-1, 3)
        unique_colors = np.unique(pixels, axis=0)
        
        # Check for brand colors
        brand_color_presence = {}
        for color_name, (min_rgb, max_rgb) in self.technical_standards['color_ranges'].items():
            min_rgb = np.array(min_rgb)
            max_rgb = np.array(max_rgb)
            
            # Check if any pixels fall within brand color ranges
            in_range = np.all((pixels >= min_rgb) & (pixels <= max_rgb), axis=1)
            percentage = np.sum(in_range) / len(pixels) * 100
            
            brand_color_presence[color_name] = {
                'present': percentage > 1.0,  # At least 1% coverage
                'percentage': round(percentage, 2)
            }
        
        # Check for teal-orange complementary scheme
        teal_orange_scheme = self._detect_teal_orange_scheme(rgb_array)
        
        return {
            'brand_colors': brand_color_presence,
            'teal_orange_scheme': teal_orange_scheme,
            'total_unique_colors': len(unique_colors),
            'color_diversity': self._calculate_color_diversity(pixels)
        }
    
    def _detect_teal_orange_scheme(self, rgb_array):
        """Detect teal-orange complementary color scheme"""
        
        # Define teal and orange ranges
        teal_range = [(0, 100, 100), (100, 200, 200)]  # Rough teal range
        orange_range = [(200, 100, 0), (255, 180, 100)]  # Rough orange range
        
        pixels = rgb_array.reshape(-1, 3)
        
        # Check for teal presence
        teal_mask = np.all((pixels >= teal_range[0]) & (pixels <= teal_range[1]), axis=1)
        teal_percentage = np.sum(teal_mask) / len(pixels) * 100
        
        # Check for orange presence  
        orange_mask = np.all((pixels >= orange_range[0]) & (pixels <= orange_range[1]), axis=1)
        orange_percentage = np.sum(orange_mask) / len(pixels) * 100
        
        has_scheme = teal_percentage > 2.0 and orange_percentage > 2.0
        
        return {
            'detected': has_scheme,
            'teal_percentage': round(teal_percentage, 2),
            'orange_percentage': round(orange_percentage, 2)
        }
    
    def _calculate_color_diversity(self, pixels):
        """Calculate color diversity (how varied the palette is)"""
        
        # Calculate standard deviation across RGB channels
        r_std = np.std(pixels[:, 0])
        g_std = np.std(pixels[:, 1]) 
        b_std = np.std(pixels[:, 2])
        
        avg_std = (r_std + g_std + b_std) / 3
        
        # Classify diversity
        if avg_std < 20:
            diversity = 'low'  # Monochromatic/restrained
        elif avg_std < 50:
            diversity = 'medium'  # Balanced palette
        else:
            diversity = 'high'  # Very diverse/colorful
        
        return {
            'score': round(avg_std, 1),
            'classification': diversity,
            'wtf_appropriate': diversity in ['low', 'medium']  # WTF prefers restrained palettes
        }
    
    def _analyze_contrast(self, img_array):
        """Analyze image contrast ratios"""
        
        # Convert to grayscale for luminance analysis
        if len(img_array.shape) == 3:
            gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
        else:
            gray = img_array
        
        # Calculate overall contrast
        min_luma = np.min(gray)
        max_luma = np.max(gray)
        overall_contrast = (max_luma - min_luma) / 255.0
        
        # Calculate local contrast (edges)
        edges = cv2.Canny(gray, 50, 150)
        edge_density = np.sum(edges > 0) / edges.size
        
        # Estimate lighting ratio (very approximate)
        hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
        shadow_pixels = np.sum(hist[0:64])  # 0-25% range
        highlight_pixels = np.sum(hist[192:256])  # 75-100% range
        
        lighting_ratio = highlight_pixels / max(shadow_pixels, 1)
        
        return {
            'overall_contrast': round(overall_contrast, 3),
            'edge_density': round(edge_density, 4),
            'estimated_lighting_ratio': round(lighting_ratio, 1),
            'meets_wtf_standard': (
                overall_contrast >= 0.6 and  # Good overall contrast
                lighting_ratio >= self.technical_standards['lighting_ratios']['min_contrast']
            )
        }
    
    def _analyze_composition(self, img_array):
        """Analyze composition against rule of thirds and balance"""
        
        height, width = img_array.shape[:2]
        
        # Rule of thirds grid points
        third_x = width // 3
        two_third_x = 2 * third_x
        third_y = height // 3
        two_third_y = 2 * third_y
        
        # Convert to grayscale for analysis
        if len(img_array.shape) == 3:
            gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
        else:
            gray = img_array
        
        # Detect interest points (corners/features)
        corners = cv2.goodFeaturesToTrack(
            gray, maxCorners=20, qualityLevel=0.1, minDistance=50
        )
        
        # Check if interest points align with rule of thirds
        thirds_alignment = 0
        if corners is not None:
            for corner in corners:
                x, y = corner[0]
                
                # Check proximity to third lines (within 10% of image dimension)
                x_threshold = width * 0.1
                y_threshold = height * 0.1
                
                near_third = (
                    abs(x - third_x) < x_threshold or
                    abs(x - two_third_x) < x_threshold or
                    abs(y - third_y) < y_threshold or  
                    abs(y - two_third_y) < y_threshold
                )
                
                if near_third:
                    thirds_alignment += 1
        
        thirds_score = thirds_alignment / max(len(corners), 1) if corners is not None else 0
        
        # Analyze balance (left vs right weight)
        left_half = gray[:, :width//2]
        right_half = gray[:, width//2:]
        
        left_energy = np.mean(left_half)
        right_energy = np.mean(right_half)
        balance_ratio = max(left_energy, right_energy) / max(min(left_energy, right_energy), 1)
        
        return {
            'rule_of_thirds_score': round(thirds_score, 2),
            'interest_points': len(corners) if corners is not None else 0,
            'balance_ratio': round(balance_ratio, 2),
            'asymmetrical_balance': 1.2 <= balance_ratio <= 2.5  # WTF prefers asymmetrical
        }
    
    def _analyze_sharpness(self, img_array):
        """Analyze image sharpness (focus quality)"""
        
        if len(img_array.shape) == 3:
            gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
        else:
            gray = img_array
        
        # Laplacian variance method for sharpness detection
        laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()
        
        # Classify sharpness
        if laplacian_var > 500:
            sharpness_level = 'excellent'
        elif laplacian_var > 200:
            sharpness_level = 'good'
        elif laplacian_var > 100:
            sharpness_level = 'acceptable'
        else:
            sharpness_level = 'poor'
        
        return {
            'laplacian_variance': round(laplacian_var, 1),
            'sharpness_level': sharpness_level,
            'meets_wtf_standard': sharpness_level in ['excellent', 'good']
        }
    
    def _analyze_noise_characteristics(self, img_array):
        """Analyze noise/grain characteristics"""
        
        if len(img_array.shape) == 3:
            gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
        else:
            gray = img_array
        
        # Apply slight blur and subtract from original to estimate noise
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        noise_map = cv2.absdiff(gray, blurred)
        noise_level = np.mean(noise_map)
        
        # Classify noise/grain
        if noise_level < 2:
            noise_classification = 'very_clean'
        elif noise_level < 5:
            noise_classification = 'clean'
        elif noise_level < 10:
            noise_classification = 'film_grain'  # Acceptable for WTF aesthetic
        elif noise_level < 20:
            noise_classification = 'noisy'
        else:
            noise_classification = 'very_noisy'
        
        return {
            'noise_level': round(noise_level, 2),
            'classification': noise_classification,
            'wtf_appropriate': noise_classification in ['clean', 'film_grain']
        }
    
    def generate_quality_report(self, image_path):
        """Generate comprehensive quality report"""
        
        print(f"🔍 WTF QUALITY CONTROL ANALYSIS")
        print(f"📁 Image: {os.path.basename(image_path)}")
        print("=" * 50)
        
        analysis = self.analyze_image_technical_quality(image_path)
        
        if 'error' in analysis:
            print(f"❌ Error: {analysis['error']}")
            return
        
        # Resolution Check
        res = analysis['resolution']
        res_status = "✅" if res['meets_standard'] else "❌"
        print(f"{res_status} Resolution: {res['width']}x{res['height']} ({res['megapixels']}MP)")
        
        # Aspect Ratio Check  
        ratio = analysis['aspect_ratio']
        ratio_status = "✅" if ratio['platform_optimized'] else "⚠️"
        print(f"{ratio_status} Aspect Ratio: {ratio['actual_ratio']} (closest: {ratio['closest_platform']})")
        
        # Brand Colors Check
        colors = analysis['color_analysis']
        brand_colors_found = sum(1 for color in colors['brand_colors'].values() if color['present'])
        color_status = "✅" if brand_colors_found >= 2 else "⚠️"
        print(f"{color_status} Brand Colors: {brand_colors_found}/4 detected")
        
        # Teal-Orange Scheme
        teal_orange = colors['teal_orange_scheme']
        scheme_status = "✅" if teal_orange['detected'] else "⚠️"
        print(f"{scheme_status} Teal-Orange Scheme: {teal_orange['detected']}")
        
        # Contrast Analysis
        contrast = analysis['contrast_analysis']
        contrast_status = "✅" if contrast['meets_wtf_standard'] else "❌"
        print(f"{contrast_status} Lighting Ratio: {contrast['estimated_lighting_ratio']}:1")
        
        # Composition Check
        comp = analysis['composition']
        comp_status = "✅" if comp['rule_of_thirds_score'] > 0.3 else "⚠️"
        print(f"{comp_status} Rule of Thirds: {comp['rule_of_thirds_score']}")
        
        balance_status = "✅" if comp['asymmetrical_balance'] else "⚠️"
        print(f"{balance_status} Asymmetrical Balance: {comp['balance_ratio']}:1")
        
        # Sharpness Check
        sharp = analysis['sharpness']
        sharp_status = "✅" if sharp['meets_wtf_standard'] else "❌"
        print(f"{sharp_status} Sharpness: {sharp['sharpness_level']} ({sharp['laplacian_variance']})")
        
        # Noise Check
        noise = analysis['noise_grain']
        noise_status = "✅" if noise['wtf_appropriate'] else "⚠️"
        print(f"{noise_status} Noise/Grain: {noise['classification']} ({noise['noise_level']})")
        
        # Overall Score
        checks = [
            res['meets_standard'],
            ratio['platform_optimized'],
            brand_colors_found >= 2,
            teal_orange['detected'],
            contrast['meets_wtf_standard'],
            comp['rule_of_thirds_score'] > 0.3,
            comp['asymmetrical_balance'],
            sharp['meets_wtf_standard'],
            noise['wtf_appropriate']
        ]
        
        score = sum(checks) / len(checks) * 100
        
        print("\n" + "=" * 50)
        if score >= 80:
            print(f"🎯 OVERALL SCORE: {score:.0f}% - EXCELLENT")
            print("✅ Meets WTF Agency brand standards")
        elif score >= 60:
            print(f"⚠️ OVERALL SCORE: {score:.0f}% - GOOD")
            print("🔧 Minor adjustments recommended")
        else:
            print(f"❌ OVERALL SCORE: {score:.0f}% - NEEDS IMPROVEMENT")
            print("🚨 Significant rework required")
        
        return analysis

if __name__ == "__main__":
    # Example usage
    qc = WTFQualityControl()
    
    # Test with available images
    test_images = [
        "brief-destroyers-album.png",
        "vogue-editorial-pov.png", 
        "the-agents-hero.png"
    ]
    
    for image_path in test_images:
        if os.path.exists(image_path):
            print(f"\n" + "="*60)
            qc.generate_quality_report(image_path)
            print("\n")
    
    print("🎯 WTF Quality Control System Ready")
    print("   Use: python wtf-quality-control.py [image_path]")
    print("   Integration: ComfyDeploy + Legnext + All workflows")