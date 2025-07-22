import streamlit as st
import requests
from streamlit_autorefresh import st_autorefresh

st.set_page_config(page_title="Soul Jams Live Counter", layout="centered")

# Auto-refresh every 5 seconds
st_autorefresh(interval=5000, key="counter-refresh")

# Track previous count
if "prev_count" not in st.session_state:
    st.session_state.prev_count = 0

# Get ticket count from backend
try:
    response = requests.get("https://ticket-counter.onrender.com/count")  # Replace with deployed backend
    count = response.json()["count"]
except:
    count = st.session_state.prev_count

# Determine current ticket phase
def get_phase(c):
    if c < 1446:
        return "Early Bird - ₹499"
    elif c < 1946:
        return "Regular - ₹755"
    else:
        return "Final Phase - ₹955"

# Styling: white bg, black text
st.markdown("""
    <style>
    body {
        background-color: white !important;
        color: black !important;
    }
    .stApp {
        background-color: white !important;
        color: black !important;
        font-family: monospace;
    }
    h1, h2, h3, .stMarkdown {
        text-align: center !important;
    }
    </style>
""", unsafe_allow_html=True)

# UI
st.title(f"{count} Tickets Sold")

if count >= 2000:
    st.success("🎉 SOLD OUT!")
else:
    st.subheader(get_phase(count))

# Trigger sound + confetti
if count > st.session_state.prev_count:
    st.audio("sparkle.mp3", format="audio/mp3")
    if count % 50 == 0:
        st.balloons()
    st.caption("🔊 Tap play above once to enable sparkle sound for future ticket sales.")

# Update state
st.session_state.prev_count = count
