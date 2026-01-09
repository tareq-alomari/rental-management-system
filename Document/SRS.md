# Software Requirements Specification (SRS)
## Rental & Apartment Management System

### 1. Introduction
**Purpose**: The system manages the lifecycle of property rentals, from property listing to contract termination.
**Scope**: Web-based Backend (API) and Mobile Frontend (Planned).

### 2. Functional Requirements
*   **User Management**: Admin, Owner, Tenant roles.
*   **Property Management**: Add/Edit Properties and Apartments.
*   **Leasing**: Create contracts with validation (No overlap).
*   **Financials**: Record payments, Generate Income Reports.
*   **Maintenance**: Submit and track maintenance requests.
*   **Notifications**: Alert users on status changes.

### 3. Non-Functional Requirements
*   **Security**: JWT Authentication, Role-Based Access Control (RBAC).
*   **Performance**: Optimized Database Indexing, Efficient API Queries.
*   **Scalability**: 3-Tier Architecture allowing independent scaling.

### 4. Constraints
*   Backend: Django (Python).
*   Database: SQLite/PostgreSQL.
