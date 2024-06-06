import pandas as pd
import yfinance as yf
import datetime as dt
import streamlit as st

st.set_page_config(page_title="Stock Market Tracker", page_icon="stock-market-ranking.svg", layout="wide",
                   initial_sidebar_state="auto", menu_items=None)

st.title("Stock Market Tracker")

asset_list = ["PETR4.SA", "VALE3.SA", "MGLU3.SA", "ITSA4.SA"]
date = dt.datetime.today()

with st.container():
    st.header("Enter the requested information:", divider='blue')
    col1, col2, col3 = st.columns(3)
    with col1:
        asset = st.selectbox(label="Desired asset:", options=asset_list)
    with col2:
        start_date = st.date_input(label="Start date:", value=dt.datetime(date.year-1, date.month, date.day))
    with col3:
        end_date = st.date_input(label="End date:", value=date)

df = yf.download(asset, start=start_date, end=end_date)

last_update = df.index.max()
last_price = round(df.loc[df.index.max(), "Adj Close"], 2)
first_price = round(df.loc[df.index.min(), "Adj Close"], 2)
min_price = round(df["Adj Close"].min(), 2)
max_price = round(df["Adj Close"].max(), 2)
delta = round(((last_price - first_price) / first_price) * 100, 2)

with st.container():
    with col1:
        st.metric(f"Last Update - {last_update}", "R$ {:,.2f}".format(last_price), f"{delta}%")
    with col2:
        st.metric("Lowest price of the period",  "R$ {:,.2f}".format(min_price))
    with col3:
        st.metric("Highest price of the period", "R$ {:,.2f}".format(max_price))

with st.container():
    st.area_chart(df[["Adj Close"]])
    st.line_chart(df[["Low", "Adj Close", "High"]], color=["#0000ff", "#00ff00", "#ff0000"])