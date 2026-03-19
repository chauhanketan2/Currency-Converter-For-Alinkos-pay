#!/usr/bin/env python3
"""
Alinkos Pay - Public Launch Script
Makes your website accessible to everyone on your network
"""

import os
import sys
import socket
import subprocess
import webbrowser
import sys
sys.path.append('.')
exec(open('app.ap.py').read())

def get_local_ip():
    """Get the local IP address"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

def check_port(port):
    """Check if port is available"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('localhost', port))
    sock.close()
    return result == 0

def main():
    print("🚀 Alinkos Pay - Public Launch")
    print("=" * 50)
    
    # Get local IP
    local_ip = get_local_ip()
    port = 5001
    
    print(f"📡 Local IP: {local_ip}")
    print(f"🔌 Port: {port}")
    
    # Check if port is available
    if check_port(port):
        print(f"⚠️  Port {port} is already in use!")
        print("Please stop the existing server first.")
        return
    
    print("\n🌐 Access URLs:")
    print(f"   Local:    http://127.0.0.1:{port}")
    print(f"   Network:  http://{local_ip}:{port}")
    
    print("\n📱 Share this link with others:")
    print(f"   http://{local_ip}:{port}")
    
    print("\n🔧 Firewall Note:")
    print("   Make sure port 5001 is allowed through Windows Firewall")
    print("   Others on your network can now access your site!")
    
    print("\n🎯 Starting server...")
    print("   Press Ctrl+C to stop the server")
    print("=" * 50)
    
    try:
        # Open browser for local testing
        webbrowser.open(f'http://127.0.0.1:{port}')
        
        # Start Flask app
        app.run(host='0.0.0.0', port=port, debug=False)
        
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
    except Exception as e:
        print(f"❌ Error starting server: {e}")

if __name__ == "__main__":
    main()
