import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

# reading files
df_reviews      = pd.read_csv("datasets/customer reviews.csv")
df_top100_books = pd.read_csv("datasets/Top-100 Trending Books.csv")

# getting max and min price
price_max = df_top100_books["book price"].max()
price_min = df_top100_books["book price"].min()

# sidebar slider to filter df_top100_books
selected_price = st.sidebar.slider("Price Range", price_min, price_max, price_max)
df_books       = df_top100_books[df_top100_books["book price"] <= selected_price]
df_books

# graphs related to df_books
graph1 = px.bar(df_books["year of publication"].value_counts())
graph2 = px.histogram(df_books["book price"])
col1, col2 = st.columns(2)
col1.plotly_chart(graph1)
col2.plotly_chart(graph2)