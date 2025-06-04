
# Social Media API Backend (FastAPI)

This project provides a backend API for a social media application built with FastAPI. It includes the following main functionalities:

- **Post Management:** Create, update, delete, and retrieve posts.
- **User Management:** Register new users and search users by ID.
- **Authentication:** User login and token-based authentication.
- **Voting System:** Upvote and downvote posts (currently supports upvote only).

---

## Getting Started

Follow these steps to set up the project locally:

### 1. Clone the Repository

```bash
git clone https://github.com/Saraswathi-Kalirajan/fastapi-project
```

### 2. Navigate into the project directory

```bash
cd FASTAPI
```

### 3. Install Dependencies

```bash
pip install fastapi[all]
```

### 4. Run the API Server

```bash
uvicorn app.main:app --reload
```

> The `--reload` flag enables auto-reloading so that code changes are reflected immediately. The server runs by default at `http://127.0.0.1:8000`.

### 5. Access API Documentation

Open your browser and navigate to:

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

This provides an interactive Swagger UI for testing your endpoints.

---

## Database Configuration

This project uses PostgreSQL. Ensure PostgreSQL is installed and running on your machine.

### 6. Create a Database

Create a new PostgreSQL database (name as per your preference).

### 7. Set Environment Variables

Create a `.env` file in the root directory with your database credentials and secret keys:

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

> Replace the placeholder values with your actual database credentials and generate a secure `SECRET_KEY`. You can generate a key using [this tool](https://fastapi.tiangolo.com/tutorial/security/).

---

## Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)

---
