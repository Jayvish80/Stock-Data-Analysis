# ============================================================
# STOCKVISION AI - STOCK MARKET ANALYSIS DASHBOARD
# ============================================================

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="StockVision AI",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# PROFESSIONAL CSS
# ============================================================

st.markdown(
    """
    <style>

    /* ================================
       MAIN APP
    ================================= */

    .stApp {
        background:
        linear-gradient(
            135deg,
            #020617 0%,
            #0f172a 45%,
            #172554 100%
        );
    }


    /* ================================
       MAIN CONTENT
    ================================= */

    .block-container {
        max-width: 1500px;
        padding-top: 2rem;
        padding-bottom: 3rem;
        padding-left: 3rem;
        padding-right: 3rem;
    }


    /* ================================
       SIDEBAR
    ================================= */

    section[data-testid="stSidebar"] {
        background:
        linear-gradient(
            180deg,
            #020617 0%,
            #0f172a 100%
        );

        border-right: 1px solid #1e293b;
    }


    section[data-testid="stSidebar"] * {
        color: #e2e8f0;
    }


    /* ================================
       SIDEBAR FILE UPLOADER
    ================================= */

    section[data-testid="stSidebar"]
    div[data-testid="stFileUploader"] {
        background: #111827;
        border: 1px solid #334155;
        border-radius: 14px;
        padding: 10px;
    }


    section[data-testid="stSidebar"]
    div[data-testid="stFileUploaderDropzone"] {
        background: #1e293b;
        border: 2px dashed #475569;
        border-radius: 10px;
    }


    /* ================================
       SIDEBAR DATE INPUT
    ================================= */

    section[data-testid="stSidebar"]
    div[data-testid="stDateInput"] input {
        background: white !important;
        color: #0f172a !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
    }


    /* ================================
       MAIN TITLE
    ================================= */

    h1 {
        font-size: 46px !important;

        background:
        linear-gradient(
            90deg,
            #38bdf8,
            #818cf8,
            #c084fc
        );

        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;

        font-weight: 900 !important;
    }


    h2, h3 {
        color: #f8fafc !important;
    }


    /* ================================
       INFO BOX
    ================================= */

    div[data-testid="stAlert"] {
        border-radius: 14px;
        border: 1px solid #334155;
    }


    /* ================================
       METRIC CARDS
    ================================= */

    div[data-testid="stMetric"] {

        background:
        linear-gradient(
            145deg,
            #1e293b,
            #0f172a
        );

        border: 1px solid #334155;

        padding: 20px;

        border-radius: 16px;

        box-shadow:
        0 8px 25px rgba(0, 0, 0, 0.25);

    }


    div[data-testid="stMetric"]:hover {

        border-color: #38bdf8;

        transform: translateY(-3px);

        transition: 0.3s;

    }


    div[data-testid="stMetricLabel"] {

        color: #94a3b8 !important;

    }


    div[data-testid="stMetricValue"] {

        color: #f8fafc !important;

        font-weight: 800;

    }


    /* ================================
       CHART CONTAINER
    ================================= */

    div[data-testid="stPlotlyChart"] {

        background: rgba(15, 23, 42, 0.65);

        border: 1px solid #1e293b;

        border-radius: 16px;

        padding: 8px;

        margin-bottom: 20px;

    }


    /* ================================
       TABS
    ================================= */

    button[data-baseweb="tab"] {

        color: #94a3b8;

        font-weight: 700;

    }


    button[data-baseweb="tab"][aria-selected="true"] {

        color: #38bdf8;

    }


    /* ================================
       BUTTONS
    ================================= */

    .stButton button {

        border-radius: 10px;

        font-weight: 700;

    }


    /* ================================
       DOWNLOAD BUTTON
    ================================= */

    .stDownloadButton button {

        width: 100%;

        background: #1e293b;

        color: #38bdf8;

        border: 1px solid #38bdf8;

        border-radius: 10px;

        font-weight: 700;

    }


    /* ================================
       FOOTER
    ================================= */

    .footer-text {

        text-align: center;

        color: #64748b;

        padding: 30px;

        margin-top: 40px;

    }

    </style>
    """,

    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("# 📈 StockVision AI")

    st.caption("Smart Stock Market Intelligence")

    st.divider()


    st.subheader("📂 Upload Market Data")


    uploaded_file = st.file_uploader(

        "Upload Stock CSV",

        type=["csv"],

        help="Upload your historical stock market CSV file."

    )


    st.divider()


    st.subheader("📌 Dashboard Modules")

    st.markdown(

        """
        📈 Price Analytics

        🕯️ Candlestick Analysis

        📊 Volume Intelligence

        📉 Risk & Returns

        📐 Technical Indicators

        🔗 Correlation Matrix

        🤖 AI Technical Signals
        """

    )


# ============================================================
# MAIN HEADER
# ============================================================

st.title("📈 StockVision AI")

st.write(

    "Intelligent stock market analytics • Technical indicators • "
    "Risk analysis • Interactive visualizations"

)


# ============================================================
# IF NO FILE UPLOADED
# ============================================================

if uploaded_file is None:

    st.info(

        "👋 Welcome to StockVision AI! "
        "Upload a historical stock CSV file from the sidebar "
        "to start your analysis."

    )


    st.subheader("🚀 What You Can Analyze")


    col1, col2, col3, col4 = st.columns(4)


    with col1:

        st.metric(

            label="📈 Price Trends",

            value="Analyze"

        )

        st.caption(

            "Analyze opening, closing, high and low prices."

        )


    with col2:

        st.metric(

            label="📊 Market Volume",

            value="Analyze"

        )

        st.caption(

            "Understand buying and selling activity."

        )


    with col3:

        st.metric(

            label="📉 Risk Analysis",

            value="Analyze"

        )

        st.caption(

            "Measure returns and market volatility."

        )


    with col4:

        st.metric(

            label="🤖 AI Signals",

            value="Analyze"

        )

        st.caption(

            "Analyze technical indicators and momentum."

        )


    st.stop()


# ============================================================
# LOAD CSV FILE
# ============================================================

try:

    df = pd.read_csv(uploaded_file)

except Exception as error:

    st.error(

        f"❌ Error loading CSV file: {error}"

    )

    st.stop()


# ============================================================
# CLEAN COLUMN NAMES
# ============================================================

df.columns = (

    df.columns

    .str.strip()

    .str.upper()

)


# ============================================================
# SHOW AVAILABLE COLUMNS
# ============================================================

with st.expander("🔍 View Dataset Information"):

    st.write(

        "Available columns:"

    )

    st.write(

        list(df.columns)

    )


# ============================================================
# FIND DATE COLUMN
# ============================================================

date_column = None


possible_date_columns = [

    "DATE",

    "DATETIME",

    "TIMESTAMP"

]


for column in possible_date_columns:

    if column in df.columns:

        date_column = column

        break


if date_column is None:

    st.error(

        "❌ Your CSV file must contain a DATE column."

    )

    st.stop()


# ============================================================
# CONVERT DATE
# ============================================================

df[date_column] = pd.to_datetime(

    df[date_column],

    errors="coerce"

)


df = df.dropna(

    subset=[date_column]

)


df = df.sort_values(

    date_column

)


# ============================================================
# CLEAN NUMERIC DATA
# ============================================================

numeric_columns = [

    "OPEN",

    "HIGH",

    "LOW",

    "CLOSE",

    "LTP",

    "VWAP",

    "VOLUME",

    "VALUE",

    "PREV. CLOSE",

    "52W H",

    "52W L",

    "NO. OF TRADES",

    "NO. OF  TRADES"

]


for column in numeric_columns:

    if column in df.columns:

        df[column] = (

            df[column]

            .astype(str)

            .str.replace(",", "", regex=False)

            .str.replace("₹", "", regex=False)

            .str.replace("$", "", regex=False)

        )


        df[column] = pd.to_numeric(

            df[column],

            errors="coerce"

        )


# ============================================================
# CLOSE PRICE VALIDATION
# ============================================================

if "CLOSE" not in df.columns:

    st.error(

        "❌ Your CSV must contain a CLOSE column."

    )

    st.stop()


# ============================================================
# DATE FILTERS
# ============================================================

with st.sidebar:

    st.divider()

    st.subheader("📅 Analysis Period")


    start_date = st.date_input(

        "Start Date",

        value=df[date_column].min().date()

    )


    end_date = st.date_input(

        "End Date",

        value=df[date_column].max().date()

    )


if start_date > end_date:

    st.error(

        "❌ Start date cannot be after end date."

    )

    st.stop()


# ============================================================
# FILTER DATA
# ============================================================

filtered_df = df[

    (

        df[date_column]

        >=

        pd.to_datetime(start_date)

    )

    &

    (

        df[date_column]

        <=

        pd.to_datetime(end_date)

    )

].copy()


if filtered_df.empty:

    st.warning(

        "⚠️ No data found for the selected dates."

    )

    st.stop()


# ============================================================
# TECHNICAL INDICATORS
# ============================================================

filtered_df["DAILY RETURN (%)"] = (

    filtered_df["CLOSE"]

    .pct_change()

    * 100

)


filtered_df["MA20"] = (

    filtered_df["CLOSE"]

    .rolling(20)

    .mean()

)


filtered_df["MA50"] = (

    filtered_df["CLOSE"]

    .rolling(50)

    .mean()

)


filtered_df["MA200"] = (

    filtered_df["CLOSE"]

    .rolling(200)

    .mean()

)


filtered_df["VOLATILITY"] = (

    filtered_df["DAILY RETURN (%)"]

    .rolling(20)

    .std()

)


# ============================================================
# RSI CALCULATION
# ============================================================

delta = filtered_df["CLOSE"].diff()


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


relative_strength = (

    average_gain

    /

    average_loss.replace(0, np.nan)

)


filtered_df["RSI"] = (

    100

    -

    (

        100

        /

        (

            1

            +

            relative_strength

        )

    )

)


# ============================================================
# MARKET METRICS
# ============================================================

latest_price = filtered_df["CLOSE"].iloc[-1]


highest_price = filtered_df["CLOSE"].max()


lowest_price = filtered_df["CLOSE"].min()


total_return = (

    (

        filtered_df["CLOSE"].iloc[-1]

        /

        filtered_df["CLOSE"].iloc[0]

        -

        1

    )

    * 100

)


average_volume = 0


if "VOLUME" in filtered_df.columns:

    average_volume = filtered_df["VOLUME"].mean()


# ============================================================
# MARKET OVERVIEW
# ============================================================

st.header("📊 Market Overview")


m1, m2, m3, m4, m5 = st.columns(5)


with m1:

    st.metric(

        "💰 Current Price",

        f"${latest_price:,.2f}"

    )


with m2:

    st.metric(

        "📈 Highest Price",

        f"${highest_price:,.2f}"

    )


with m3:

    st.metric(

        "📉 Lowest Price",

        f"${lowest_price:,.2f}"

    )


with m4:

    st.metric(

        "📊 Average Volume",

        f"{average_volume:,.0f}"

    )


with m5:

    st.metric(

        "🚀 Total Return",

        f"{total_return:.2f}%"

    )


# ============================================================
# AI TECHNICAL SIGNAL
# ============================================================

latest = filtered_df.iloc[-1]


score = 0


if pd.notna(latest["MA20"]):

    if latest["CLOSE"] > latest["MA20"]:

        score += 1

    else:

        score -= 1


if pd.notna(latest["MA50"]):

    if latest["CLOSE"] > latest["MA50"]:

        score += 1

    else:

        score -= 1


if pd.notna(latest["RSI"]):

    if latest["RSI"] < 30:

        score += 2

    elif latest["RSI"] > 70:

        score -= 2


if score >= 3:

    signal = "🟢 BUY / ACCUMULATE"

    signal_message = (

        "Positive technical momentum detected."

    )


elif score <= -2:

    signal = "🔴 AVOID / BEARISH"

    signal_message = (

        "Negative technical momentum detected."

    )


else:

    signal = "🟡 HOLD / WAIT"

    signal_message = (

        "Market conditions are mixed."

    )


st.success(

    f"🤖 AI Technical Signal: {signal}\n\n"

    f"{signal_message}\n\n"

    f"Technical Score: {score}"

)


# ============================================================
# TABS
# ============================================================

tab1, tab2, tab3, tab4, tab5 = st.tabs(

    [

        "📈 Price Analysis",

        "📊 Volume Analysis",

        "📉 Risk Analysis",

        "📐 Technical Indicators",

        "🔗 Advanced Analytics"

    ]

)


# ============================================================
# TAB 1 - PRICE ANALYSIS
# ============================================================

with tab1:

    st.header("📈 Price Analysis")


    # 1. Closing Price

    fig1 = px.line(

        filtered_df,

        x=date_column,

        y="CLOSE",

        title="1️⃣ Closing Price Trend"

    )


    fig1.update_layout(

        template="plotly_dark",

        hovermode="x unified"

    )


    st.plotly_chart(

        fig1,

        use_container_width=True

    )


    # 2. OHLC

    price_columns = [

        column

        for column in [

            "OPEN",

            "HIGH",

            "LOW",

            "CLOSE"

        ]

        if column in filtered_df.columns

    ]


    if price_columns:

        fig2 = px.line(

            filtered_df,

            x=date_column,

            y=price_columns,

            title="2️⃣ Open, High, Low & Close"

        )


        fig2.update_layout(

            template="plotly_dark"

        )


        st.plotly_chart(

            fig2,

            use_container_width=True

        )


    # 3. Candlestick

    if all(

        column in filtered_df.columns

        for column in [

            "OPEN",

            "HIGH",

            "LOW",

            "CLOSE"

        ]

    ):

        candle = go.Figure(

            data=[

                go.Candlestick(

                    x=filtered_df[date_column],

                    open=filtered_df["OPEN"],

                    high=filtered_df["HIGH"],

                    low=filtered_df["LOW"],

                    close=filtered_df["CLOSE"]

                )

            ]

        )


        candle.update_layout(

            title="3️⃣ Candlestick Chart",

            template="plotly_dark",

            xaxis_rangeslider_visible=False

        )


        st.plotly_chart(

            candle,

            use_container_width=True

        )


    # 4. Area Chart

    fig4 = px.area(

        filtered_df,

        x=date_column,

        y="CLOSE",

        title="4️⃣ Price Area Chart"

    )


    fig4.update_layout(

        template="plotly_dark"

    )


    st.plotly_chart(

        fig4,

        use_container_width=True

    )


# ============================================================
# TAB 2 - VOLUME ANALYSIS
# ============================================================

with tab2:

    st.header("📊 Volume Analysis")


    if "VOLUME" in filtered_df.columns:


        # 5. Volume

        fig5 = px.bar(

            filtered_df,

            x=date_column,

            y="VOLUME",

            title="5️⃣ Trading Volume"

        )


        fig5.update_layout(

            template="plotly_dark"

        )


        st.plotly_chart(

            fig5,

            use_container_width=True

        )


        # 6. Volume Moving Average

        filtered_df["VOLUME MA20"] = (

            filtered_df["VOLUME"]

            .rolling(20)

            .mean()

        )


        fig6 = px.line(

            filtered_df,

            x=date_column,

            y="VOLUME MA20",

            title="6️⃣ Volume Moving Average"

        )


        fig6.update_layout(

            template="plotly_dark"

        )


        st.plotly_chart(

            fig6,

            use_container_width=True

        )


    if "VALUE" in filtered_df.columns:


        # 7. Trading Value

        fig7 = px.area(

            filtered_df,

            x=date_column,

            y="VALUE",

            title="7️⃣ Trading Value"

        )


        fig7.update_layout(

            template="plotly_dark"

        )


        st.plotly_chart(

            fig7,

            use_container_width=True

        )


    trade_column = None


    if "NO. OF TRADES" in filtered_df.columns:

        trade_column = "NO. OF TRADES"


    elif "NO. OF  TRADES" in filtered_df.columns:

        trade_column = "NO. OF  TRADES"


    if trade_column:

        # 8. Number of Trades

        fig8 = px.line(

            filtered_df,

            x=date_column,

            y=trade_column,

            title="8️⃣ Number of Trades"

        )


        fig8.update_layout(

            template="plotly_dark"

        )


        st.plotly_chart(

            fig8,

            use_container_width=True

        )


# ============================================================
# TAB 3 - RISK ANALYSIS
# ============================================================

with tab3:

    st.header("📉 Risk & Returns")


    # 9. Daily Returns

    fig9 = px.bar(

        filtered_df,

        x=date_column,

        y="DAILY RETURN (%)",

        title="9️⃣ Daily Returns"

    )


    fig9.update_layout(

        template="plotly_dark"

    )


    st.plotly_chart(

        fig9,

        use_container_width=True

    )


    # 10. Return Distribution

    fig10 = px.histogram(

        filtered_df,

        x="DAILY RETURN (%)",

        nbins=40,

        title="🔟 Return Distribution"

    )


    fig10.update_layout(

        template="plotly_dark"

    )


    st.plotly_chart(

        fig10,

        use_container_width=True

    )


    # 11. Volatility

    fig11 = px.line(

        filtered_df,

        x=date_column,

        y="VOLATILITY",

        title="1️⃣1️⃣ Rolling Volatility"

    )


    fig11.update_layout(

        template="plotly_dark"

    )


    st.plotly_chart(

        fig11,

        use_container_width=True

    )


    # 12. Box Plot

    fig12 = px.box(

        filtered_df,

        y="CLOSE",

        title="1️⃣2️⃣ Price Distribution"

    )


    fig12.update_layout(

        template="plotly_dark"

    )


    st.plotly_chart(

        fig12,

        use_container_width=True

    )


# ============================================================
# TAB 4 - TECHNICAL INDICATORS
# ============================================================

with tab4:

    st.header("📐 Technical Indicators")


    # 13. Moving Averages

    ma_chart = go.Figure()


    ma_chart.add_trace(

        go.Scatter(

            x=filtered_df[date_column],

            y=filtered_df["CLOSE"],

            name="Close Price"

        )

    )


    ma_chart.add_trace(

        go.Scatter(

            x=filtered_df[date_column],

            y=filtered_df["MA20"],

            name="MA20"

        )

    )


    ma_chart.add_trace(

        go.Scatter(

            x=filtered_df[date_column],

            y=filtered_df["MA50"],

            name="MA50"

        )

    )


    ma_chart.add_trace(

        go.Scatter(

            x=filtered_df[date_column],

            y=filtered_df["MA200"],

            name="MA200"

        )

    )


    ma_chart.update_layout(

        title="1️⃣3️⃣ Moving Average Analysis",

        template="plotly_dark",

        hovermode="x unified"

    )


    st.plotly_chart(

        ma_chart,

        use_container_width=True

    )


    # 14. VWAP

    if "VWAP" in filtered_df.columns:


        vwap_chart = go.Figure()


        vwap_chart.add_trace(

            go.Scatter(

                x=filtered_df[date_column],

                y=filtered_df["CLOSE"],

                name="Close Price"

            )

        )


        vwap_chart.add_trace(

            go.Scatter(

                x=filtered_df[date_column],

                y=filtered_df["VWAP"],

                name="VWAP"

            )

        )


        vwap_chart.update_layout(

            title="1️⃣4️⃣ Price vs VWAP",

            template="plotly_dark"

        )


        st.plotly_chart(

            vwap_chart,

            use_container_width=True

        )


    # 15. RSI

    rsi_chart = go.Figure()


    rsi_chart.add_trace(

        go.Scatter(

            x=filtered_df[date_column],

            y=filtered_df["RSI"],

            name="RSI"

        )

    )


    rsi_chart.add_hline(

        y=70,

        line_dash="dash",

        annotation_text="Overbought"

    )


    rsi_chart.add_hline(

        y=30,

        line_dash="dash",

        annotation_text="Oversold"

    )


    rsi_chart.update_layout(

        title="1️⃣5️⃣ RSI Momentum Analysis",

        template="plotly_dark",

        yaxis_range=[0, 100]

    )


    st.plotly_chart(

        rsi_chart,

        use_container_width=True

    )


# ============================================================
# TAB 5 - ADVANCED ANALYTICS
# ============================================================

with tab5:

    st.header("🔗 Advanced Analytics")


    correlation_columns = [

        "OPEN",

        "HIGH",

        "LOW",

        "CLOSE",

        "VWAP",

        "VOLUME",

        "VALUE",

        "LTP"

    ]


    available_columns = [

        column

        for column in correlation_columns

        if column in filtered_df.columns

    ]


    if len(available_columns) >= 2:


        correlation_matrix = (

            filtered_df[available_columns]

            .corr()

        )


        correlation_chart = px.imshow(

            correlation_matrix,

            text_auto=True,

            aspect="auto",

            title="🔗 Correlation Heatmap"

        )


        correlation_chart.update_layout(

            template="plotly_dark"

        )


        st.plotly_chart(

            correlation_chart,

            use_container_width=True

        )


# ============================================================
# DATA TABLE
# ============================================================

st.header("📋 Stock Data Preview")


st.dataframe(

    filtered_df.tail(100),

    use_container_width=True,

    hide_index=True

)


# ============================================================
# DOWNLOAD ANALYSIS
# ============================================================

st.header("📥 Export Analysis")


csv_data = filtered_df.to_csv(

    index=False

).encode("utf-8")


st.download_button(

    label="📥 Download Complete Analysis CSV",

    data=csv_data,

    file_name="stockvision_ai_analysis.csv",

    mime="text/csv"

)


# ============================================================
# FOOTER
# ============================================================

st.markdown(

    """

    <div class="footer-text">

        📈 StockVision AI

        <br>

        Intelligent Stock Market Analytics Dashboard

        <br>

        Built with Python • Streamlit • Pandas • Plotly

    </div>

    """,

    unsafe_allow_html=True

)
