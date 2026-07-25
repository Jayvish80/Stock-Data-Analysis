import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="AI Stock Market Analysis",
    page_icon="📈",
    layout="wide"
)


# =====================================================
# TITLE
# =====================================================

st.title("📈 AI Stock Market Analysis Dashboard")

st.markdown(
    """
    Upload your stock market CSV file and analyze price trends,
    volume, returns, technical indicators, risk, and correlations.
    """
)


# =====================================================
# CSV UPLOAD
# =====================================================

uploaded_file = st.file_uploader(
    "📂 Upload Stock Market CSV File",
    type=["csv"]
)


if uploaded_file is None:

    st.info("👆 Please upload a CSV file to start analysis.")

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
# DATE CLEANING
# =====================================================

if "DATE" in df.columns:

    df["DATE"] = pd.to_datetime(
        df["DATE"],
        errors="coerce"
    )

    df = df.sort_values(
        by="DATE"
    )


# =====================================================
# NUMERIC DATA CLEANING
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
            .str.strip()

        )

        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )


# =====================================================
# FEATURE ENGINEERING
# =====================================================

# Daily Return

df["DAILY RETURN (%)"] = (

    df["CLOSE"]
    .pct_change()
    * 100

)


# Price Change

df["PRICE CHANGE"] = (

    df["CLOSE"]
    -
    df["PREV. CLOSE"]

)


# Intraday Range

