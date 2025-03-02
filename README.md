# 📊 STOCKSENSE - AI-Powered Stock Analysis & Recommendations

STOCKSENSE is a **stock analysis and recommendation** web application built using **Streamlit**, **yfinance**, and **Gemini AI**. It provides **real-time stock data**, **AI-driven insights**, and **interactive visualizations** to help users make informed investment decisions. 

---

## 🚀 Features

✅ **Real-Time Stock Data** – Fetch live stock prices, historical trends, and key financial metrics using `yfinance`.  
✅ **AI-Powered Recommendations** – Gemini AI analyzes market trends and provides investment suggestions.  
✅ **Interactive Charts & Visualizations** – Stock price movements, technical indicators, and historical trends.  
✅ **Theming & UI Customization** – Dark mode support, custom styling, and improved UI with Streamlit theming.  
✅ **User-Friendly Interface** – Simple, intuitive, and easy-to-use layout.  

---

## 📈 Stock Analysis & AI Recommendations

STOCKSENSE leverages **Yahoo Finance (`yfinance`)** for financial data and **Gemini AI** for stock recommendations. The AI analyzes:

📌 **Historical Price Trends** – Detects patterns and movements over time.  
📌 **Technical Indicators** – Uses **Moving Averages, RSI, Bollinger Bands**, and more.  
📌 **Market Sentiment** – Evaluates financial news and market conditions.  
📌 **Risk Assessment** – Predicts stock volatility and future trends.  

Based on this analysis, **STOCKSENSE provides AI-powered Buy/Hold/Sell recommendations**.

---

## 🔑 Setting Up the Gemini API Key

STOCKSENSE requires a **Gemini API key** to access AI-powered stock recommendations.  

### 1️⃣ **Get a Gemini API Key**
1. Visit **[Gemini AI](https://ai.google.dev/)**.
2. Sign in with your Google account.
3. Navigate to the API Key section.
4. Generate a new API key and **copy** it.

### 2️⃣ **Store the API Key in `./streamlit/secrets.toml`**
```toml
GEMINI_API_KEY = "YOUR API KEY"
```

---

## 🛠 Installation

### 1️⃣ **Clone the Repository**
```sh
git clone https://github.com/yourusername/STOCKSENSE.git
cd STOCKSENSE
```

### 2️⃣ **Create a Virtual Environment (Optional)**
```sh
python -m venv venv
source venv/bin/activate  # On Windows: `venv\Scripts\activate`
```

### 3️⃣ **Install Dependencies**
```sh
pip install -r requirements.txt
```

### 4️⃣ **Run the Application**
```sh
streamlit run main.py
```

---