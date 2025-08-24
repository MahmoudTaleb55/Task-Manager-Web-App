# Task Manager Pro - Professional Web Application

A professional task management application built with Django that demonstrates modern web development practices, user authentication, and professional UI/UX design.

## 🚀 Features

### Authentication & Security
- **Custom User Model**: Extended Django's AbstractUser for flexibility
- **Secure Authentication**: Login, signup, and logout functionality
- **Password Validation**: Built-in Django password validators
- **Session Management**: Secure session handling with CSRF protection
- **User-specific Data**: Tasks are isolated per user

### Task Management
- **Create Tasks**: Add new tasks with titles
- **Task Status**: Mark tasks as pending or completed
- **User-specific Tasks**: Each user sees only their own tasks
- **Clean UI**: Modern Bootstrap 5 interface
- **Responsive Design**: Works on desktop and mobile devices

### Professional UI/UX
- **Modern Design**: Clean, professional interface with gradients and shadows
- **Bootstrap 5**: Responsive framework with custom styling
- **Icons**: Bootstrap Icons for visual appeal
- **Color-coded Elements**: Visual indicators for different actions
- **Accessibility**: Proper form labels and semantic HTML

## 🛠️ Technology Stack

- **Backend**: Django 5.0.4
- **Frontend**: Bootstrap 5, Custom CSS
- **Database**: SQLite (development), ready for PostgreSQL/MySQL
- **Authentication**: Django's built-in auth system with custom user model
- **Templates**: Django template language with template inheritance

## 📦 Installation & Setup

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Task-Manager-Web-App
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Open http://localhost:8000 in your browser
   - Sign up for a new account or use existing credentials

## 🎯 Usage

1. **Sign Up**: Create a new account using the signup page
2. **Login**: Access your personalized dashboard
3. **Create Tasks**: Use the "New Task" button to add tasks
4. **Manage Tasks**: Toggle task status between pending and completed
5. **Logout**: Securely end your session

## 🔧 Project Structure

```
Task-Manager-Web-App/
├── accounts/          # Authentication app
│   ├── models.py      # Custom User model
│   ├── views.py       # Auth views (login, signup, logout)
│   ├── forms.py       # Authentication forms
│   ├── urls.py        # Auth routes
│   └── templates/     # Auth templates
├── tasks/             # Task management app
│   ├── models.py      # Task model with user relationship
│   ├── views.py       # Task CRUD operations
│   ├── forms.py       # Task form
│   ├── urls.py        # Task routes
│   └── templates/     # Task templates
├── templates/         # Project-level templates
│   └── base.html      # Base template with navigation
├── web_django/        # Django project settings
│   ├── settings.py    # Project configuration
│   └── urls.py        # Main URL routing
└── README.md          # This file
```

## 🎨 Design Features

- **Gradient Backgrounds**: Modern aesthetic with smooth gradients
- **Card-based Layout**: Clean organization of content
- **Hover Effects**: Interactive elements with smooth transitions
- **Responsive Navigation**: Adapts to different screen sizes
- **Consistent Color Scheme**: Professional color palette

## 🔒 Security Features

- **CSRF Protection**: Built-in Django CSRF tokens
- **Password Hashing**: Secure password storage
- **Session Security**: Proper session management
- **User Isolation**: Data separation between users
- **Form Validation**: Server-side validation

## 🚀 Deployment Ready

This application is prepared for deployment with:
- Proper static file configuration
- Environment variable setup for production
- Database configuration flexibility
- Security settings for production use

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 🆘 Support

For support or questions, please open an issue in the GitHub repository.

---

**Built with ❤️ for professional web development**
