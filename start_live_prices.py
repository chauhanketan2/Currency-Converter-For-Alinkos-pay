#!/usr/bin/env python3
"""
Live Price Updater for Alinkos Pay
This script fetches live prices and keeps them updated automatically
"""

import threading
import time
import requests
from datetime import datetime

def update_prices_continuously():
    """Update prices every 5 minutes"""
    while True:
        try:
            # Fetch live prices
            url = "https://api.coingecko.com/api/v3/simple/price"
            params = {
                'ids': 'bitcoin,ethereum,tether,binancecoin,cardano,solana,ripple',
                'vs_currencies': 'usd,eur,gbp,jpy,inr',
                'include_24hr_change': 'true',
                'include_24hr_vol': 'true',
                'include_last_updated_at': 'true'
            }
            
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            print(f"✅ Live prices updated at {timestamp}")
            print(f"   BTC: ${data['bitcoin']['usd']:,.2f} | ₹{data['bitcoin']['inr']:,.2f}")
            print(f"   ETH: ${data['ethereum']['usd']:,.2f} | ₹{data['ethereum']['inr']:,.2f}")
            print(f"   USDT: ${1.00:.2f} | ₹{data['tether']['inr']:,.2f}")
            print(f"   BNB: ${data['binancecoin']['usd']:,.2f} | ₹{data['binancecoin']['inr']:,.2f}")
            print(f"   ADA: ${data['cardano']['usd']:,.2f} | ₹{data['cardano']['inr']:,.2f}")
            print(f"   SOL: ${data['solana']['usd']:,.2f} | ₹{data['solana']['inr']:,.2f}")
            print(f"   XRP: ${data['ripple']['usd']:,.2f} | ₹{data['ripple']['inr']:,.2f}")
            print("-" * 50)
            
            # Wait 5 minutes before next update
            time.sleep(300)
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Error fetching prices: {e}")
            print("⏳ Retrying in 1 minute...")
            time.sleep(60)
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            time.sleep(60)

if __name__ == "__main__":
    print("🚀 Starting Live Price Updater for Alinkos Pay")
    print("📡 Fetching live prices from CoinGecko API")
    print("⏰ Updates every 5 minutes")
    print("🔄 Press Ctrl+C to stop")
    print("=" * 50)
    
    try:
        update_prices_continuously()
    except KeyboardInterrupt:
        print("\n⏹️  Price updater stopped by user")
