# Developer Manual

## Technical Architecture
- **Framework**: Django 5.x + Django Rest Framework.
- **Database**: SQLite (Dev) / PostgreSQL (Prod).
- **Auth**: JWT (SimpleJWT).

## Setup Environment
1. Clone Repository.
2. Create Virtual Env: `python -m venv venv`.
3. Install Deps: `pip install -r requirements.txt`.
4. Migrate: `python manage.py migrate`.
5. Run Server: `python manage.py runserver`.

## Project Structure
- `users/`: Custom User Model & Roles.
- `properties/`: Real Estate Logic.
- `contracts/`: Leasing Logic & Signals.
- `finance/`: Payments & Reports.
- `core_settings/`: Dynamic System Configuration (Feature Flags, Global Variables).

## Testing
Run the comprehensive test suite:
```bash
python manage.py test users properties contracts finance
```

## API Documentation
Swagger is available at `/api/docs/` when the server is running.
Redoc is available at `/api/redoc/`.
