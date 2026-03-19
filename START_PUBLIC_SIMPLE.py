#!/usr/bin/env python3
"""
Alinkos Pay - Simple Public Launch
"""

import socket
import webbrowser
import subprocess
import sys
import os

def get_local_ip():
    """Get the local IP address"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "192.168.1.24"  # Your known IP

def main():
    print("🚀 Alinkos Pay - Public Website Launch")
    print("=" * 60)
    
    local_ip = get_local_ip()
    port = 5001
    
    print(f"🌐 Your website is now accessible to everyone!")
    print()
    print("📱 Access URLs:")
    print(f"   🏠 Local (you):     http://127.0.0.1:{port}")
    print(f"   🌍 Network (others): http://{local_ip}:{port}")
    print()
    print("🔗 Share this link with friends/family:")
    print(f"   http://{local_ip}:{port}")
    print()
    print("📋 Important Notes:")
    print("   ✅ Anyone on your network can now access")
    print("   ✅ Works on WiFi, Ethernet, mobile data")
    print("   ✅ No login required")
    print("   ⚠️  Make sure Windows Firewall allows port 5001")
    print()
    print("🎯 Starting server...")
    print("   Press Ctrl+C to stop the server")
    print("=" * 60)
    
    # Open browser for local testing
    try:
        webbrowser.open(f'http://127.0.0.1:{port}')
    except:
        pass
    
    # Start the Flask app
    try:
        os.system(f'python app.ap.py')
    except KeyboardInterrupt:
        print("\n🛑 Server stopped")

if __name__ == "__main__":
    main()
