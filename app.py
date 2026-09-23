import streamlit as st
import time

st.set_page_config(
    page_title="BeyondForge | DevPersona Simulator",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 BeyondForge: DevPersona Simulator")
st.caption("Autonomous Multi-Agent Developer Simulation & Code Review Engine powered by IBM Bob 2.0")

st.markdown("---")

col_code, col_review = st.columns([1, 1])

with col_code:
    st.subheader("💻 Code Submission")
    default_code = '''def get_user_records(user_id):
    # Fetch user records from database
    query = "SELECT * FROM users WHERE id = " + str(user_id)
    results = db.execute(query)
    
    for r in results:
        process_transaction(r)
        
    return results'''
    
    code_input = st.text_area("Paste code snippet / Pull Request diff here:", value=default_code, height=300)
    simulate_btn = st.button("⚡ Run Multi-Agent Persona Simulation", type="primary")

with col_review:
    st.subheader("👥 Simulated Engineering Round-Table")
    
    if simulate_btn:
        with st.spinner("Orchestrating IBM Bob 2.0 subagent debate..."):
            time.sleep(1.5)
            
        st.success("✅ Multi-Agent Simulation Complete!")
        
        # Merge Confidence Score
        st.metric(label="Merge Confidence Score", value="38%", delta="-62% (Blocked)")
        
        st.markdown("---")
        
        # Persona 1
        with st.expander("🛡️ Alex Vance (Security Lead) - [CRITICAL]", expanded=True):
            st.error("Flag: High Severity SQL Injection detected in line 3!")
            st.write("Concatenating `user_id` directly into the SQL string allows trivial query injection. Must use parameterized queries.")
            
        # Persona 2
        with st.expander("👶 Leo Miller (Junior Developer) - [CONFUSED]", expanded=True):
            st.warning("Flag: High Cognitive Load / Missing Documentation")
            st.write("What does `process_transaction(r)` do inside the loop? There are no type annotations or docstrings explaining the structure of `r`.")

        # Persona 3
        with st.expander("⚡ Marcus Kane (Principal SRE) - [WARNING]", expanded=True):
            st.warning("Flag: Potential N+1 / Blocking Latency Trap")
            st.write("Sequential processing inside the database iteration loop will block thread workers under high throughput.")

        # Persona 4
        with st.expander("💥 Raven Quinn (QA Chaos Monkey) - [EXCEPTION BREACH]", expanded=True):
            st.error("Flag: Unhandled Null / Type Mutation Hazard")
            st.write("If `user_id` is passed as `None` or an empty object, this directly executes an invalid SQL query causing unhandled runtime failure.")
            
        st.markdown("---")
        st.subheader("🤖 IBM Bob 2.0 Automated Remediation Patch")
        st.code('''# Refactored with parameterized query and error handling
def get_user_records(user_id: int) -> list:
    """Safely fetch and batch-process user transaction records."""
    if not user_id:
        raise ValueError("Invalid user_id provided")
        
    query = "SELECT * FROM users WHERE id = :user_id"
    results = db.execute(query, {"user_id": user_id})
    
    return [process_transaction(r) for r in results]''', language="python")
    else:
        st.info("Click 'Run Multi-Agent Persona Simulation' to initiate review.")
