# Nvidia Stock Price Fetcher

A simple Python script to fetch and display the current stock price for Nvidia (NVDA).

## Features

- Fetches real-time Nvidia stock price data
- Displays current price and daily percentage change
- Shows last update timestamp
- Uses Yahoo Finance API through `yfinance` package

## Installation

1. Clone this repository:
```bash
git clone https://github.com/uvaaland/nvdia_price.git
cd nvdia_price
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

Simply run the script:
```bash
python fetch_price.py
```

The script will display:
- Current stock price
- Daily price change (as a percentage)
- Last update timestamp

## Example Output

```
Nvidia (NVDA) Stock Price:
Price: $547.21
Daily Change: 2.15%
Last Updated: 2025-01-30 13:10:45
```

## Requirements

- Python 3.6 or higher
- Dependencies listed in `requirements.txt`:
  - yfinance
  - pandas

## License

This project is open source and available under the MIT License.