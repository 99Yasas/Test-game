import streamlit as st
import random
import time

st.set_page_config(page_title="Car Dodge Game", page_icon="🚗")
st.title("Car Dodge Game 🚗")
st.write("Move your car (🚗) left or right to avoid obstacles (🚧)!")

# Initialize state
if "car_pos" not in st.session_state:
    st.session_state.car_pos = 2
if "obstacles" not in st.session_state:
    st.session_state.obstacles = []
if "score" not in st.session_state:
    st.session_state.score = 0
if "game_over" not in st.session_state:
    st.session_state.game_over = False
if "last_update" not in st.session_state:
    st.session_state.last_update = time.time()

ROAD_WIDTH = 5
TICK_INTERVAL = 0.5  # seconds between ticks

# Functions
def move_left():
    if st.session_state.car_pos > 0:
        st.session_state.car_pos -= 1

def move_right():
    if st.session_state.car_pos < ROAD_WIDTH-1:
        st.session_state.car_pos += 1

def reset_game():
    st.session_state.car_pos = 2
    st.session_state.obstacles = []
    st.session_state.score = 0
    st.session_state.game_over = False
    st.session_state.last_update = time.time()

def update_game():
    now = time.time()
    if now - st.session_state.last_update > TICK_INTERVAL and not st.session_state.game_over:
        # Move obstacles down
        st.session_state.obstacles.insert(0, ["🚧" if random.random() < 0.3 else " " for _ in range(ROAD_WIDTH)])
        if len(st.session_state.obstacles) > 10:
            st.session_state.obstacles.pop()

        # Check collision
        if len(st.session_state.obstacles) >= 10:
            if st.session_state.obstacles[-1][st.session_state.car_pos] == "🚧":
                st.session_state.game_over = True

        if not st.session_state.game_over:
            st.session_state.score += 1
        st.session_state.last_update = now

# Controls
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

# Update game state
update_game()

# Display road
road_display = ""
for i, row in enumerate(reversed(st.session_state.obstacles)):
    line = ""
    for j, cell in enumerate(row):
        if i == 0 and j == st.session_state.car_pos:
            line += "🚗"
        else:
            line += cell
    road_display += line + "\n"

st.text(road_display)

if st.session_state.game_over:
    st.error(f"💥 Game Over! Final Score: {st.session_state.score}")

pygame.quit()
sys.exit()

