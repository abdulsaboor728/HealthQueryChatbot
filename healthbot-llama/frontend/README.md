# 🩺 HealthBot – Local Llama Health Assistant

A lightweight **AI chatbot for general health questions** built using **Llama 3.2**, **FastAPI**, and a simple **HTML frontend**.

The chatbot answers **only general health-related questions** and refuses to answer unrelated queries.

The system runs **completely locally** using **Ollama**, meaning no external API keys are required.

---

# 🚀 Features

- 🧠 Local LLM using **Llama 3.2 via Ollama**
- ⚡ Fast **FastAPI backend**
- 🌐 Simple **HTML + JavaScript frontend**
- 🛡 **Health-only guardrails**
- 🔒 Rejects non-health questions
- 💻 Runs completely **offline**
- 🧩 Modular architecture

---

# 🏗 System Architecture

```
User (Browser)
      ↓
Frontend (HTML + JavaScript)
      ↓
POST /chat
      ↓
FastAPI Backend
      ↓
Health Guardrails
      ↓
Llama 3.2 Model via Ollama
      ↓
Response returned to browser
```

---

# 📂 Project Structure

```
healthbot-llama
│
├── backend
│   ├── app.py
│   ├── guardrails.py
│   ├── llama_client.py
│   ├── prompts.py
│   └── requirements.txt
│
├── frontend
│   └── index.html
│
└── README.md
```

---

# ⚙️ Requirements

- Python **3.10+**
- **Ollama**
- Llama model (`llama3.2:3b`)
- FastAPI
- Uvicorn

---

# 🧠 Install Ollama

Install Ollama:

https://ollama.com

Start Ollama:

```bash
ollama serve
```

Download the model:

```bash
ollama pull llama3.2:3b
```

Verify installation:

```bash
curl http://localhost:11434/api/tags
```

---

# ⚙️ Backend Setup

Navigate to the backend folder:

```bash
cd backend
```

Create virtual environment:

```bash
python3 -m venv .venv
```

Activate environment:

Mac/Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install fastapi uvicorn requests pydantic
```

Run the backend:

```bash
uvicorn app:app --reload --port 8000
```

Backend API will run at:

```
http://localhost:8000
```

API documentation:

```
http://localhost:8000/docs
```

---

# 🌐 Frontend Setup

Navigate to frontend folder:

```bash
cd frontend
```

Start a simple web server:

```bash
python3 -m http.server 5500
```

Open the chatbot in your browser:

```
http://localhost:5500
```

---

# 🧪 Testing API

You can test the API using curl:

```bash
curl -X POST http://localhost:8000/chat \
-H "Content-Type: application/json" \
-d '{"message":"What helps with mild sore throat?"}'
```

Expected response:

```json
{
  "allowed": true,
  "reply": "Drinking warm fluids and gargling salt water may help soothe a mild sore throat."
}
```

---

# 🛡 Guardrails

The chatbot includes a **health-topic filter** that prevents answering unrelated questions.

Example:

### Allowed

```
What helps with a sore throat?
```

### Rejected

```
Write a business proposal
```

Response:

```
I can only answer general health-related questions.
```

---

# 🔮 Future Improvements

- Add **RAG (Retrieval Augmented Generation)** using medical documents
- Add **vector database** for trusted health knowledge
- Implement **conversation memory**
- Add **LLM-based topic classification**
- Add **streaming responses**
- Improve UI/UX

---

# 🧑‍💻 Technologies Used

- Python
- FastAPI
- Ollama
- Llama 3.2
- JavaScript
- HTML
- Uvicorn

---

# 📜 License

This project is intended for **educational and experimental purposes only**.

The chatbot provides **general health information** and should not be considered medical advice.

---

# 🙌 Acknowledgements

- Meta AI – Llama models
- Ollama – Local LLM runtime
- FastAPI – Python API framework