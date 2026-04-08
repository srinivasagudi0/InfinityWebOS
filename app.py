from datetime import datetime

import streamlit as st
from support import *

st.set_page_config(page_title="InfinityOS", page_icon=":computer:", layout="wide")

now = datetime.now()
clock_time = now.strftime("%I:%M %p")
clock_date = now.strftime("%A, %B %d").replace(" 0", " ")

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&display=swap');

    :root {
        --text: #f8fbff;
        --muted: rgba(248, 251, 255, 0.72);
        --glass: rgba(22, 14, 10, 0.30);
        --glass-strong: rgba(8, 10, 18, 0.42);
        --glass-border: rgba(255, 255, 255, 0.14);
        --shadow: 0 20px 60px rgba(0, 0, 0, 0.36);
    }

    .stApp {
        background:
            linear-gradient(120deg, rgba(255, 181, 103, 0.90), rgba(255, 62, 62, 0.92) 26%, rgba(15, 4, 6, 0.98) 48%, rgba(215, 51, 221, 0.88) 75%, rgba(41, 55, 112, 0.88)),
            radial-gradient(circle at 18% 18%, rgba(255, 240, 180, 0.34), transparent 18%),
            radial-gradient(circle at 78% 20%, rgba(255, 0, 140, 0.24), transparent 18%),
            radial-gradient(circle at 86% 78%, rgba(63, 206, 255, 0.20), transparent 20%);
        color: var(--text);
        font-family: 'Space Grotesk', sans-serif;
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    .main .block-container {
        max-width: 100%;
        min-height: 100vh;
        padding: 0.8rem 1rem 8rem;
    }

    h1, h2, h3, p, label, div, span, button {
        font-family: 'Space Grotesk', sans-serif !important;
    }

    .desktop {
        min-height: calc(100vh - 8rem);
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }

    .topbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 14px;
        padding: 0.2rem 0.2rem 0;
    }

    .brand {
        display: flex;
        align-items: center;
        gap: 14px;
        max-width: 680px;
    }

    .brand-kicker {
        display: inline-block;
        padding: 0.45rem 0.75rem;
        border-radius: 999px;
        background: rgba(255, 255, 255, 0.10);
        border: 1px solid rgba(255, 255, 255, 0.12);
        font-size: 0.72rem;
        letter-spacing: 0.16em;
        text-transform: uppercase;
        backdrop-filter: blur(12px);
    }

    .brand-text {
        display: flex;
        flex-direction: column;
        gap: 0.25rem;
    }

    .brand h1 {
        margin: 0;
        font-size: clamp(1.5rem, 3vw, 2.1rem);
        line-height: 1;
        font-weight: 700;
        text-shadow: 0 10px 30px rgba(0, 0, 0, 0.18);
    }

    .brand p {
        margin: 0;
        max-width: 420px;
        color: var(--muted);
        font-size: 0.88rem;
        line-height: 1.4;
    }

    .clock-card {
        min-width: 188px;
        padding: 0.8rem 0.95rem;
        border-radius: 18px;
        background: rgba(10, 12, 20, 0.26);
        border: 1px solid rgba(255, 255, 255, 0.14);
        backdrop-filter: blur(16px);
        box-shadow: var(--shadow);
        text-align: right;
    }

    .clock-time {
        font-size: 1.45rem;
        font-weight: 700;
        line-height: 1;
    }

    .clock-date {
        margin-top: 0.3rem;
        color: var(--muted);
        font-size: 0.82rem;
    }

    .glow-space {
        flex: 1;
        display: grid;
        place-items: center;
    }

    .glow-ring {
        width: min(30vw, 260px);
        aspect-ratio: 1;
        border-radius: 999px;
        background:
            radial-gradient(circle at 30% 30%, rgba(255, 255, 255, 0.4), transparent 24%),
            radial-gradient(circle at 50% 50%, rgba(255, 89, 89, 0.26), transparent 44%),
            linear-gradient(145deg, rgba(255, 255, 255, 0.18), rgba(255, 255, 255, 0.02));
        border: 1px solid rgba(255, 255, 255, 0.14);
        box-shadow: 0 0 100px rgba(255, 64, 64, 0.20), inset 0 0 30px rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(10px);
    }

    .dock-wrap {
        position: fixed;
        left: 50%;
        bottom: 16px;
        transform: translateX(-50%);
        width: min(1540px, calc(100vw - 34px));
        z-index: 9999;
    }

    .dock {
        padding: 0.62rem;
        border-radius: 26px;
        background: linear-gradient(180deg, rgba(93, 56, 38, 0.44), rgba(10, 12, 19, 0.52));
        border: 1px solid var(--glass-border);
        backdrop-filter: blur(26px) saturate(145%);
        box-shadow: var(--shadow);
    }

    .dock-grid {
        display: grid;
        grid-template-columns: repeat(11, minmax(0, 1fr));
        gap: 9px;
        align-items: center;
    }

    .dock-grid > div {
        width: 100%;
    }

    .dock-grid div[data-testid="stButton"] {
        margin: 0;
        width: 100%;
    }

    .dock-grid .stButton > button {
        width: 100%;
        height: 76px;
        min-height: 76px;
        border-radius: 19px;
        border: 1px solid rgba(255, 255, 255, 0.16);
        color: white;
        font-size: 0.78rem;
        font-weight: 700;
        line-height: 1.15;
        padding: 0.45rem 0.25rem;
        box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.16), 0 10px 18px rgba(0, 0, 0, 0.18);
        transition: transform 0.16s ease, filter 0.16s ease, border-color 0.16s ease;
    }

    .dock-grid .stButton > button:hover {
        transform: translateY(-7px) scale(1.02);
        filter: brightness(1.05);
        border-color: rgba(255, 255, 255, 0.34);
        color: white;
    }

    .dock-grid .stButton > button:focus {
        box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.16), 0 10px 18px rgba(0, 0, 0, 0.18);
    }

    div[data-testid="column"]:nth-of-type(1) .stButton > button,
    div[data-testid="column"]:nth-of-type(2) .stButton > button,
    div[data-testid="column"]:nth-of-type(3) .stButton > button,
    div[data-testid="column"]:nth-of-type(4) .stButton > button,
    div[data-testid="column"]:nth-of-type(5) .stButton > button {
        background:
            linear-gradient(180deg, rgba(255, 255, 255, 0.18), rgba(255, 255, 255, 0.02)),
            linear-gradient(180deg, #132743, #08182d);
    }

    .dock-link {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 100%;
        height: 76px;
        min-height: 76px;
        box-sizing: border-box;
        border-radius: 19px;
        text-decoration: none;
        color: white;
        font-weight: 700;
        font-size: 0.78rem;
        line-height: 1.15;
        text-align: center;
        padding: 0.45rem 0.25rem;
        border: 1px solid rgba(255, 255, 255, 0.16);
        box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.16), 0 10px 18px rgba(0, 0, 0, 0.18);
        transition: transform 0.16s ease, filter 0.16s ease, border-color 0.16s ease;
    }

    .dock-link:hover {
        transform: translateY(-7px) scale(1.02);
        filter: brightness(1.06);
        border-color: rgba(255, 255, 255, 0.34);
    }

    .google,
    .youtube,
    .spotify,
    .trash {
        background:
            linear-gradient(180deg, rgba(255, 255, 255, 0.18), rgba(255, 255, 255, 0.02)),
            linear-gradient(180deg, #132743, #08182d);
        color: white;
    }

    .divider {
        width: 1px;
        height: 48px;
        margin: 0 auto;
        background: rgba(255, 255, 255, 0.22);
        border-radius: 999px;
    }

    @media (max-width: 1200px) {
        .dock-grid {
            grid-template-columns: repeat(6, minmax(0, 1fr));
        }
    }

    @media (max-width: 760px) {
        .main .block-container {
            padding: 0.9rem 0.7rem 15rem;
        }

        .topbar {
            flex-direction: column;
            align-items: stretch;
        }

        .clock-card {
            width: 100%;
            text-align: left;
        }

        .dock-wrap {
            width: calc(100vw - 14px);
            bottom: 8px;
        }

        .dock-grid {
            grid-template-columns: repeat(4, minmax(0, 1fr));
            gap: 8px;
        }

        .dock-grid .stButton > button,
        .dock-link {
            height: 68px;
            min-height: 68px;
            font-size: 0.74rem;
        }

        .divider {
            display: none;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <div class="desktop">
        <div class="topbar">
            <div class="brand">
                <div class="brand-kicker">Desktop Preview</div>
                <div class="brand-text">
                    <h1>InfinityOS</h1>
                    <p>Minimal desktop, centered glass dock, cleaner proportions.</p>
                </div>
            </div>
            <div class="clock-card">
                <div class="clock-time">{clock_time}</div>
                <div class="clock-date">{clock_date}</div>
            </div>
        </div>
        <div class="glow-space">
            <div class="glow-ring"></div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="dock-wrap">
        <div class="dock">
            <div class="dock-grid">
    """,
    unsafe_allow_html=True,
)

dock_cols = st.columns(11, gap="small")

with dock_cols[0]:
    if st.button("⌘\nCalc", key="launch_calc"):
        open_calculator()

with dock_cols[1]:
    if st.button("⌘\nNotes", key="launch_notes"):
        open_notepad()

with dock_cols[2]:
    if st.button("⌘\nFiles", key="launch_files"):
        open_file_explorer()

with dock_cols[3]:
    if st.button("⌘\nSettings", key="launch_settings"):
        open_settings()

with dock_cols[4]:
    if st.button("⌘\nMusic", key="launch_music"):
        open_music_player()

with dock_cols[5]:
    st.markdown('<a class="dock-link google" href="https://www.google.com/" target="_blank">⌘<br>Google</a>', unsafe_allow_html=True)

with dock_cols[6]:
    st.markdown('<a class="dock-link youtube" href="https://www.youtube.com/" target="_blank">⌘<br>YouTube</a>', unsafe_allow_html=True)

with dock_cols[7]:
    st.markdown('<a class="dock-link spotify" href="https://open.spotify.com/" target="_blank">⌘<br>Spotify</a>', unsafe_allow_html=True)

with dock_cols[8]:
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

with dock_cols[9]:
    if st.button("⌘\nBin", key="launch_bin"):
        open_file_explorer()

with dock_cols[10]:
    if st.button("⌘\nApps", key="launch_apps"):
        open_file_explorer()

st.markdown(
    """
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)
