import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="StockVision AI",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown(
    """
    <style>

    /* =================================================
       MAIN APPLICATION BACKGROUND
    ================================================= */

    .stApp {

        background:
        linear-gradient(
            135deg,
            #0f172a 0%,
            #111827 50%,
            #020617 100%
        );

        color: #f8fafc;

    }


    /* =================================================
       MAIN CONTENT
    ================================================= */

    .block-container {

        padding-top: 2rem;

        padding-bottom: 3rem;

    }


    /* =================================================
       SIDEBAR BACKGROUND
    ================================================= */

    section[data-testid="stSidebar"] {

        background:

        linear-gradient(
            180deg,
            #111827,
            #020617
        );

        border-right: 1px solid #334155;

    }


    /* =================================================
       SIDEBAR ALL TEXT
    ================================================= */

    section[data-testid="stSidebar"] * {

        color: #f8fafc !important;

    }


    /* =================================================
       FILE UPLOADER OUTER BOX
    ================================================= */

    section[data-testid="stSidebar"]
    div[data-testid="stFileUploader"] {

        background: #ffffff !important;

        border-radius: 14px !important;

        padding: 10px !important;

        border: 2px solid #cbd5e1 !important;

    }


    /* =================================================
       FILE UPLOADER TEXT
    ================================================= */

    section[data-testid="stSidebar"]
    div[data-testid="stFileUploader"] label {

        color: #0f172a !important;

        font-weight: 700 !important;

    }


    /* =================================================
       UPLOADER DROPZONE
    ================================================= */

    section[data-testid="stSidebar"]
    div[data-testid="stFileUploaderDropzone"] {

        background: #ffffff !important;

        border: 2px dashed #94a3b8 !important;

        border-radius: 10px !important;

    }


    /* =================================================
       UPLOADED FILE NAME
    ================================================= */

    section[data-testid="stSidebar"]
    div[data-testid="stFileUploader"] span {

        color: #0f172a !important;

        font-weight: 600 !important;

    }


    /* =================================================
       UPLOADED FILE INFORMATION
    ================================================= */

    section[data-testid="stSidebar"]
    div[data-testid="stFileUploader"] small {

        color: #475569 !important;

    }


    /* =================================================
       BROWSE FILE BUTTON
    ================================================= */

    section[data-testid="stSidebar"]
    div[data-testid="stFileUploader"] button {

        background: #2563eb !important;

        color: #ffffff !important;

        border: none !important;

        border-radius: 8px !important;

        font-weight: 700 !important;

    }


    /* =================================================
       DATE INPUT CONTAINER
    ================================================= */

    section[data-testid="stSidebar"]
    div[data-testid="stDateInput"] {

        margin-bottom: 18px;

    }


    /* =================================================
       DATE INPUT LABEL
    ================================================= */

    section[data-testid="stSidebar"]
    div[data-testid="stDateInput"] label {

        color: #f8fafc !important;

        font-size: 15px !important;

        font-weight: 700 !important;

    }


    /* =================================================
       DATE INPUT WHITE BOX
    ================================================= */

    section[data-testid="stSidebar"]
    div[data-testid="stDateInput"] input {

        background: #ffffff !important;

        color: #0f172a !important;

        border: 2px solid #cbd5e1 !important;

        border-radius: 12px !important;

        padding: 12px !important;

        font-size: 15px !important;

        font-weight: 600 !important;

    }


    /* =================================================
       DATE PLACEHOLDER
    ================================================= */

    section[data-testid="stSidebar"]
    div[data-testid="stDateInput"] input::placeholder {

        color: #64748b !important;

        opacity: 1 !important;

    }


    /* =================================================
       DATE INPUT FOCUS
    ================================================= */

    section[data-testid="stSidebar"]
    div[data-testid="stDateInput"] input:focus {

        border-color: #2563eb !important;

        box-shadow:

        0 0 0 2px

        rgba(37, 99, 235, 0.25) !important;

    }


    /* =================================================
       TITLE
    ================================================= */

    .main-title {

        font-size: 42px;

        font-weight: 800;

        background:

        linear-gradient(

            90deg,

            #38bdf8,

            #818cf8,

            #c084fc

        );

        -webkit-background-clip: text;

        -webkit-text-fill-color: transparent;

        margin-bottom: 0px;

    }


    /* =================================================
       SUBTITLE
    ================================================= */

    .subtitle {

        color: #94a3b8;

        font-size: 17px;

        margin-top: 5px;

        margin-bottom: 30px;

    }


    /* =================================================
       KPI CARDS
    ================================================= */

    .metric-card {

        background:

        linear-gradient(

            145deg,

            rgba(30, 41, 59, 0.95),

            rgba(15, 23, 42, 0.95)

        );

        border: 1px solid #334155;

        border-radius: 18px;

        padding: 22px;

        min-height: 125px;

        box-shadow:

        0 10px 30px

        rgba(0, 0, 0, 0.25);

        transition: 0.3s;

    }


    .metric-card:hover {

        transform: translateY(-5px);

        border-color: #38bdf8;

        box-shadow:

        0 15px 35px

        rgba(56, 189, 248, 0.15);

    }


    .metric-title {

        color: #94a3b8;

        font-size: 13px;

        font-weight: 600;

        text-transform: uppercase;

        letter-spacing: 1px;

    }


    .metric-value {

        font-size: 27px;

        font-weight: 800;

        color: #f8fafc;

        margin-top: 10px;

    }


    /* =================================================
       SIGNAL CARD
    ================================================= */

    .signal-card {

        padding: 25px;

        border-radius: 20px;

        background:

        linear-gradient(

            135deg,

            #172554,

            #1e1b4b

        );

        border: 1px solid #3730a3;

        box-shadow:

        0 10px 30px

        rgba(79, 70, 229, 0.18);

        margin-top: 25px;

        margin-bottom: 25px;

    }


    .signal-title {

        color: #a5b4fc;

        font-size: 14px;

        text-transform: uppercase;

        letter-spacing: 1px;

    }


    .signal-value {

        font-size: 34px;

        font-weight: 800;

        margin-top: 10px;

    }


    /* =================================================
       SECTION HEADER
    ================================================= */

    .section-header {

        font-size: 26px;

        font-weight: 750;

        color: #f8fafc;

        margin-top: 25px;

        margin-bottom: 15px;

    }


    /* =================================================
       CHART CONTAINER
    ================================================= */

    div[data-testid="stPlotlyChart"] {

        background:

        rgba(15, 23, 42, 0.75);

        border-radius: 18px;

        padding: 10px;

        border: 1px solid #1e293b;

        box-shadow:

        0 10px 25px

        rgba(0, 0, 0, 0.18);

        margin-bottom: 20px;

    }


    /* =================================================
       TABS
    ================================================= */

    button[data-baseweb="tab"] {

        font-size: 15px;

        font-weight: 600;

        color: #94a3b8;

    }


    button[data-baseweb="tab"][aria-selected="true"] {

        color: #38bdf8;

    }


    /* =================================================
       DOWNLOAD BUTTON
    ================================================= */

    .stDownloadButton button {

        width: 100%;

        border-radius: 10px;

        border: 1px solid #38bdf8;

        background: #0f172a;

        color: #38bdf8;

        font-weight: 700;

    }


    .stDownloadButton button:hover {

        background: #38bdf8;

        color: #020617;

    }


    /* =================================================
       FOOTER
    ================================================= */

    .footer {

        text-align: center;

        color: #64748b;

        margin-top: 40px;

        padding: 20px;

        border-top: 1px solid #1e293b;

    }

    </style>
    """,

    unsafe_allow_html=True
)


