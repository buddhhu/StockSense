import streamlit as st
from utils import get_stock_data, get_key_metrics, create_price_chart
from styles import apply_custom_styles
from ai_recommendations import analyze_stock_data, format_recommendation

def format_number(num):
    return f"{num:,}"

st.set_page_config(
    page_title="Stock Data Visualization",
    page_icon="📈",
    layout="wide"
)

apply_custom_styles()

# Header
st.title("📈 Stock Data Visualization")
st.markdown("Enter a stock symbol to view financial data and AI-powered recommendations")

# Input section
col1, col2 = st.columns([2, 1])
with col1:
    symbol = st.text_input("Enter Stock Symbol (e.g., AAPL)", value="AAPL").upper()
with col2:
    period = st.selectbox(
        "Select Time Period",
        options=["1mo", "3mo", "6mo", "1y", "2y", "5y"],
        index=3
    )

# Main content
if symbol:
    with st.spinner(f'Fetching data for {symbol}...'):
        hist_data, stock_info = get_stock_data(symbol, period)

        if hist_data is not None and stock_info is not None:
            current_price = stock_info.get('currentPrice', 0) or stock_info.get("open", 0)
            previous_close = stock_info.get('previousClose', 0)
            price_change = current_price - previous_close
            price_change_pct = (price_change / previous_close) * 100 if previous_close else 0

            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric(
                    "Current Price",
                    f"${current_price:.2f}",
                    f"{price_change:+.2f} ({price_change_pct:+.2f}%)"
                )
            with col2:
                st.metric("Trading Volume", f"{stock_info.get('volume', 0):,}")
            with col3:
                st.metric("Market Cap", f"${stock_info.get('marketCap', 0)/1e9:.2f}B")

            st.plotly_chart(create_price_chart(hist_data, symbol), use_container_width=True)

            with st.spinner('Generating AI analysis...'):
                analysis = analyze_stock_data(hist_data, symbol, stock_info)
                format_recommendation(analysis)

            st.subheader("Key Financial Metrics")
            metrics_df = get_key_metrics(stock_info)
            st.dataframe(metrics_df, use_container_width=True)

            st.subheader("Historical Data")
            hist_df = hist_data.reset_index()
            hist_df['Date'] = hist_df['Date'].dt.date
            st.dataframe(hist_df, use_container_width=True)

            col1, col2 = st.columns(2)
            with col1:
                csv_metrics = metrics_df.to_csv(index=False).encode('utf-8')
                st.download_button(
                    "Download Metrics CSV",
                    csv_metrics,
                    f"{symbol}_metrics.csv",
                    "text/csv",
                    key='metrics_download'
                )

            with col2:
                csv_hist = hist_df.to_csv(index=False).encode('utf-8')
                st.download_button(
                    "Download Historical Data CSV",
                    csv_hist,
                    f"{symbol}_historical_data.csv",
                    "text/csv",
                    key='historical_download'
                )
        else:
            st.error("Unable to fetch stock data. Please check the symbol and try again.")

# Footer
st.markdown("---")
st.markdown("Data provided by Yahoo Finance | AI Analysis powered by Gemini")