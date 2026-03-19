@echo off
title Alinkos Pay - Public Website
color 0A
echo.
echo ========================================
echo    🚀 Alinkos Pay - Public Website
echo ========================================
echo.
echo 🌐 Making your website accessible to everyone!
echo.
echo 📱 Your website will be available at:
echo    🏠 Local (you):     http://127.0.0.1:5001
echo    🌍 Network (others): http://192.168.1.24:5001
echo.
echo 🔗 Share this link with friends/family:
echo    http://192.168.1.24:5001
echo.
echo ✅ Anyone on your network can now access
echo ✅ Works on WiFi, Ethernet, mobile data
echo ✅ No login required
echo.
echo ⚠️  Make sure Windows Firewall allows port 5001
echo.
echo 🎯 Starting server...
echo    Press Ctrl+C to stop the server
echo ========================================
echo.
python START_PUBLIC_SIMPLE.py
pause
