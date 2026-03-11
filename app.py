import openai # Gen AI library

# Function to analyze BGV records for Angi Technicians
def analyze_technician_risk(technician_name, report_text):
    # System Instruction for the AI
    system_prompt = "You are a US Background Verification Specialist for Angi. Analyze the provided report and flag if the technician is eligible or not based on criminal history."
    
    # User Request
    user_prompt = f"Technician: {technician_name}\nReport Summary: {report_text}\n\nTasks:\n1. Check for Criminal Records.\n2. Is this technician a 'New Entry' or 'Re-Verification'?\n3. Final Decision: Fit for Angi (Yes/No)?"

    print(f"--- Analyzing BGV for {technician_name} ---")
    
    # Logic: Sending data to Gen AI (OpenAI/Gemini)
    # response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[...])
    
    # For your project demo, we simulate the AI output:
    analysis_result = f"Decision for {technician_name}: FLAG FOR REVIEW. Reason: Found minor record in 2022. Need Manual Audit."
    return analysis_result

# Example usage for your GitHub project
tech_report = "Candidate applied as a new technician. Record shows a clean background check except for a speeding ticket in 2021."
print(analyze_technician_risk("John Doe", tech_report))