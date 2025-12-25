import streamlit as st
from datetime import datetime
from DataStructres import PriorityQueue, Stack

st.set_page_config(
    page_title="Task Manager",
    page_icon="📝",
    layout="wide"
)

st.markdown("""
<style>
    .priority-1 {
        background-color: #ff4444;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        color: white;
    }
    .priority-2 {
        background-color: #ff8800;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        color: white;
    }
    .priority-3 {
        background-color: #ffbb33;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        color: white;
    }
    .priority-4 {
        background-color: #00C851;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        color: white;
    }
    .priority-5 {
        background-color: #33b5e5;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        color: white;
    }
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #0e1117;
        color: #fafafa;
        text-align: center;
        padding: 10px;
        border-top: 2px solid #ff4b4b;
    }
</style>
""", unsafe_allow_html=True)

def initialize_session_state():
    if 'pending_queue' not in st.session_state:
        st.session_state.pending_queue = PriorityQueue()
    if 'completed_stack' not in st.session_state:
        st.session_state.completed_stack = Stack()
    if 'task_counter' not in st.session_state:
        st.session_state.task_counter = 0

initialize_session_state()

def get_priority_badge(priority):
    colors = {
        1: ("🔴 Critical", "#ff4444"),
        2: ("🟠 High", "#ff8800"),
        3: ("🟡 Medium", "#ffbb33"),
        4: ("🟢 Low", "#00C851"),
        5: ("🔵 Very Low", "#33b5e5")
    }
    label, color = colors.get(priority, ("Unknown", "#666666"))
    return f'<span style="background-color: {color}; color: white; padding: 5px 10px; border-radius: 5px; font-weight: bold;">{label}</span>'

st.title("📝 Task Manager")
st.markdown("**DSA Project**: Priority Queue & Stack Implementation")
st.markdown("---")

