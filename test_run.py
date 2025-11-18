import json
from src.app import process_single_form, process_multiple_forms

# --- CONFIGURATION ---
# Use the file names that are actually in your data folder
FORM_1_PATH = "data/form1.pdf"
FORM_2_PATH = "data/form2.pdf"
# ---------------------

print(f"--- 1. Testing Single Form ---")
print(f"File: {FORM_1_PATH}")
print("Query: 'What is the applicant's name?'\n")

try:
    # 1. Process a single form
    single_result = process_single_form(
        pdf_path=FORM_1_PATH,
        question="What is the applicant's name?"
    )
    
    # Pretty-print the JSON result
    print("--- Single Form Result ---")
    print(json.dumps(single_result, indent=2))

except Exception as e:
    print(f"ERROR processing single form: {e}")


print(f"\n\n--- 2. Testing Multi-Form Analysis ---")
print(f"Files: {FORM_1_PATH}, {FORM_2_PATH}\n")

try:
    # 2. Process multiple forms
    #
    # --- THIS IS THE FIX ---
    # The argument name is 'pdf_list', not 'pdf_paths'
    multi_result = process_multiple_forms(
        pdf_list=[FORM_1_PATH, FORM_2_PATH]
    )
    # --- END OF FIX ---
    
    # Pretty-print the JSON result
    print("--- Multi-Form Result ---")
    print(json.dumps(multi_result, indent=2))

except Exception as e:
    print(f"ERROR processing multiple forms: {e}")