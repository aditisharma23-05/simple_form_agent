import pandas as pd

def analyze_multiple_forms(forms):
    # forms = list of dicts containing extracted fields
    df = pd.DataFrame(forms)

    insights = {}

    if "Phone" in df.columns:
        insights["unique_phone_count"] = df["Phone"].nunique()

    if "Name" in df.columns:
        insights["names_list"] = df["Name"].dropna().tolist()

    if "DOB" in df.columns:
        insights["dob_range"] = [df["DOB"].min(), df["DOB"].max()]

    return insights
