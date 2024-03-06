import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

hours_df = pd.DataFrame({
    'hr': range(24),
    'cnt': np.random.randint(0, 1000, size=24)
})

days_df = pd.DataFrame({
    'mnth': range(1, 13),
    'cnt': np.random.randint(0, 10000, size=12)
})

st.title('Bike Rental Analysis')

st.subheader('Number of Bicycle Rentals per Hour')
plt.figure(figsize=(10, 6))
plt.bar(hours_df['hr'], hours_df['cnt'], color="#FA8072")
plt.title('Number of Bicycle Rentals per Hour', loc="center", fontsize=15)
plt.xlabel('Hour')
plt.ylabel('Rent Amount')
plt.xticks(hours_df['hr'])
plt.grid(axis='y', linestyle='--')
st.pyplot(plt)

st.subheader('Number of Bicycle Rentals per Month')
monthly_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
days_df.index = monthly_order

plt.figure(figsize=(10, 5))
plt.bar(days_df.index, days_df['cnt'], color="#FA8072")
plt.title("Number of Bicycle Rentals per Month", loc="center", fontsize=15)
plt.xlabel("Month")
plt.ylabel("Rent Amount")
plt.xticks(rotation=30, fontsize=10)
plt.grid(axis='y', linestyle='--')
st.pyplot(plt)
