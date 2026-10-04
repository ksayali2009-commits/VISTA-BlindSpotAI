import streamlit as st
from transformers import pipeline

# --- CONFIG ---
st.set_page_config(page_title="VISTA", layout="centered")

# --- APP TITLE ---
st.markdown("<h1 style='text-align:center; color:white;'>VISTA - Blind Spot AI</h1>", unsafe_allow_html=True)

# --- MODE SWITCHER ---
mode = st.sidebar.radio("Choose Mode:", ["Dark", "Light", "Eye Comfort"])

if mode == "Dark":
    st.markdown("<style>body {background-color: #000000; color: #FFFFFF;}</style>", unsafe_allow_html=True)
elif mode == "Light":
    st.markdown("<style>body {background-color: #FFFFFF; color: #000000;}</style>", unsafe_allow_html=True)
elif mode == "Eye Comfort":
    st.markdown("<style>body {background-color: #2E3B2E; color: #E0E0C0;}</style>", unsafe_allow_html=True)

# --- PROFILE CREATOR ---
st.sidebar.header("Create Profile")
name = st.sidebar.text_input("Name")
role = st.sidebar.text_input("Role (e.g., Student, Engineer)")
goal = st.sidebar.text_area("Decision Goal")

if name:
    st.sidebar.success(f"Profile saved for {name}")

# --- AI MODEL ---
generator = pipeline("text-generation", model="gpt2")

# --- HISTORY ---
if "history" not in st.session_state:
    st.session_state["history"] = []

user_input = st.text_area("Describe your decision reasoning:")

if st.button("Analyze Blind Spots"):
    if user_input.strip():
        response = generator(
            f"Analyze blind spots in reasoning: {user_input}",
            max_length=150,
            num_return_sequences=1
        )[0]["generated_text"]

        st.session_state["history"].append({"input": user_input, "output": response})
        st.subheader("AI Suggestions")
        st.write(response)

# --- HISTORY VIEW ---
if st.session_state["history"]:
    st.subheader("Past Analyses")
    for i, entry in enumerate(st.session_state["history"], 1):
        st.markdown(f"**{i}. Input:** {entry['input']}")
        st.markdown(f"**Output:** {entry['output']}")
