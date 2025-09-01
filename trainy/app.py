# app.py
import streamlit as st
import pandas as pd
import time
from model import load_or_train_model
from utils import plot_confusion_matrix, plot_roc_curve, classification_report_df, plot_permission_bar
from models import main_backend  
st.set_page_config(
    page_title="DefenX",
    page_icon="🔒",
    layout="wide"
)

model = load_or_train_model()

st.sidebar.title("🔎 Navigation")
page = st.sidebar.radio("Go to:", ["🏠 Home", "🔍 Detect App", "📊 Insights", "ℹ️ About"])

if page == "🏠 Home":
    st.title("🏠 DefenX")
    uploaded_file = st.file_uploader("📂 Upload CSV Dataset", type=["csv"])
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df.head())
        
        if "label" in df.columns:
            X = df.drop("label", axis=1)
            y_true = df["label"]
            y_pred = model.predict(X)
            y_proba = model.predict_proba(X)[:, 1]

            from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

            acc = accuracy_score(y_true, y_pred) * 100
            precision = precision_score(y_true, y_pred, zero_division=0) * 100
            recall = recall_score(y_true, y_pred, zero_division=0) * 100
            f1 = f1_score(y_true, y_pred, zero_division=0) * 100
            cm = confusion_matrix(y_true, y_pred)

            st.metric("Accuracy", f"{acc:.2f}%")
            col1, col2, col3 = st.columns(3)
            col1.metric("Precision", f"{precision:.2f}%")
            col2.metric("Recall", f"{recall:.2f}%")
            col3.metric("F1-Score", f"{f1:.2f}%")

            st.plotly_chart(plot_confusion_matrix(cm), use_container_width=True)
            st.pyplot(plot_roc_curve(y_true, y_proba))

            st.subheader("📄 Classification Report")
            st.dataframe(classification_report_df(y_true, y_pred))

elif page == "🔍 Detect App":
    st.title("🔍 Detect Fake App")
    col1, col2 = st.columns(2)
    
    with col1:
        app_name = st.text_input("📱 App Name")
        developer = st.text_input("👨‍💻 Developer")
        downloads = st.number_input("⬇️ Downloads", min_value=0, step=1000)
        
    with col2:
        rating = st.slider("⭐ Rating", 0.0, 5.0, 4.0, step=0.1)
        size = st.number_input("📦 Size (MB)", min_value=1, max_value=500)
        
    permissions = st.multiselect(
        "🔑 Permissions",
        ["SMS","Contacts","Camera","Location","Microphone","Storage","Phone State","Internet","Overlay","Accessibility"],
        default=["Internet"]
    )

    if st.button("🤖 Detect (ML Model)"):
        with st.spinner("⏳ Running Model..."):
            time.sleep(2)
            features = pd.DataFrame([{
                "downloads": downloads,
                "rating": rating,
                "size": size,
                "sms_permission": 1 if "SMS" in permissions else 0,
                "accessibility_permission": 1 if "Accessibility" in permissions else 0,
                "overlay_permission": 1 if "Overlay" in permissions else 0
            }])
            prediction = model.predict(features)[0]
            proba = model.predict_proba(features)[0][1]

            if prediction == 1:
                st.error(f"⚠️ Fake App! Confidence: {proba*100:.1f}%")
            else:
                st.success(f"✅ Safe App! Confidence: {proba*100:.1f}%")

elif page == "📊 Insights":
    st.title("📊 Insights")
    st.markdown("### Most Risky Permissions in Fake Apps")
    
    permissions_data = {"SMS": 40, "Accessibility": 25, "Overlay": 15, "Camera": 10, "Location": 10}
    st.pyplot(plot_permission_bar(permissions_data))

elif page == "ℹ️ About":
    st.title("ℹ️ About Project")
    st.markdown(
        """
        **Fake Banking App Detector**  
        **Hackathon 2025**  

        This project aims to protect users from fake banking apps using Machine Learning.
        It predicts the likelihood of an app being fake based on downloads, ratings, size, and dangerous permissions.
        """
    )