df["INTRADAY RANGE"] = (

    df["HIGH"]
    -
    df["LOW"]

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


# Rolling Volatility

df["VOLATILITY"] = (

    df["DAILY RETURN (%)"]
    .rolling(20)
    .std()

)


# Volume Moving Average

df["VOLUME MA20"] = (

    df["VOLUME"]
    .rolling(20)
    .mean()

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

average_gain = gain.rolling(14).mean()

average_loss = loss.rolling(14).mean()

rs = average_gain / average_loss

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
# SIDEBAR FILTERS
# =====================================================

st.sidebar.header("🔍 Filters")


min_date = df["DATE"].min()

max_date = df["DATE"].max()


start_date = st.sidebar.date_input(
    "Start Date",
    min_date
)


end_date = st.sidebar.date_input(
    "End Date",
    max_date
)


filtered_df = df[

    (df["DATE"] >= pd.to_datetime(start_date))
    &
    (df["DATE"] <= pd.to_datetime(end_date))

]


# =====================================================
# KPI SECTION
# =====================================================

st.header("📊 Key Performance Indicators")


latest_price = filtered_df["CLOSE"].iloc[-1]

highest_price = filtered_df["HIGH"].max()

lowest_price = filtered_df["LOW"].min()

average_volume = filtered_df["VOLUME"].mean()

total_return = (

    (
        filtered_df["CLOSE"].iloc[-1]
        /
        filtered_df["CLOSE"].iloc[0]
    )
    - 1

) * 100


col1, col2, col3, col4, col5 = st.columns(5)


col1.metric(
    "Latest Price",
    f"₹{latest_price:,.2f}"
)


col2.metric(
    "Highest Price",
    f"₹{highest_price:,.2f}"
)


col3.metric(
    "Lowest Price",
    f"₹{lowest_price:,.2f}"
)


col4.metric(
    "Average Volume",
    f"{average_volume:,.0f}"
)


col5.metric(
    "Total Return",
    f"{total_return:.2f}%"
)


st.divider()


# =====================================================
# TABS
# =====================================================

tab1, tab2, tab3, tab4, tab5 = st.tabs(

    [
        "📈 Price Charts",
        "📊 Volume Charts",
        "📉 Returns & Risk",
        "📐 Technical Analysis",
        "🔗 Advanced Analysis"
    ]

)


# =====================================================
# TAB 1: PRICE CHARTS
# =====================================================

with tab1:

    st.header("📈 Price Analysis")


    # =================================================
    # CHART 1: CLOSING PRICE
    # =================================================

    st.subheader("1️⃣ Closing Price Trend")


    fig1 = px.line(

        filtered_df,

        x="DATE",

        y="CLOSE",

        title="Closing Price Trend"

    )


    st.plotly_chart(

        fig1,

        use_container_width=True

    )


    # =================================================
    # CHART 2: OPEN VS CLOSE
    # =================================================

    st.subheader("2️⃣ Open vs Close Price")


    fig2 = go.Figure()


    fig2.add_trace(

        go.Scatter(

            x=filtered_df["DATE"],

            y=filtered_df["OPEN"],

            name="Open Price"

        )

    )


    fig2.add_trace(

        go.Scatter(

            x=filtered_df["DATE"],

            y=filtered_df["CLOSE"],

            name="Close Price"

        )

    )


    fig2.update_layout(

        title="Opening Price vs Closing Price",

        xaxis_title="Date",

        yaxis_title="Price"

    )


    st.plotly_chart(

        fig2,

        use_container_width=True

    )


    # =================================================
    # CHART 3: HIGH VS LOW
    # =================================================

    st.subheader("3️⃣ High vs Low Price")


    fig3 = go.Figure()


    fig3.add_trace(

        go.Scatter(

            x=filtered_df["DATE"],

            y=filtered_df["HIGH"],

            name="High Price"

        )

    )


    fig3.add_trace(

        go.Scatter(

            x=filtered_df["DATE"],

            y=filtered_df["LOW"],

            name="Low Price",

            fill="tonexty"

        )

    )


    fig3.update_layout(

        title="High and Low Price Range",

        xaxis_title="Date",

        yaxis_title="Price"

    )


    st.plotly_chart(

        fig3,

        use_container_width=True

    )


    # =================================================
    # CHART 4: CANDLESTICK
    # =================================================

    st.subheader("4️⃣ Candlestick Chart")


    candle = go.Figure(

        data=[

            go.Candlestick(

                x=filtered_df["DATE"],

                open=filtered_df["OPEN"],

                high=filtered_df["HIGH"],

                low=filtered_df["LOW"],

                close=filtered_df["CLOSE"]

            )

        ]

    )


    candle.update_layout(

        title="OHLC Candlestick Chart",

        height=600,

        xaxis_rangeslider_visible=False

    )


    st.plotly_chart(

        candle,

        use_container_width=True

    )


# =====================================================
# TAB 2: VOLUME CHARTS
# =====================================================

with tab2:

    st.header("📊 Volume and Trading Activity")


    # =================================================
    # CHART 5: VOLUME
    # =================================================

    st.subheader("5️⃣ Trading Volume")


    fig5 = px.bar(

        filtered_df,

        x="DATE",

        y="VOLUME",

        title="Daily Trading Volume"

    )


    st.plotly_chart(

        fig5,

        use_container_width=True

    )


    # =================================================
    # CHART 6: VALUE
    # =================================================

    st.subheader("6️⃣ Trading Value")


    fig6 = px.area(

        filtered_df,

        x="DATE",

        y="VALUE",

        title="Daily Trading Value"

    )


    st.plotly_chart(

        fig6,

        use_container_width=True

    )


    # =================================================
    # CHART 7: NUMBER OF TRADES
    # =================================================

    st.subheader("7️⃣ Number of Trades")


    fig7 = px.line(

        filtered_df,

        x="DATE",

        y="NO. OF  TRADES",

        title="Number of Trades"

    )


    st.plotly_chart(

        fig7,

        use_container_width=True

    )


# =====================================================
# TAB 3: RETURNS AND RISK
# =====================================================

with tab3:

    st.header("📉 Returns and Risk Analysis")


    # =================================================
    # CHART 8: DAILY RETURNS
    # =================================================

    st.subheader("8️⃣ Daily Returns")


    fig8 = px.bar(

        filtered_df,

        x="DATE",

        y="DAILY RETURN (%)",

        title="Daily Returns (%)"

    )


    st.plotly_chart(

        fig8,

        use_container_width=True

    )


    # =================================================
    # CHART 9: RETURN DISTRIBUTION
    # =================================================

    st.subheader("9️⃣ Return Distribution")


    fig9 = px.histogram(

        filtered_df,

        x="DAILY RETURN (%)",

        nbins=40,

        title="Daily Return Distribution"

    )


    st.plotly_chart(

        fig9,

        use_container_width=True

    )


    # =================================================
    # CHART 10: VOLATILITY
    # =================================================

    st.subheader("🔟 Rolling Volatility")


    fig10 = px.line(

        filtered_df,

        x="DATE",

        y="VOLATILITY",

        title="20-Day Rolling Volatility"

    )


    st.plotly_chart(

        fig10,

        use_container_width=True

    )


    # =================================================
    # CHART 11: PRICE DISTRIBUTION
    # =================================================

    st.subheader("1️⃣1️⃣ Price Distribution")


    fig11 = px.box(

        filtered_df,

        y="CLOSE",

        title="Closing Price Distribution"

    )


    st.plotly_chart(

        fig11,

        use_container_width=True

    )


# =====================================================
# TAB 4: TECHNICAL ANALYSIS
# =====================================================

with tab4:

    st.header("📐 Technical Analysis")


    # =================================================
    # CHART 12: MOVING AVERAGES
    # =================================================

    st.subheader("1️⃣2️⃣ Moving Average Analysis")


    fig12 = go.Figure()


    fig12.add_trace(

        go.Scatter(

            x=filtered_df["DATE"],

            y=filtered_df["CLOSE"],

            name="Close Price"

        )

    )


    fig12.add_trace(

        go.Scatter(

            x=filtered_df["DATE"],

            y=filtered_df["MA20"],

            name="20-Day MA"

        )

    )


    fig12.add_trace(

        go.Scatter(

            x=filtered_df["DATE"],

            y=filtered_df["MA50"],

            name="50-Day MA"

        )

    )


    fig12.add_trace(

        go.Scatter(

            x=filtered_df["DATE"],

            y=filtered_df["MA200"],

            name="200-Day MA"

        )

    )


    fig12.update_layout(

        title="Moving Average Analysis",

        xaxis_title="Date",

        yaxis_title="Price"

    )


    st.plotly_chart(

        fig12,

        use_container_width=True

    )


    # =================================================
    # CHART 13: VWAP
    # =================================================

    st.subheader("1️⃣3️⃣ VWAP Analysis")


    fig13 = go.Figure()


    fig13.add_trace(

        go.Scatter(

            x=filtered_df["DATE"],

            y=filtered_df["CLOSE"],

            name="Close Price"

        )

    )


    fig13.add_trace(

        go.Scatter(

            x=filtered_df["DATE"],

            y=filtered_df["VWAP"],

            name="VWAP"

        )

    )


    fig13.update_layout(

        title="Closing Price vs VWAP",

        xaxis_title="Date",

        yaxis_title="Price"

    )


    st.plotly_chart(

        fig13,

        use_container_width=True

    )


    # =================================================
    # CHART 14: RSI
    # =================================================

    st.subheader("1️⃣4️⃣ RSI Momentum Indicator")


    fig14 = go.Figure()


    fig14.add_trace(

        go.Scatter(

            x=filtered_df["DATE"],

            y=filtered_df["RSI"],

            name="RSI"

        )

    )


    fig14.add_hline(

        y=70,

        line_dash="dash",

        annotation_text="Overbought"

    )


    fig14.add_hline(

        y=30,

        line_dash="dash",

        annotation_text="Oversold"

    )


    fig14.update_layout(

        title="Relative Strength Index",

        yaxis_title="RSI"

    )


    st.plotly_chart(

        fig14,

        use_container_width=True

    )


# =====================================================
# TAB 5: ADVANCED ANALYSIS
# =====================================================

with tab5:

    st.header("🔗 Advanced Data Analysis")


    # =================================================
    # CHART 15: CORRELATION HEATMAP
    # =================================================

    st.subheader("1️⃣5️⃣ Correlation Heatmap")


    correlation_columns = [

        "OPEN",

        "HIGH",

        "LOW",

        "PREV. CLOSE",

        "LTP",

        "CLOSE",

        "VWAP",

        "VOLUME",

        "VALUE",

        "NO. OF  TRADES"

    ]


    available_columns = [

        column

        for column in correlation_columns

        if column in filtered_df.columns

    ]


    correlation_matrix = (

        filtered_df[available_columns]

        .corr()

    )


    heatmap = px.imshow(

        correlation_matrix,

        text_auto=True,

        aspect="auto",

        title="Stock Market Feature Correlation"

    )


    st.plotly_chart(

        heatmap,

        use_container_width=True

    )


# =====================================================
# DOWNLOAD DATA
# =====================================================

st.divider()

st.header("📥 Download Analysis Data")


csv = filtered_df.to_csv(

    index=False

).encode("utf-8")


st.download_button(

    label="📥 Download Analyzed CSV",

    data=csv,

    file_name="stock_market_analysis.csv",

    mime="text/csv"

)