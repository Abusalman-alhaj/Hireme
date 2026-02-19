# 🚀 HireMe API – Job Application Management Backend

🔗 **Live Demo (Swagger Docs):**  
https://hireme-75o8.onrender.com/docs

A production-ready backend system built with **FastAPI**, deployed on **Render**, and integrated with **TiDB Cloud**.  
Now fully containerized using **Docker & Docker Compose** 🐳

---

## 🏗 Architecture Overview

The system consists of:

- **Users** (Admin / Regular Users)
- **Jobs** (Created by Admin)
- **Applications** (Users apply to jobs)

### 🔐 Authentication Flow

1. User registers  
2. Password is hashed using **Argon2**  
3. User logs in  
4. JWT token is generated  
5. Token is required for protected routes  
6. Role-based access control enforced  

---

## 🛠 Tech Stack

- FastAPI
- SQLAlchemy ORM
- TiDB Cloud (MySQL-compatible distributed SQL)
- Argon2 password hashing
- JWT Authentication
- Docker & Docker Compose 🐳
- Render (Deployment)

---

## 📌 Features

- User Registration & Login
- JWT Authentication
- Role-Based Authorization (Admin/User)
- Job Creation (Admin Only)
- Job Listing (Public)
- Job Application System
- Secure Password Hashing
- Cloud Database with SSL
- Dockerized Development & Deployment

---

## ▶️ Run Locally (Without Docker)

```bash
git clone https://github.com/Abusalman-alhaj/Hireme.git
cd Hireme
pip install -r requirements.txt
uvicorn app.main:app --reload
```

App runs at:
```
http://127.0.0.1:8000/docs
```

---

## 🐳 Run With Docker (Recommended)

### 1️⃣ Build and Start Containers

```bash
docker compose up --build
```

App runs at:
```
http://localhost:8000/docs
```

### 2️⃣ Stop Containers

```bash
docker compose down
```

---

## 📦 Docker Details

### Dockerfile
- Uses Python slim image
- Optimized layer caching
- Runs FastAPI via Uvicorn

### docker-compose.yml
- Builds the application service
- Exposes port **8000**
- Ready for production extension (DB, Redis, etc.)

---

## 📁 Project Structure

```
Hireme/
│
├── app/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## 🌍 Deployment

The API is deployed on **Render** and connected to **TiDB Cloud**.

Live Swagger:
https://hireme-75o8.onrender.com/docs

---

## 💡 Future Improvements

- CI/CD Pipeline
- Unit & Integration Tests
- Email Notifications
- Admin Dashboard
- Pagination & Filtering
- Refresh Tokens

---

### ⭐ If you found this project useful, consider giving it a star!