# =====================================================
# HEADER
# =====================================================

st.markdown(

    '<div class="main-title">📈 StockVision AI</div>',

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


# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.markdown(

        "## 📊 StockVision AI"

    )

    st.markdown("---")


    # =================================================
    # CSV UPLOAD
    # =================================================

    uploaded_file = st.file_uploader(

        "📂 Upload Stock CSV",

        type=["csv"]

    )


    st.markdown("---")


    # =================================================
    # FEATURES
    # =================================================

    st.markdown(

        "### 📌 Dashboard Features"

    )

    st.markdown(

        """
        📈 Price Analysis

        🕯️ Candlestick Chart

        📊 Volume Analysis

        📉 Returns & Risk

        📐 Technical Indicators

        🔗 Correlation Analysis

        🤖 AI Technical Signal

        """

    )


# =====================================================
# CHECK FILE
# =====================================================

if uploaded_file is None:

    st.info(

        "👆 Upload a CSV file from the sidebar to start analysis."

    )

    st.stop()


# =====================================================
# LOAD DATA
# =====================================================

df = pd.read_csv(

    uploaded_file

)


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

        "DATE"

    )


# =====================================================
# NUMERIC CLEANING
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

            .str.replace(

                ",",

                "",

                regex=False

            )

            .str.replace(

                "₹",

                "",

                regex=False

            )

        )

        df[column] = pd.to_numeric(

            df[column],

            errors="coerce"

        )


