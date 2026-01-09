# Rental Management System - Backend Documentation

## Overview
This backend is built using **Django** and **Django Rest Framework (DRF)**. It serves as the data and logic layer for the Rental Management System mobile application (Flutter).

## Project Structure
- `config/`: Main project configuration and URL routing.
- `users/`: User management (Auth, Roles, Profiles).
- `properties/`: Real estate management (Properties, Apartments).
- `contracts/`: Lease agreements between Tenants and Properties.
- `finance/`: Payment processing and history.
- `maintenance/`: Maintenance request tracking.
- `notifications/`: User alert system.

## Setup Instructions
1. **Prerequisites**: Python 3.10+
2. **Installation**:
   ```bash
   cd backend
   python -m venv venv
   .\venv\Scripts\Activate
   pip install -r requirements.txt # (Ensure you freeze requirements)
   ```
3. **Database Migration**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
4. **Run Server**:
   ```bash
   python manage.py runserver
   ```

## API Endpoints (v1)
All endpoints are prefixed with `/api/v1/`.

### Users & Auth
- `GET /users/`: List users.
- `POST /users/`: Create user.
- `GET /roles/`: List roles.

### Properties
- `GET /properties/`: List properties.
- `GET /apartments/`: List apartments.

### Contracts
- `GET /contracts/`: List active contracts.
- `POST /contracts/`: Create new contract.

### Finance
- `GET /payments/`: List payments.

### Maintenance
- `GET /maintenance/requests/`: List maintenance requests.

## Testing
Run unit tests using:
```bash
python manage.py test
```
