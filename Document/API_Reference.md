# API Reference Guide

## Base URL
`http://127.0.0.1:8000/api/v1/`

## Authentication
**Type**: Bearer Token (JWT)
**Headers**: `Authorization: Bearer <access_token>`

---

## Endpoints

### 1. Authentication
| Method | Endpoint | Description | Payload |
| :--- | :--- | :--- | :--- |
| `POST` | `/token/` | Obtain Access/Refresh Pair | `username`, `password` |
| `POST` | `/token/refresh/` | Refresh Access Token | `refresh` |

### 2. Users (`/users/`)
| Method | Endpoint | Description | Access |
| :--- | :--- | :--- | :--- |
| `GET` | `/users/` | List all users | Admin |
| `POST` | `/users/` | Create new user | Admin/Public |
| `GET` | `/users/{id}/` | Get user details | Auth |

### 3. Roles (`/roles/`)
- `GET /roles/`: List available roles (Admin, Owner, Tenant).

### 4. Properties (`/properties/`)
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/properties/` | List properties |
| `POST` | `/properties/` | Create property |
| `GET` | `/apartments/` | List all apartments |
| `POST` | `/apartments/` | Add apartment unit |

### 5. Contracts (`/contracts/`)
- `GET /contracts/`: List active/expired contracts.
- `POST /contracts/`: Create new contract (Triggers Validation).
    - **Required Fields**: `tenant_id`, `apartment_id`, `start_date`, `end_date`, `rent_amount`.

### 6. Finance (`/payments/`)
- `GET /payments/`: History of payments.
- `POST /payments/`: Record a payment.
- `GET /finance/reports/monthly_income/`: **Report** - Total income.
- `GET /finance/reports/vacant_apartments/`: **Report** - List vacant units.

### 7. Maintenance (`/maintenance/requests/`)
- `GET /requests/`: List requests.
- `POST /requests/`: Submit new issue.
- `PATCH /requests/{id}/`: Update status/cost.

### 8. Notifications (`/notifications/`)
- `GET /notifications/`: List user alerts.

### 9. System Settings (`/settings/`)
- `GET /settings/`: List configuration.
    - **Public**: Accessible by all.
    - **Private**: Accessible by Admin only.
- `PATCH /settings/{id}/`: Update configuration (Admin only).
