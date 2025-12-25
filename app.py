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


with st.sidebar:
    st.header("➕ Add New Task")
    st.markdown("Fill in the details below to add a new task:")
    
    with st.form(key="task_form", clear_on_submit=True):
        task_name = st.text_input("Task Name", placeholder="Enter task description...")
        priority = st.selectbox(
            "Priority Level",
            options=[1, 2, 3, 4, 5],
            format_func=lambda x: {
                1: "🔴 1 - Critical",
                2: "🟠 2 - High",
                3: "🟡 3 - Medium",
                4: "🟢 4 - Low",
                5: "🔵 5 - Very Low"
            }[x]
        )
        
        submit_button = st.form_submit_button("Add Task", use_container_width=True)
        
        if submit_button:
            if task_name.strip():
                task = {
                    'id': st.session_state.task_counter,
                    'name': task_name.strip(),
                    'priority': priority,
                    'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                
                st.session_state.pending_queue.insert(task)
                st.session_state.task_counter += 1
                
                st.success(f"✅ Task added successfully!")
                st.rerun()
            else:
                st.error("❌ Please enter a task name!")
            
    st.markdown("---")
    st.subheader("📊 Statistics")
    st.metric("Pending Tasks", st.session_state.pending_queue.size())
    st.metric("Completed Tasks", st.session_state.completed_stack.size())

tab1, tab2 = st.tabs(["📋 Pending Tasks", "✅ Completed Tasks"])

with tab1:
    st.subheader("Pending Tasks Queue")
    st.markdown("Tasks are prioritized from highest (1) to lowest (5) priority.")
    
    if st.session_state.pending_queue.isEmpty():
        st.info("🎉 No pending tasks! Add a task from the sidebar to get started.")
    else:
        all_tasks = st.session_state.pending_queue.getAllTasks()
        sorted_tasks = sorted(all_tasks, key=lambda x: (x['priority'], x['timestamp']))
        
        for idx, task in enumerate(sorted_tasks):
            col1, col2 = st.columns([4, 1])
            
            with col1:
                st.markdown(f"""
                <div class="priority-{task['priority']}">
                    <h4 style="margin: 0;">{task['name']}</h4>
                    <p style="margin: 5px 0 0 0; font-size: 0.9em;">
                        {get_priority_badge(task['priority'])} | 
                        <span style="opacity: 0.8;">📅 {task['timestamp']}</span>
                    </p>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                if st.button("✓ Complete", key=f"complete_{task['id']}", use_container_width=True):
                    completed_task = st.session_state.pending_queue.extract_min()
                    if completed_task:
                        completed_task['completed_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        st.session_state.completed_stack.push(completed_task)
                        st.success(f"✅ Completed: {completed_task['name']}")
                        st.rerun()