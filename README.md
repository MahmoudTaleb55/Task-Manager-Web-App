# 🗂️ Task Manager Web App

A minimal, responsive **CRUD application** built with Django for managing daily tasks.  
Designed to demonstrate clean architecture, rapid delivery, and production‑ready coding practices in a compact, easy‑to‑review format.

---

## 🚀 Features
- Create, edit, delete, and toggle task status
- Server‑side form validation with user‑friendly error messages
- Responsive layout for desktop and mobile (Bootstrap)
- Clean project structure ready for deployment

---

## 🛠 Tech Stack
- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Django Templates, Bootstrap
- **Database:** SQLite (development) — easily switchable to MySQL/PostgreSQL
- **Other Tools:** Django Messages Framework for flash notifications

---

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/MahmoudTaleb55/your-repo-name.git
   cd your-repo-name

2. **Create & activate a virtual environment:**
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate

3. **Install dependencies:**
   pip install -r requirements.txt

4. **Run migrations:**
   python manage.py makemigrations
   python manage.py migrate

5. **Start the development server:**
   python manage.py runserver

6. **Access the app:**
   Open your browser and go to: http://127.0.0.1:8000
