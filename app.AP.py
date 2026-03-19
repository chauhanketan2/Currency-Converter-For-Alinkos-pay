"""
Alinkos Pay - Cryptocurrency Trading Platform
A CoinGecko-style crypto market application for USDT/INR trading
"""

from flask import Flask, render_template, jsonify, request
import json
import random
from datetime import datetime, timedelta
import math
import os
import requests

app = Flask(__name__)

# Live price data
def get_live_prices():
    """Fetch live prices from CoinGecko API"""
    try:
        # Get prices for major cryptocurrencies
        url = "https://api.coingecko.com/api/v3/simple/price"
        params = {
            'ids': 'bitcoin,ethereum,tether,binancecoin,cardano,solana,ripple',
            'vs_currencies': 'usd,eur,gbp,jpy,inr',
            'include_24hr_change': 'true',
            'include_24hr_vol': 'true',
            'include_last_updated_at': 'true'
        }
        
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        
        data = response.json()
        
        # Convert to our format
        prices = {
            'BTC': {
                'name': 'Bitcoin',
                'symbol': 'BTC',
                'current_price': 6608946.00 / 93.30,  # Convert from INR to USD
                'change_24h': data['bitcoin']['usd_24h_change'],
                'market_cap': data['bitcoin']['usd_market_cap'],
                'volume_24h': data['bitcoin']['usd_24h_vol'],
                'current_price_inr': 6608946.00,
                'logo': '/static/images/btc-logo.svg'
            },
            'ETH': {
                'name': 'Ethereum',
                'symbol': 'ETH',
                'current_price': data['ethereum']['usd'],
                'change_24h': data['ethereum']['usd_24h_change'],
                'market_cap': data['ethereum']['usd_market_cap'],
                'volume_24h': data['ethereum']['usd_24h_vol'],
                'current_price_inr': data['ethereum']['inr'],
                'logo': '/static/images/eth-logo.svg'
            },
            'USDT': {
                'name': 'Tether',
                'symbol': 'USDT',
                'current_price': 1.00,
                'change_24h': 0.02,
                'market_cap': 83200000000,
                'volume_24h': 24500000000,
                'current_price_inr': 93.30,
                'logo': '/static/images/usdt-logo.svg'
            },
            'BNB': {
                'name': 'Binance Coin',
                'symbol': 'BNB',
                'current_price': data['binancecoin']['usd'],
                'change_24h': data['binancecoin']['usd_24h_change'],
                'market_cap': data['binancecoin']['usd_market_cap'],
                'volume_24h': data['binancecoin']['usd_24h_vol'],
                'current_price_inr': data['binancecoin']['inr'],
                'logo': '/static/images/bnb-logo.svg'
            },
            'ADA': {
                'name': 'Cardano',
                'symbol': 'ADA',
                'current_price': data['cardano']['usd'],
                'change_24h': data['cardano']['usd_24h_change'],
                'market_cap': data['cardano']['usd_market_cap'],
                'volume_24h': data['cardano']['usd_24h_vol'],
                'current_price_inr': data['cardano']['inr'],
                'logo': '/static/images/ada-logo.svg'
            },
            'SOL': {
                'name': 'Solana',
                'symbol': 'SOL',
                'current_price': data['solana']['usd'],
                'change_24h': data['solana']['usd_24h_change'],
                'market_cap': data['solana']['usd_market_cap'],
                'volume_24h': data['solana']['usd_24h_vol'],
                'current_price_inr': data['solana']['inr'],
                'logo': '/static/images/sol-logo.svg'
            },
            'XRP': {
                'name': 'Ripple',
                'symbol': 'XRP',
                'current_price': data['ripple']['usd'],
                'change_24h': data['ripple']['usd_24h_change'],
                'market_cap': data['ripple']['usd_market_cap'],
                'volume_24h': data['ripple']['usd_24h_vol'],
                'current_price_inr': data['ripple']['inr'],
                'logo': '/static/images/xrp-logo.svg'
            }
        }
        
        return prices
        
    except Exception as e:
        print(f"Error fetching live prices: {e}")
        return get_fallback_prices()

