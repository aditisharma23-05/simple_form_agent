# Intelligent Form Agent (CMS-1500)

This is an advanced, AI-powered pipeline for Intelligent Document Processing (IDP). The agent is built to ingest, understand, and hold conversations about complex healthcare forms (specifically the CMS-1500).

The core of this project is a **Dual-Memory Retrieval-Augmented Generation (RAG)** system. It intelligently separates structured data (like names and billing totals) into a **SQL Database** and unstructured text (like diagnosis notes) into a **Vector Database**. A `langchain` agent then queries one or both of these "memories" to answer complex, plain-English questions.

## 🚀 Features

* **AI-Powered Extraction:** Uses `gpt-4o` to read a scanned PDF (or text-based PDF) and convert its contents into a clean, standardized JSON object.
* **Dual-Memory RAG:** Combines the factual query power of **SQL** with the contextual search power of a **Vector Database** (ChromaDB).
* **Conversational Agent:** A `langchain`-based agent acts as the "brain," capable of understanding a user's question, deciding which tool (SQL or Vector) to use, and synthesizing a human-readable answer.
* **Holistic Insights:** Can answer questions that span *multiple* forms, such as "What is the average total charge for all claims?" or "How many patients are named John?"
* **Streamlit UI:** A clean, multi-page web application for:
    1.  Uploading and processing new PDF forms.
    2.  Chatting with the agent to query all processed forms.
* **Modular & Extendable:** All core logic is separated into a Python package (`src/form_agent`) for `extraction`, `storage`, and `agent` logic, making it clean and easy to maintain.
* **API-Ready:** Includes a `FastAPI` endpoint (`/api/v1/submit_claim`) that allows *digital-native* (JSON) forms to be submitted, bypassing the OCR step and feeding directly into the storage pipeline.

## 🔧 Installation

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/your-username/intelligent-form-agent.git](https://github.com/your-username/intelligent-form-agent.git)
    cd intelligent-form_agent
    ```

2.  **Create the Conda Environment:**
    This will install Python, Tesseract (for OCR), and all required Python packages from the `environment.yml` file.
    ```bash
    conda env create -f environment.yml
    ```

3.  **Activate the Environment:**
    ```bash
    conda activate form_agent_env
    ```

4.  **Set Your API Key:**
    This project requires an OpenAI API key for `gpt-4o`.
    *(Note: For Windows, use `set` instead of `export`)*
    ```bash
    export OPENAI_API_KEY='sk-Your-Key-Here'
    ```

## ▶️ Usage (Running the App)

The main way to use this project is through the Streamlit web app.

1.  **Run the App:**
    Make sure your `(form_agent_env)` is active and your API key is set.
    ```bash
    streamlit run app.py
    ```

2.  **Use the App:**
    Your browser will open to `http://localhost:8501`.
    * **Upload:** Go to the **"Upload New Claim"** page. Upload your sample PDF (e.g., `my_sample.pdf`). The app will show "success" when it's done processing.
    * **Chat:** Go to the **"Chat with Claims"** page. You can now ask questions about the form(s) you've uploaded.

## 📌 Demonstration & Example Runs

Here are the three example runs as required by the assignment.

### Example 1: Answering a question from a single form
(This example uses the "fake" PDF with John A. Doe's info)

> **User:** "What was the total charge for the patient John A. Doe?"
>
> **Agent (Thinking):** "This is a factual question about a 'total charge'. I will use my **SQL Tool**."
>
> **Agent (Answer):** "The total charge for John A. Doe's claim (form\_id: my\_sample.pdf\_...) was $250.00."

### Example 2: Generating a summary of one form
> **User:** "Give me a summary of form 'my\_sample.pdf\_...'"
>
> **Agent (Thinking):** "The user is asking for a summary. I will use my **SQL Tool** to get the facts (patient name, total) and my **Vector Tool** to get the context (diagnosis notes), then synthesize them."
>
> **Agent (Answer):** "This is a claim for patient John A. Doe (DOB: 04 12 1985) for a total of $250.00. The claim involves one service line for an office visit (Code: 99214) linked to a tibia fracture (Diagnosis: S82.101A)."

### Example 3: Providing a holistic answer across multiple forms
(This example assumes *two* forms have been uploaded)

> **User:** "What is the average total charge for all claims?"
>
> **Agent (Thinking):** "This is a holistic, aggregate question. I must use my **SQL Tool** and run an `AVG()` query."
>
> **Agent (Answer):** "The average total charge across all 2 indexed claims is $... (e.g., $375.50)."

## 🧱 Extending the Project

* **Add More Tools:** Create new tools for the agent in `agent.py` (e.g., a tool that sends emails, a calculator, or a web search tool).
* **Use Local LLMs:** Modify `extraction.py` and `agent.py` to use a local model via `Ollama` instead of the OpenAI API to make this project 100% free to run.
* **Add Data Validation:** Implement Pydantic models in `extraction.py` to validate the `gpt-4o` output before it's sent to the `storage` module.
* **Anonymize PII:** Use the `pii_compliance` block in our JSON schema to create a new agent tool that automatically redacts sensitive data.

## 📜 License

This project is licensed under the MIT License.