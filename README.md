# Task Manager Website

A Django-based task manager with user authentication, task/subtask management, and category organization.

## Setup Instructions
1. Clone the repository: `git clone <repo-url>`
2. Create a virtual environment: `python -m venv venv`
3. Activate the environment: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Create a `.env` file with `SECRET_KEY`, `DEBUG`, and `DATABASE_URL`.
6. Run migrations: `python manage.py migrate`
7. Start the development server: `python manage.py runserver`

## Development
- Django version: 5.0
- Database: SQLite (development), PostgreSQL (production)
- CSS Framework: Tailwind CSS (planned)
