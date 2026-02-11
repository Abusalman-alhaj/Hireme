# 🚀 HireMe API – Job Application Management Backend

🔗 **Live Demo:** https://hireme-75o8.onrender.com/docs

A production-ready backend system built with FastAPI and deployed on Render, integrated with TiDB Cloud.


## 🏗 Architecture Overview

The system consists of:

- **Users** (Admin / Regular Users)
- **Jobs** (Created by Admin)
- **Applications** (Users apply to jobs)

### 🔐 Authentication Flow
1. User registers
2. Password is hashed using Argon2
3. User logs in
4. JWT token is generated
5. Token is required for protected routes
6. Role-based access control enforced


## 🛠 Tech Stack

- FastAPI
- SQLAlchemy ORM
- TiDB Cloud (MySQL-compatible distributed SQL)
- Argon2 password hashing
- JWT Authentication
- Render (Deployment)


## 📌 Features

- User Registration & Login
- JWT Authentication
- Role-Based Authorization (Admin/User)
- Job Creation (Admin Only)
- Job Listing (Public)
- Job Application System
- Secure Password Hashing
- Cloud Database with SSL


## ▶️ Run Locally

```bash
git clone https://github.com/Abusalman-alhaj/Hireme.git
cd Hireme
pip install -r requirements.txt
uvicorn app.main:app --reload

