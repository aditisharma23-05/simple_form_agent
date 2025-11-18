
# 📄 **Form Extraction Agent (Offline Pipeline)**

This project implements a **fully offline multi-form extraction pipeline** that processes PDF documents and extracts structured information using OCR and text-based parsing.
It is designed to work **without internet** and uses only local Python libraries available in the provided environment.

---

## 🚀 **Features**

* Extracts text from **multiple PDF forms**.
* Works entirely **offline** (no API calls).
* Supports both **machine-readable PDFs** and **scanned PDFs**.
* Modular pipeline with reusable components.
* Outputs structured results in a clean JSON dictionary.
* Includes **test helper, logs, and reproducible steps**.

---

## 🧩 **Architecture Overview**

```
input/
 ├── form1.pdf
 └── form2.pdf

src/
 ├── extractor/
 │    ├── ocr_reader.py        # OCR + machine text extractor
 │    ├── regex_parser.py      # Information extraction using patterns
 │    └── pipeline.py          # Orchestrates the entire extraction flow
 │
 ├── utils/
 │    ├── io_utils.py          # File loading helpers
 │    └── text_cleaner.py      # Text normalization utilities
 │
 ├── tests/
 │    └── test_extractor.py    # Quick sanity test for the pipeline
 │
 └── main.py                    # Run the extraction on all input forms

output/
 └── results.json               # Final structured extraction
```

---

## 📦 **Tech Stack (Offline Compatible)**

* **Python 3.10**
* **PyMuPDF (pymupdf)** — PDF text extraction
* **Pytesseract + Tesseract OCR** — fallback OCR
* **Regex parsing**
* **Pandas / JSON** for structured output

---

## 🔧 **How It Works**

### **1. Load PDF**

Using either:

* `PyMuPDF` for machine text
* `Tesseract OCR` for scanned images

### **2. Clean Text**

Normalize spaces, remove artifacts, unify formatting.

### **3. Parse Text**

Extracts fields using regex rules such as:

```
Name, Email, Phone, Address, DOB, etc.
```

### **4. Aggregate Results**

Each PDF generates a structured dictionary:

```json
{
  "file": "form1.pdf",
  "name": "John Doe",
  "email": "john@email.com",
  "phone": "9876543210"
}
```

All files combined → `output/results.json`.

---

## ▶️ **How to Run**

### **Step 1: Place your PDF forms**

Put at least **two PDFs** inside:

```
input/
```

Example:

```
input/form1.pdf
input/form2.pdf
```

### **Step 2: Run the pipeline**

```
python src/main.py
```

### **Step 3: View results**

Generated JSON file:

```
output/results.json
```

---

## 🧪 Testing

To run the basic extractor test:

```
python src/tests/test_extractor.py
```

This validates that:

* PDFs load correctly
* Text extraction works
* Regex parsing does not break

---

## 🧰 Sample Forms

You can use any public sample forms such as:

* Personal Information Form
* Employee Information Form
* Student Registration Form

Or create simple PDFs containing:

```
Name:
Email:
Phone:
Address:
DOB:
```

---

## 📝 **Notes**

* 100% offline pipeline — works without network.
* Avoid large scanned PDFs for faster processing.
* Add new regex rules in `regex_parser.py` as needed.

---

## 📌 **Future Improvements**

* Add ML-based entity extraction (NER).
* Add web-based UI using Streamlit.
* Support table extraction.

---

## 🤝 Contributing

Pull requests are welcome.
For major changes, please open an issue first.

