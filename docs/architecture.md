Here is your **clean, professional, text-only `architecture.md`**, formatted for direct copy–paste into your GitHub repo.

---

# architecture.md

**Intelligent Form Agent – System Architecture**

This document explains the full architecture, module responsibilities, data flow, and design decisions behind the Intelligent Form Agent.
The system is intentionally modular, offline, and easy to extend.

---

## 1. Overview

The Intelligent Form Agent is a modular pipeline that processes PDF forms and performs:

1. PDF text extraction (with OCR fallback)
2. Structured field extraction (regex-driven)
3. Question answering using offline vector search
4. Summary generation using template logic
5. Multi-form aggregation and insights

Every component is isolated for clarity and testability.

---

## 2. High-Level Pipeline

The processing flow can be summarized as:

**PDF File → Text Extraction → Field Extraction → QA → Summarization → Multi-Form Analysis**

The modules interact through clean, predictable function interfaces.

---

## 3. Components and Responsibilities

### 3.1 extractor.py

**Purpose:** Extract text from PDF forms.

Responsibilities:

* Load PDF using PyMuPDF
* Extract textual content directly
* Detect pages with no text
* Apply OCR using pytesseract for scanned pages
* Clean and normalize the extracted text
* Return complete text for downstream tasks

Design Decisions:

* PyMuPDF chosen for accuracy
* OCR fallback guarantees compatibility with scanned forms
* Kept stateless and pure for easy testing

---

### 3.2 field_extractor.py

**Purpose:** Extract structured fields from raw text.

Responsibilities:

* Define regex patterns for Name, Email, Phone, DOB, Address
* Identify possible label-keyword variations
* Return a dictionary of extracted values
* Handle missing or malformed fields gracefully

Design Decisions:

* Regex-based approach works offline and is explainable
* Patterns can be expanded for domain-specific needs
* No ML used to keep extraction deterministic

---

### 3.3 qa_engine.py

**Purpose:** Answer user questions using offline semantic similarity.

Responsibilities:

* Split text into sentences
* Compute TF-IDF vectors for each sentence and question
* Apply cosine similarity to rank relevance
* Return the most relevant matching sentence as answer

Design Decisions:

* Offline TF-IDF chosen for portability
* No LLM or embeddings required
* Approach is interpretable and lightweight
* Can be seamlessly upgraded to sentence-transformers

---

### 3.4 summarizer.py

**Purpose:** Generate a short summary for each form.

Responsibilities:

* Inspect extracted fields
* Fill in template-based summary statements
* Produce a readable, concise summary

Design Decisions:

* Avoid ML summarization to maintain offline usage
* Template-based method ensures stability
* Encourages consistency in output

---

### 3.5 multi_form_agent.py

**Purpose:** Analyse multiple forms together.

Responsibilities:

* Combine extracted fields from multiple forms
* Convert data into a pandas DataFrame
* Perform group-level insights (unique counts, ranges, lists, etc.)
* Return structured result objects

Design Decisions:

* pandas used for simplicity and power
* Analysis logic intentionally minimal but extendable

---

### 3.6 app.py

**Purpose:** Orchestrate the entire pipeline.

Responsibilities:

* Provide high-level functions `process_single_form()` and `process_multiple_forms()`
* Sequence the pipeline modules
* Provide a unified API for the entire system
* Used by notebooks, tests, and UI integrations

Design Decisions:

* Acts as an orchestrator, not a logic holder
* Keeps modules individually testable

---

## 4. Data Flow Summary

1. **Input**: User provides one or more PDF files.
2. **Extractor**:
   Extracts text → handles OCR fallback → cleans output.
3. **Field Extractor**:
   Parses normalized text → retrieves structured fields.
4. **QA Engine**:
   Receives question + text → returns most relevant sentence.
5. **Summarizer**:
   Generates a summary using extracted fields.
6. **Multi-Form Agent** (optional):
   Aggregates multiple forms → produces document-level insights.
7. **Output**: JSON-like structured results.

---

## 5. Design Principles

### Offline First

The entire system runs without internet access.
All components rely on packages already available in the environment.

### Modular & Testable

Each stage is isolated:

* No hidden dependencies
* Easy unit testing
* Easy to replace individual modules

### Transparent & Explainable

Regex for extraction, TF-IDF for QA, and templates for summarisation ensure:

* Predictable behaviour
* Reproducible output
* Easy debugging

### Easily Extendable

Users can:

* Add new regex patterns
* Swap TF-IDF with sentence-transformers
* Add new summary rules
* Introduce new aggregation logic

---

## 6. Limitations & Future Improvements

1. Regex extraction may fail on heavily unstructured forms.
2. TF-IDF QA may not answer multi-sentence questions accurately.
3. OCR accuracy depends on PDF quality.
4. Summaries are template-driven, not generative.

Potential enhancements:

* Use sentence-transformer embeddings (already installable offline).
* Add layout-aware extraction using PyMuPDF block coordinates.
* Build a Streamlit UI for end-users.
* Add form classification layers.

---

## 7. Conclusion

The Intelligent Form Agent is a clean, offline, and robust pipeline ideal for intelligent PDF form processing.
Its modular architecture ensures scalability, transparency, and ease of extension while maintaining simplicity.


