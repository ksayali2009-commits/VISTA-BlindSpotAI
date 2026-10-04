
import streamlit as st
from transformers import pipeline

# --- PAGE CONFIG ---
st.set_page_config(page_title="VISTA", layout="wide")

# --- HEADER BANNER ---
st.markdown("<h1 style='text-align: center; color: #00FFAA;'>🧠 VISTA - Blind Spot AI 🧠</h1>", unsafe_allow_html=True)

# --- GLOBAL STYLES ---
st.markdown(
    """
    <style>
    body {
        background-color: #121212; /* Dark background */
        color: #ffffff; /* White text */
        font-family: 'Segoe UI', sans-serif;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #45a049;
        transform: scale(1.05);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- MODE SWITCHER ---
mode = st.radio("🎨 Choose Mode:", ["🌙 Dark", "☀️ Light", "👓 Eye Comfort"])

if mode == "🌙 Dark":
    st.markdown("<style>body {background-color: #000000; color: #FFFFFF;}</style>", unsafe_allow_html=True)
elif mode == "☀️ Light":
    st.markdown("<style>body {background-color: #FFFFFF; color: #000000;}</style>", unsafe_allow_html=True)
elif mode == "👓 Eye Comfort":
    st.markdown("<style>body {background-color: #2E3B2E; color: #E0E0C0;}</style>", unsafe_allow_html=True)

# --- LAYOUT ---
col1, col2 = st.columns([1,2])

with col1:
    st.header("👤 Create Profile")
    name = st.text_input("Name")
    role = st.text_input("💼 Role (e.g., Student, Engineer)")
    goal = st.text_input("🎯 Decision Goal")

with col2:
    st.header("📝 Decision Reasoning")
    user_input = st.text_area("Describe your decision reasoning:")
    generator = pipeline("text-generation", model="gpt2")

    if st.button("🔍 Analyze Blind Spots"):
        if user_input.strip():
            response = generator(
                f"Analyze blind spots in reasoning: {user_input}",
                max_length=150,
                num_return_sequences=1
            )[0]["generated_text"]

            if "history" not in st.session_state:
                st.session_state["history"] = []
            st.session_state["history"].append({"input": user_input, "output": response})

            st.subheader("✨ AI Suggestions")
            st.write(response)

# --- HISTORY VIEW ---
if "history" in st.session_state and st.session_state["history"]:
    st.subheader("📜 Past Analyses")
    for i, entry in enumerate(st.session_state["history"], 1):
        st.markdown(f"**{i}. Input:** {entry['input']}")
        st.markdown(f"**Output:** {entry['output']}")

# --- FOOTER ---
st.markdown("<p style='text-align:center; color:gray;'>Made with ❤️ for Hack2Skill</p>", unsafe_allow_html=True)
