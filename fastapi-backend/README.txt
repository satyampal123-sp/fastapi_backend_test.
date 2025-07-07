🧠 FastAPI Backend Practical Test
This is a simple backend application built using FastAPI for handling user login, prompt submission, and retrieving user-specific prompt history. It demonstrates basic understanding of FastAPI, authentication, routing, and in-memory data handling.

🚀 Features
✅ User Login with hardcoded credentials

✅ Prompt Submission and fake AI-style responses

✅ User-specific Prompt History

✅ Token-based Authentication using Bearer Token

⚠️ All data is stored in memory (no DB used)

🛠️ Tech Stack
Python 3.11+

FastAPI

Uvicorn (ASGI server)

Pydantic (data validation)

📦 Installation & Running Locally
1. Clone the repo
git clone https://github.com/your-username/fastapi-practical-test.git
cd fastapi-practical-test
2. Install dependencies
pip install -r requirements.txt
3. Run the app
uvicorn main:app --reload
4. Open your browser
Navigate to:
📄 http://127.0.0.1:8000/docs (Swagger UI)

🔐 Hardcoded Users
Username	Password
alice	password123
bob	secret

📮 API Endpoints
1. Login
http
POST /login/
Request Body:
json
{
  "username": "alice",
  "password": "password123"
}
Response:
json
{
  "token": "some-generated-token"
}
2. Submit Prompt
http
POST /prompt/
Headers:
makefile
Authorization: Bearer <token>
Request Body:
json
{
  "prompt": "Tell me a joke"
}
Response:
json
{
  "response": "Interesting..."
}
3. Get Prompt History
http
GET /history/
Headers:
Authorization: Bearer <token>
Response:
json
[
  {
    "timestamp": "2025-07-05T14:35:10",
    "prompt": "Tell me a joke",
    "response": "Interesting..."
  },
  ...
]
⚠️ Known Limitations
No persistent storage — history is lost when app restarts

Tokens are not JWT — just UUIDs stored in memory

No rate limiting or password hashing

🗂️ Suggested Project Structure
graphql
.
├── main.py           # FastAPI app entry point
├── auth.py           # Login and token logic
├── models.py         # Pydantic schemas
├── routes.py         # All route definitions
├── memory.py         # In-memory storage logic
└── requirements.txt  # Python dependencies
🧪 Sample cURL Commands
Login:
curl -X POST http://127.0.0.1:8000/login/ \
  -H "Content-Type: application/json" \
  -d '{"username": "alice", "password": "password123"}'
Submit Prompt:
curl -X POST http://127.0.0.1:8000/prompt/ \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Tell me a joke"}'

Get History:
curl -X GET http://127.0.0.1:8000/history/ \
  -H "Authorization: Bearer <token>"
✅ Author & Credits
Built as part of a Backend Developer Practical Test using FastAPI.

