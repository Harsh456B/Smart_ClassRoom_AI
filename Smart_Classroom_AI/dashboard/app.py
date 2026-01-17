import streamlit as st
import json
import time
import os

st.set_page_config(page_title="Smart Classroom AI", layout="wide")
st.title("🎓 Smart Classroom AI – Live Dashboard")

placeholder = st.empty()

while True:
    with placeholder.container():

        if os.path.exists("runtime/live_data.json"):
            try:
                with open("runtime/live_data.json") as f:
                    data = json.load(f)

                col1, col2, col3 = st.columns(3)

                col1.metric("👥 Faces", data["faces_detected"])
                col2.metric("✅ Recognized", data["recognized_faces"])
                col3.metric("❌ Unknown", data["unknown_faces"])

                st.subheader("😊 Recent Emotions")
                st.write(data["recent_emotions"])

                st.subheader("👀 Attention")
                st.write("Focused:", data["focused"])
                st.write("Not Focused:", data["not_focused"])

                st.subheader("📱 Phone Usage")
                st.write("Detected:", data["phone_detected"])

            except:
                st.warning("Data updating...")

        else:
            st.warning("Waiting for live data...")

    time.sleep(1)
