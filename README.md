# Blog Website

This is a simple blog website built with Django. Users can create an account, log in, and log out, as well as view all blog posts.

## Features

- **User Authentication**
  - Sign Up: Users can create a new account.
  - Log In: Users can log into their account.
  - Log Out: Users can log out from their session.
  
- **Blog Posts**
  - Display all blog posts on the homepage for easy access and browsing.

## Tech Stack

- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (default Django database for development)

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/asiq-dev/django-blog.git
    ```
   
2. **Navigate into the project directory:**
    ```bash
    cd django-blog
    ```

3. **Create a virtual environment:**
    ```bash
    python -m venv venv
    ```
   
4. **Activate the virtual environment:**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```

5. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

6. **Apply migrations to set up the database:**
    ```bash
    python manage.py migrate
    ```

7. **Create a superuser (for admin access):**
    ```bash
    python manage.py createsuperuser
    ```

8. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

9. **Open the website in your browser:**
   Visit `http://127.0.0.1:8000/` to see the blog website in action.

## Usage

- **Sign Up**: Register a new account by navigating to the Sign-Up page.
- **Log In**: Log in to the website with your credentials.
- **Log Out**: Safely log out from your account.
- **View Blog Posts**: Browse all available blog posts on the homepage.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License.
