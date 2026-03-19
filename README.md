# 🏎️ Tilt Racer — Streamlit + Phone Controller

A browser racing game played on your PC, steered by tilting your phone.
Uses PeerJS (WebRTC) for real-time peer-to-peer tilt data — no backend needed.

## Files
```
tilt-racer/
├── app.py           # Streamlit entry point
├── game.html        # Full game + controller HTML (embedded by Streamlit)
├── requirements.txt
└── README.md
```

## Deploy to Streamlit Cloud (free)

1. Push this folder to a GitHub repo
2. Go to https://share.streamlit.io → New app
3. Select your repo, set **Main file** to `app.py`
4. Click **Deploy** — done!

## How to play

1. Open the Streamlit app URL on your **PC**
2. A QR code appears bottom-right — **scan it with your phone**
3. On **iPhone**: tap "Allow Motion Sensor" when prompted
4. Hold your phone flat like a steering wheel
5. **Tilt left/right** to dodge incoming traffic
6. Press **Start Game** on the PC

## Fallback controls
- **PC keyboard**: Arrow keys or A/D (for testing without a phone)
- **Phone touch buttons**: ◀ ▶ buttons on screen (if gyro not available)

## How it works
- Streamlit reads `?ctrl=PEER_ID` from the URL via `st.query_params`
- Injects the peer ID into `game.html` before rendering
- PC page creates a PeerJS host → generates QR with `?ctrl=<id>`
- Phone page scans QR → connects as peer → streams tilt data at 20 Hz
- No WebSocket server needed — PeerJS is fully peer-to-peer via WebRTC
