#!/bin/bash

# WTF Brand Assets Upload Script
# Makes it easy to upload brand assets to GitHub

echo "🎯 WTF BRAND ASSETS UPLOAD"
echo "========================="

cd ~/wtf-brand-local

# Check Git status
echo "📊 Checking current status..."
git status

echo ""
echo "📁 Files ready to upload:"
git status --porcelain

# Ask for confirmation
echo ""
read -p "🚀 Upload these files to GitHub? (y/n): " -n 1 -r
echo ""

if [[ $REPLY =~ ^[Yy]$ ]]
then
    echo "📤 Adding files..."
    git add .
    
    echo "📝 Enter commit message (or press Enter for default):"
    read -r commit_message
    
    if [ -z "$commit_message" ]; then
        commit_message="Add WTF brand assets - $(date +%Y-%m-%d)"
    fi
    
    echo "💾 Committing with message: $commit_message"
    git commit -m "$commit_message"
    
    echo "🚀 Pushing to GitHub..."
    git push origin main
    
    if [ $? -eq 0 ]; then
        echo ""
        echo "✅ SUCCESS! Brand assets uploaded to GitHub"
        echo "🔗 Check: https://github.com/daniwally/wtf-brand-assets"
        echo ""
        
        # Trigger sync to Oscar's workflows
        echo "🔄 Syncing to Oscar's workflows..."
        cd /home/ubuntu/.openclaw/workspace-oscar/wtf-brand-assets && python3 scripts/sync-to-workflows.py
        
        echo ""
        echo "🎯 COMPLETE! Brand assets now available in all AI workflows"
    else
        echo "❌ ERROR: Upload failed. Check network connection."
    fi
else
    echo "⏸️  Upload cancelled."
fi

echo ""
echo "📋 FOLDERS FOR UPLOAD:"
echo "   ~/wtf-brand-local/key-visuals/hero-templates/"
echo "   ~/wtf-brand-local/key-visuals/campaign-references/"
echo "   ~/wtf-brand-local/key-visuals/style-guides/"  
echo "   ~/wtf-brand-local/colors/"