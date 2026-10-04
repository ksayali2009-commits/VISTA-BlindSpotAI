import streamlit as st
from transformers import pipeline

# --- PAGE CONFIG ---
st.set_page_config(page_title="VISTA - Blind Spot AI", layout="wide")

# --- CACHE MODEL LOADING (Efficiency) ---
@st.cache_resource
def load_model():
    return pipeline("text-generation", model="gpt2")

generator = load_model()

# --- GLOBAL STYLES (Accessibility: semantic tags + contrast) ---
st.markdown(
    """
    <style>
    body {
        background-color: #121212;
        color: #ffffff;
        font-family: 'Segoe UI', sans-serif;
    }
    h1, h2, h3 {
        font-weight: bold;
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

# --- HEADER ---
st.markdown("<h1 style='text-align: center; color: #00FFAA;'>🧠 VISTA - Blind Spot AI 🧠</h1>", unsafe_allow_html=True)

# --- MODE SWITCHER ---
def apply_mode(mode):
    if mode == "🌙 Dark":
        st.markdown("<style>body {background-color: #000000; color: #FFFFFF;}</style>", unsafe_allow_html=True)
    elif mode == "☀️ Light":
        st.markdown("<style>body {background-color: #FFFFFF; color: #000000;}</style>", unsafe_allow_html=True)
    elif mode == "👓 Eye Comfort":
        st.markdown("<style>body {background-color: #2E3B2E; color: #E0E0C0;}</style>", unsafe_allow_html=True)

mode = st.radio("🎨 Choose Mode:", ["🌙 Dark", "☀️ Light", "👓 Eye Comfort"])
apply_mode(mode)

# --- PROFILE CREATOR ---
def create_profile():
    st.header("👤 Create Profile")
    name = st.text_input("Name")
    role = st.text_input("💼 Role (e.g., Student, Engineer)")
    goal = st.text_input("🎯 Decision Goal")
    return name, role, goal

# --- DECISION ANALYZER ---
def analyze_reasoning(user_input):
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

# --- LAYOUT ---
col1, col2 = st.columns([1, 2])

with col1:
    name, role, goal = create_profile()

with col2:
    st.header("📝 Decision Reasoning")
    user_input = st.text_area("Describe your decision reasoning:")
    if st.button("🔍 Analyze Blind Spots"):
        analyze_reasoning(user_input)

# --- HISTORY ---
if "history" in st.session_state and st.session_state["history"]:
    st.subheader("📜 Past Analyses")
    for i, entry in enumerate(st.session_state["history"], 1):
        st.markdown(f"**{i}. Input:** {entry['input']}")
        st.markdown(f"**Output:** {entry['output']}")

# --- FOOTER ---
st.markdown("<p style='text-align:center; color:gray;'>Made with ❤️ for Hack2Skill</p>", unsafe_allow_html=True)

