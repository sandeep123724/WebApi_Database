# 🏥 Hospital Patient Management System API

## 📌 Project Overview

The Hospital Patient Management System API is a RESTful backend application developed using Python, Flask, and SQLite.

This project allows hospitals to manage patient records through API endpoints. It supports patient registration, patient listing, viewing patient details, and patient deletion.

The application also performs input validation using regular expressions to ensure data quality before storing records in the database.

---

# 🚀 Features

### Patient Registration

* Add new patients
* Validate patient information before saving

### Patient Listing

* Retrieve all registered patients

### Patient Details

* Fetch information for a specific patient using their ID

### Patient Deletion

* Remove patient records from the database

### Data Validation

* Name validation
* Email validation
* Phone number validation

---

# 🛠 Technologies Used

* Python 3
* Flask
* SQLite3
* Regular Expressions (Regex)
* REST API

---

# 📂 Project Structure

```text
hospital_patient_management/
│
├── app.py
├── hospital.db
├── requirements.txt
└── README.md
```

---

# 🗄 Database Schema

### Patients Table

| Column  | Type                |
| ------- | ------------------- |
| id      | INTEGER PRIMARY KEY |
| name    | TEXT                |
| dob     | TEXT                |
| gender  | TEXT                |
| email   | TEXT UNIQUE         |
| phone   | TEXT UNIQUE         |
| address | TEXT                |

---

# 📡 API Endpoints

## Home

### Request

```http
GET /
```

### Response

```text
patient management api running
```

---

## Register Patient

### Request

```http
POST /patient
```

### JSON Body

```json
{
  "name": "Sandeep",
  "dob": "2003-05-10",
  "gender": "Male",
  "email": "sandeep@gmail.com",
  "phone": "9876543210",
  "address": "Pune"
}
```

### Response

```text
patient register successfully
```

---

## Get All Patients

### Request

```http
GET /patients
```

### Response

```json
[
  {
    "id": 1,
    "name": "Sandeep",
    "dob": "2003-05-10",
    "gender": "Male",
    "email": "sandeep@gmail.com",
    "phone": "9876543210",
    "address": "Pune"
  }
]
```

---

## Get Single Patient

### Request

```http
GET /details/1
```

### Response

```json
{
  "id": 1,
  "name": "Sandeep",
  "dob": "2003-05-10",
  "gender": "Male",
  "email": "sandeep@gmail.com",
  "phone": "9876543210",
  "address": "Pune"
}
```

---

## Delete Patient

### Request

```http
DELETE /delete/1
```

### Response

```json
{
  "message": "patient delete successfully"
}
```

---

# 🔍 Validation Rules

### Name Validation

* Only alphabetic characters are allowed.

Example:

```text
Sandeep ✅
Sandeep123 ❌
```

### Email Validation

Example:

```text
abc@gmail.com ✅
abcgmail.com ❌
```

### Phone Validation

Rules:

* Must contain exactly 10 digits.
* Must start with 6, 7, 8, or 9.

Example:

```text
9876543210 ✅
1234567890 ❌
```

---

# ▶️ How to Run

## Clone Repository

```bash
git clone https://github.com/your-username/hospital-patient-management-api.git
```

## Install Flask

```bash
pip install flask
```

## Run Application

```bash
python app.py
```

Server starts at:

```text
http://127.0.0.1:5000
```

---

# 🧠 Concepts Demonstrated

* Object-Oriented Programming (OOP)
* Flask API Development
* SQLite Database Operations
* CRUD Operations
* Input Validation
* Regex Pattern Matching
* Dynamic URL Parameters
* Exception Handling
* Database Design

---

# 🔮 Future Improvements

* Update Patient API
* Doctor Management Module
* Appointment Booking System
* Billing Management
* JWT Authentication
* Password Security
* SQLAlchemy ORM
* Docker Deployment
* Unit Testing

---

# 👨‍💻 Author

Sandeep

Electronics & Telecommunication Engineer

Data Science | Generative AI | Agentic AI Learner

---

# ⭐ Project Goal

The goal of this project is to learn backend development by building a real-world hospital management API using Flask, SQLite, validation techniques, and RESTful architecture.
