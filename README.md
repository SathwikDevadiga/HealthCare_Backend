# 🏥 Healthcare Backend API

This project is a backend system for a healthcare application built using Django, Django REST Framework (DRF), and PostgreSQL. It provides secure JWT-based user authentication, and RESTful APIs for managing doctors, patients, and their mappings.

---

## 🧰 Requirements

- Python 3.8+
- PostgreSQL
- pip
- virtualenv

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

git clone https://github.com/SathwikDevadiga/healthcare_backend.git
cd healthcare_backend

### 2. Create and Activate Virtual Environment
python -m venv venv
venv\Scripts\activate     # Windows
# source venv/bin/activate   # macOS/Linux

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Configure Environment Variables
Create a .env file and add your settings:

SECRET_KEY=your_secret_key
DEBUG=True
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password

### 5. Setup PostgreSQL Database
Ensure PostgreSQL is running and the database mentioned above exists.

### 6. Run Migrations
python manage.py makemigrations
python manage.py migrate

### 7. Run the Server
python manage.py runserver


Django Healthcare Backend - API Testing Steps (Using Postman or any API client)
================================================================================

💡 Base URL: http://127.0.0.1:8000/

1. AUTHENTICATION ENDPOINTS
-----------------------------

✅ Register a new user:
URL: POST /api/auth/register/
Body (JSON):
{
  "username": "john123",
  "email": "john@example.com",
  "password": "testpassword123"
}

✅ Login and get JWT token:
URL: POST /api/auth/login/
Body (JSON):
{
  "username": "john123",
  "password": "testpassword123"
}
Response: access and refresh token

📌 Use the access token in headers for authenticated requests:
Header: Authorization: Bearer <access_token>


2. PATIENT MANAGEMENT ENDPOINTS
--------------------------------

✅ Create a new patient:
URL: POST /api/patients/
Headers: Authorization: Bearer <access_token>
Body (JSON):
{
  "name": "Alice Smith",
  "age": 30,
  "gender": "Female",
  "medical_history": "Diabetes"
}

✅ List all patients for logged-in user:
URL: GET /api/patients/


✅ Get a specific patient:
URL: GET /api/patients/<id>/

✅ Update a patient:
URL: PUT /api/patients/<id>/
Body: 
{
  "name": "Alice Smith",
  "age": 40,
  "gender": "Female",
  "medical_history": "Diabetes"
}

✅ Delete a patient:
URL: DELETE /api/patients/<id>/



3. DOCTOR MANAGEMENT ENDPOINTS
-------------------------------

✅ Create a new doctor:
URL: POST /api/doctors/
Headers: Authorization
Body (JSON):
{
  "name": "Dr. Mehta",
  "specialization": "Cardiology",
  "experience": 10
}

✅ List all doctors:
URL: GET /api/doctors/


✅ Get a specific doctor:
URL: GET /api/doctors/<id>/


✅ Update a doctor:
URL: PUT /api/doctors/<id>/
Body:
{
  "name": "Dr. Mehta",
  "specialization": "Cardiology",
  "experience": 15
}

✅ Delete a doctor:
URL: DELETE /api/doctors/<id>/


4. PATIENT-DOCTOR MAPPING ENDPOINTS
------------------------------------

✅ Assign doctor to patient:
URL: POST /api/mappings/create/
Body (JSON):
{
  "patient": <patient_id>,
  "doctor": <doctor_id>
}

✅ Get all mappings:
URL: GET /api/mappings/

✅ Get doctors for a specific patient:
URL: GET /api/mappings/<patient_id>/

✅ Remove doctor from patient:
URL: DELETE /api/mappings/delete/<mapping_id>/


------------------
✅ All endpoints return JSON responses.
✅ Use 127.0.0.1:8000/admin/ to manage users and models through the admin panel.
✅ Be sure to use the JWT token in headers for protected endpoints.