def get_fallback_prices():
    """Fallback prices when API is unavailable"""
    return {
        'USDT': {
            'name': 'Tether',
            'symbol': 'USDT',
            'current_price': 1.00,
            'change_24h': 0.02,
            'market_cap': 83200000000,
            'volume_24h': 24500000000,
            'current_price_inr': 93.30,
            'logo': '/static/images/usdt-logo.svg'
        },
        'BTC': {
            'name': 'Bitcoin',
            'symbol': 'BTC',
            'current_price': 6608946.00 / 93.30,  # Convert from INR to USD
            'change_24h': 3.2,
            'market_cap': 84500000000,
            'volume_24h': 12800000000,
            'current_price_inr': 6608946.00,
            'logo': '/static/images/btc-logo.svg'
        },
        'ETH': {
            'name': 'Ethereum',
            'symbol': 'ETH',
            'current_price': 215726.80 / 92.47,  # Convert from INR to USD
            'change_24h': 1.5,
            'market_cap': 26900000000,
            'volume_24h': 8900000000,
            'current_price_inr': 215726.80,
            'logo': '/static/images/eth-logo.svg'
        },
        'BNB': {
            'name': 'Binance Coin',
            'symbol': 'BNB',
            'current_price': 45678.90 / 92.47,  # Convert from INR to USD
            'change_24h': 2.1,
            'market_cap': 45000000000,
            'volume_24h': 1200000000,
            'current_price_inr': 45678.90,
            'logo': '/static/images/bnb-logo.svg'
        },
        'ADA': {
            'name': 'Cardano',
            'symbol': 'ADA',
            'current_price': 45.67 / 92.47,  # Convert from INR to USD
            'change_24h': -0.8,
            'market_cap': 16000000000,
            'volume_24h': 450000000,
            'current_price_inr': 45.67,
            'logo': '/static/images/ada-logo.svg'
        },
        'SOL': {
            'name': 'Solana',
            'symbol': 'SOL',
            'current_price': 14567.89 / 92.47,  # Convert from INR to USD
            'change_24h': 4.2,
            'market_cap': 62000000000,
            'volume_24h': 2800000000,
            'current_price_inr': 14567.89,
            'logo': '/static/images/sol-logo.svg'
        },
        'XRP': {
            'name': 'Ripple',
            'symbol': 'XRP',
            'current_price': 38.45 / 92.47,  # Convert from INR to USD
            'change_24h': 1.8,
            'market_cap': 21000000000,
            'volume_24h': 1200000000,
            'current_price_inr': 38.45,
            'logo': '/static/images/xrp-logo.svg'
        }
    }

def generate_chart_data(symbol, days=30):
    """Generate price chart data for a given cryptocurrency"""
    base_price = {
        'USDT': 92.47,
        'BTC': 6867793 / 92.47,  # Convert back from INR to USD
        'ETH': 215726.80 / 92.47,  # Convert back from INR to USD
        'BNB': 45678.90 / 92.47,  # Convert back from INR to USD
        'ADA': 45.67 / 92.47,  # Convert back from INR to USD
        'SOL': 14567.89 / 92.47,  # Convert back from INR to USD
        'XRP': 38.45 / 92.47  # Convert back from INR to USD
    }
    
    data = []
    current_price = base_price[symbol]
    
    for i in range(days):
        # Generate realistic price movement
        change = random.uniform(-0.05, 0.05)
        price = current_price * (1 + change)
        timestamp = datetime.now() - timedelta(days=days-i)
        data.append({
            'timestamp': timestamp.isoformat(),
            'price': price
        })
        current_price = price
    
    return data

def generate_market_stats():
    """Generate market statistics"""
    return {
        'total_market_cap': 2850000000000,
        'total_volume_24h': 45600000000,
        'market_cap_change_24h': 3.2,
        'volume_change_24h': 8.5,
        'btc_dominance': 52.3,
        'eth_dominance': 18.7,
        'active_cryptos': 24783,
        'active_exchanges': 742
    }

@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')

@app.route('/markets')
def markets_simple():
    """Simple markets route"""
    cryptos = get_live_prices()
    return render_template('markets.html', cryptos=cryptos)

@app.route('/Alinkos-Pay/Market/Page')
def markets():
    """Markets page - USDT/INR focus"""
    cryptos = get_live_prices()
    return render_template('markets.html', cryptos=cryptos)

@app.route('/trade')
def trade_simple():
    """Simple trade route"""
    cryptos = get_live_prices()
    return render_template('trade.html', cryptos=cryptos)

@app.route('/Alinkos-Pay/Trade/Page')
def trade():
    """Trading page"""
    cryptos = get_live_prices()
    return render_template('trade.html', cryptos=cryptos)

@app.route('/converter')
def converter():
    """Currency converter page"""
    return render_template('converter.html')

@app.route('/wallet')
def wallet_simple():
    """Simple wallet route"""
    return render_template('wallet.html')

@app.route('/Alinkos-Pay/Wallet/Page')
def wallet():
    """Wallet page"""
    return render_template('wallet.html')

@app.route('/api/crypto-data')
def api_crypto_data():
    """API endpoint for cryptocurrency data"""
    cryptos = get_live_prices()
    return jsonify(cryptos)

