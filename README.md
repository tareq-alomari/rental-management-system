# Rental Management System (RMS)

A robust, enterprise-grade backend system for managing real estate properties, listing apartments, creating lease contracts, and tracking payments. Built with Django and Django Rest Framework.

## 🚀 Key Features
*   **Role-Based Access Control**: Admin, Property Owners, and Tenants.
*   **Property Management**: Manage buildings, units, and vacancy status.
*   **Leasing Engine**: Automated contract validation and status handling (Signals).
*   **Financial System**: Track rent payments and generate financial reports.
*   **Maintenance Ticketing**: Submit and resolve maintenance requests.
*   **Dynamic Settings**: Configurable system parameters via API/Admin.
*   **API First**: Fully documented REST API (Swagger/OpenAPI).

## 🛠️ Tech Stack
*   **Language**: Python 3.10+
*   **Framework**: Django 5.0, Django Rest Framework (DRF)
*   **Authentication**: JWT (SimpleJWT)
*   **Documentation**: drf-spectacular (Swagger UI)
*   **Database**: SQLite (Dev) / PostgreSQL (Ready)
*   **CI/CD**: GitHub Actions & Docker

## 📚 Documentation
Detailed documentation is available in the [`Document/`](./Document) directory:
*   [📄 User Manual](./Document/User_Manual.md)
*   [💻 Developer Manual](./Document/Developer_Manual.md)
*   [🔗 API Reference](./Document/API_Reference.md)
*   [📊 Architecture & Diagrams](./Document/ERD.md)
*   [📝 Use Cases](./Document/Use_Cases.md)

## ⚡ Quick Start

### Prerequisites
*   Python 3.10+
*   Git

### Installation
1.  **Clone the repo**
    ```bash
    git clone https://github.com/tareq-alomari/rental-management-system.git
    cd rental-management-system
    ```

2.  **Setup Virtual Environment**
    ```bash
    python -m venv venv
    # Windows
    .\venv\Scripts\activate
    # Linux/Mac
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r backend/requirements.txt
    ```

4.  **Run Migrations & Seed Data**
    ```bash
    cd backend
    python manage.py migrate
    python manage.py seed_data      # Create initial Users & Contracts
    python manage.py seed_settings  # Create initial System Configuration
    ```

5.  **Start Server**
    ```bash
    python manage.py runserver
    ```
    Access the API at `http://127.0.0.1:8000/api/docs/`

## 🧪 Testing
Run the comprehensive test suite to ensure everything is working:
```bash
python manage.py test users properties contracts finance core_settings
```
