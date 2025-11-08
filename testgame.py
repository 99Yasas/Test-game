import streamlit as st

st.set_page_config(page_title="Tic-Tac-Toe", page_icon="🎮")
st.title("Tic-Tac-Toe Game")
st.write("Play against yourself! Click on the buttons to place X or O.")

# Initialize game board
if "board" not in st.session_state:
    st.session_state.board = [""] * 9
if "turn" not in st.session_state:
    st.session_state.turn = "X"
if "winner" not in st.session_state:
    st.session_state.winner = None

def check_winner(board):
    combos = [
        [0,1,2], [3,4,5], [6,7,8], # rows
        [0,3,6], [1,4,7], [2,5,8], # columns
        [0,4,8], [2,4,6]           # diagonals
    ]
    for combo in combos:
        a,b,c = combo
        if board[a] == board[b] == board[c] and board[a] != "":
            return board[a]
    if "" not in board:
        return "Draw"
    return None

# Display board
for i in range(3):
    cols = st.columns(3)
    for j, col in enumerate(cols):
        idx = i*3 + j
        if col.button(st.session_state.board[idx] or " ", key=idx):
            if st.session_state.board[idx] == "" and st.session_state.winner is None:
                st.session_state.board[idx] = st.session_state.turn
                st.session_state.turn = "O" if st.session_state.turn == "X" else "X"
                st.session_state.winner = check_winner(st.session_state.board)

# Show winner
if st.session_state.winner:
    if st.session_state.winner == "Draw":
        st.success("It's a Draw!")
    else:
        st.success(f"{st.session_state.winner} Wins!")

# Reset button
if st.button("Reset Game"):
    st.session_state.board = [""] * 9
    st.session_state.turn = "X"
    st.session_state.winner = None
