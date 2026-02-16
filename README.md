# Logistics Management System

## 📌 Description

This project is a logistics management system that supports both land and maritime transportation.

The application allows:

- Client registration
- Product registration
- Warehouse and port management
- Land shipment management
- Maritime shipment management
- Discount calculation based on quantity
- Shipment filtering
- Token-based security validation

The system was developed as a technical assessment using modern backend and frontend technologies.

---

## 🏗 Architecture

### Backend
- FastAPI
- SQLAlchemy ORM
- SQLite database
- Token-based authentication (HTTP Bearer)
- Pytest for unit testing

### Frontend
- React
- Axios
- React Router (SPA navigation)

---

## ⚙️ Business Rules

### Land Logistics
- If quantity > 10 → 5% discount applied
- License plate format: 3 letters + 3 numbers (ABC123)
- Unique 10-character alphanumeric guide number

### Maritime Logistics
- If quantity > 10 → 3% discount applied
- Fleet number format: 3 letters + 4 numbers + 1 letter (ABC1234D)
- Unique 10-character alphanumeric guide number

The system stores:
- Original shipping price
- Applied discount
- Final shipping price

---

## 🔐 Security

All endpoints are protected using HTTP Bearer token validation.

Example header:

Authorization: Bearer secret123

---

## 🧪 Unit Testing

Unit tests were implemented using Pytest to validate:

- Security enforcement
- Land discount calculation
- Error handling
- Input validation

To run tests:

