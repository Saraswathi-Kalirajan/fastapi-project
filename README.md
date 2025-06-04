
# Social Media API Backend (FastAPI)

**Technologies & Dependencies Used:**  
This project leverages modern Python frameworks and tools including FastAPI, Uvicorn, SQLAlchemy, Pydantic, JWT, Passlib,and PostgreSQL. It is containerized using Docker, ensuring easy deployment and scalability. Version control is managed via GitHub, demonstrating good development practices. These skills are highly valuable for backend development roles.

---

## 🚀 Features

- **🧑 User Management:** Register, login, and manage user profiles.
- **🔐 JWT Authentication:** Secure access with OAuth2 password flow.
- **📝 Posts:** Full CRUD (Create, Read, Update, Delete) support with user ownership.
- **👍 Votes:** Like/dislike functionality with one vote per user per post.
- **🗃️ Database:** PostgreSQL with SQLAlchemy ORM and Alembic for migrations.
- **🐳 Dockerized:** Easily run using Docker Compose.
- **✅ Testing:** Pytest-based tests for major endpoints.
- **☁️ Docker Hub:** Pull the pre-built API image directly from Docker Hub.

---

## 🧰 Tech Stack

| Component           | Technology/Package                                         |
|---------------------|------------------------------------------------------------|
| Framework           | FastAPI                                                    |
| Server              | Uvicorn                                                    |
| Database            | PostgreSQL                                                 |
| ORM                 | SQLAlchemy                                                 |
| Migrations          | Alembic                                                    |
| Authentication      | JWT + OAuth2 (PasswordBearer)                               |
| Password Hashing    | Passlib (bcrypt)                                           |
| Testing             | Pytest, TestClient                                         |
| Containerization    | Docker, Docker Compose                                     |
| Deployment          | Docker Hub                                                 |

---

## 🖥️ Local Setup

### 1. Clone this repository:

```bash
git clone https://github.com/Saraswathi-Kalirajan/fastapi-project
cd FASTAPI
```

### 2. Set Environment Variables:

Create a `.env` file in the root directory with the following content, replacing placeholders with your actual credentials:

```env
DATABASE_HOSTNAME=localhost
DATABASE_PORT=5432
DATABASE_NAME=your_database_name
DATABASE_USERNAME=your_username
DATABASE_PASSWORD=your_password
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

*Tip:* Generate a secure `SECRET_KEY` using [FastAPI security tutorial](https://fastapi.tiangolo.com/tutorial/security/).

### 3. Run the API Server:

```bash
uvicorn app.main:app --reload
```

### 4. Access the API Documentation:

Open your browser and go to:

[http://localhost:8000/docs](http://localhost:8000/docs)

### 5. Run Tests:

```bash
pytest -v 
```

---



## 📚 Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Alembic](https://alembic.sqlalchemy.org/)
- [JWT (PyJWT)](https://pyjwt.readthedocs.io/)
- [Passlib](https://passlib.readthedocs.io/)
- [Docker](https://www.docker.com/)
- [Pytest](https://docs.pytest.org/)

---
