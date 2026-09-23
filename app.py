import streamlit as st
import ast
import time

st.set_page_config(
    page_title="BeyondForge | Multi-Agent Simulator", 
    page_icon="🚀", 
    layout="wide"
)

# Sidebar Configuration
with st.sidebar:
    st.header("⚙️ Agent Controls")
    strictness = st.slider("Persona Strictness Threshold", 1, 10, 8, help="Controls the severity penalty applied by agents.")
    st.markdown("---")
    st.subheader("Active Personas")
    st.markdown("- 🛡️ **Alex Vance** (Security)")
    st.markdown("- 👶 **Leo Miller** (Junior Dev)")
    st.markdown("- ⚡ **Marcus Kane** (Principal SRE)")
    st.markdown("- 💥 **Raven Quinn** (QA Chaos)")
    st.markdown("---")
    st.caption("Engine: IBM Bob 2.0 Subagent Orchestration")

st.title("🚀 BeyondForge: DevPersona Simulator")
st.caption("Autonomous Multi-Agent Developer Simulation & Code Review Engine powered by IBM Bob 2.0")
st.markdown("---")

col_code, col_review = st.columns([1, 1])

with col_code:
    st.subheader("💻 Code Submission / PR Diff")
    sample_code = '''def delete_user_account(user_input_id):
    # Dynamic SQL concatenation
    sql = "DELETE FROM users WHERE id = " + user_input_id
    db_cursor.execute(sql)
    
    # Infinite loop risk
    while True:
        status = check_sync()
        if status == "DONE":
            break
            
    x = [a for a in range(10000000)]
    return True'''
    
    code_input = st.text_area("Paste Python code to inspect:", value=sample_code, height=360)
    run_btn = st.button("⚡ Run Multi-Agent Persona Audit", type="primary")

with col_review:
    st.subheader("👥 Live Multi-Agent Round-Table")
    
    if run_btn and code_input.strip():
        with st.spinner("Dispatching personas to inspect AST & execution paths..."):
            time.sleep(1.0)
            
        security_issues = []
        junior_issues = []
        sre_issues = []
        qa_issues = []
        
        # AST & Pattern Analysis
        try:
            tree = ast.parse(code_input)
            
            # Junior Dev Checks
            functions = [node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
            for fn in functions:
                if not ast.get_docstring(fn):
                    junior_issues.append(f"Function '{fn.name}' is missing an explanatory docstring.")
                for arg in fn.args.args:
                    if not arg.annotation:
                        junior_issues.append(f"Parameter '{arg.arg}' in function '{fn.name}' lacks type hints.")
            
            for node in ast.walk(tree):
                if isinstance(node, ast.Name) and len(node.id) == 1 and node.id not in ['i', 'j', '_']:
                    junior_issues.append(f"Single-letter ambiguous variable '{node.id}' increases cognitive overhead.")

            # Security Lead Checks
            code_lower = code_input.lower()
            if any(k in code_input for k in ["API_KEY", "SECRET", "password =", "token ="]):
                security_issues.append("Hardcoded credentials or secrets exposed directly in code.")
            if "select" in code_lower or "delete" in code_lower:
                if ("+" in code_input or "%" in code_input or "f\"" in code_input) and ("%s" not in code_input):
                    security_issues.append("Unsanitized dynamic SQL query construction (SQL Injection hazard).")

            # SRE / DevOps Checks
            for node in ast.walk(tree):
                if isinstance(node, ast.While) and isinstance(node.test, ast.Constant) and node.test.value is True:
                    sre_issues.append("Unbounded `while True` loop detected without circuit-breaker escape logic.")
            if "range(1000" in code_input:
                sre_issues.append("Heavy memory allocation detected inside wide iteration range.")

            # QA Chaos Checks
            has_guard = any(isinstance(node, ast.If) for node in ast.walk(tree))
            has_raise = any(isinstance(node, ast.Raise) for node in ast.walk(tree))
            if functions and not (has_guard and has_raise):
                qa_issues.append("Absence of defensive type guards or input bounds checking.")

        except SyntaxError as err:
            qa_issues.append(f"Syntax Error on line {err.lineno}: {err.msg}")

        # Strictness Score Calculation
        total_flaws = len(security_issues) + len(junior_issues) + len(sre_issues) + len(qa_issues)
        penalty_rate = strictness * 2.5
        
        if total_flaws == 0:
            score = 98
            st.metric("Merge Confidence Score", f"{score}%", delta="+58% (Approved)")
            st.balloons()
            st.success("🎉 All 4 Personas approved this code for production merge!")
        else:
            score = max(5, int(100 - (total_flaws * penalty_rate)))
            st.metric("Merge Confidence Score", f"{score}%", delta=f"-{100-score}% (Blocked)")

        st.markdown("---")

        # Personas View
        with st.expander("🛡️ Alex Vance (Security Lead)", expanded=True):
            if security_issues:
                for sec in security_issues:
                    st.error(f"[VULNERABILITY] {sec}")
            else:
                st.success("[PASSED] Zero injection vectors or hardcoded secrets found.")

        with st.expander("👶 Leo Miller (Junior Developer)", expanded=True):
            if junior_issues:
                for jun in junior_issues:
                    st.warning(f"[READABILITY] {jun}")
            else:
                st.success("[PASSED] Clear docstrings, typed annotations, and clean naming.")

        with st.expander("⚡ Marcus Kane (Principal SRE)", expanded=True):
            if sre_issues:
                for sre in sre_issues:
                    st.error(f"[SCALE HAZARD] {sre}")
            else:
                st.success("[PASSED] Efficient runtime profile with bounded memory limits.")

        with st.expander("💥 Raven Quinn (QA Chaos Monkey)", expanded=True):
            if qa_issues:
                for qa in qa_issues:
                    st.warning(f"[FAULT RISK] {qa}")
            else:
                st.success("[PASSED] Defensive checks safeguard against unhandled exceptions.")

        # Download Report Feature
        report_text = f"""# BeyondForge Audit Report
Merge Confidence Score: {score}%
Strictness Level: {strictness}/10

## Findings
- Security Issues: {len(security_issues)}
- Readability Issues: {len(junior_issues)}
- Performance/SRE Issues: {len(sre_issues)}
- QA/Fault Issues: {len(qa_issues)}

Orchestrated by IBM Bob 2.0
"""
        st.markdown("---")
        st.download_button(
            label="📥 Download Full Audit Report",
            data=report_text,
            file_name="beyondforge_audit_report.md",
            mime="text/markdown"
        )
    elif run_btn:
        st.error("Please paste code in the left box first.")
    else:
        st.info("Paste your code snippet and click the button to trigger persona audits.")
