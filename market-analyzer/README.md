# News-Driven Market Impact & Stock Prediction Analyzer

This project analyzes real-time financial news to assess sentiment and predict short-term stock price movements.  
It combines:
- News sentiment analysis (FinBERT)
- Market data (Yahoo Finance)
- ML prediction models (XGBoost)
- Interactive dashboard (Streamlit)


How code will flow between files:
1.	utils/ → helpers for fetching news & stock data.
2.	data/ → store cached data, maybe preprocessed CSVs.
3.	models/ → sentiment model + ML predictor.
4.	dashboard/ → Streamlit app to display predictions.
5.	main.py → ties everything together (entry point).