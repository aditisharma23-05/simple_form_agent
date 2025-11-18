import re

FIELD_PATTERNS = {
    "Name": r"(Name|Applicant|Employee)\s*[:\-]\s*([A-Za-z ]+)",
    "Email": r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
    "Phone": r"\b[6-9]\d{9}\b",
    "DOB": r"(DOB|Date of Birth)\s*[:\-]?\s*([0-9]{2}[\/\-][0-9]{2}[\/\-][0-9]{2,4})",
    "Address": r"(Address)\s*[:\-]\s*([A-Za-z0-9,\. ]+)"
}

def extract_fields(text):
    extracted = {}

    for field, pattern in FIELD_PATTERNS.items():
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            # take the last group if available
            extracted[field] = match.group(len(match.groups()))
    
    return extracted
