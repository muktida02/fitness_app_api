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

---

## 📦 Setup Instructions

### 1️⃣ Clone Repository
```bash
git clone https://github.com/muktida02/fitness_app_api.git
cd omnify-django


