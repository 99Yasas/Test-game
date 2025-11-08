import streamlit as st
import random
import time

st.set_page_config(page_title="Car Dodge Game", page_icon="🚗")
st.title("Car Dodge Game 🚗")
st.write("Move your car left or right to avoid the obstacles (🚧). Use buttons to control your car.")

# Initialize game state
if "road" not in st.session_state:
    st.session_state.road = [" "] * 5  # 5 columns
if "car_pos" not in st.session_state:
    st.session_state.car_pos = 2       # start in middle
if "score" not in st.session_state:
    st.session_state.score = 0
if "game_over" not in st.session_state:
    st.session_state.game_over = False
if "obstacles" not in st.session_state:
    st.session_state.obstacles = []

# Functions
def move_left():
    if st.session_state.car_pos > 0:
        st.session_state.car_pos -= 1

def move_right():
    if st.session_state.car_pos < 4:
        st.session_state.car_pos += 1

def reset_game():
    st.session_state.car_pos = 2
    st.session_state.score = 0
    st.session_state.game_over = False
    st.session_state.obstacles = []

def update_road():
    # Add new obstacle randomly
    new_row = [" "] * 5
    if random.random() < 0.3:  # 30% chance
        new_row[random.randint(0,4)] = "🚧"
    st.session_state.obstacles.insert(0, new_row)
    if len(st.session_state.obstacles) > 10:
        st.session_state.obstacles.pop()

def check_collision():
    if len(st.session_state.obstacles) >= 10:
        if st.session_state.obstacles[-1][st.session_state.car_pos] == "🚧":
            st.session_state.game_over = True

# Control buttons
cols = st.columns([1,1,1])
with cols[0]:
    if st.button("⬅️ Left"):
        move_left()
with cols[1]:
    st.write(f"Score: {st.session_state.score}")
with cols[2]:
    if st.button("➡️ Right"):
        move_right()
        
if st.button("Reset Game"):
    reset_game()

# Game tick
if not st.session_state.game_over:
    update_road()
    st.session_state.score += 1
    check_collision()

# Display road
road_display = ""
for i, row in enumerate(reversed(st.session_state.obstacles)):
    row_display = ""
    for j, cell in enumerate(row):
        if i == 0 and j == st.session_state.car_pos:
            row_display += "🚗"
        else:
            row_display += cell
    road_display += row_display + "\n"
st.text(road_display)

# Game over message
if st.session_state.game_over:
    st.error(f"💥 Game Over! Your final score: {st.session_state.score}")

