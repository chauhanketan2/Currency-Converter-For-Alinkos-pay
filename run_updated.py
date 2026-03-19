#!/usr/bin/env python3
"""
Run the updated Alinkos Pay site
"""

import subprocess
import sys
import os

def main():
    """Run the updated application"""
    print("Starting Updated Alinkos Pay...")
    print("New Features Added:")
    print("- BNB (Binance Coin) support")
    print("- ADA (Cardano) support")
    print("- Updated price changes")
    print("- Enhanced crypto showcase")
    print("=" * 50)
    
    # Change to the correct directory
    os.chdir('C:/Users/Ketan/OneDrive/Dokumen')
    
    # Run the application
    try:
        subprocess.run([sys.executable, 'app.ap.py'], check=True)
    except KeyboardInterrupt:
        print("\nServer stopped by user")
    except Exception as e:
        print(f"Error starting server: {e}")

if __name__ == "__main__":
    main()
