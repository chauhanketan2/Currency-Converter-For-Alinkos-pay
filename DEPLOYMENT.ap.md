# 🚀 Alinkos Pay - Deployment Guide

## 📋 Quick Start

### Method 1: Local Network Access
```bash
# Navigate to project directory
cd C:/Users/Ketan/alinkos_pay

# Start production server
python start_production.py
```

### Method 2: Direct Flask Run
```bash
# Navigate to project directory
cd C:/Users/Ketan/alinkos_pay

# Run in production mode
python app.py
```

## 🌐 Access URLs

Once running, the site will be available at:

- **Local Access**: `http://localhost:5001`
- **Network Access**: `http://YOUR_IP_ADDRESS:5001`
- **Home Page**: `http://localhost:5001/`
- **Trade Page**: `http://localhost:5001/Alinkos-Pay/Trade/Page`
- **Wallet Page**: `http://localhost:5001/Alinkos-Pay/Wallet/Page`

## 🔧 Finding Your IP Address

### Windows
```bash
# Open Command Prompt and run:
ipconfig
# Look for "IPv4 Address" under your active network adapter
```

### Alternative Method
```bash
# Check public IP (for external access)
curl ifconfig.me
```

## 📱 Mobile & Other Device Access

1. **Connect to same network** as the server computer
2. **Find server IP** using methods above
3. **Access via browser**: `http://SERVER_IP:5001`
4. **Full functionality available** on all devices

## 🔒 Security Notes

- ✅ **Debug mode disabled** for production
- ✅ **Host set to 0.0.0.0** for network access
- ✅ **Port 5001** configured
- ⚠️ **Firewall may need configuration** for external access

## 🌍 Public Deployment Options

### Option 1: Local Network (Recommended for testing)
- Perfect for team/family access
- No internet required
- Full functionality

### Option 2: Cloud Services
- **Heroku**: Free tier available
- **PythonAnywhere**: Python hosting
- **DigitalOcean**: VPS hosting
- **AWS EC2**: Cloud server

### Option 3: Static Hosting
- Export as static files
- Host on Netlify/Vercel
- Limited functionality (no real-time updates)

## 🎯 Current Features Available

### ✅ Working Features
- **Real-time price updates** (every 5 seconds)
- **Currency converter** with live rates
- **Trading interface** with order book
- **Wallet management** with portfolio view
- **Responsive design** for all devices
- **Live data** for USDT/INR, BTC/INR, ETH/INR

### 📊 Current Prices
- **USDT/INR**: ₹92.47
- **BTC/INR**: ₹68,67,793
- **ETH/INR**: ₹2,15,727

## 🚀 Ready to Launch

Your Alinkos Pay site is **production-ready** and can be accessed by anyone on your network!
