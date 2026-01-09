# Comprehensive Use Cases

## 1. Actors Description
| Actor | Description |
| :--- | :--- |
| **Admin** | Superuser with full access to managing users, roles, and viewing all system data. |
| **Owner** | Property owner who manages their properties, apartments, and contracts. |
| **Tenant** | User renting an apartment, responsible for payments and maintenance requests. |
| **System** | Automated processes (validations, signals, notifications). |

---

## 2. Authentication & User Management
### UC-01: User Login
*   **Actors**: All
*   **Flow**:
    1. Actor submits credentials (username/password).
    2. System validates credentials.
    3. System returns JWT Access & Refresh Tokens.
*   **Exception**: Invalid credentials -> Show error.

### UC-02: User Registration (Admin Only)
*   **Actors**: Admin
*   **Flow**:
    1. Admin enters user details and assigns Role (Owner/Tenant).
    2. System creates user account.
    3. System confirms creation.

---

## 3. Property Management
### UC-03: Add Property
*   **Actors**: Owner
*   **Flow**:
    1. Owner enters Property Name, Location, Description.
    2. System saves Property linked to Owner.

### UC-04: Add Apartment
*   **Actors**: Owner
*   **Precondition**: Property exists.
*   **Flow**:
    1. Owner selects Property.
    2. Owner enters Apartment Number, Floor, Monthly Rent.
    3. System sets status to 'VACANT'.
    4. System saves Apartment.

---

## 4. Leasing & Contracts
### UC-05: Create Lease Contract
*   **Actors**: Owner
*   **Precondition**: Apartment Status is VACANT.
*   **Flow**:
    1. Owner selects Tenant and Apartment.
    2. Owner defines Start Date and End Date.
    3. Owner sets Rent Amount.
    4. **System Validation**: Checks for overlapping active contracts.
    5. System saves Contract.
    6. System (Signal) updates Apartment Status to 'RENTED'.

### UC-06: Terminate Contract
*   **Actors**: Owner
*   **Flow**:
    1. Owner selects active Contract.
    2. Owner selects "Terminate".
    3. System changes Contract Status to 'TERMINATED'.
    4. System (Signal) updates Apartment Status to 'VACANT'.

---

## 5. Financial Operations
### UC-07: Record Payment
*   **Actors**: Tenant (via Online) or Owner (Manual Record)
*   **Flow**:
    1. Actor selects Contract.
    2. Actor enters Amount and Method (Cash/Online).
    3. System saves Payment transaction.
    4. System updates Payment Status (Pending -> Completed).

### UC-08: View Financial Reports
*   **Actors**: Admin, Owner
*   **Flow**:
    1. Actor requests "Monthly Income".
    2. System aggregates all 'COMPLETED' payments.
    3. System displays total income and breakdown by payment method.

---

## 6. Maintenance
### UC-09: Submit Maintenance Request
*   **Actors**: Tenant
*   **Flow**:
    1. Tenant selects their Apartment.
    2. Tenant describes issue (e.g., "Leaky faucet").
    3. System saves Request with status 'PENDING'.

### UC-10: Update Maintenance Status
*   **Actors**: Owner
*   **Flow**:
    1. Owner views Pending requests.
    2. Owner updates status (e.g., 'IN_PROGRESS', 'COMPLETED') and adds Cost.
    3. System notifies Tenant of update.

---

## 7. System Configuration
### UC-11: Update System Settings
*   **Actors**: Admin
*   **Flow**:
    1. Admin navigates to Settings.
    2. Admin modifies a value (e.g., Toggle Maintenance Mode).
    3. System updates the setting immediately.
