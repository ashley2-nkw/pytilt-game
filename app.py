import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="Tilt Racer",
    page_icon="🏎️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide all Streamlit chrome so game is full-screen
st.markdown("""
<style>
#MainMenu, header, footer { visibility: hidden; }
.stApp { margin: 0 !important; }
.block-container {
    padding: 0 !important;
    max-width: 100% !important;
}
</style>
""", unsafe_allow_html=True)

# Read ?ctrl=PEER_ID from the URL (set by QR code)
ctrl_id = st.query_params.get("ctrl", "")

# Load HTML template and inject the peer ID
html = Path("game.html").read_text()
html = html.replace("__CTRL_ID__", ctrl_id)

components.html(html, height=780, scrolling=False)
