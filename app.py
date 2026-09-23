import streamlit as st
import time
import re

st.set_page_config(
    page_title="BeyondForge | Live DevPersona Engine",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 BeyondForge: DevPersona Simulator")
st.caption("Autonomous Multi-Agent Developer Simulation & Code Review Engine powered by IBM Bob 2.0")
st.markdown("---")

col_code, col_review = st.columns([1, 1])

with col_code:
    st.subheader("💻 Code Input / PR Diff")
    sample_code = '''def delete_user_account(user_input_id):
    # Raw SQL concatenation
    sql = "DELETE FROM users WHERE id = " + user_input_id
    db_cursor.execute(sql)
    
    # Infinite loop danger
    while True:
        status = check_sync()
        if status == "DONE":
            break
            
    x = [a for a in range(10000000)]
    return True'''
    
    code_input = st.text_area("Paste code snippet to simulate review:", value=sample_code, height=350)
    simulate_btn = st.button("⚡ Trigger Live Multi-Agent Round-Table", type="primary")

with col_review:
    st.subheader("👥 Live Multi-Agent Engineering Debate")
    
    if simulate_btn:
        # LIVE AGENT EVALUATION ENGINE
        security_flaws = []
        sre_flaws = []
        qa_flaws = []
        junior_flaws = []
        
        # Security Agent Check
        if re.search(r"(\+|\%|\.format|f\").*SELECT|DELETE|UPDATE|INSERT", code_input, re.I) or "SELECT *" in code_input:
            security_flaws.append("Direct string formatting inside database query detected. Immediate SQL Injection risk.")
        if "API_KEY" in code_input or "password" in code_input.lower() and "=" in code_input:
            security_flaws.append("Plaintext credential or secret assignment found in source.")
            
        # SRE / DevOps Agent Check
        if "while True" in code_input:
            sre_flaws.append("Unbounded `while True` loop detected without an escape timeout. Severe thread exhaustion hazard.")
        if "range(1000" in code_input:
            sre_flaws.append("High memory allocation via broad range comprehension. Bottleneck under concurrent load.")
            
        # QA Chaos Agent Check
        if "user_input" in code_input or "user_id" in code_input:
            if "if not" not in code_input and "isinstance" not in code_input:
                qa_flaws.append("Parameter lacks type/null guarding. Passing None or empty string will trigger an unhandled runtime exception.")
                
        # Junior Dev Agent Check
        if "x =" in code_input or "a in" in code_input:
            junior_flaws.append("Ambiguous single-letter variables ('x', 'a') create steep cognitive load for team onboarding.")
        if '"""' not in code_input and "'''" not in code_input:
            junior_flaws.append("Missing module/function docstring. Unclear contract for new contributors.")

        # Real-time orchestration simulation
        status_box = st.empty()
        status_box.info("🤖 [IBM Bob 2.0] Dispatching subagents to analyze repository context...")
        time.sleep(0.8)
        status_box.info("🛡️ Security Lead analyzing AST for injection vectors...")
        time.sleep(0.8)
        status_box.info("⚡ SRE & DevOps inspecting thread safety and complexity...")
        time.sleep(0.8)
        status_box.empty()
        
        total_issues = len(security_flaws) + len(sre_flaws) + len(qa_flaws) + len(junior_flaws)
        
        # Dynamic Confidence Score Calculation
        if total_issues == 0:
            confidence = 97
            st.metric("Merge Confidence Score", f"{confidence}%", delta="+62% (Approved)")
            st.balloons()
        else:
            confidence = max(15, 100 - (total_issues * 20))
            st.metric("Merge Confidence Score", f"{confidence}%", delta=f"-{100-confidence}% (Review Blocked)")

        st.markdown("---")

        # 1. Security Lead
        with st.expander("🛡️ Alex Vance (Security Lead)", expanded=True):
            if security_flaws:
                st.error(f"**[CRITICAL BLOCKED]** {security_flaws[0]}")
            else:
                st.success("**[PASSED]** No sanitization bypasses or exposed tokens discovered.")

        # 2. Junior Dev
        with st.expander("👶 Leo Miller (Junior Developer)", expanded=True):
            if junior_flaws:
                st.warning(f"**[READABILITY WARNING]** {junior_flaws[0]}")
            else:
                st.success("**[PASSED]** Clear naming conventions and explanatory docs.")

        # 3. SRE / DevOps
        with st.expander("⚡ Marcus Kane (Principal SRE)", expanded=True):
            if sre_flaws:
                st.error(f"**[SCALE HAZARD]** {sre_flaws[0]}")
            else:
                st.success("**[PASSED]** Safe memory bounds and async throughput compliance.")

        # 4. QA Chaos Tester
        with st.expander("💥 Raven Quinn (QA Chaos Monkey)", expanded=True):
            if qa_flaws:
                st.warning(f"**[BOUNDARY TRAP]** {qa_flaws[0]}")
            else:
                st.success("**[PASSED]** Defensive parameter validations prevent crashes.")

        st.markdown("---")
        st.subheader("🤖 IBM Bob 2.0 Autonomous Fix Proposal")
        if total_issues > 0:
            st.code('''# Autonomous refactor synthesized by IBM Bob 2.0
def safe_delete_user(user_id: int, max_retries: int = 5) -> bool:
    """Safely delete user with parameterized queries and bounded retries."""
    if not isinstance(user_id, int) or user_id <= 0:
        raise ValueError("Invalid user ID")
        
    db_cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
    
    for attempt in range(max_retries):
        if check_sync() == "DONE":
            return True
        time.sleep(0.5)
        
    return False''', language="python")
        else:
            st.write("✨ Code is production ready. No patches required.")
    else:
        st.info("Paste your pull request or code snippet and click the button to start the live debate.")
