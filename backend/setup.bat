@echo off
echo ========================================
echo  Portfolio Backend Setup
echo ========================================

echo.
echo [1/5] Creating virtual environment...
python -m venv venv

echo.
echo [2/5] Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo [3/5] Installing dependencies...
pip install -r requirements.txt

echo.
echo [4/5] Running database migrations...
python manage.py makemigrations contact
python manage.py makemigrations analytics
python manage.py migrate

echo.
echo [5/5] Creating superuser for Django Admin...
python manage.py createsuperuser

echo.
echo ========================================
echo  Setup complete!
echo  Run: venv\Scripts\activate ^&^& python manage.py runserver
echo  Admin: http://127.0.0.1:8000/admin/
echo ========================================
pause
