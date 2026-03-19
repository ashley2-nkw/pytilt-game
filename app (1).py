import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="Tilt Racer",
    page_icon="🏎️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit chrome
st.markdown("""
<style>
#MainMenu, header, footer { visibility: hidden; }
.stApp { margin: 0 !important; }
.block-container { padding: 0 !important; max-width: 100% !important; }
</style>
""", unsafe_allow_html=True)

ctrl_id = st.query_params.get("ctrl", "")

if ctrl_id:
    # ── Phone / controller mode ──────────────────────────────
    # No URL bar needed, just render the controller
    html = Path("game.html").read_text()
    html = html.replace("__CTRL_ID__", ctrl_id)
    html = html.replace("__BASE_URL__", "")
    components.html(html, height=900, scrolling=False)

else:
    # ── PC / host mode ───────────────────────────────────────
    # The iframe can't read window.parent.location (cross-origin),
    # so we ask the user to paste their Streamlit URL once.
    # That URL gets injected into the HTML → used to build the QR.

    st.markdown("""
    <div style="background:#0a0a0f;color:#888;font-family:'Courier New',monospace;
        font-size:12px;padding:10px 16px 2px;">
        📋 Paste your Streamlit app URL so the QR code points to the right place:
    </div>
    """, unsafe_allow_html=True)

    base_url = st.text_input(
        label="url",
        placeholder="https://your-app.streamlit.app",
        label_visibility="collapsed",
    ).strip().rstrip("/")

    if not base_url:
        st.markdown("""
        <div style="background:#0a0a0f;color:#444;font-family:'Courier New',monospace;
            font-size:11px;padding:2px 16px 10px;">
            ☝️ Enter URL above → QR appears in-game (bottom-right) → scan with phone → tilt to race!
        </div>
        """, unsafe_allow_html=True)

    html = Path("game.html").read_text()
    html = html.replace("__CTRL_ID__", "")
    html = html.replace("__BASE_URL__", base_url)
    components.html(html, height=820, scrolling=False)
