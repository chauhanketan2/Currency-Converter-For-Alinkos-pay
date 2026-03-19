# Alinkos Pay - Cryptocurrency Trading Platform

A CoinGecko-style crypto market application with USDT/INR trading focus, built with Flask and modern web technologies.

## 🚀 Features

### Core Functionality
- **Real-time Price Tracking**: Live cryptocurrency prices with automatic updates
- **USDT/INR Focus**: Specialized trading pair with competitive rates
- **Interactive Charts**: 24H, 7D, 1M, 1Y price charts with multiple timeframes
- **Currency Converter**: Real-time crypto-to-fiat conversion
- **Market Statistics**: Comprehensive market data and analytics
- **Responsive Design**: Mobile-friendly interface with Bootstrap 5
- **Live Updates**: Auto-refresh prices every 5 seconds

### Key Features
- **Market Overview**: Total market cap, volume, dominance metrics
- **Crypto Table**: Sortable table with price changes, market cap, volume
- **Sparkline Charts**: Mini price charts for each cryptocurrency
- **Converter Tool**: Instant currency conversion with real-time rates
- **Professional UI**: Modern, clean interface inspired by CoinGecko

## 🛠️ Technology Stack

### Backend
- **Flask**: Python web framework
- **Bootstrap 5**: Responsive UI framework
- **Chart.js**: Interactive charting library
- **Font Awesome**: Icon library
- **REST API**: JSON endpoints for data and conversion

### Frontend
- **HTML5/CSS3**: Modern semantic markup
- **JavaScript ES6+**: Interactive functionality
- **Bootstrap 5**: Mobile-first responsive design
- **AJAX**: Asynchronous data fetching

### Data Features
- **Mock Data**: Realistic cryptocurrency data generation
- **Real-time Updates**: Simulated live price feeds
- **Conversion API**: Multi-currency conversion support
- **Chart Data**: Historical price data generation

## 📁 Project Structure

```
alinkos_pay/
├── app.py                 # Main Flask application
├── requirements.txt         # Python dependencies
├── README.md             # Project documentation
├── templates/            # HTML templates
│   ├── layout.html       # Base layout template
│   ├── index.html        # Home page
│   └── markets.html      # Markets page
└── static/              # Static assets
    ├── css/
    │   └── style.css    # Custom styles
    └── js/
        └── main.js      # JavaScript functionality
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
```bash
git clone <repository-url>
cd alinkos_pay
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the application**
```bash
python app.py
```

5. **Access the application**
- Open browser and go to: `http://localhost:5001`
- Home page: `http://localhost:5001/`
- Markets page: `http://localhost:5001/markets`

## 📊 API Endpoints

### Cryptocurrency Data
- **GET** `/api/crypto-data`
- Returns: JSON with all cryptocurrency data
- Includes: Price, market cap, volume, 24h change

### Chart Data
- **GET** `/api/chart-data/<symbol>`
- Parameters: `days` (default: 30)
- Returns: Historical price data for charts

### Market Statistics
- **GET** `/api/market-stats`
- Returns: Market-wide statistics and metrics

### Currency Converter
- **GET** `/api/convert`
- Parameters: `from_amount`, `from_currency`, `to_currency`
- Returns: Conversion result with timestamp

## 🎨 Pages

### Home Page (`/`)
- **Hero Section**: Eye-catching introduction with key crypto prices
- **Features Grid**: Platform capabilities and benefits
- **Statistics**: Trading volume, active users, uptime
- **CTA Section**: Call-to-action for user registration

### Markets Page (`/markets`)
- **Market Overview**: Key statistics cards with live updates
- **Crypto Table**: Comprehensive market data with sparklines
- **Converter Tool**: Real-time currency conversion
- **About Section**: Platform features and information

## 🎯 Key Features Demonstrated

### Design & UX
- **CoinGecko-style Interface**: Professional crypto market design
- **Responsive Layout**: Mobile and desktop optimized
- **Interactive Elements**: Hover effects, animations, transitions
- **Modern UI**: Clean, contemporary design language

### Technical Implementation
- **RESTful APIs**: Well-structured backend endpoints
- **Real-time Updates**: Live price feeds and data refresh
- **Data Visualization**: Interactive charts and sparklines
- **Currency Conversion**: Multi-currency support with live rates

### Production Features
- **Error Handling**: Graceful error management and user feedback
- **Performance**: Optimized loading and smooth interactions
- **Scalability**: Modular code structure for easy expansion
- **Security**: Input validation and safe data handling

## 🔧 Configuration

### Environment Variables
```bash
FLASK_ENV=development
FLASK_DEBUG=True
FLASK_HOST=0.0.0.0
FLASK_PORT=5001
```

### Customization
- **Add Cryptocurrencies**: Update mock data in `app.py`
- **Modify Styling**: Edit `static/css/style.css`
- **Change Rates**: Update conversion rates in API
- **Add Features**: Extend templates and JavaScript

## 📱 Mobile Responsiveness

- **Breakpoints**: 576px, 768px, 992px, 1200px
- **Touch-friendly**: Optimized for mobile interactions
- **Performance**: Fast loading on all devices
- **Accessibility**: Semantic HTML and ARIA labels

## 🚀 Deployment

### Development
```bash
python app.py
```

### Production (with Gunicorn)
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5001 app:app
```

### Docker (optional)
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5001
CMD ["python", "app.py"]
```

## 🔮 Future Enhancements

### Phase 1: Real Data Integration
- Connect to real cryptocurrency APIs (CoinGecko, CoinMarketCap)
- Implement WebSocket for real-time price updates
- Add historical data caching and storage

### Phase 2: Advanced Features
- User authentication and portfolio tracking
- Trading interface and order management
- Price alerts and notifications
- Advanced charting with technical indicators

### Phase 3: Platform Expansion
- Mobile app development (React Native)
- API rate limiting and caching
- Multi-language support
- Advanced security features

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📞 Support

For questions and support:
- Create an issue in the repository
- Check the documentation and code comments
- Review the API endpoints for integration examples

---

**Built with ❤️ for the cryptocurrency community**
