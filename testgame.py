import streamlit as st
import time
import random

st.set_page_config(page_title="Reaction Game", page_icon="🎯")
st.title("Reaction Time Game 🎯")
st.write("Click the button as fast as you can when it appears!")

# Initialize game state
if "game_started" not in st.session_state:
    st.session_state.game_started = False
if "start_time" not in st.session_state:
    st.session_state.start_time = 0
if "reaction_time" not in st.session_state:
    st.session_state.reaction_time = 0

def start_game():
    st.session_state.game_started = True
    delay = random.uniform(2, 5)  # Random delay before button appears
    time.sleep(delay)
    st.session_state.start_time = time.time()

def click_button():
    st.session_state.reaction_time = round(time.time() - st.session_state.start_time, 3)
    st.success(f"Your reaction time: {st.session_state.reaction_time} seconds")
    st.session_state.game_started = False

# Start / reset game
if st.button("Start"):
    start_game()

# Show reaction button if game started
if st.session_state.game_started:
    if st.button("Click Me!"):
        click_button()

# Reset reaction time
if st.button("Reset"):
    st.session_state.reaction_time = 0
    st.session_state.game_started = False

    st.session_state.winner = None

