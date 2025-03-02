import pandas as pd
import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

def get_stock_data(symbol, period='1y'):
    """Fetch stock data from Yahoo Finance"""
    try:
        stock = yf.Ticker(symbol)
        hist = stock.history(period=period)
        info = stock.info
        return hist, info
    except Exception as e:
        st.error(f"Error fetching data for {symbol}: {str(e)}")
        return None, None

def format_number(number):
    """Format large numbers with K, M, B suffixes"""
    if number is None:
        return "N/A"

    if isinstance(number, str):
        return number

    if number >= 1_000_000_000:
        return f"{number/1_000_000_000:.2f}B"
    elif number >= 1_000_000:
        return f"{number/1_000_000:.2f}M"
    elif number >= 1_000:
        return f"{number/1_000:.2f}K"
    else:
        return f"{number:.2f}"

def get_key_metrics(info):
    """Extract key metrics from stock info"""
    metrics = {
        'Market Cap': format_number(info.get('marketCap')),
        'PE Ratio': format_number(info.get('trailingPE')),
        'EPS': format_number(info.get('trailingEps')),
        '52 Week High': format_number(info.get('fiftyTwoWeekHigh')),
        '52 Week Low': format_number(info.get('fiftyTwoWeekLow')),
        'Volume': format_number(info.get('volume')),
        'Avg Volume': format_number(info.get('averageVolume')),
        'Dividend Yield': f"{info.get('dividendYield', 0)*100:.2f}%" if info.get('dividendYield') else 'N/A'
    }
    return pd.DataFrame(list(metrics.items()), columns=['Metric', 'Value'])

def create_price_chart(data, symbol):
    """Create an interactive price chart using Plotly"""
    fig = go.Figure(data=[go.Candlestick(x=data.index,
                open=data['Open'],
                high=data['High'],
                low=data['Low'],
                close=data['Close'])])

    fig.update_layout(
        title=f'{symbol} Stock Price',
        yaxis_title='Price (USD)',
        template='plotly_white',
        xaxis_rangeslider_visible=False,
        height=500
    )

    return fig