# =====================================================
# FEATURE ENGINEERING
# =====================================================

df["DAILY RETURN (%)"] = (

    df["CLOSE"]

    .pct_change()

    * 100

)


df["PRICE CHANGE"] = (

    df["CLOSE"]

    -

    df["PREV. CLOSE"]

)


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


df["VOLUME MA20"] = (

    df["VOLUME"]

    .rolling(20)

    .mean()

)


# =====================================================
# RSI
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


avg_gain = gain.rolling(14).mean()

avg_loss = loss.rolling(14).mean()


rs = avg_gain / avg_loss


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
# DATE FILTER
# =====================================================

st.sidebar.markdown(

    "### 📅 Date Filter"

)


start_date = st.sidebar.date_input(

    "Start Date",

    df["DATE"].min()

)


end_date = st.sidebar.date_input(

    "End Date",

    df["DATE"].max()

)


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

]


# =====================================================
# CURRENT DATA
# =====================================================

latest = filtered_df.iloc[-1]


current_price = latest["CLOSE"]


highest_price = filtered_df["HIGH"].max()


lowest_price = filtered_df["LOW"].min()


average_volume = filtered_df["VOLUME"].mean()


total_return = (

    (

        filtered_df["CLOSE"].iloc[-1]

        /

        filtered_df["CLOSE"].iloc[0]

    )

    -

    1

) * 100


# =====================================================
# KPI CARDS
# =====================================================

st.markdown(

    '<div class="section-header">📊 Market Overview</div>',

    unsafe_allow_html=True

)


kpi1, kpi2, kpi3, kpi4, kpi5 = st.columns(5)


