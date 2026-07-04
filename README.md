# Student Management API - FastAPI

A complete, end-to-end RESTful API for managing students, teachers, courses, attendance, marks, and fees. Built with modern Python and FastAPI, demonstrating industry-standard Layered Architecture, OAuth2 Authentication, and SQLAlchemy ORM.

## 🚀 Features

- **Layered Architecture:** Clear separation of concerns (Routers -> Services -> Repositories -> Models).
- **FastAPI Framework:** High-performance, asynchronous web framework.
- **SQLAlchemy ORM:** Complete database modeling with One-To-Many, Many-To-Many, and One-To-One relationships.
- **Pydantic Validation:** Strict input/output validation via Pydantic Schemas.
- **Authentication & Authorization:** Secure OAuth2 with JWT (JSON Web Tokens) and Role-Based Access Control (RBAC).
- **Middleware:** Custom logging middleware to trace requests and execution time.
- **Background Tasks:** Non-blocking operations (e.g., simulating email sending and report generation).
- **Interactive Documentation:** Automatic Swagger UI (`/docs`) and ReDoc (`/redoc`).
- **Dockerized:** Ready to build and run using Docker.

## 📁 Project Structure

```text
Student-Management--FAST-API/
├── app/
│   ├── api/            # API Routers (Endpoints)
│   ├── core/           # Configuration & Security (JWT, Hashing)
│   ├── db/             # Database connection & Sessions
│   ├── middleware/     # Custom HTTP Middlewares
│   ├── models/         # SQLAlchemy DB Models
│   ├── repository/     # Database CRUD operations
│   ├── schemas/        # Pydantic validation schemas
│   ├── services/       # Business Logic
│   ├── tests/          # Pytest unit tests
│   ├── utils/          # Utilities (RBAC Roles)
│   └── main.py         # FastAPI application instance
├── Dockerfile          # Docker configuration
└── requirements.txt    # Python dependencies
```

## 🛠️ Tech Stack

- **Python 3.11+**
- **FastAPI** (Web Framework)
- **Uvicorn** (ASGI Server)
- **SQLAlchemy** (ORM)
- **Pydantic** (Data Validation)
- **Passlib & Python-Jose** (Security & JWT)
- **SQLite** (Default DB, easily swappable to PostgreSQL)

## 🏁 Getting Started (Local Development)

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd Student-Management--FAST-API
```

### 2. Create a Virtual Environment
```bash
python -m venv venv

# Activate on Windows:
.\venv\Scripts\activate

# Activate on macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
The SQLite database will automatically be created on the first run.
```bash
uvicorn app.main:app --reload
```

### 5. Access the API
Open your browser and navigate to the interactive documentation:
- **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)

## 🐳 Docker Setup

If you prefer using Docker, you can build and run the application in a container:

```bash
# Build the Docker image
docker build -t student-management-api .

# Run the container
docker run -p 8000:8000 student-management-api
```

## 🧪 Running Tests

The project includes a testing suite using `pytest` and FastAPI's `TestClient`.

```bash
pytest app/tests/
```

## 🛡️ Authentication Flow

1. Create a user via `/auth/register` (Passwords are hashed via Bcrypt).
2. Login via `/auth/login` to receive an `access_token`.
3. Use the token in the `Authorization` header (`Bearer <token>`) to access protected endpoints.
4. **RBAC:** Endpoints can be protected using dependencies like `Depends(require_admin)` or `Depends(require_teacher)`.