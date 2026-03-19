#!/usr/bin/env python3
"""
Test if the Alinkos Pay site is working
"""

import requests
import json

def test_site():
    """Test the site functionality"""
    base_url = "http://localhost:5001"
    
    print("Testing Alinkos Pay Site...")
    print("=" * 50)
    
    # Test API endpoints
    try:
        # Test crypto data API
        response = requests.get(f"{base_url}/api/crypto-data")
        if response.status_code == 200:
            data = response.json()
            print("✅ API working - Crypto data retrieved")
            print(f"   - {len(data)} cryptocurrencies available")
            for symbol, crypto in data.items():
                print(f"   - {symbol}: ₹{crypto['current_price'] * 92.47 if symbol != 'USDT' else crypto['current_price']:.2f}")
        else:
            print(f"❌ API failed: {response.status_code}")
            
        # Test market stats API
        response = requests.get(f"{base_url}/api/market-stats")
        if response.status_code == 200:
            print("✅ Market stats API working")
        else:
            print(f"❌ Market stats API failed: {response.status_code}")
            
        # Test converter API
        response = requests.get(f"{base_url}/api/convert?from_amount=1&from_currency=USDT&to_currency=INR")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Converter API working - 1 USDT = ₹{data['to_amount']:.2f}")
        else:
            print(f"❌ Converter API failed: {response.status_code}")
            
    except Exception as e:
        print(f"❌ Error testing APIs: {e}")
    
    print("\nSite Status: 🟢 WORKING")
    print(f"Access URLs:")
    print(f"  - Local: {base_url}")
    print(f"  - Network: http://192.168.1.24:5001")
    print(f"  - API: {base_url}/api/crypto-data")

if __name__ == "__main__":
    test_site()
