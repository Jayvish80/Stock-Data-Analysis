import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestRegressor


# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="AI Stock Investment Analyzer",
    page_icon="🤖",
    layout="wide"
)


# =====================================================
# TITLE
# =====================================================

st.title("🤖 AI Stock Investment Analysis Dashboard")

st.markdown(
    """
    Upload historical stock market data and receive a
    data-driven technical analysis signal.
    """
)


# =====================================================
# UPLOAD CSV
# =====================================================

uploaded_file = st.file_uploader(
    "📂 Upload Stock Market CSV File",
    type=["csv"]
)


if uploaded_file is None:

    st.info(
        "👆 Upload your CSV file to start AI stock analysis."
    )

    st.stop()


# =====================================================
# LOAD DATA
# =====================================================

df = pd.read_csv(uploaded_file)


# =====================================================
# CLEAN COLUMN NAMES
# =====================================================

df.columns = (
    df.columns
    .str.strip()
)


# =====================================================
# DATE PROCESSING
# =====================================================

if "DATE" in df.columns:

    df["DATE"] = pd.to_datetime(
        df["DATE"],
        errors="coerce"
    )

    df = df.sort_values(
        "DATE"
    )


# =====================================================
# NUMERIC COLUMN CLEANING
# =====================================================

numeric_columns = [

    "OPEN",
    "HIGH",
    "LOW",
    "PREV. CLOSE",
    "LTP",
    "CLOSE",
    "VWAP",
    "52W H",
    "52W L",
    "VOLUME",
    "VALUE",
    "NO. OF  TRADES"

]


for column in numeric_columns:

    if column in df.columns:

        df[column] = (

            df[column]
            .astype(str)
            .str.replace(",", "", regex=False)
            .str.replace("₹", "", regex=False)

        )

        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )


# =====================================================
# FEATURE ENGINEERING
# =====================================================

df["RETURN"] = (
    df["CLOSE"]
    .pct_change()
    * 100
)


# Moving Averages

df["MA20"] = (
    df["CLOSE"]
    .rolling(20)
    .mean()
)


df["MA50"] = (
    df["CLOSE"]
    .rolling(50)
    .mean()
)


df["MA200"] = (
    df["CLOSE"]
    .rolling(200)
    .mean()
)


# Volatility

df["VOLATILITY"] = (

    df["RETURN"]
    .rolling(20)
    .std()

)


# =====================================================
# RSI CALCULATION
# =====================================================

delta = df["CLOSE"].diff()

gain = delta.where(
    delta > 0,
    0
)

loss = -delta.where(
    delta < 0,
    0
)


average_gain = (
    gain
    .rolling(14)
    .mean()
)


average_loss = (
    loss
    .rolling(14)
    .mean()
)


rs = (
    average_gain
    /
    average_loss
)


df["RSI"] = (
    100
    -
    (
        100
        /
        (1 + rs)
    )
)


# =====================================================
# VOLUME AVERAGE
# =====================================================

df["VOLUME_MA20"] = (

    df["VOLUME"]
    .rolling(20)
    .mean()

)


# =====================================================
# REMOVE MISSING VALUES
# =====================================================

df = df.dropna()


# =====================================================
# CURRENT DATA
# =====================================================

latest = df.iloc[-1]


current_price = latest["CLOSE"]

ma20 = latest["MA20"]

ma50 = latest["MA50"]

rsi = latest["RSI"]

volatility = latest["VOLATILITY"]

current_volume = latest["VOLUME"]

average_volume = latest["VOLUME_MA20"]


# =====================================================
# TECHNICAL SCORE
# =====================================================

score = 0

reasons = []


# -----------------------------------------------------
# TREND SCORE
# -----------------------------------------------------

if current_price > ma20:

    score += 1

    reasons.append(
        "Price is above the 20-day moving average."
    )

else:

    score -= 1

    reasons.append(
        "Price is below the 20-day moving average."
    )


if current_price > ma50:

    score += 1

    reasons.append(
        "Price is above the 50-day moving average."
    )

else:

    score -= 1

    reasons.append(
        "Price is below the 50-day moving average."
    )


# -----------------------------------------------------
# RSI SCORE
# -----------------------------------------------------

if rsi < 30:

    score += 2

    reasons.append(
        "RSI indicates an oversold condition."
    )

elif rsi > 70:

    score -= 2

    reasons.append(
        "RSI indicates an overbought condition."
    )

else:

    reasons.append(
        "RSI is in a neutral zone."
    )


# -----------------------------------------------------
# VOLUME SCORE
# -----------------------------------------------------

if current_volume > average_volume:

    score += 1

    reasons.append(
        "Trading volume is above its 20-day average."
    )

else:

    reasons.append(
        "Trading volume is below its 20-day average."
    )


# =====================================================
# FINAL SIGNAL
# =====================================================

