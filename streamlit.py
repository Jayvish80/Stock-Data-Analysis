# ============================================================
# STOCKVISION AI
# PROFESSIONAL STOCK MARKET ANALYTICS DASHBOARD
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
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* ======================================================
       GLOBAL PAGE
    ====================================================== */

    .stApp {

        background:

        radial-gradient(
            circle at top right,
            #172554 0%,
            #0f172a 35%,
            #020617 100%
        );

        color: #f8fafc;

    }


    /* ======================================================
       MAIN CONTENT WIDTH
    ====================================================== */

    .block-container {

        max-width: 1500px;

        padding-top: 2.5rem;

        padding-bottom: 3rem;

        padding-left: 3rem;

        padding-right: 3rem;

    }


    /* ======================================================
       SIDEBAR
    ====================================================== */

    section[data-testid="stSidebar"] {

        background:

        linear-gradient(

            180deg,

            #020617 0%,

            #0f172a 100%

        );

        border-right:

        1px solid #1e293b;

    }


    /* SIDEBAR TEXT */

    section[data-testid="stSidebar"] * {

        color: #e2e8f0;

    }


    /* ======================================================
       SIDEBAR BRAND
    ====================================================== */

    .sidebar-brand {

        text-align: center;

        padding: 10px 0 25px 0;

    }


    .sidebar-logo {

        font-size: 42px;

        margin-bottom: 5px;

    }


    .sidebar-title {

        font-size: 22px;

        font-weight: 800;

        background:

        linear-gradient(

            90deg,

            #38bdf8,

            #818cf8

        );

        -webkit-background-clip: text;

        -webkit-text-fill-color: transparent;

    }


    .sidebar-subtitle {

        color: #64748b;

        font-size: 12px;

        margin-top: 5px;

    }


    /* ======================================================
       FILE UPLOADER
    ====================================================== */

    section[data-testid="stSidebar"]

    div[data-testid="stFileUploader"] {

        background: #111827 !important;

        border: 1px solid #334155 !important;

        border-radius: 14px !important;

        padding: 10px !important;

    }


    section[data-testid="stSidebar"]

    div[data-testid="stFileUploaderDropzone"] {

        background: #1e293b !important;

        border: 2px dashed #475569 !important;

        border-radius: 10px !important;

    }


    section[data-testid="stSidebar"]

    div[data-testid="stFileUploaderDropzone"] * {

        color: #e2e8f0 !important;

    }


    section[data-testid="stSidebar"]

    div[data-testid="stFileUploader"] button {

        background: #2563eb !important;

        color: white !important;

        border: none !important;

        border-radius: 8px !important;

        font-weight: 700 !important;

    }


    /* ======================================================
       DATE INPUTS
    ====================================================== */

    section[data-testid="stSidebar"]

    div[data-testid="stDateInput"] label {

        color: #cbd5e1 !important;

        font-weight: 700 !important;

    }


    section[data-testid="stSidebar"]

    div[data-testid="stDateInput"] input {

        background: #ffffff !important;

        color: #0f172a !important;

        border: 2px solid #334155 !important;

        border-radius: 10px !important;

        font-weight: 600 !important;

    }


    /* ======================================================
       HEADER
    ====================================================== */

    .dashboard-header {

        display: flex;

        align-items: center;

        gap: 18px;

        margin-bottom: 8px;

    }


    .header-icon {

        width: 58px;

        height: 58px;

        display: flex;

        align-items: center;

        justify-content: center;

        border-radius: 14px;

        background:

        linear-gradient(

            135deg,

            #38bdf8,

            #2563eb

        );

        font-size: 32px;

        box-shadow:

        0 10px 30px

        rgba(37, 99, 235, 0.3);

    }


    .main-title {

        font-size: 46px;

        font-weight: 900;

        line-height: 1;

        background:

        linear-gradient(

            90deg,

            #38bdf8,

            #818cf8,

            #c084fc

        );

        -webkit-background-clip: text;

        -webkit-text-fill-color: transparent;

    }


    .subtitle {

        color: #94a3b8;

        font-size: 16px;

        margin-top: 10px;

        margin-bottom: 28px;

    }


    /* ======================================================
       WELCOME CARD
    ====================================================== */

    .welcome-card {

        padding: 25px;

        border-radius: 18px;

        background:

        linear-gradient(

            135deg,

            rgba(30, 64, 175, 0.35),

            rgba(30, 41, 59, 0.75)

        );

        border: 1px solid #334155;

        margin-top: 20px;

        margin-bottom: 25px;

    }


    .welcome-title {

        font-size: 22px;

        font-weight: 800;

        color: #f8fafc;

    }


    .welcome-text {

        color: #94a3b8;

        margin-top: 8px;

        line-height: 1.6;

    }


    /* ======================================================
       KPI CARDS
    ====================================================== */

    .metric-card {

        min-height: 140px;

        padding: 22px;

        border-radius: 18px;

        background:

        linear-gradient(

            145deg,

            rgba(30, 41, 59, 0.95),

            rgba(15, 23, 42, 0.95)

        );

        border: 1px solid #334155;

        box-shadow:

        0 10px 25px

        rgba(0, 0, 0, 0.2);

        transition: all 0.3s ease;

    }


    .metric-card:hover {

        transform: translateY(-5px);

        border-color: #38bdf8;

        box-shadow:

        0 15px 35px

        rgba(56, 189, 248, 0.15);

    }


    .metric-icon {

        font-size: 22px;

        margin-bottom: 10px;

    }


    .metric-title {

        color: #94a3b8;

        font-size: 12px;

        font-weight: 700;

        text-transform: uppercase;

        letter-spacing: 1px;

    }


    .metric-value {

        color: #f8fafc;

        font-size: 26px;

        font-weight: 800;

        margin-top: 8px;

    }


    /* ======================================================
       SECTION TITLE
    ====================================================== */

    .section-title {

        font-size: 25px;

        font-weight: 800;

        margin-top: 30px;

        margin-bottom: 18px;

        color: #f8fafc;

    }


    /* ======================================================
       AI SIGNAL
    ====================================================== */

    .signal-card {

        padding: 25px;

        border-radius: 20px;

        background:

        linear-gradient(

            135deg,

            #172554,

            #1e1b4b

        );

        border: 1px solid #4338ca;

        box-shadow:

        0 12px 35px

        rgba(79, 70, 229, 0.2);

        margin-top: 25px;

        margin-bottom: 25px;

    }


    .signal-label {

        color: #a5b4fc;

        font-size: 13px;

        font-weight: 700;

        letter-spacing: 1px;

        text-transform: uppercase;

    }


    .signal-value {

        font-size: 34px;

        font-weight: 900;

        margin-top: 8px;

    }


    .signal-description {

        color: #cbd5e1;

        margin-top: 10px;

    }


    /* ======================================================
       CHART CONTAINER
    ====================================================== */

    div[data-testid="stPlotlyChart"] {

        background:

        rgba(15, 23, 42, 0.65);

        border: 1px solid #1e293b;

        border-radius: 18px;

        padding: 8px;

        margin-bottom: 22px;

    }


    /* ======================================================
       TABS
    ====================================================== */

    button[data-baseweb="tab"] {

        color: #94a3b8;

        font-size: 15px;

        font-weight: 700;

    }


    button[data-baseweb="tab"][aria-selected="true"] {

        color: #38bdf8;

    }


    /* ======================================================
       DOWNLOAD BUTTON
    ====================================================== */

    .stDownloadButton button {

        width: 100%;

        background: #1e293b;

        color: #38bdf8;

        border: 1px solid #38bdf8;

        border-radius: 10px;

        font-weight: 700;

    }


    .stDownloadButton button:hover {

        background: #38bdf8;

        color: #020617;

    }


    /* ======================================================
       FOOTER
    ====================================================== */

    .footer {

        text-align: center;

        color: #64748b;

        padding: 30px;

        margin-top: 40px;

        border-top: 1px solid #1e293b;

    }

    </style>
    """,

    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(

        """
        <div class="sidebar-brand">

            <div class="sidebar-logo">📈</div>

            <div class="sidebar-title">
                StockVision AI
            </div>

            <div class="sidebar-subtitle">
                Smart Market Intelligence
            </div>

        </div>
        """,

        unsafe_allow_html=True

    )


    st.markdown("---")


    st.markdown("### 📂 Upload Market Data")


    uploaded_file = st.file_uploader(

        "Upload Stock CSV",

        type=["csv"],

        help="Upload historical stock market data in CSV format."

    )


    st.markdown("---")


    if uploaded_file is not None:

        st.markdown("### 📅 Analysis Period")


        # Date inputs are created later
        # after the CSV is loaded


    st.markdown("---")


    st.markdown("### 📌 Dashboard Modules")

    st.markdown(

        """
        📈 Price Analytics

        🕯️ Candlestick Analysis

        📊 Volume Intelligence

        📉 Risk & Returns

        📐 Technical Indicators

        🔗 Correlation Matrix

        🤖 AI Signal Engine

        """

    )


# ============================================================
# HEADER
# ============================================================

st.markdown(

    """
    <div class="dashboard-header">

        <div class="header-icon">
            📈
        </div>

        <div class="main-title">
            StockVision AI
        </div>

    </div>
    """,

    unsafe_allow_html=True

)


st.markdown(

    """
    <div class="subtitle">

    Intelligent stock market analytics • Technical indicators •

    Risk analysis • Interactive visualizations

    </div>

    """,

    unsafe_allow_html=True

)


# ============================================================
# NO FILE UPLOADED
# ============================================================

if uploaded_file is None:

    st.markdown(

        """
        <div class="welcome-card">

            <div class="welcome-title">

                👋 Welcome to StockVision AI

            </div>

            <div class="welcome-text">

                Upload your historical stock CSV file from the

                sidebar to unlock interactive price analysis,

                technical indicators, risk metrics, and AI-powered

                technical signals.

            </div>

        </div>

        """,

        unsafe_allow_html=True

    )


    # FEATURE CARDS

    st.markdown(

        '<div class="section-title">🚀 What You Can Analyze</div>',

        unsafe_allow_html=True

    )


    c1, c2, c3, c4 = st.columns(4)


    with c1:

        st.info(

            "📈 Price Trends\n\nAnalyze historical opening, closing, high and low prices."

        )


    with c2:

        st.info(

            "📊 Market Volume\n\nUnderstand buying and selling activity."

        )


    with c3:

        st.info(

            "📉 Risk Analysis\n\nMeasure returns and market volatility."

        )


    with c4:

        st.info(

            "🤖 AI Signals\n\nAnalyze technical indicators and market momentum."

        )


    st.stop()


# ============================================================
# LOAD CSV
# ============================================================

try:

    df = pd.read_csv(uploaded_file)

except Exception as error:

    st.error(

        f"❌ Could not read the CSV file: {error}"

    )

    st.stop()


# ============================================================
# CLEAN COLUMN NAMES
# ============================================================

df.columns = (

    df.columns

    .str.strip()

)


# ============================================================
# DATE COLUMN
# ============================================================

if "DATE" not in df.columns:

    st.error(

        "❌ Your CSV must contain a DATE column."

    )

    st.write(

        "Available columns:",

        list(df.columns)

    )

    st.stop()


df["DATE"] = pd.to_datetime(

    df["DATE"],

    errors="coerce"

)


df = df.dropna(

    subset=["DATE"]

)


df = df.sort_values(

    "DATE"

)


# ============================================================
# NUMERIC COLUMNS
# ============================================================

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

            .str.replace("$", "", regex=False)

        )


        df[column] = pd.to_numeric(

            df[column],

            errors="coerce"

        )


# ============================================================
# REQUIRED CLOSE COLUMN
# ============================================================

if "CLOSE" not in df.columns:

    st.error(

        "❌ Your CSV must contain a CLOSE column."

    )

    st.stop()


# ============================================================
# FEATURE ENGINEERING
# ============================================================

df["DAILY RETURN (%)"] = (

    df["CLOSE"]

    .pct_change()

    * 100

)


if "PREV. CLOSE" in df.columns:

    df["PRICE CHANGE"] = (

        df["CLOSE"]

        -

        df["PREV. CLOSE"]

    )

else:

    df["PRICE CHANGE"] = df["CLOSE"].diff()


if "HIGH" in df.columns and "LOW" in df.columns:

    df["INTRADAY RANGE"] = (

        df["HIGH"]

        -

        df["LOW"]

    )


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


df["VOLATILITY"] = (

    df["DAILY RETURN (%)"]

    .rolling(20)

    .std()

)


if "VOLUME" in df.columns:

    df["VOLUME MA20"] = (

        df["VOLUME"]

        .rolling(20)

        .mean()

    )


# ============================================================
# RSI
# ============================================================

delta = df["CLOSE"].diff()


gain = delta.where(

    delta > 0,

    0

)


loss = -delta.where(

    delta < 0,

    0

)


avg_gain = gain.rolling(14).mean()


avg_loss = loss.rolling(14).mean()


rs = avg_gain / avg_loss.replace(

    0,

    np.nan

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


# ============================================================
# DATE FILTERS
# ============================================================

with st.sidebar:

    start_date = st.date_input(

        "Start Date",

        value=df["DATE"].min().date(),

        min_value=df["DATE"].min().date(),

        max_value=df["DATE"].max().date()

    )


    end_date = st.date_input(

        "End Date",

        value=df["DATE"].max().date(),

        min_value=df["DATE"].min().date(),

        max_value=df["DATE"].max().date()

    )


if start_date > end_date:

    st.error(

        "❌ Start Date cannot be after End Date."

    )

    st.stop()


filtered_df = df[

    (

        df["DATE"]

        >=

        pd.to_datetime(start_date)

    )

    &

    (

        df["DATE"]

        <=

        pd.to_datetime(end_date)

    )

].copy()


if filtered_df.empty:

    st.warning(

        "⚠️ No data found for the selected date range."

    )

    st.stop()


# ============================================================
# CURRENT MARKET METRICS
# ============================================================

latest = filtered_df.iloc[-1]


current_price = latest["CLOSE"]


highest_price = filtered_df["CLOSE"].max()


lowest_price = filtered_df["CLOSE"].min()


total_return = (

    (

        filtered_df["CLOSE"].iloc[-1]

        /

        filtered_df["CLOSE"].iloc[0]

    )

    -

    1

) * 100


if "VOLUME" in filtered_df.columns:

    average_volume = filtered_df["VOLUME"].mean()

else:

    average_volume = 0


# ============================================================
# MARKET OVERVIEW
# ============================================================

st.markdown(

    '<div class="section-title">📊 Market Overview</div>',

    unsafe_allow_html=True

)


k1, k2, k3, k4, k5 = st.columns(5)


def create_metric(

    container,

    icon,

    title,

    value

):

    container.markdown(

        f"""

        <div class="metric-card">

            <div class="metric-icon">

                {icon}

            </div>

            <div class="metric-title">

                {title}

            </div>

            <div class="metric-value">

                {value}

            </div>

        </div>

        """,

        unsafe_allow_html=True

    )


create_metric(

    k1,

    "💰",

    "Current Price",

    f"${current_price:,.2f}"

)


create_metric(

    k2,

    "📈",

    "Highest Price",

    f"${highest_price:,.2f}"

)


create_metric(

    k3,

    "📉",

    "Lowest Price",

    f"${lowest_price:,.2f}"

)


create_metric(

    k4,

    "📊",

    "Average Volume",

    f"{average_volume:,.0f}"

)


create_metric(

    k5,

    "🚀",

    "Total Return",

    f"{total_return:.2f}%"

)


# ============================================================
# AI TECHNICAL SIGNAL
# ============================================================

score = 0

signal_reasons = []


if pd.notna(latest["MA20"]):

    if current_price > latest["MA20"]:

        score += 1

        signal_reasons.append(

            "Price is above the 20-day moving average."

        )

    else:

        score -= 1

        signal_reasons.append(

            "Price is below the 20-day moving average."

        )


if pd.notna(latest["MA50"]):

    if current_price > latest["MA50"]:

        score += 1

        signal_reasons.append(

            "Price is above the 50-day moving average."

        )

    else:

        score -= 1

        signal_reasons.append(

            "Price is below the 50-day moving average."

        )


if pd.notna(latest["RSI"]):

    if latest["RSI"] < 30:

        score += 2

        signal_reasons.append(

            "RSI indicates an oversold condition."

        )

    elif latest["RSI"] > 70:

        score -= 2

        signal_reasons.append(

            "RSI indicates an overbought condition."

        )


if (

    "VOLUME" in filtered_df.columns

    and

    pd.notna(latest["VOLUME MA20"])

):

    if latest["VOLUME"] > latest["VOLUME MA20"]:

        score += 1

        signal_reasons.append(

            "Trading volume is above its 20-day average."

        )


if score >= 3:

    signal = "🟢 BUY / ACCUMULATE"

    signal_text = "Positive technical momentum detected."


elif score <= -2:

    signal = "🔴 AVOID / BEARISH"

    signal_text = "Negative technical momentum detected."


else:

    signal = "🟡 HOLD / WAIT"

    signal_text = "Market conditions are mixed."


st.markdown(

    f"""

    <div class="signal-card">

        <div class="signal-label">

            🤖 AI TECHNICAL SIGNAL

        </div>

        <div class="signal-value">

            {signal}

        </div>

        <div class="signal-description">

            {signal_text}

            <br>

            Technical Score: <b>{score}</b>

        </div>

    </div>

    """,

    unsafe_allow_html=True

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
# TAB 1 — PRICE ANALYSIS
# ============================================================

with tab1:

    st.markdown(

        '<div class="section-title">📈 Price Analysis</div>',

        unsafe_allow_html=True

    )


    # CHART 1

    fig1 = px.line(

        filtered_df,

        x="DATE",

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


    # CHART 2

    available_price_columns = [

        column

        for column in [

            "OPEN",

            "HIGH",

            "LOW",

            "CLOSE"

        ]

        if column in filtered_df.columns

    ]


    fig2 = px.line(

        filtered_df,

        x="DATE",

        y=available_price_columns,

        title="2️⃣ Open, High, Low & Close Prices"

    )


    fig2.update_layout(

        template="plotly_dark",

        hovermode="x unified"

    )


    st.plotly_chart(

        fig2,

        use_container_width=True

    )


    # CHART 3

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

                    x=filtered_df["DATE"],

                    open=filtered_df["OPEN"],

                    high=filtered_df["HIGH"],

                    low=filtered_df["LOW"],

                    close=filtered_df["CLOSE"]

                )

            ]

        )


        candle.update_layout(

            title="3️⃣ Interactive Candlestick Chart",

            template="plotly_dark",

            xaxis_rangeslider_visible=False

        )


        st.plotly_chart(

            candle,

            use_container_width=True

        )


    # CHART 4

    fig4 = px.area(

        filtered_df,

        x="DATE",

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
# TAB 2 — VOLUME
# ============================================================

with tab2:

    st.markdown(

        '<div class="section-title">📊 Volume Analysis</div>',

        unsafe_allow_html=True

    )


    if "VOLUME" in filtered_df.columns:

        # CHART 5

        fig5 = px.bar(

            filtered_df,

            x="DATE",

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


        # CHART 6

        fig6 = px.line(

            filtered_df,

            x="DATE",

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

        # CHART 7

        fig7 = px.area(

            filtered_df,

            x="DATE",

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


    if "NO. OF  TRADES" in filtered_df.columns:

        # CHART 8

        fig8 = px.line(

            filtered_df,

            x="DATE",

            y="NO. OF  TRADES",

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
# TAB 3 — RISK ANALYSIS
# ============================================================

with tab3:

    st.markdown(

        '<div class="section-title">📉 Risk & Returns</div>',

        unsafe_allow_html=True

    )


    # CHART 9

    fig9 = px.bar(

        filtered_df,

        x="DATE",

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


    # CHART 10

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


    # CHART 11

    fig11 = px.line(

        filtered_df,

        x="DATE",

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


    # CHART 12

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
# TAB 4 — TECHNICAL INDICATORS
# ============================================================

with tab4:

    st.markdown(

        '<div class="section-title">📐 Technical Indicators</div>',

        unsafe_allow_html=True

    )


    # CHART 13

    ma_fig = go.Figure()


    for column in [

        "CLOSE",

        "MA20",

        "MA50",

        "MA200"

    ]:

        ma_fig.add_trace(

            go.Scatter(

                x=filtered_df["DATE"],

                y=filtered_df[column],

                name=column

            )

        )


    ma_fig.update_layout(

        title="1️⃣3️⃣ Moving Average Analysis",

        template="plotly_dark",

        hovermode="x unified"

    )


    st.plotly_chart(

        ma_fig,

        use_container_width=True

    )


    # CHART 14

    if "VWAP" in filtered_df.columns:

        vwap_fig = go.Figure()


        vwap_fig.add_trace(

            go.Scatter(

                x=filtered_df["DATE"],

                y=filtered_df["CLOSE"],

                name="Close Price"

            )

        )


        vwap_fig.add_trace(

            go.Scatter(

                x=filtered_df["DATE"],

                y=filtered_df["VWAP"],

                name="VWAP"

            )

        )


        vwap_fig.update_layout(

            title="1️⃣4️⃣ Price vs VWAP",

            template="plotly_dark"

        )


        st.plotly_chart(

            vwap_fig,

            use_container_width=True

        )


    # CHART 15

    rsi_fig = go.Figure()


    rsi_fig.add_trace(

        go.Scatter(

            x=filtered_df["DATE"],

            y=filtered_df["RSI"],

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

        title="1️⃣5️⃣ RSI Momentum Analysis",

        template="plotly_dark"

    )


    st.plotly_chart(

        rsi_fig,

        use_container_width=True

    )


# ============================================================
# TAB 5 — ADVANCED ANALYTICS
# ============================================================

with tab5:

    st.markdown(

        '<div class="section-title">🔗 Advanced Analytics</div>',

        unsafe_allow_html=True

    )


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


    if len(available_columns) >= 2:

        correlation = (

            filtered_df[available_columns]

            .corr()

        )


        heatmap = px.imshow(

            correlation,

            text_auto=True,

            aspect="auto",

            title="🔗 Feature Correlation Heatmap"

        )


        heatmap.update_layout(

            template="plotly_dark"

        )


        st.plotly_chart(

            heatmap,

            use_container_width=True

        )


# ============================================================
# DOWNLOAD DATA
# ============================================================

st.markdown(

    '<div class="section-title">📥 Export Analysis</div>',

    unsafe_allow_html=True

)


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

    <div class="footer">

        📈 StockVision AI

        <br>

        Intelligent Stock Market Analytics Dashboard

        <br>

        Built with Python • Streamlit • Pandas • Plotly

    </div>

    """,

    unsafe_allow_html=True

)
