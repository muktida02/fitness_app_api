# 🧪 Fitness Studio Booking API (Django + DRF)

A simple **Booking API** for a fictional fitness studio offering classes like **Yoga, Zumba, and HIIT**.  
This project is built in **Python (Django + Django REST Framework)** using SQLite (in-memory/file DB).  

---

## 📌 Objective
The goal of this project is to demonstrate:
- Backend API design using Django REST Framework
- Clean and modular code structure
- Handling booking logic (available slots, overbooking prevention)
- Timezone-aware datetime handling (IST by default, convert dynamically)
- Error handling, validation, and good coding practices

---

## 🚀 Features
- View all upcoming classes (`GET /classes`)
- Book a class (`POST /book`)
- View all bookings by email (`GET /bookings`)
- **Enhancements (extra APIs):**
  - Add a new class dynamically (`POST /classes/add/`)
  - Update available slots (`PATCH /classes/<id>/update-slots/`)
  - Cancel a booking (frees slot) (`DELETE /bookings/<id>/cancel/`)
  - Delete a class (`DELETE /classes/<id>/delete/`)
  - View all bookings for a class (`GET /classes/<id>/bookings/`)

---

## 🛠️ Tech Stack
- **Python 3.10+**
- **Django 5.x**
- **Django REST Framework**
- **SQLite** (default Django DB)
- **pytz** (for timezone management)

---

## 📂 Project Structure
```python
omnify-django/
├── api/                   # Main app (models, views, serializers, urls)
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
├── omnify_django/         # Django project settings
│   ├── settings.py
│   ├── urls.py
├── db.sqlite3             # SQLite DB (auto-created)
├── manage.py
├── README.md
```

---

## 📦 Setup Instructions

### 1️⃣ Clone Repository
```python
git clone https://github.com/muktida02/fitness_app_api.git
cd omnify-django
```

### 2️⃣ Create Virtual Environment
# Create venv
```python
python -m venv venv  
```

# Activate (Linux/Mac)
```python
source venv/bin/activate
```

# Activate (Windows PowerShell)
```python
venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```python
pip install -r requirements.txt
```

### 4️⃣ Run Migrations
```python
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Load Sample Seed Data (optional)

python manage.py shell

```python
from api.models import FitnessClass
from datetime import datetime
import pytz

ist = pytz.timezone("Asia/Kolkata")

FitnessClass.objects.create(
  name="Yoga",
  datetime=ist.localize(datetime(2025, 8, 3, 10, 0)),
  instructor="Anita",
  available_slots=5
)
FitnessClass.objects.create(
  name="Zumba",
  datetime=ist.localize(datetime(2025, 8, 3, 17, 0)),
  instructor="Raj",
  available_slots=3
)
FitnessClass.objects.create(
  name="HIIT",
  datetime=ist.localize(datetime(2025, 8, 4, 7, 0)),
  instructor="Sneha",
  available_slots=2
)
exit()
```

### 6️⃣ Start Server
```python
python manage.py runserver
```

Server will be available at:
👉 http://127.0.0.1:8000/

## 📌 API Endpoints & Sample Requests

### 🔹 Get All Classes

```bash
curl -X GET http://127.0.0.1:8000/classes/
```

---

### 🔹 Book a Class

```bash
curl -X POST http://127.0.0.1:8000/book/ \
  -H "Content-Type: application/json" \
  -d '{"class_id":1,"client_name":"John Doe","client_email":"john@example.com"}'
```

---

### 🔹 Get Bookings by Email

```bash
curl -X GET "http://127.0.0.1:8000/bookings/?email=john@example.com"
```

---

### 🔹 Add a New Class

```bash
curl -X POST http://127.0.0.1:8000/classes/add/ \
  -H "Content-Type: application/json" \
  -d '{"name":"Pilates","datetime":"2025-08-05T09:00:00Z","instructor":"Meera","available_slots":10}'
```

---

### 🔹 Update Available Slots

```bash
curl -X PATCH http://127.0.0.1:8000/classes/1/update-slots/ \
  -H "Content-Type: application/json" \
  -d '{"available_slots":8}'
```

---

### 🔹 Cancel a Booking

```bash
curl -X DELETE http://127.0.0.1:8000/bookings/1/cancel/
```

---

### 🔹 Delete a Class

```bash
curl -X DELETE http://127.0.0.1:8000/classes/1/delete/
```

---

### 🔹 View All Bookings for a Class

```bash
curl -X GET http://127.0.0.1:8000/classes/1/bookings/
```
