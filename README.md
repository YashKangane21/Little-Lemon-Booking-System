# Little Lemon — Back-End Developer Capstone

This project extends the earlier Little Lemon booking application with Django REST Framework APIs, menu management, token authentication, registration, and API tests. The original HTML booking interface and MySQL-backed reservation functionality are retained.

## Requirements
- Python 3.12
- MySQL Server
- Dependencies in `requirements.txt`

## Setup (Windows PowerShell)
1. Create the database:
   ```sql
   CREATE DATABASE littlelemon CHARACTER SET utf8mb4;
   ```
2. Install dependencies:
   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```
3. Set your own MySQL credentials:
   ```powershell
   $env:DB_NAME="littlelemon"
   $env:DB_USER="root"
   $env:DB_PASSWORD="YOUR_MYSQL_PASSWORD"
   $env:DB_HOST="127.0.0.1"
   $env:DB_PORT="3306"
   ```
4. Apply migrations and run:
   ```powershell
   python manage.py migrate
   python manage.py runserver
   ```
5. Open `http://127.0.0.1:8000/book/`.

## API endpoints
- `GET /api/menu/` — list menu items (public)
- `/api/menu/<id>/` — retrieve, create, update, or delete menu items (write operations require authentication)
- `/api/bookings/` — booking CRUD (authentication required)
- `POST /auth/users/` — register a user
- `POST /api-token-auth/` — obtain an authentication token

See `Readme.txt` for the peer-testing endpoint list and authentication steps.

## Run tests
```powershell
python manage.py test restaurant
```

## Insomnia
Register a user, obtain a token, then add `Authorization: Token YOUR_TOKEN` for protected requests. Use JSON request bodies for POST/PUT/PATCH.

## Important
- Configure your own MySQL credentials; no password is included.
- The existing booking webpage is retained. API booking requests are authenticated.
- Verify all endpoints and course-specific rubric expectations in your environment before submitting.
