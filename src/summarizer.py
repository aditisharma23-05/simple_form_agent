def summarize_fields(fields):
    summary_parts = []

    if "Name" in fields:
        summary_parts.append(f"The form belongs to {fields['Name']}.")
    
    if "Address" in fields:
        summary_parts.append("It includes residential address details.")
    
    if "Phone" in fields:
        summary_parts.append("Contact information like phone number is present.")
    
    if "DOB" in fields:
        summary_parts.append("Date of birth details are included.")
    
    if "Email" in fields:
        summary_parts.append("Email ID is mentioned.")

    if not summary_parts:
        return "The form contains basic details and structured fields."

    return " ".join(summary_parts)