@app.route('/api/chart-data/<symbol>')
def api_chart_data(symbol, days=30):
    """API endpoint for chart data"""
    # Generate realistic chart data based on current price
    try:
        prices = get_live_prices()
        if symbol not in prices:
            return jsonify({'error': 'Cryptocurrency not found'}), 404
        
        current_price = prices[symbol]['current_price']
        data = []
        
        for i in range(days):
            # Generate realistic price movement
            change = random.uniform(-0.05, 0.05)
            price = current_price * (1 + change)
            timestamp = datetime.now() - timedelta(days=days-i)
            data.append({
                'timestamp': timestamp.isoformat(),
                'price': price
            })
            current_price = price
        
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/market-stats')
def api_market_stats():
    """API endpoint for market statistics"""
    try:
        prices = get_live_prices()
        total_market_cap = sum([crypto['market_cap'] for crypto in prices.values()])
        total_volume = sum([crypto['volume_24h'] for crypto in prices.values()])
        
        # Calculate dominance
        btc_dominance = (prices['BTC']['market_cap'] / total_market_cap) * 100 if total_market_cap > 0 else 0
        eth_dominance = (prices['ETH']['market_cap'] / total_market_cap) * 100 if total_market_cap > 0 else 0
        
        return jsonify({
            'total_market_cap': total_market_cap,
            'total_volume_24h': total_volume,
            'market_cap_change_24h': 3.2,
            'volume_change_24h': 8.5,
            'btc_dominance': round(btc_dominance, 2),
            'eth_dominance': round(eth_dominance, 2),
            'active_cryptos': len(prices),
            'active_exchanges': 742,
            'last_updated': datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/convert')
def api_convert():
    """Comprehensive currency conversion API"""
    from_amount = request.args.get('from_amount', 1, type=float)
    from_currency = request.args.get('from_currency', 'USDT')
    to_currency = request.args.get('to_currency', 'INR')
    
    try:
        prices = get_live_prices()
        
        # Handle crypto to crypto conversion
        if from_currency in prices and to_currency in prices:
            from_price = prices[from_currency]['current_price']
            to_price = prices[to_currency]['current_price']
            result = from_amount * (from_price / to_price)
        # Handle crypto to fiat conversion
        elif from_currency in prices and to_currency.upper() in prices[from_currency]:
            result = from_amount * prices[from_currency][f'current_price_{to_currency.lower()}']
        # Handle fiat to crypto conversion
        elif to_currency in prices and from_currency.upper() in prices[to_currency]:
            result = from_amount / prices[to_currency][f'current_price_{from_currency.lower()}']
        else:
            # Handle fiat to fiat conversion (simplified)
            fiat_rates = {
                'USD': 1.0, 'EUR': 0.92, 'GBP': 0.79, 'JPY': 110.50, 'INR': 92.47
            }
            if from_currency.upper() in fiat_rates and to_currency.upper() in fiat_rates:
                result = from_amount * (fiat_rates[to_currency.upper()] / fiat_rates[from_currency.upper()])
            else:
                result = from_amount
        
        return jsonify({
            'from_amount': from_amount,
            'from_currency': from_currency,
            'to_amount': result,
            'to_currency': to_currency,
            'rate': result / from_amount if from_amount != 0 else 1,
            'timestamp': datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/all-conversions')
def api_all_conversions():
    """Get all possible conversions for a given amount"""
    from_amount = request.args.get('amount', 1, type=float)
    from_currency = request.args.get('from_currency', 'USDT')
    
    try:
        prices = get_live_prices()
        currencies = list(prices.keys()) + ['USD', 'EUR', 'GBP', 'JPY', 'INR']
        conversions = []
        
        for to_currency in currencies:
            if from_currency != to_currency:
                try:
                    if from_currency in prices and to_currency in prices:
                        from_price = prices[from_currency]['current_price']
                        to_price = prices[to_currency]['current_price']
                        result = from_amount * (from_price / to_price)
                    elif from_currency in prices and to_currency.upper() in prices[from_currency]:
                        result = from_amount * prices[from_currency][f'current_price_{to_currency.lower()}']
                    elif to_currency in prices and from_currency.upper() in prices[to_currency]:
                        result = from_amount / prices[to_currency][f'current_price_{from_currency.lower()}']
                    else:
                        fiat_rates = {
                            'USD': 1.0, 'EUR': 0.92, 'GBP': 0.79, 'JPY': 110.50, 'INR': 92.47
                        }
                        if from_currency.upper() in fiat_rates and to_currency.upper() in fiat_rates:
                            result = from_amount * (fiat_rates[to_currency.upper()] / fiat_rates[from_currency.upper()])
                        else:
                            result = from_amount
                    
                    conversions.append({
                        'from_currency': from_currency,
                        'to_currency': to_currency,
                        'from_amount': from_amount,
                        'to_amount': result,
                        'rate': result / from_amount if from_amount != 0 else 1
                    })
                except:
                    continue
        
        return jsonify({
            'conversions': conversions,
            'timestamp': datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    import os
    # Production configuration
    port = int(os.environ.get('PORT', 5001))
    app.run(debug=False, host='0.0.0.0', port=port)