if score >= 3:

    signal = "🟢 BUY / ACCUMULATE"

    signal_description = (
        "The technical indicators show a relatively positive setup. "
        "Consider waiting for confirmation and managing risk."
    )


elif score <= -2:

    signal = "🔴 AVOID / BEARISH"

    signal_description = (
        "The technical indicators show weakness. "
        "Waiting for stronger confirmation may be preferable."
    )


else:

    signal = "🟡 HOLD / WAIT"

    signal_description = (
        "The indicators are mixed. "
        "Waiting for a clearer trend may reduce uncertainty."
    )


# =====================================================
# KPI DASHBOARD
# =====================================================

st.subheader("📊 Current Stock Analysis")


col1, col2, col3, col4, col5 = st.columns(5)


col1.metric(
    "Current Price",
    f"₹{current_price:,.2f}"
)


col2.metric(
    "RSI",
    f"{rsi:.2f}"
)


col3.metric(
    "20-Day MA",
    f"₹{ma20:,.2f}"
)


col4.metric(
    "50-Day MA",
    f"₹{ma50:,.2f}"
)


col5.metric(
    "AI Score",
    f"{score}"
)


# =====================================================
# SIGNAL
# =====================================================

st.divider()

st.header("🤖 AI Technical Signal")

st.subheader(signal)

st.info(signal_description)


# =====================================================
# SIGNAL EXPLANATION
# =====================================================

st.subheader("🔍 Why This Signal?")


for reason in reasons:

    st.write(
        "• " + reason
    )


# =====================================================
# BUY ZONE / RISK LEVEL
# =====================================================

st.divider()

st.header("🎯 Price Analysis")


# Possible entry zone

entry_low = min(
    current_price,
    ma20
)


entry_high = max(
    current_price,
    ma20
)


# Stop loss

stop_loss = ma50 * 0.97


# Target

target_price = current_price * 1.10


col1, col2, col3 = st.columns(3)


col1.metric(
    "Possible Entry Zone",
    f"₹{entry_low:,.2f} - ₹{entry_high:,.2f}"
)


col2.metric(
    "Illustrative Risk Level",
    f"₹{stop_loss:,.2f}"
)


col3.metric(
    "Illustrative Target",
    f"₹{target_price:,.2f}"
)


st.warning(
    """
    These levels are illustrative calculations based on historical
    technical indicators and are not guaranteed future prices.
    """
)


# =====================================================
# PRICE + MOVING AVERAGES
# =====================================================

st.header("📈 AI Technical Chart")


fig = go.Figure()


fig.add_trace(
    go.Scatter(
        x=df["DATE"],
        y=df["CLOSE"],
        name="Close Price"
    )
)


fig.add_trace(
    go.Scatter(
        x=df["DATE"],
        y=df["MA20"],
        name="20-Day MA"
    )
)


fig.add_trace(
    go.Scatter(
        x=df["DATE"],
        y=df["MA50"],
        name="50-Day MA"
    )
)


fig.update_layout(
    title="Price Trend with Moving Averages",
    xaxis_title="Date",
    yaxis_title="Price",
    height=600
)


st.plotly_chart(
    fig,
    use_container_width=True
)


# =====================================================
# RSI CHART
# =====================================================

st.header("📊 RSI Momentum Analysis")


rsi_fig = go.Figure()


rsi_fig.add_trace(
    go.Scatter(
        x=df["DATE"],
        y=df["RSI"],
        name="RSI"
    )
)


rsi_fig.add_hline(
    y=70,
    line_dash="dash",
    annotation_text="Overbought"
)


rsi_fig.add_hline(
    y=30,
    line_dash="dash",
    annotation_text="Oversold"
)


rsi_fig.update_layout(
    title="Relative Strength Index",
    yaxis_title="RSI",
    height=450
)


st.plotly_chart(
    rsi_fig,
    use_container_width=True
)


# =====================================================
# VOLUME ANALYSIS
# =====================================================

st.header("📊 Volume Confirmation")


volume_fig = go.Figure()


volume_fig.add_trace(
    go.Bar(
        x=df["DATE"],
        y=df["VOLUME"],
        name="Trading Volume"
    )
)


volume_fig.add_trace(
    go.Scatter(
        x=df["DATE"],
        y=df["VOLUME_MA20"],
        name="Average Volume"
    )
)


volume_fig.update_layout(
    title="Trading Volume vs Average Volume",
    height=500
)


st.plotly_chart(
    volume_fig,
    use_container_width=True
)


# =====================================================
# VOLATILITY
# =====================================================

st.header("⚠️ Risk and Volatility")


volatility_fig = px.line(
    df,
    x="DATE",
    y="VOLATILITY",
    title="20-Day Rolling Volatility"
)


st.plotly_chart(
    volatility_fig,
    use_container_width=True
)


# =====================================================
# DATA TABLE
# =====================================================

st.header("📋 AI Analysis Dataset")


st.dataframe(
    df.tail(50),
    use_container_width=True
)