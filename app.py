import streamlit as st
st.markdown("<h1 style='text-align: center; color: #00FFAA;'>🌌 VISTA - Blind Spot AI 🌌</h1>", unsafe_allow_html=True)
st.markdown(
    """
    <style>
    body {
        background-color: #121212; /* Dark background */
        color: #ffffff; /* White text */
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


from transformers import pipeline

# --- CONFIG ---
st.set_page_config(page_title="VISTA", layout="centered")

# --- APP TITLE ---
st.markdown("<h1 style='text-align:center; color:white;'>VISTA - Blind Spot AI</h1>", unsafe_allow_html=True)

# --- MODE SWITCHER ---
ckground-color: #FFFFFF; color: #000000;}</style>", unsafe_allow_html=True)
elif mode == "Eye Comfort":
    st.markdown("<style>body {background-color: #2E3B2E; color: #E0E0C0;}</style>", unsafe_allow_html=True)

# --- PROFILE CREATOR ---mode = st.sidebar.radio("Choose Mode:", ["Dark", "Light", "Eye Comfort"])

if mode == "Dark":
    st.markdown("<style>body {background-color: #000000; color: #FFFFFF;}</style>", unsafe_allow_html=True)
elif mode == "Light":
    st.markdown("<style>body {ba

col1, col2 = st.columns([1,2])

with col1:
    mode = st.radio("🌙 Choose Mode:", ["Dark", "Light", "Eye Comfort"])
    st.header("Create Profile")
    name = st.text_input("👤 Name")
    role = st.text_input("💼 Role (e.g., Student, Engineer)")
    goal = st.text_input("🎯 Decision Goal")

with col2:
    user_input = st.text_area("📝 Describe your decision reasoning:")
    if st.button("🔍 Analyze Blind Spots"):
        if user_input.strip():
            response = generator(
                f"Analyze blind spots in reasoning: {user_input}",
                max_length=150,
                num_return_sequences=1
            )[0]["generated_text"]

            st.session_state["history"].append({"input": user_input, "output": response})
            st.subheader("AI Suggestions")
            st.write(response)

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
