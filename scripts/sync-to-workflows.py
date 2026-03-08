#!/usr/bin/env python3
"""
WTF Brand Assets - Sync to Workflows
Synchronizes brand assets to Oscar's generation workflows
"""

import os
import shutil
from pathlib import Path

def sync_brand_assets():
    """Sync brand assets to all workflow directories"""
    
    # Source: brand assets repo
    source_dir = Path(__file__).parent.parent
    
    # Destinations: workflow directories  
    destinations = [
        '../elementos-comfydeploy/brand-assets/',
        '../legnext-demo/brand-assets/',
        '../output/brand-assets/'
    ]
    
    print("🎯 WTF Brand Assets Sync")
    print("=" * 30)
    
    for dest in destinations:
        dest_path = source_dir / dest
        dest_path.mkdir(parents=True, exist_ok=True)
        
        print(f"📁 Syncing to: {dest}")
        
        # Copy logos
        if (source_dir / 'logos').exists():
            shutil.copytree(
                source_dir / 'logos', 
                dest_path / 'logos', 
                dirs_exist_ok=True
            )
            
        # Copy typography  
        if (source_dir / 'typography').exists():
            shutil.copytree(
                source_dir / 'typography',
                dest_path / 'typography',
                dirs_exist_ok=True
            )
            
        # Copy colors
        if (source_dir / 'colors').exists():
            shutil.copytree(
                source_dir / 'colors',
                dest_path / 'colors', 
                dirs_exist_ok=True
            )
            
        print(f"   ✅ Synced to {dest}")
    
    print("\n🚀 Brand assets synchronized!")
    print("   All workflows now have access to latest brand assets")

if __name__ == "__main__":
    sync_brand_assets()