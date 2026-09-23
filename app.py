import streamlit as st
import json
from groq import Groq

st.set_page_config(
    page_title="BeyondForge | Autonomous Multi-Agent Simulator", 
    page_icon="🚀", 
    layout="wide"
)

# Sidebar sathi API Key input
with st.sidebar:
    st.header("⚙️ Engine Configuration")
    groq_api_key = st.text_input("Enter Groq API Key", type="password", placeholder="gsk_...")
    st.caption("Powered by Llama-3.3-70b-versatile via Groq & IBM Bob 2.0 architecture.")
    st.markdown("---")
    st.subheader("Active Personas")
    st.markdown("- 🛡️ **Alex Vance** (Security Lead)")
    st.markdown("- 👶 **Leo Miller** (Junior Dev)")
    st.markdown("- ⚡ **Marcus Kane** (Principal SRE)")
    st.markdown("- 💥 **Raven Quinn** (QA Chaos Monkey)")

st.title("🚀 BeyondForge: DevPersona Simulator")
st.caption("Cross-Language Multi-Agent Engineering Round-Table powered by IBM Bob 2.0")
st.markdown("---")

col_code, col_review = st.columns([1, 1])

with col_code:
    st.subheader("💻 Code Submission / PR Diff")
    sample_code = """// Paste ANY language (Python, JS, Go, Java, C++)
function processUserData(userId, rawInput) {
    let query = "SELECT * FROM users WHERE id = " + userId;
    db.execute(query);

    while(true) {
        let status = checkJob();
        if(status === 'DONE') break;
    }

    let x = [];
    return true;
}"""
    code_input = st.text_area("Paste code snippet to audit:", value=sample_code, height=380)
    run_btn = st.button("⚡ Run Live Multi-Agent Persona Audit", type="primary")

with col_review:
    st.subheader("👥 Live Multi-Agent Debate")

    if run_btn:
        if not groq_api_key:
            st.error("Sidebar madhe tuzhi Groq API Key (`gsk_...`) paste kar!")
        elif not code_input.strip():
            st.warning("Pahila davyabaajula code paste kar.")
        else:
            with st.spinner("🤖 IBM Bob 2.0 dispatching autonomous personas across AST & runtime vectors..."):
                try:
                    client = Groq(api_key=groq_api_key)
                    
                    system_prompt = """
You are BeyondForge, an autonomous multi-agent code evaluation engine orchestrated by IBM Bob 2.0.
Analyze the user's submitted code across any programming language.
You MUST output ONLY valid JSON matching this exact structure:
{
  "confidence_score": <int between 0 and 100>,
  "security_agent": {
    "status": "<PASSED or CRITICAL>",
    "feedback": "<Alex Vance concise security critique on injections, tokens, sanitization>"
  },
  "junior_agent": {
    "status": "<PASSED or WARNING>",
    "feedback": "<Leo Miller critique on readability, documentation, confusing variable names>"
  },
  "sre_agent": {
    "status": "<PASSED or SCALE_HAZARD>",
    "feedback": "<Marcus Kane critique on infinite loops, memory leaks, latency, concurrency>"
  },
  "qa_agent": {
    "status": "<PASSED or FAULT_RISK>",
    "feedback": "<Raven Quinn critique on null safety, type guarding, unhandled exceptions>"
  },
  "autonomous_fix": "<Synthesized fully production-ready corrected code patch>"
}
Do not write markdown quotes or explanations outside the JSON object.
"""

                    response = client.chat.completions.create(
                        model="llama3-8b-8192",
                        messages=[
                            {"role": "system", "content": system_prompt},
                            {"role": "user", "content": f"Code to review:\n\n{code_input}"}
                        ],
                        response_format={"type": "json_object"},
                        temperature=0.2
                    )

                    result = json.loads(response.choices[0].message.content)
                    
                    score = result.get("confidence_score", 50)
                    if score >= 80:
                        st.metric("Merge Confidence Score", f"{score}%", delta=f"+{score-50}% (Approved)")
                        st.balloons()
                        st.success("🎉 All personas reached consensus: Code approved for deployment.")
                    else:
                        st.metric("Merge Confidence Score", f"{score}%", delta=f"-{100-score}% (Review Blocked)")
                        st.error("⚠️ Review blocked by persona round-table. Critical remediations required.")

                    st.markdown("---")

                    # 1. Alex Vance
                    sec = result.get("security_agent", {})
                    with st.expander("🛡️ Alex Vance (Security Lead)", expanded=True):
                        if sec.get("status") == "PASSED":
                            st.success(f"**[PASSED]** {sec.get('feedback')}")
                        else:
                            st.error(f"**[VULNERABILITY]** {sec.get('feedback')}")

                    # 2. Leo Miller
                    jun = result.get("junior_agent", {})
                    with st.expander("👶 Leo Miller (Junior Developer)", expanded=True):
                        if jun.get("status") == "PASSED":
                            st.success(f"**[PASSED]** {jun.get('feedback')}")
                        else:
                            st.warning(f"**[READABILITY]** {jun.get('feedback')}")

                    # 3. Marcus Kane
                    sre = result.get("sre_agent", {})
                    with st.expander("⚡ Marcus Kane (Principal SRE)", expanded=True):
                        if sre.get("status") == "PASSED":
                            st.success(f"**[PASSED]** {sre.get('feedback')}")
                        else:
                            st.error(f"**[SCALE HAZARD]** {sre.get('feedback')}")

                    # 4. Raven Quinn
                    qa = result.get("qa_agent", {})
                    with st.expander("💥 Raven Quinn (QA Chaos Monkey)", expanded=True):
                        if qa.get("status") == "PASSED":
                            st.success(f"**[PASSED]** {qa.get('feedback')}")
                        else:
                            st.warning(f"**[FAULT RISK]** {qa.get('feedback')}")

                    st.markdown("---")
                    st.subheader("🤖 IBM Bob 2.0 Autonomous Fix Proposal")
                    st.code(result.get("autonomous_fix", "# No patch required"), language="text")

                except Exception as e:
                    st.error(f"Execution Error: {str(e)}")
    else:
        st.info("Sidebar madhe Groq Key taka, davyakade kontahi code paste kara ani review trigger kara.")
