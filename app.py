import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Supermarket Sales Dashboard", layout="wide")

# Load dataset
df = pd.read_csv("SuperMarket Analysis.csv")

st.title("🛒 Supermarket Sales Dashboard")

# Show dataset
st.subheader("📌 Dataset Preview")
st.dataframe(df.head())

# -----------------------------
# 1️⃣ Total Sales by City
# -----------------------------
st.subheader("🏙️ Total Sales by City")

fig, ax = plt.subplots(figsize=(8, 4))
sns.barplot(data=df, x='City', y='Sales', estimator=sum, ax=ax)
plt.xticks(rotation=20)
st.pyplot(fig)

# -----------------------------
# 2️⃣ Product Line Sales Distribution
# -----------------------------
st.subheader("📦 Sales by Product Line")

fig2, ax2 = plt.subplots(figsize=(8, 4))
sns.barplot(data=df, x='Product line', y='Sales', estimator=sum, ax=ax2)
plt.xticks(rotation=30)
st.pyplot(fig2)

# -----------------------------
# 3️⃣ Rating Distribution (Boxplot)
# -----------------------------
st.subheader("⭐ Customer Rating Distribution")

fig3, ax3 = plt.subplots(figsize=(6, 4))
sns.boxplot(data=df, x='Branch', y='Rating', ax=ax3)
st.pyplot(fig3)

# -----------------------------
# 4️⃣ Heatmap - Correlation
# -----------------------------
st.subheader("🔥 Correlation Heatmap")

corr = df[['Unit price', 'Quantity', 'Tax 5%', 'Sales', 'cogs', 'gross income', 'Rating']].corr()

fig4, ax4 = plt.subplots(figsize=(8, 5))
sns.heatmap(corr, annot=True, cmap='YlGnBu', ax=ax4)
st.pyplot(fig4)

# -----------------------------
# 5️⃣ Monthly Sales (if Date column present)
# -----------------------------
st.subheader("📅 Sales Over Time")

df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.to_period('M')

monthly = df.groupby('Month')['Sales'].sum()

fig5, ax5 = plt.subplots(figsize=(8, 4))
monthly.plot(ax=ax5, marker='o')
ax5.set_title("Monthly Sales Trend")
st.pyplot(fig5)

