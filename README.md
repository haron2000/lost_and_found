Lost and Found ID App - README.txt

============================================
Overview
============================================
The Lost and Found ID App is a web-based platform that helps people recover lost identification cards. Users can report found IDs or search for their lost ones by ID number.

============================================
Features
============================================
- Report Lost or Found IDs: Submit ID details (number, location, description)
- Search for Lost IDs: Check if an ID has been reported
- User Authentication: Secure login with Django
- Database Storage: Stores all reports for easy access

============================================
Technologies Used
============================================
- Backend: Django (Python)
- Frontend: HTML, CSS, Bootstrap
- Database: SQLite

============================================
Installation Guide
============================================
1. Clone repository:
   git clone [repository-url]
   cd lost-and-found-id-app

2. Set up virtual environment:
   python -m venv venv
   venv\Scripts\activate (Windows) / source venv/bin/activate (Mac/Linux)

3. Install requirements:
   pip install -r requirements.txt

4. Run migrations:
   python manage.py migrate

5. Create admin user:
   python manage.py createsuperuser

6. Run server:
   python manage.py runserver

7. Access app at:
   http://127.0.0.1:8000

