from .extractor import extract_text_from_pdf
from .field_extractor import extract_fields
from .qa_engine import answer_question
from .summarizer import summarize_fields
from .multi_form_agent import analyze_multiple_forms

def process_single_form(pdf_path, question=None):
    text = extract_text_from_pdf(pdf_path)
    fields = extract_fields(text)

    summary = summarize_fields(fields)
    answer = answer_question(question, text) if question else None

    return {
        "fields": fields,
        "summary": summary,
        "answer": answer
    }

def process_multiple_forms(pdf_list):
    all_forms = []

    for pdf in pdf_list:
        text = extract_text_from_pdf(pdf)
        fields = extract_fields(text)
        all_forms.append(fields)

    return analyze_multiple_forms(all_forms)
