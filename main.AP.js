// Alinkos Pay - Main JavaScript

// Initialize sparkline charts
function createSparkline(canvasId, data, color) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    
    const ctx = canvas.getContext('2d');
    const width = canvas.width;
    const height = canvas.height;
    
    // Generate sparkline data
    const points = 20;
    const step = width / points;
    
    ctx.strokeStyle = color;
    ctx.lineWidth = 2;
    ctx.beginPath();
    
    for (let i = 0; i < points; i++) {
        const x = i * step;
        const y = height / 2 + (Math.random() - 0.5) * height * 0.6;
        
        if (i === 0) {
            ctx.moveTo(x, y);
        } else {
            ctx.lineTo(x, y);
        }
    }
    
    ctx.stroke();
}

// Initialize market stats
async function loadMarketStats() {
    try {
        const response = await fetch('/api/market-stats');
        const stats = await response.json();
        
        // Update market stats with animation
        updateStatWithAnimation('totalMarketCap', formatCurrency(stats.total_market_cap));
        updateStatWithAnimation('totalVolume', formatCurrency(stats.total_volume_24h));
        updateStatWithAnimation('btcDominance', stats.btc_dominance + '%');
        updateStatWithAnimation('activeCryptos', stats.active_cryptos.toLocaleString());
        
    } catch (error) {
        console.error('Error loading market stats:', error);
    }
}


function updateStatWithAnimation(elementId, finalValue) {
    const element = document.getElementById(elementId);
    if (!element) return;
    
    const originalValue = element.textContent;
    const isPercentage = originalValue.includes('%');
    const isCurrency = originalValue.includes('₹') || originalValue.includes('B') || originalValue.includes('K');
    
    let numericValue = finalValue.replace(/[^0-9.]/g, '');
    let current = 0;
    const increment = parseFloat(numericValue) / 50;
    
    const timer = setInterval(() => {
        current += increment;
        if (current >= parseFloat(numericValue)) {
            current = parseFloat(numericValue);
            clearInterval(timer);
        }
        
        let displayValue = current.toFixed(isCurrency && !isPercentage ? 0 : 1);
        if (isCurrency) {
            if (numericValue >= 1000000000) {
                displayValue = (current / 1000000000).toFixed(1) + 'B+';
            } else if (numericValue >= 1000) {
                displayValue = (current / 1000).toFixed(0) + 'K+';
            } else {
                displayValue = current.toFixed(0);
            }
            displayValue = '₹' + displayValue;
        } else if (isPercentage) {
            displayValue = displayValue + '%';
        }
        
        element.textContent = displayValue;
    }, 20);
}


function formatCurrency(value) {
    if (value >= 1000000000) {
        return '₹' + (value / 1000000000).toFixed(1) + 'B+';
    } else if (value >= 1000) {
        return '₹' + (value / 1000).toFixed(0) + 'B';
    } else {
        return '₹' + value.toFixed(0);
    }
}

// Converter functionality
async function initializeConverter() {
    const form = document.getElementById('converterForm');
    if (!form) return;
    
    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const fromAmount = parseFloat(document.getElementById('fromAmount').value);
        const fromCurrency = document.getElementById('fromCurrency').value;
        const toCurrency = document.getElementById('toCurrency').value;
        
        try {
            const response = await fetch(`/api/convert?from_amount=${fromAmount}&from_currency=${fromCurrency}&to_currency=${toCurrency}`);
            const data = await response.json();
            
            document.getElementById('toAmount').value = data.to_amount.toFixed(2);
            
            const resultDiv = document.getElementById('conversionResult');
            document.getElementById('resultText').textContent = 
                `${data.from_amount} ${data.from_currency} = ${data.to_amount.toFixed(2)} ${data.to_currency}`;
            document.getElementById('timestamp').textContent = `Updated: ${new Date(data.timestamp).toLocaleString()}`;
            
            resultDiv.style.display = 'block';
            
        } catch (error) {
            console.error('Conversion error:', error);
        }
    });
}

// Auto-update crypto prices
async function initializePriceUpdates() {
    try {
        const response = await fetch('/api/crypto-data');
        const data = await response.json();
        
        // Update table prices
        Object.keys(data).forEach(symbol => {
            const row = document.querySelector(`[data-symbol="${symbol}"]`);
            if (row) {
                const priceCell = row.querySelector('.current-price');
                const changeCell = row.querySelector('.change');
                
                const newPrice = data[symbol].current_price;
                const oldPrice = window.cryptosData ? window.cryptosData[symbol].current_price : newPrice;
                const change = oldPrice ? ((newPrice - oldPrice) / oldPrice) * 100 : data[symbol].change_24h;
                
                // Update price (convert to INR for non-USDT)
                const inrPrice = symbol !== 'USDT' ? newPrice * 92.47 : newPrice;
                priceCell.textContent = `₹${inrPrice.toFixed(2)}`;
                
                // Update change
                changeCell.className = `change ${change > 0 ? 'positive' : 'negative'}`;
                changeCell.innerHTML = `<i class="fas fa-caret-${change > 0 ? 'up' : 'down'}"></i>${Math.abs(change).toFixed(2)}%`;
            }
        });
        
        // Update global data
        window.cryptosData = data;
        
        // Update sparklines
        updateSparklines();
        
    } catch (error) {
        console.error('Update error:', error);
    }
}

// Update sparklines with current data
function updateSparklines() {
    if (!window.cryptosData) return;
    
    Object.keys(window.cryptosData).forEach(symbol => {
        const color = window.cryptosData[symbol].change_24h > 0 ? '#10b981' : '#ef4444';
        createSparkline(`sparkline-${symbol}`, [], color);
    });
}

// Initialize sparklines
function initializeSparklines() {
    if (!window.cryptosData) return;
    
    Object.keys(window.cryptosData).forEach(symbol => {
        const color = window.cryptosData[symbol].change_24h > 0 ? '#10b981' : '#ef4444';
        createSparkline(`sparkline-${symbol}`, [], color);
    });
}

// Page initialization
document.addEventListener('DOMContentLoaded', function() {
    // Load initial data
    loadMarketStats();
    initializeConverter();
    
    // Initialize sparklines after a short delay
    setTimeout(() => {
        initializeSparklines();
        initializePriceUpdates();
    }, 100);
    
    // Set up price updates every 5 seconds
    setInterval(initializePriceUpdates, 5000);
});

// Export functions for global access
window.AlinkosPay = {
    createSparkline,
    loadMarketStats,
    formatCurrency
};
