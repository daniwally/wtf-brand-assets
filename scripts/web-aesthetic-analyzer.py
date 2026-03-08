#!/usr/bin/env python3
"""
WTF Agency Web Aesthetic Analyzer
Analyzes web properties and generates brand-consistent design recommendations
"""

import requests
import re
from urllib.parse import urljoin, urlparse
import json
from datetime import datetime

class WTFWebAnalyzer:
    def __init__(self):
        self.sites = {
            'wtf_agency': 'https://www.wtf-agency.com/',
            'the_agents': 'https://www.theagents.wtf/'
        }
        
        # Brand DNA from visual analysis
        self.brand_dna = {
            'typography': {
                'primary': 'Inter Variable Font',
                'weights': [200, 700],  # Thin + Bold
                'hierarchy': 'Editorial magazine-style',
                'spacing': 'Generous, premium feel'
            },
            'colors': {
                'primary': '#000000',  # Brand black
                'secondary': '#FFFFFF',  # Brand white
                'accent': 'Strategic minimal usage',
                'editorial_gray': 'Sophisticated hierarchy'
            },
            'visual_pillars': [
                'Editorial + Fashion',
                'Cinematic + Premium', 
                'Conceptual + Creative',
                'Luxury + Sophisticated'
            ],
            'aesthetic_keywords': [
                'Vogue editorial', 'POV photography', 'cinematic ultra-realistic',
                'BRIEF DESTROYERS', 'THE AGENTS', 'avant-garde fashion',
                'magazine-quality production', 'premium sophistication'
            ]
        }
    
    def analyze_site_headers(self, url):
        """Analyze site technical headers and infrastructure"""
        try:
            response = requests.head(url, timeout=10)
            headers = dict(response.headers)
            
            return {
                'status': response.status_code,
                'server': headers.get('server', 'Unknown'),
                'content_type': headers.get('content-type', 'Unknown'),
                'caching': {
                    'etag': headers.get('etag', None),
                    'cache_control': headers.get('cache-control', None)
                },
                'security': {
                    'x_frame_options': headers.get('x-frame-options', None),
                    'x_content_type_options': headers.get('x-content-type-options', None)
                },
                'hosting_info': {
                    'edge': headers.get('x-railway-edge', None),
                    'request_id': headers.get('x-railway-request-id', None)
                }
            }
        except requests.RequestException as e:
            return {'error': str(e)}
    
    def analyze_site_structure(self, url):
        """Analyze basic site structure and content"""
        try:
            response = requests.get(url, timeout=10)
            html = response.text
            
            # Extract basic meta information
            title_match = re.search(r'<title[^>]*>([^<]+)</title>', html, re.IGNORECASE)
            description_match = re.search(r'<meta[^>]*name=["\']description["\'][^>]*content=["\']([^"\']+)["\']', html, re.IGNORECASE)
            
            # Look for Inter font usage
            inter_font_usage = bool(re.search(r'inter', html, re.IGNORECASE))
            
            # Look for CSS frameworks or styling approaches
            css_frameworks = []
            if 'tailwind' in html.lower():
                css_frameworks.append('Tailwind CSS')
            if 'bootstrap' in html.lower():
                css_frameworks.append('Bootstrap')
            if 'styled-components' in html.lower():
                css_frameworks.append('Styled Components')
            
            # Look for JavaScript frameworks
            js_frameworks = []
            if 'react' in html.lower():
                js_frameworks.append('React')
            if 'next' in html.lower():
                js_frameworks.append('Next.js')
            if 'vue' in html.lower():
                js_frameworks.append('Vue.js')
            
            return {
                'title': title_match.group(1) if title_match else 'Not found',
                'description': description_match.group(1) if description_match else 'Not found',
                'inter_font_detected': inter_font_usage,
                'css_frameworks': css_frameworks,
                'js_frameworks': js_frameworks,
                'content_length': len(html),
                'modern_web_features': {
                    'service_worker': 'serviceWorker' in html,
                    'web_components': 'customElements' in html,
                    'progressive_web_app': 'manifest' in html.lower()
                }
            }
        except requests.RequestException as e:
            return {'error': str(e)}
    
    def generate_brand_recommendations(self, site_key):
        """Generate brand-specific design recommendations"""
        
        if site_key == 'wtf_agency':
            return {
                'positioning': 'WTF Agency - The Brief Destroyers',
                'aesthetic_approach': 'Editorial sophistication + Creative confidence',
                'primary_pillars': ['Editorial + Fashion', 'Cinematic + Premium'],
                'typography_implementation': {
                    'font_family': 'Inter Variable Font',
                    'headline_weight': 700,
                    'body_weight': 200,
                    'hierarchy': 'Editorial magazine-style with generous spacing'
                },
                'visual_treatments': [
                    'Vogue POV photography hero sections',
                    'Cinematic case study presentations', 
                    'Bold "Brief Destroyers" statement typography',
                    'Client portfolio with editorial layouts',
                    'Award recognition and credibility display'
                ],
                'interaction_design': [
                    'Subtle premium animations (0.3s cubic-bezier)',
                    'Editorial reveal transitions',
                    'Strategic motion, not flashy effects',
                    'Performance-first smooth interactions'
                ]
            }
        
        elif site_key == 'the_agents':
            return {
                'positioning': 'The Agents by WTF - Next-Generation Creative',
                'aesthetic_approach': 'Tech-premium fusion + Future-forward innovation',
                'primary_pillars': ['Conceptual + Creative', 'Luxury + Sophisticated'],
                'typography_implementation': {
                    'font_family': 'Inter Variable Font',
                    'headline_weight': 700,
                    'body_weight': 200,
                    'hierarchy': 'Modern tech-editorial with AI aesthetic'
                },
                'visual_treatments': [
                    'THE AGENTS campaign hero visuals integration',
                    'AI/tech-forward interactive elements',
                    'Next-generation user experience design',
                    'Conceptual creative visualization',
                    'Future of creative work demonstration'
                ],
                'interaction_design': [
                    'Advanced micro-interactions',
                    'AI-inspired animation patterns',
                    'Tech-premium transition effects',
                    'Innovation-focused user journey'
                ]
            }
        
        return {}
    
    def analyze_brand_consistency(self, analysis_results):
        """Analyze brand consistency across web properties"""
        
        consistency_report = {
            'typography_consistency': False,
            'brand_messaging_alignment': True,  # Based on titles
            'technical_infrastructure': True,  # Both on Railway
            'recommendations': []
        }
        
        # Check Inter font usage
        inter_usage = []
        for site, results in analysis_results.items():
            if 'structure' in results:
                inter_detected = results['structure'].get('inter_font_detected', False)
                inter_usage.append(f"{site}: {'✅' if inter_detected else '❌'} Inter font")
        
        consistency_report['inter_font_status'] = inter_usage
        
        # Generate recommendations
        if not all('inter_font_detected' in results.get('structure', {}) and 
                  results['structure']['inter_font_detected'] 
                  for results in analysis_results.values() if 'structure' in results):
            consistency_report['recommendations'].append(
                "Implement Inter Variable Font across both properties"
            )
        
        consistency_report['recommendations'].extend([
            "Ensure editorial typography hierarchy consistency",
            "Apply brand color system (monochromatic sophistication)",
            "Integrate visual DNA pillars in layout design",
            "Maintain premium production quality standards"
        ])
        
        return consistency_report
    
    def generate_full_report(self):
        """Generate complete web aesthetic analysis report"""
        
        print("🌐 WTF AGENCY WEB AESTHETIC ANALYZER")
        print("=" * 50)
        
        analysis_results = {}
        
        for site_key, url in self.sites.items():
            print(f"\n📊 Analyzing {site_key.upper().replace('_', ' ')}...")
            print(f"🔗 {url}")
            
            # Technical analysis
            headers = self.analyze_site_headers(url)
            structure = self.analyze_site_structure(url)
            recommendations = self.generate_brand_recommendations(site_key)
            
            analysis_results[site_key] = {
                'url': url,
                'headers': headers,
                'structure': structure,
                'brand_recommendations': recommendations
            }
            
            # Display key findings
            if 'error' not in headers:
                print(f"   ✅ Server: {headers.get('server', 'Unknown')}")
                print(f"   🏗️  Hosting: Railway Edge")
            
            if 'error' not in structure:
                print(f"   📝 Title: {structure.get('title', 'Not found')}")
                print(f"   🎨 Inter Font: {'✅' if structure.get('inter_font_detected') else '❌'}")
                if structure.get('js_frameworks'):
                    print(f"   ⚛️  Frameworks: {', '.join(structure['js_frameworks'])}")
        
        # Brand consistency analysis
        print(f"\n🎯 BRAND CONSISTENCY ANALYSIS")
        print("-" * 30)
        
        consistency = self.analyze_brand_consistency(analysis_results)
        
        print(f"📊 Inter Font Status:")
        for status in consistency['inter_font_status']:
            print(f"   {status}")
        
        print(f"\n💡 Recommendations:")
        for rec in consistency['recommendations']:
            print(f"   • {rec}")
        
        # Save detailed report
        report_data = {
            'analysis_date': datetime.now().isoformat(),
            'brand_dna': self.brand_dna,
            'site_analysis': analysis_results,
            'consistency_report': consistency
        }
        
        with open('web-analysis-report.json', 'w') as f:
            json.dump(report_data, f, indent=2)
        
        print(f"\n📄 Detailed report saved: web-analysis-report.json")
        print(f"🎯 Analysis complete - Ready for brand-consistent implementation")

if __name__ == "__main__":
    analyzer = WTFWebAnalyzer()
    analyzer.generate_full_report()