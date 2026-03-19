#!/usr/bin/env python3
"""
Live Price Updater for Alinkos Pay
Fetches real-time cryptocurrency prices from CoinGecko API
"""

import requests
import json
import time
from datetime import datetime, timedelta
import random

class LivePriceUpdater:
    def __init__(self):
        self.api_key = None  # CoinGecko API is free for basic usage
        self.base_url = "https://api.coingecko.com/api/v3"
        self.cryptocurrencies = {
            'USDT': 'tether',
            'BTC': 'bitcoin',
            'ETH': 'ethereum',
            'BNB': 'binancecoin',
            'ADA': 'cardano',
            'SOL': 'solana',
            'XRP': 'ripple'
        }
        self.fiat_currencies = {
            'USD': 'usd',
            'EUR': 'eur',
            'GBP': 'gbp',
            'JPY': 'jpy',
            'INR': 'inr'
        }
    
    def get_live_prices(self):
        """Fetch live prices from CoinGecko API"""
        try:
            # Get prices for all cryptocurrencies against USD
            coin_ids = ','.join(self.cryptocurrencies.values())
            url = f"{self.base_url}/simple/price"
            params = {
                'ids': coin_ids,
                'vs_currencies': ','.join(self.fiat_currencies.values()),
                'include_24hr_change': 'true',
                'include_24hr_vol': 'true',
                'include_last_updated_at': 'true'
            }
            
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            # Format the data for our application
            formatted_data = {}
            for symbol, coin_id in self.cryptocurrencies.items():
                if coin_id in data:
                    coin_data = data[coin_id]
                    formatted_data[symbol] = {
                        'name': self.get_coin_name(symbol),
                        'symbol': symbol,
                        'current_price': {
                            'USD': coin_data.get('usd', 0),
                            'EUR': coin_data.get('eur', 0),
                            'GBP': coin_data.get('gbp', 0),
                            'JPY': coin_data.get('jpy', 0),
                            'INR': coin_data.get('inr', 0)
                        },
                        'change_24h': coin_data.get('usd_24h_change', 0),
                        'market_cap': coin_data.get('usd_market_cap', 0),
                        'volume_24h': coin_data.get('usd_24h_vol', 0),
                        'circulating_supply': 0,  # Would need additional API call
                        'last_updated': coin_data.get('last_updated_at', 0),
                        'logo': f"/static/images/{symbol.lower()}-logo.svg"
                    }
            
            return formatted_data
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching live prices: {e}")
            return self.get_fallback_data()
        except Exception as e:
            print(f"Unexpected error: {e}")
            return self.get_fallback_data()
    
    def get_fallback_data(self):
        """Fallback data when API is unavailable"""
        return {
            'USDT': {
                'name': 'Tether',
                'symbol': 'USDT',
                'current_price': {
                    'USD': 1.00,
                    'EUR': 0.92,
                    'GBP': 0.79,
                    'JPY': 110.50,
                    'INR': 92.47
                },
                'change_24h': 0.02,
                'market_cap': 83200000000,
                'volume_24h': 24500000000,
                'circulating_supply': 10087700000,
                'last_updated': datetime.now().isoformat(),
                'logo': "/static/images/usdt-logo.svg"
            }
            # ... other cryptocurrencies with fallback data
        }
    
    def get_coin_name(self, symbol):
        """Get full name for cryptocurrency symbol"""
        names = {
            'USDT': 'Tether',
            'BTC': 'Bitcoin',
            'ETH': 'Ethereum',
            'BNB': 'Binance Coin',
            'ADA': 'Cardano',
            'SOL': 'Solana',
            'XRP': 'Ripple'
        }
        return names.get(symbol, symbol)
    
    def convert_currency(self, amount, from_currency, to_currency):
        """Convert between any two currencies"""
        try:
            # Get live prices
            prices = self.get_live_prices()
            
            # Handle crypto to crypto conversion
            if from_currency in prices and to_currency in prices:
                from_price = prices[from_currency]['current_price']['USD']
                to_price = prices[to_currency]['current_price']['USD']
                return amount * (from_price / to_price)
            
            # Handle crypto to fiat conversion
            elif from_currency in prices and to_currency in self.fiat_currencies:
                return amount * prices[from_currency]['current_price'][to_currency]
            
            # Handle fiat to crypto conversion
            elif to_currency in prices and from_currency in self.fiat_currencies:
                return amount / prices[to_currency]['current_price'][from_currency]
            
            # Handle fiat to fiat conversion (simplified)
            elif from_currency in self.fiat_currencies and to_currency in self.fiat_currencies:
                # Use USD as base for fiat conversion
                usd_rates = {
                    'USD': 1.0,
                    'EUR': 0.92,
                    'GBP': 0.79,
                    'JPY': 110.50,
                    'INR': 92.47
                }
                return amount * (usd_rates[to_currency] / usd_rates[from_currency])
            
            return amount
            
        except Exception as e:
            print(f"Conversion error: {e}")
            return amount
    
    def update_prices_file(self):
        """Update the prices file with live data"""
        try:
            prices = self.get_live_prices()
            
            # Create a JSON file with current prices
            price_data = {
                'timestamp': datetime.now().isoformat(),
                'prices': prices,
                'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
            }
            
            with open('C:/Users/Ketan/OneDrive/Dokumen/live_prices.json', 'w') as f:
                json.dump(price_data, f, indent=2)
            
            print(f"Prices updated at {price_data['last_updated']}")
            return True
            
        except Exception as e:
            print(f"Error updating prices file: {e}")
            return False
    
    def start_auto_update(self, interval_minutes=5):
        """Start automatic price updates"""
        print(f"Starting live price updates every {interval_minutes} minutes...")
        
        while True:
            try:
                self.update_prices_file()
                time.sleep(interval_minutes * 60)
            except KeyboardInterrupt:
                print("Price updater stopped by user")
                break
            except Exception as e:
                print(f"Auto-update error: {e}")
                time.sleep(60)  # Wait 1 minute before retrying

if __name__ == "__main__":
    updater = LivePriceUpdater()
    
    # Test live prices
    print("Testing live price fetching...")
    prices = updater.get_live_prices()
    
    for symbol, data in prices.items():
        print(f"{symbol}: ${data['current_price']['USD']:.2f} USD | ₹{data['current_price']['INR']:.2f} INR")
    
    # Test conversion
    print("\nTesting currency conversion...")
    result = updater.convert_currency(100, 'BTC', 'INR')
    print(f"100 BTC = ₹{result:,.2f}")
    
    # Update prices file
    updater.update_prices_file()