def metric_card(

    container,

    title,

    value

):

    container.markdown(

        f"""

        <div class="metric-card">

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


metric_card(

    kpi1,

    "Current Price",

    f"₹{current_price:,.2f}"

)


metric_card(

    kpi2,

    "Highest Price",

    f"₹{highest_price:,.2f}"

)


metric_card(

    kpi3,

    "Lowest Price",

    f"₹{lowest_price:,.2f}"

)


metric_card(

    kpi4,

    "Average Volume",

    f"{average_volume:,.0f}"

)


metric_card(

    kpi5,

    "Total Return",

    f"{total_return:.2f}%"

)


# =====================================================
# AI SIGNAL
# =====================================================

score = 0


if current_price > latest["MA20"]:

    score += 1

else:

    score -= 1


if current_price > latest["MA50"]:

    score += 1

else:

    score -= 1


if latest["RSI"] < 30:

    score += 2


elif latest["RSI"] > 70:

    score -= 2


if latest["VOLUME"] > latest["VOLUME MA20"]:

    score += 1


if score >= 3:

    signal = "🟢 BUY / ACCUMULATE"


elif score <= -2:

    signal = "🔴 AVOID / BEARISH"


else:

    signal = "🟡 HOLD / WAIT"


st.markdown(

    f"""

    <div class="signal-card">

    <div class="signal-title">

    🤖 AI TECHNICAL SIGNAL

    </div>

    <div class="signal-value">

    {signal}

    </div>

    <p>

    Technical Score: <b>{score}</b>

    </p>

    </div>

    """,

    unsafe_allow_html=True

)


# =====================================================
# TABS
# =====================================================

tab1, tab2, tab3, tab4, tab5 = st.tabs(

    [

        "📈 Price",

        "📊 Volume",

        "📉 Risk",

        "📐 Technical",

        "🔗 Advanced"

    ]

)


# =====================================================
# TAB 1: PRICE
# =====================================================

with tab1:

    st.markdown(

        '<div class="section-header">📈 Price Analysis</div>',

        unsafe_allow_html=True

    )


    fig1 = px.line(

        filtered_df,

        x="DATE",

        y="CLOSE",

        title="Closing Price Trend"

    )


    fig1.update_layout(

        template="plotly_dark"

    )


    st.plotly_chart(

        fig1,

        use_container_width=True

    )


    fig2 = go.Figure()


    fig2.add_trace(

        go.Scatter(

            x=filtered_df["DATE"],

            y=filtered_df["OPEN"],

            name="Open"

        )

    )


    fig2.add_trace(

        go.Scatter(

            x=filtered_df["DATE"],

            y=filtered_df["CLOSE"],

            name="Close"

        )

    )


    fig2.update_layout(

        title="Open vs Close Price",

        template="plotly_dark"

    )


    st.plotly_chart(

        fig2,

        use_container_width=True

    )


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

        title="Interactive Candlestick Chart",

        template="plotly_dark",

        xaxis_rangeslider_visible=False

    )


    st.plotly_chart(

        candle,

        use_container_width=True

    )


# =====================================================
# TAB 2: VOLUME
# =====================================================

with tab2:

    st.markdown(

        '<div class="section-header">📊 Trading Activity</div>',

        unsafe_allow_html=True

    )


    fig5 = px.bar(

        filtered_df,

        x="DATE",

        y="VOLUME",

        title="Trading Volume"

    )


    fig5.update_layout(

        template="plotly_dark"

    )


    st.plotly_chart(

        fig5,

        use_container_width=True

    )


    fig6 = px.area(

        filtered_df,

        x="DATE",

        y="VALUE",

        title="Trading Value"

    )


    fig6.update_layout(

        template="plotly_dark"

    )


    st.plotly_chart(

        fig6,

        use_container_width=True

    )


    fig7 = px.line(

        filtered_df,

        x="DATE",

        y="NO. OF  TRADES",

        title="Number of Trades"

    )


    fig7.update_layout(

        template="plotly_dark"

    )


    st.plotly_chart(

        fig7,

        use_container_width=True

    )


# =====================================================
# TAB 3: RISK
# =====================================================

with tab3:

    st.markdown(

        '<div class="section-header">📉 Returns & Risk</div>',

        unsafe_allow_html=True

    )


    fig8 = px.bar(

        filtered_df,

        x="DATE",

        y="DAILY RETURN (%)",

        title="Daily Returns"

    )


    fig8.update_layout(

        template="plotly_dark"

    )


    st.plotly_chart(

        fig8,

        use_container_width=True

    )


    fig9 = px.histogram(

        filtered_df,

        x="DAILY RETURN (%)",

        nbins=40,

        title="Return Distribution"

    )


    fig9.update_layout(

        template="plotly_dark"

    )


    st.plotly_chart(

        fig9,

        use_container_width=True

    )


    fig10 = px.line(

        filtered_df,

        x="DATE",

        y="VOLATILITY",

        title="Rolling Volatility"

    )


    fig10.update_layout(

        template="plotly_dark"

    )


    st.plotly_chart(

        fig10,

        use_container_width=True

    )


    fig11 = px.box(

        filtered_df,

        y="CLOSE",

        title="Price Distribution"

    )


    fig11.update_layout(

        template="plotly_dark"

    )


    st.plotly_chart(

        fig11,

        use_container_width=True

    )


# =====================================================
# TAB 4: TECHNICAL
# =====================================================

with tab4:

    st.markdown(

        '<div class="section-header">📐 Technical Indicators</div>',

        unsafe_allow_html=True

    )


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

        title="Moving Average Analysis",

        template="plotly_dark"

    )


    st.plotly_chart(

        ma_fig,

        use_container_width=True

    )


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

        title="Price vs VWAP",

        template="plotly_dark"

    )


    st.plotly_chart(

        vwap_fig,

        use_container_width=True

    )


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

        title="RSI Momentum Analysis",

        template="plotly_dark"

    )


    st.plotly_chart(

        rsi_fig,

        use_container_width=True

    )


# =====================================================
# TAB 5: ADVANCED
# =====================================================

with tab5:

    st.markdown(

        '<div class="section-header">🔗 Advanced Analytics</div>',

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


    correlation = (

        filtered_df[available_columns]

        .corr()

    )


    heatmap = px.imshow(

        correlation,

        text_auto=True,

        aspect="auto",

        title="Feature Correlation Heatmap"

    )


    heatmap.update_layout(

        template="plotly_dark"

    )


    st.plotly_chart(

        heatmap,

        use_container_width=True

    )


# =====================================================
# DOWNLOAD
# =====================================================

st.markdown(

    '<div class="section-header">📥 Export Analysis</div>',

    unsafe_allow_html=True

)


csv = filtered_df.to_csv(

    index=False

).encode("utf-8")


st.download_button(

    label="📥 Download Complete Analysis CSV",

    data=csv,

    file_name="stockvision_analysis.csv",

    mime="text/csv"

)


# =====================================================
# FOOTER
# =====================================================

st.markdown(

    """

    <div class="footer">

    📈 StockVision AI • Built with Python, Streamlit,
    Pandas & Plotly

    </div>

    """,

    unsafe_allow_html=True

)
