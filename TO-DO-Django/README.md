# Django To-Do List Application

A complete Django web application for managing personal to-do tasks with user authentication and full CRUD functionality.

## Features

- **User Authentication**: Register, login, and logout functionality
- **Task Management**: Create, read, update, and delete tasks
- **User-specific Tasks**: Each user can only see and manage their own tasks
- **Task Details**: Title, description, due date, and completion status
- **Modern UI**: Bootstrap-based responsive design
- **Admin Interface**: Django admin panel for task management
- **Messages Framework**: Success and error notifications
- **Pagination**: Task list pagination for better performance
- **Task Statistics**: Dashboard showing task completion statistics

## Technologies Used

- **Backend**: Django 5.2.1
- **Database**: SQLite (default)
- **Frontend**: HTML5, CSS3, Bootstrap 5.3
- **Icons**: Bootstrap Icons
- **Authentication**: Django's built-in authentication system

## Project Structure

```
TO-DO-Django/
├── manage.py
├── requirements.txt
├── README.md
├── db.sqlite3 (created after migrations)
├── todoproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── todoapp/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── tests.py
│   └── migrations/
├── templates/
│   ├── base.html
│   ├── registration/
│   │   ├── login.html
│   │   └── register.html
│   └── todoapp/
│       ├── task_list.html
│       ├── task_form.html
│       └── task_confirm_delete.html
└── static/
    └── css/
        └── custom.css
```

## Installation & Setup

1. **Clone or download the project** to your local machine

2. **Navigate to the project directory**:
   ```bash
   cd TO-DO-Django
   ```

3. **Install Django** (if not already installed):
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations** to create the database:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser** (for admin access):
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the application**:
   - Main app: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## Usage

### For Regular Users

1. **Register**: Create a new account at `/register/`
2. **Login**: Sign in at `/login/`
3. **Dashboard**: View your tasks and statistics
4. **Create Tasks**: Add new tasks with title, description, and due date
5. **Manage Tasks**: Edit, complete, or delete existing tasks
6. **Logout**: Sign out securely

### For Administrators

1. **Access Admin Panel**: Go to `/admin/` and login with superuser credentials
2. **Manage Users**: View and manage user accounts
3. **Manage Tasks**: View and manage all tasks across users
4. **View Statistics**: See task statistics and user activity

## Models

### Task Model
- `user`: Foreign key to User (owner of the task)
- `title`: Task title (required, max 200 characters)
- `description`: Detailed description (optional)
- `complete`: Boolean indicating completion status
- `due_date`: Optional due date and time
- `created`: Timestamp when task was created
- `updated`: Timestamp when task was last updated

## Views

### Authentication Views
- `CustomLoginView`: Enhanced login with Bootstrap styling
- `CustomLogoutView`: Logout with success message
- `register_view`: User registration with custom form

### Task Views
- `TaskListView`: Display user's tasks with statistics
- `TaskCreateView`: Create new tasks
- `TaskUpdateView`: Edit existing tasks
- `TaskDeleteView`: Delete tasks with confirmation
- `toggle_task_complete`: Toggle task completion status

## URL Patterns

```python
# Authentication URLs
/login/          # Login page
/logout/         # Logout
/register/       # User registration

# Task URLs
/                # Task list (redirects to task list)
/task/create/    # Create new task
/task/<id>/update/  # Edit task
/task/<id>/delete/  # Delete task
/task/<id>/toggle/  # Toggle completion

# Admin
/admin/          # Django admin panel
```

## Security Features

- **CSRF Protection**: All forms include CSRF tokens
- **Login Required**: Task views require authentication
- **User Isolation**: Users can only access their own tasks
- **SQL Injection Protection**: Using Django ORM
- **XSS Protection**: Template auto-escaping enabled

## Customization

### Adding New Fields
1. Update the `Task` model in `models.py`
2. Create and run migrations
3. Update forms in `forms.py`
4. Update templates to display new fields

### Styling Changes
1. Modify `static/css/custom.css` for custom styles
2. Update templates for layout changes
3. Add new Bootstrap components as needed

### Adding Features
1. Create new views in `views.py`
2. Add URL patterns in `urls.py`
3. Create corresponding templates
4. Update navigation in `base.html`

## Troubleshooting

### Common Issues

1. **Static files not loading**:
   - Ensure `STATIC_URL` is set in settings
   - Run `python manage.py collectstatic` for production

2. **Template not found**:
   - Check `TEMPLATES` setting in `settings.py`
   - Verify template paths are correct

3. **Database errors**:
   - Run `python manage.py makemigrations`
   - Run `python manage.py migrate`

4. **Permission denied**:
   - Ensure you're logged in for task operations
   - Check if user owns the task being accessed

## Production Deployment

For production deployment, consider:

1. **Security Settings**:
   - Set `DEBUG = False`
   - Configure `ALLOWED_HOSTS`
   - Use environment variables for sensitive data

2. **Database**:
   - Use PostgreSQL or MySQL instead of SQLite
   - Configure database settings

3. **Static Files**:
   - Configure static file serving
   - Use CDN for better performance

4. **Security**:
   - Use HTTPS
   - Configure security headers
   - Set up monitoring and logging

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Write tests for new functionality
5. Submit a pull request


## Support

For questions or issues, please create an issue in the project repository .

---

**Created with Django 5.2.1 and Bootstrap 5.3**
