import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

def fetch_nvidia_price():
    # Create a Ticker object for Nvidia
    nvda = yf.Ticker("NVDA")
    
    # Get today's date
    end_date = datetime.now()
    # Get date from 7 days ago
    start_date = end_date - timedelta(days=7)
    
    # Fetch the historical data for the last 7 days
    hist = nvda.history(start=start_date, end=end_date)
    
    if hist.empty:
        return "No data available"
    
    # Get the latest closing price
    latest_close = hist['Close'].iloc[-1]
    
    # Calculate daily change
    daily_change = ((latest_close - hist['Close'].iloc[-2]) / hist['Close'].iloc[-2]) * 100
    
    return {
        'price': round(latest_close, 2),
        'change_percent': round(daily_change, 2),
        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

if __name__ == "__main__":
    try:
        result = fetch_nvidia_price()
        if isinstance(result, dict):
            print(f"Nvidia (NVDA) Stock Price:")
            print(f"Price: ${result['price']}")
            print(f"Daily Change: {result['change_percent']}%")
            print(f"Last Updated: {result['date']}")
        else:
            print(result)
    except Exception as e:
        print(f"Error fetching stock price: {str(e)}")
