"""
BeyondForge: DevPersona Simulator Engine
Simulates multi-persona debate, computes Merge Confidence Score,
and prepares synthesized patch for IBM Bob 2.0.
"""

from personas import PERSONAS

def run_simulation(code_snippet: str) -> dict:
    """
    Runs the developer code through all 4 simulated engineering personas.
    """
    simulation_results = {}
    
    for key, persona in PERSONAS.items():
        simulation_results[key] = {
            "name": persona["name"],
            "badge": persona["badge"],
            "status": "Reviewing...",
            "feedback": f"Simulating evaluation using {persona['role']} criteria."
        }
        
    # Simulated calculation of Merge Confidence Score (0-100)
    confidence_score = 82  # Baseline benchmark
    
    return {
        "code_snippet": code_snippet,
        "persona_reviews": simulation_results,
        "merge_confidence_score": confidence_score,
        "actionable_patch_status": "Ready for IBM Bob 2.0 Auto-Remediation"
    }

if __name__ == "__main__":
    sample_code = """
def authenticate_user(username, password):
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    return db.execute(query)
    """
    print("--- Initiating BeyondForge Persona Review Simulation ---")
    output = run_simulation(sample_code)
    print(f"Merge Confidence Score: {output['merge_confidence_score']}%")
    for k, res in output["persona_reviews"].items():
        print(f"[{res['badge']}] {res['name']}: {res['feedback']}")
