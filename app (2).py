import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px


# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="Stock Market Analysis Dashboard",
    page_icon="📈",
    layout="wide"
)


# =====================================================
# TITLE
# =====================================================

st.title("📈 Stock Market Analysis Dashboard")

st.write(
    "Upload your stock market CSV file to perform interactive data analysis."
)


# =====================================================
# CSV FILE UPLOAD
# =====================================================

uploaded_file = st.file_uploader(
    "📂 Upload Stock Market CSV File",
    type=["csv"]
)


# =====================================================
# IF FILE IS UPLOADED
# =====================================================

if uploaded_file is not None:

    # Read uploaded CSV file

    df = pd.read_csv(uploaded_file)


    # -------------------------------------------------
    # SHOW ORIGINAL DATA
    # -------------------------------------------------

    st.success("✅ CSV file uploaded successfully!")

    st.subheader("📋 Uploaded Dataset")

    st.dataframe(
        df.head(),
        use_container_width=True
    )


    # -------------------------------------------------
    # DATASET INFORMATION
    # -------------------------------------------------

    st.subheader("📊 Dataset Information")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Rows",
        df.shape[0]
    )

    col2.metric(
        "Total Columns",
        df.shape[1]
    )

    col3.metric(
        "Missing Values",
        df.isnull().sum().sum()
    )


    # =================================================
    # CLEAN COLUMN NAMES
    # =================================================

    df.columns = (
        df.columns
        .str.strip()
    )


    # =================================================
    # DATE COLUMN DETECTION
    # =================================================

    if "DATE" in df.columns:

        df["DATE"] = pd.to_datetime(
            df["DATE"],
            errors="coerce"
        )

        df = df.sort_values(
            by="DATE"
        )


    # =================================================
    # NUMERIC DATA CLEANING
    # =================================================

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
        "NO. OF TRADES"
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


    # =================================================
    # FEATURE ENGINEERING
    # =================================================

    if "CLOSE" in df.columns:

        # Daily Return

        df["DAILY RETURN (%)"] = (
            df["CLOSE"]
            .pct_change()
            * 100
        )


        # Price Change

        if "PREV. CLOSE" in df.columns:

            df["PRICE CHANGE"] = (
                df["CLOSE"]
                -
                df["PREV. CLOSE"]
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


        # Volatility

        df["VOLATILITY"] = (
            df["DAILY RETURN (%)"]
            .rolling(20)
            .std()
        )


    # =================================================
    # KPI CARDS
    # =================================================

    if "CLOSE" in df.columns:

        latest_price = df["CLOSE"].iloc[-1]

        highest_price = df["HIGH"].max()

        lowest_price = df["LOW"].min()

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Latest Close",
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


    # =================================================
    # TABS
    # =================================================

    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        [
            "📈 Price",
            "📊 Volume",
            "📉 Returns",
            "📐 Technical Analysis",
            "📋 Data"
        ]
    )


    # =================================================
    # TAB 1: PRICE ANALYSIS
    # =================================================

    with tab1:

        st.subheader("📈 Stock Price Analysis")


        if (
            "DATE" in df.columns
            and
            "CLOSE" in df.columns
        ):

            fig = px.line(
                df,
                x="DATE",
                y="CLOSE",
                title="Closing Price Trend"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )


        if (
            "DATE" in df.columns
            and
            "OPEN" in df.columns
            and
            "CLOSE" in df.columns
        ):

            fig = go.Figure()

            fig.add_trace(
                go.Scatter(
                    x=df["DATE"],
                    y=df["OPEN"],
                    name="Open Price"
                )
            )

            fig.add_trace(
                go.Scatter(
                    x=df["DATE"],
                    y=df["CLOSE"],
                    name="Close Price"
                )
            )

            fig.update_layout(
                title="Open vs Close Price",
                xaxis_title="Date",
                yaxis_title="Price"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )


    # =================================================
    # TAB 2: VOLUME ANALYSIS
    # =================================================

    with tab2:

        st.subheader("📊 Trading Volume Analysis")


        if (
            "DATE" in df.columns
            and
            "VOLUME" in df.columns
        ):

            fig = px.bar(
                df,
                x="DATE",
                y="VOLUME",
                title="Daily Trading Volume"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )


        if (
            "DATE" in df.columns
            and
            "VALUE" in df.columns
        ):

            fig = px.area(
                df,
                x="DATE",
                y="VALUE",
                title="Trading Value"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )


    # =================================================
    # TAB 3: RETURNS ANALYSIS
    # =================================================

    with tab3:

        st.subheader("📉 Returns Analysis")


        if "DAILY RETURN (%)" in df.columns:

            fig = px.bar(
                df,
                x="DATE",
                y="DAILY RETURN (%)",
                title="Daily Stock Returns"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )


            fig2 = px.histogram(
                df,
                x="DAILY RETURN (%)",
                nbins=40,
                title="Daily Return Distribution"
            )

            st.plotly_chart(
                fig2,
                use_container_width=True
            )


    # =================================================
    # TAB 4: TECHNICAL ANALYSIS
    # =================================================

    with tab4:

        st.subheader("📐 Moving Average Analysis")


        if "CLOSE" in df.columns:

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
                title="Moving Average Analysis",
                xaxis_title="Date",
                yaxis_title="Price"
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )


    # =================================================
    # TAB 5: DATA
    # =================================================

    with tab5:

        st.subheader("📋 Complete Uploaded Data")


        st.dataframe(
            df,
            use_container_width=True
        )


        # Download cleaned data

        csv = df.to_csv(
            index=False
        ).encode("utf-8")


        st.download_button(
            label="📥 Download Cleaned Data",
            data=csv,
            file_name="cleaned_stock_data.csv",
            mime="text/csv"
        )


else:

    # =================================================
    # BEFORE UPLOAD
    # =================================================

    st.info(
        "👆 Please upload a CSV file to start the stock market analysis."
    )