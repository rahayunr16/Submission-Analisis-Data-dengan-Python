# -*- coding: utf-8 -*-
"""dashboardbikesharing.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fOKu79NyF77s-rG2Y54dpTa7pEYBz3yN
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def create_user_v_season_df(day1_df):
    user_v_season = day1_df.groupby("season", as_index=False)["total_rentals"].sum()
    return user_v_season_df

def day_summary_df(day1_df):
    day_summary = day1_df.groupby("working_day", as_index=False)["total_rentals"].sum()
    return day_summary_df

def day_summary1_df(day1_df):
    day_summary1 = day1_df.groupby('weather_condition', as_index=False)['total_rentals'].sum()
    return day_summary1_df
    
def hour_summary1(hour1_df):
    hour_summary1 = hour1_df.groupby('weather_condition', as_index=False)['total_rentals'].sum()
    return hour_summary1_df

order = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
def day_summary2_df(day1_df):
    day_summary2 = day1_df.groupby('weekday', as_index=False)['total_rentals'].sum()
    day_summary2['weekday'] = pd.Categorical(day_summary2['weekday'], categories=order, ordered=True)
    day_summary2 = day_summary2.sort_values('weekday')
    return day_summary2_df

def month_summary_df(day1_df):
    day1_df['month'] = day1_df['month'].astype(str)
    month_summary = day1_df.groupby('month', as_index=False)['total_rentals'].sum()
    month_summary = month_summary.dropna(subset=['month'])
    order = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    month_summary['month'] = pd.Categorical(month_summary['month'], categories=order, ordered=True)
    month_summary = month_summary.sort_values('month')
    return month_summary_df

def user_counts_df(day1_df):
    user_counts = [day1_df['registered_users'].sum(), day1_df['casual_users'].sum()]
    return user_counts_df

def hourly_rentals_df(hour1_df):
    hourly_rentals = hour_df.groupby('hour', as_index=False)['total_rentals'].sum()
    return hourly_rentals_df

def create_monthly_orders_df(day1_df):
    day1_df['date'] = pd.to_datetime(day1_df['date'])
    monthly_orders_df = day1_df.resample(rule='ME', on='date').agg({
        "registered_users": "nunique",
        "casual_users":"nunique",
        "total_rentals": "sum"
    })
    monthly_orders_df.index = monthly_orders_df.index.strftime('%Y-%m')
    monthly_orders_df = monthly_orders_df.reset_index()
    monthly_orders_df.head()
    return monthly_orders_df

day1_df = pd.read_csv("day1_data.csv")
hour1_df = pd.read_csv("hour1_data.csv")
day1_df["date"] = pd.to_datetime(day1_df["date"])
hour1_df["date"] = pd.to_datetime(hour1_df["date"])

min_date = day1_df["date"].min()
max_date = day1_df["date"].max()

min_date = min_date.date()
max_date = max_date.date()

with st.sidebar:

    start_date, end_date = st.date_input(
        label ='Filter Rentang Waktu', min_value = min_date, max_value= max_date,
        value = [min_date, max_date]
    )
main_df = day1_df [ (day1_df["date"] >= str(start_date)) &
                    (day1_df["date"] <= str(end_date) ) ]

with st.sidebar:

    min_hour = 0
    max_hour = 23
    start_hour, end_hour = st.slider(
        label='Rentang Jam dalam Sehari',
        min_value=min_hour,
        max_value=max_hour,
        value=[min_hour, max_hour],
        step=1
    )
    
filtered_df = hour1_df[(hour1_df["hour"] >= start_hour) & 
                     (hour1_df["hour"] <= end_hour)]

st.header('DASHBOARD BIKE-SHARING RENTALS')


st.subheader("Pola Musiman pada Total Penyewaan Sepeda")

fig, ax = plt.subplots(figsize=(6, 6))

graph = sns.barplot(
    data=user_v_season,
    x='season',
    y='total_rentals',
    ax=ax
)

for i in graph.containers:
    graph.bar_label(i, fmt="%d", fontsize=12, color="black")

plt.xlabel("Season", fontsize=12)
plt.ylabel("Total Rentals", fontsize=12)

st.pyplot(fig)

st.subheader("Perbandingan Total Penyewaan Sepeda pada Hari Kerja vs Akhir Pekan")

fig, ax = plt.subplots(figsize=(8, 6))  
colors = ["#D9534F", "#BBD2E2"]

graph = sns.barplot(
    data=day_summary,
    x="working_day",
    y="total_rentals",
    hue="working_day",
    palette=colors,
    legend=False,
    ax=ax
)

for i in graph.containers:
    graph.bar_label(i, fmt="%d", fontsize=12, color="black")

plt.title("Hubungan Hari Kerja dengan Total Penyewaan", fontsize=14)
plt.xlabel("Hari Kerja", fontsize=12)
plt.ylabel("Total Penyewaan", fontsize=12)

st.pyplot(fig)

st.subheader("Pengaruh Kondisi Cuaca pada Total Penyewaan Sepeda")

daycolors = ['#FFD700', '#B0C4DE', '#4682B4']
hourcolors = ['#FFD700', '#B0C4DE', '#4682B4', '#2F4F4F']

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

graph1 = sns.barplot(
    ax=axes[0],
    data=day_summary1,
    x='weather_condition',
    y='total_rentals',
    hue='weather_condition',
    palette=daycolors,
    legend=False
)

axes[0].set_title('Hubungan Cuaca & Total Penyewaan berdasarkan hari', fontsize=14)
axes[0].set_xlabel('Kondisi Cuaca', fontsize=12)
axes[0].set_ylabel('Total Penyewaan', fontsize=12)

for i in graph1.containers:
    graph1.bar_label(i, fmt="%d", fontsize=12, color="black")

graph2 = sns.barplot(
    ax=axes[1],
    data=hour_summary1,
    x='weather_condition',
    y='total_rentals',
    hue='weather_condition',
    palette=hourcolors,
    legend=False
)

axes[1].set_title('Hubungan Cuaca & Total Penyewaan berdasarkan jam', fontsize=14)
axes[1].set_xlabel('Kondisi Cuaca', fontsize=12)
axes[1].set_ylabel('Total Penyewaan', fontsize=12)

for i in graph2.containers:
    graph2.bar_label(i, fmt="%d", fontsize=12, color="black")

plt.tight_layout()
st.pyplot(fig)

st.subheader("Total Penyewaan Sepeda dalam Seminggu")

fig, ax = plt.subplots(figsize=(8, 6))

colors = ['#FF1493', '#FF5733', '#FF8D1A', '#FFD700', '#32CD32', '#1E90FF', '#8A2BE2']

graph = sns.barplot(
    data=day_summary2,
    x='weekday',
    y='total_rentals',
    hue='weekday',
    palette=colors,
    legend=False,
    ax=ax
)
   
for i in graph.containers:
    graph.bar_label(i, fmt="%d", fontsize=12, color="black")

plt.xlabel("Hari dalam Seminggu", fontsize=12)
plt.ylabel("Total Penyewaan", fontsize=12)

st.pyplot(fig)
 
st.subheader("Total Penyewaan Sepeda per Bulan")

fig, ax = plt.subplots(figsize=(10, 6))

colors = sns.color_palette("pastel", 12)

graph = sns.barplot(
    data=month_summary,
    x='month',
    y='total_rentals',
    palette=colors,
    ax=ax
)

for i in graph.containers:
    graph.bar_label(i, fmt="%d", fontsize=11, color="black", label_type="edge", padding=3)

plt.xticks(rotation=45, ha="right")

plt.title("Hubungan Bulan dengan Total Penyewaan", fontsize=14)
plt.xlabel("Bulan", fontsize=12)
plt.ylabel("Total Penyewaan", fontsize=12)

plt.tight_layout()
st.pyplot(fig)

   
st.subheader("Rasio Total dari Pengguna Terdaftar dan Pengguna Kasual")

fig, ax = plt.subplots(figsize=(7, 7))

plt.pie(
    user_counts,
    labels=labels,
    autopct='%1.1f%%',
    colors=colors,
    startangle=90,
    wedgeprops={'edgecolor': 'black'}
)

plt.title("Perbandingan Pengguna Terdaftar vs Pengguna Kasual", fontsize=14)

plt.axis('equal')

st.pyplot(fig)
   
st.subheader("Tren Total Penyewaan Sepeda dari Waktu ke Waktu")

fig, ax = plt.subplots(figsize=(10, 5))

sns.lineplot(
    data=hour_df.groupby('hour', as_index=False)['total_rentals'].sum(),
    x='hour',
    y='total_rentals',
    marker='o',  # Tambahkan titik di setiap jam
    color='royalblue',  # Warna garis
    linewidth=2,
    ax=ax
)

ax.set_title('Tren Penyewaan Sepeda per Jam', fontsize=14)
ax.set_xlabel('Jam dalam Sehari', fontsize=12)
ax.set_ylabel('Total Penyewaan', fontsize=12)

ax.grid(axis='y', linestyle='--', alpha=0.7)

st.pyplot(fig)


fig, ax = plt.subplots(figsize=(12, 6))

sns.lineplot(
    data=monthly_rentals, 
    x='year_month', 
    y='total_rentals', 
    marker='o', 
    color='b',
    ax=ax
)

ax.set_title('Tren Total Penyewaan Per Bulan (2011-2012)', fontsize=14)
ax.set_xlabel('Bulan', fontsize=12)
ax.set_ylabel('Total Penyewaan', fontsize=12)

plt.xticks(rotation=45)

ax.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()

st.pyplot(fig)
