import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px
from pathlib import Path

# ------------------------
# Load Model
# ------------------------
MODEL_PATH = Path("artifacts/model_trainer/model.joblib")

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

model = load_model()


# ------------------------
# Feature Engineering (same as training)
# ------------------------
def feature_engineering(df):

    df["date"] = pd.to_datetime(df["date"])

    # Price gap
    df["gap_comp1"] = df["price"] - df["comp1_price"]
    df["gap_comp2"] = df["price"] - df["comp2_price"]
    df["gap_comp3"] = df["price"] - df["comp3_price"]

    # Lag features
    df["price_lag_1"] = df["price"].shift(1)
    df["volume_lag_1"] = df["volume"].shift(1)

    # Rolling windows
    df["volume_ma_7"] = df["volume"].rolling(window=7).mean()
    df["volume_ma_30"] = df["volume"].rolling(window=30).mean()

    df = df.dropna()
    df = df.drop(columns=["date"])

    return df


# ------------------------
# Streamlit UI
# ------------------------
st.set_page_config(
    page_title="Oil Retail Price Optimization",
    page_icon="⛽",
    layout="wide"
)

st.title("⛽ Oil Retail Price Optimization Dashboard")
st.write("This dashboard predicts **fuel volume** based on price and suggests optimal pricing.")


# -------------------------------------
# Navigation Menu
# -------------------------------------
menu = st.sidebar.radio(
    "Navigation",
    ["Home", "Predict", "Charts", "Model Info"],
    index=0
)


# -------------------------------------
# HOME PAGE
# -------------------------------------
if menu == "Home":
    st.subheader("📌 Project Overview")

    st.markdown("""
    ### 🔍 What this app does
    - Predicts daily **fuel volume**  
    - Suggests **best fuel price** to maximize profit  
    - Shows **charts** and **model metrics**  
    - Works with your MLOps pipeline (MLflow, artifacts, etc.)

    ### 🏗 Technology Used
    - Python  
    - XGBoost  
    - Streamlit  
    - MLflow  
    - Custom MLOps Pipeline  
    """)


# -------------------------------------
# PREDICT PAGE
# -------------------------------------
if menu == "Predict":
    st.subheader("📈 Predict Volume + Recommend Best Price")

    uploaded_file = st.file_uploader("Upload today's JSON data", type=["json"])

    if uploaded_file is not None:
        today = pd.read_json(uploaded_file)
        st.write("### Uploaded Input Data")
        st.write(today)

        # Generate feature engineered df
        df = feature_engineering(today.copy())

        X = df.drop(columns=["volume"])
        prediction = model.predict(X)[0]

        st.success(f"### Predicted Volume: **{prediction:,.2f} liters**")

        # ----------------------
        # Price Optimization Logic
        # ----------------------
        price_range = np.arange(100, 200, 0.1)
        profit_results = []

        for p in price_range:
            temp = X.copy()
            temp["price"] = p
            temp["gap_comp1"] = p - today["comp1_price"][0]
            temp["gap_comp2"] = p - today["comp2_price"][0]
            temp["gap_comp3"] = p - today["comp3_price"][0]
            v = model.predict(temp)[0]
            profit_results.append(v * p)

        best_index = np.argmax(profit_results)
        best_price = price_range[best_index]
        best_profit = profit_results[best_index]

        st.success(f"### 💰 Recommended Price: **₹{best_price:.2f}**")
        st.success(f"### 💵 Expected Profit: **₹{best_profit:,.2f}**")

        # Chart
        chart_df = pd.DataFrame({
            "Price": price_range,
            "Profit": profit_results
        })

        fig = px.line(chart_df, x="Price", y="Profit", title="Profit Curve")
        st.plotly_chart(fig, use_container_width=True)


# -------------------------------------
# CHARTS PAGE
# -------------------------------------
if menu == "Charts":
    st.subheader("📊 Model Charts")

    processed_path = Path("artifacts/data_transformation/processed.csv")

    if not processed_path.exists():
        st.error("Processed file not found. Run the pipeline first.")
    else:
        df = pd.read_csv(processed_path)

        st.write("### Sample Training Data")
        st.write(df.head())

        # Actual vs predicted chart
        X = df.drop(columns=["volume"])
        y = df["volume"]
        y_pred = model.predict(X)

        fig2 = px.line(
            x=np.arange(len(y)),
            y=[y, y_pred],
            labels={"x": "Index", "value": "Volume"},
            title="Actual vs Predicted Volume"
        )
        fig2.data[0].name = "Actual"
        fig2.data[1].name = "Predicted"

        st.plotly_chart(fig2, use_container_width=True)


# -------------------------------------
# MODEL INFO
# -------------------------------------
if menu == "Model Info":
    st.subheader("ℹ Model Information")

    st.write("📌 Model stored at:")
    st.code(str(MODEL_PATH))

    st.write("### 🔧 Model Parameters")
    st.json(model.get_params())

    st.write("### 📁 Artifacts Folder")
    st.write("`artifacts/`")

    st.info("Track experiments using **MLflow UI**:\n\n`mlflow ui`")

