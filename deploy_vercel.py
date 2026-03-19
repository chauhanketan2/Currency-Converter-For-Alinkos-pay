#!/usr/bin/env python3
"""
Alinkos Pay - Vercel Deployment Script
Automated deployment to Vercel platform
"""

import os
import sys
import subprocess
import json

def check_files():
    """Check if all required files exist"""
    required_files = [
        'app.py',
        'requirements.txt', 
        'vercel.json',
        'static/',
        'templates/'
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    return missing_files

def check_vercel_config():
    """Check Vercel configuration"""
    try:
        with open('vercel.json', 'r') as f:
            config = json.load(f)
        
        print("📋 Vercel Configuration:")
        print(f"   ✅ Version: {config.get('version')}")
        print(f"   ✅ Source: {config['builds'][0]['src']}")
        print(f"   ✅ Routes: {config['routes'][0]['src']} → {config['routes'][0]['dest']}")
        print(f"   ✅ Runtime: {config['functions']['app.py']['runtime']}")
        return True
    except Exception as e:
        print(f"❌ Vercel config error: {e}")
        return False

def check_requirements():
    """Check requirements.txt"""
    try:
        with open('requirements.txt', 'r') as f:
            requirements = f.read().strip()
        
        print("📦 Python Requirements:")
        for req in requirements.split('\n'):
            if req.strip():
                print(f"   ✅ {req.strip()}")
        return True
    except Exception as e:
        print(f"❌ Requirements error: {e}")
        return False

def main():
    print("🚀 Alinkos Pay - Vercel Deployment Check")
    print("=" * 60)
    
    # Check files
    missing = check_files()
    if missing:
        print("❌ Missing files:")
        for file in missing:
            print(f"   - {file}")
        print("\nPlease ensure all files are present before deployment.")
        return False
    
    # Check configurations
    vercel_ok = check_vercel_config()
    req_ok = check_requirements()
    
    if vercel_ok and req_ok:
        print("\n✅ All checks passed! Ready for Vercel deployment.")
        print("\n🎯 Next Steps:")
        print("1. Install Vercel CLI: npm install -g vercel")
        print("2. Login to Vercel: vercel login")
        print("3. Deploy: vercel --prod")
        print("4. Your site will be live at: https://your-project.vercel.app")
        print("\n📋 Files ready:")
        print("   ✅ app.py (Flask application)")
        print("   ✅ requirements.txt (Dependencies)")
        print("   ✅ vercel.json (Configuration)")
        print("   ✅ static/ (Assets)")
        print("   ✅ templates/ (HTML)")
        
        print("\n🌟 Your website is ready for global deployment!")
    else:
        print("\n❌ Some checks failed. Please fix issues before deploying.")
    
    print("=" * 60)

if __name__ == "__main__":
    main()
