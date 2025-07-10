import streamlit as st
import requests
import time
from shared_state import get_count
from streamlit_autorefresh import st_autorefresh

# Set minimal page config
st.set_page_config(page_title="Tickets Sold", layout="centered", initial_sidebar_state="collapsed")

# Refresh every 5 seconds
st_autorefresh(interval=5000, key="counter-refresh")

# Load sparkle sound
audio_file = open("sparkle.mp3", "rb").read()

# Track previous count
if "prev_count" not in st.session_state:
    st.session_state.prev_count = 0

# Get count from Flask backend
try:
    response = requests.get("http://localhost:5000/count")  # Update with deployed backend URL
    count = response.json()["count"]
except:
    count = st.session_state.prev_count

# Ticket phase logic
phase = (
    "Early Bird - ₹499" if count < 1200 else
    "Regular - ₹755" if count < 1850 else
    "Final Phase - ₹955"
)

# UI Styling
st.markdown(
    """
    <style>
    body {
        background-color: white;
        color: black;
        font-family: 'Courier New', monospace;
    }
    h1, h2, h3, .stMarkdown {
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Render counter UI
st.title(f"{count} Tickets Sold")

if count < 2000:
    st.subheader(phase)
else:
    st.success("🎉 SOLD OUT!")

# Sound and Confetti Logic
if count > st.session_state.prev_count:
    st.audio(audio_file, format="audio/mp3")
    if count % 50 == 0:
        st.balloons()

# Update tracker
st.session_state.prev_count = count
