# 📰 AI-Powered News Digest Automation

An end-to-end Python automation pipeline that fetches the latest business news, summarizes it using a Large Language Model (LLM), and delivers a clean, readable digest directly to your inbox.

---

## 🚀 Overview

This project demonstrates how to integrate external APIs, LLM-based summarization, and email automation into a production-ready workflow.

**Key capabilities:**

* Fetches real-time news data from a public API
* Uses an LLM to generate concise summaries
* Sends formatted email digests automatically
* Environment-driven configuration for security and scalability

---

## 🧱 Architecture

```text
                ┌──────────────────────┐
                │   News API (REST)    │
                └─────────┬────────────┘
                          │
                          ▼
                ┌──────────────────────┐
                │   Data Fetch Layer   │
                │    (requests)        │
                └─────────┬────────────┘
                          │
                          ▼
                ┌──────────────────────┐
                │  LLM Summarization   │
                │ (LangChain + Gemini) │
                └─────────┬────────────┘
                          │
                          ▼
                ┌──────────────────────┐
                │ Email Service Layer  │
                │   (SMTP - Gmail)     │
                └─────────┬────────────┘
                          │
                          ▼
                ┌──────────────────────┐
                │     End User Inbox   │
                └──────────────────────┘
```

---

## ⚙️ Tech Stack

* **Python**
* **Requests** – API communication
* **LangChain** – LLM orchestration
* **Google Gemini API** – text generation
* **SMTP (Gmail)** – email delivery
* **dotenv** – environment management

---

## 🔌 APIs Used

### 1. News API

* **Endpoint:** `https://newsapi.org/v2/top-headlines`
* **Purpose:** Fetch latest business headlines
* **Parameters used:**

  * `country=us`
  * `category=business`
  * `language=en`
  * `apiKey`

**Response:**
Returns structured JSON containing articles with title, description, and metadata.

---

### 2. Google Gemini API (via LangChain)

* **Model:** `gemini-3-flash-preview`
* **Purpose:** Summarize raw news articles into readable insights
* **Integration:** Through LangChain’s chat model abstraction

**Flow:**

```text
Raw Articles → Prompt इंजेक्शन → LLM → Structured Summary
```

---

### 3. Gmail SMTP Server

* **Host:** `smtp.gmail.com`
* **Port:** `465 (SSL)`
* **Purpose:** Send automated email digests

---

## 🔄 Workflow

1. Load environment variables
2. Fetch news articles via API
3. Convert JSON data into prompt
4. Generate summary using LLM
5. Format email body
6. Send email via SMTP

---

## 📁 Project Structure

```text
.
├── main.py            # Core pipeline (fetch → summarize → send)
├── send_email.py      # Email service abstraction
├── requirements.txt   # Dependencies
├── .env.example       # Environment variable template
└── .gitignore
```

---

## 🔐 Environment Variables

Create a `.env` file:

```env
NEWS_API_KEY=your_news_api_key
GOOGLE_API_KEY=your_google_api_key
SENDER_GMAIL=your_email@gmail.com
MY_GMAIL_PASSWORD=your_app_password
RECEIVER_GMAIL=recipient_email@gmail.com
```

> ⚠️ Use Gmail App Passwords instead of your real password.

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python main.py
```

---

## 📬 Sample Output

* Subject: **AI News Digest**
* Content: Clean, summarized key points from latest business news

---

## 💡 Design Decisions

* **Separation of concerns:** Email logic isolated from core pipeline
* **LLM abstraction via LangChain:** Enables easy model swapping
* **Environment-based config:** Secure and production-friendly
* **Minimal dependencies:** Keeps the system lightweight and maintainable

---

## 📈 Potential Improvements

* Add scheduling (Cron / Celery / Airflow)
* HTML email formatting
* Topic-based personalization
* Database storage for historical digests
* Retry & error handling for API failures

---

## 🧠 What This Project Demonstrates

* API integration patterns
* LLM-powered automation
* Clean backend architecture
* Real-world automation use case
* Production-conscious design

---

## 📜 License

MIT License

---

## 👤 Author

Your Name
[LinkedIn] | [GitHub]

---
