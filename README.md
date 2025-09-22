# Meta-Backend-Capstone-Project
Meta Back-End Developer | Capstone Project

## Little Lemon Restaurant Management System

Django REST API for restaurant menu and booking management with user authentication.

### Tech Stack
- Django 5.2.6
- Django REST Framework
- MySQL Database
- Djoser Authentication

### API Endpoints

#### Authentication Flow

1. **User Registration**
   ```bash
   POST /auth/users/
   Content-Type: application/json

   {
     "username": "newuser",
     "password": "securepassword123",
     "email": "user@example.com"
   }
   ```

2. **Login & Get Token**
   ```bash
   POST /auth/token/login/
   Content-Type: application/json

   {
     "username": "newuser",
     "password": "securepassword123"
   }

   # Response: {"auth_token": "your_token_here"}
   ```

3. **Use Token in Requests**
   ```bash
   GET /restaurant/menu/
   Authorization: Token your_token_here
   ```

4. **Logout (Invalidate Token)**
   ```bash
   POST /auth/token/logout/
   Authorization: Token your_token_here
   ```

#### Restaurant API
- `GET/POST /restaurant/menu/` - Menu items (CRUD)
- `GET/POST /restaurant/booking/tables/` - Table bookings (CRUD)

### Development Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver 0.0.0.0:8000
```

### Admin Access
- URL: http://localhost:8000/admin/
- Username: admin
- Password: admin123
