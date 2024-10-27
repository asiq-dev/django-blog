Blog Website
This is a simple blog website built with Django. Users can create an account, log in, and log out, as well as view all blog posts.

Features
User Authentication
Sign Up: Users can create a new account.
Log In: Users can log into their account.
Log Out: Users can log out from their session.
Blog Posts
Display all blog posts on the homepage for easy access and browsing.
Tech Stack
Backend: Django
Frontend: HTML, CSS, JavaScript
Database: SQLite (default Django database for development)
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/your-repository-name.git
Navigate into the project directory:

bash
Copy code
cd your-repository-name
Create a virtual environment:

bash
Copy code
python -m venv venv
Activate the virtual environment:

On Windows:
bash
Copy code
venv\Scripts\activate
On macOS and Linux:
bash
Copy code
source venv/bin/activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Apply migrations to set up the database:

bash
Copy code
python manage.py migrate
Create a superuser (for admin access):

bash
Copy code
python manage.py createsuperuser
Run the development server:

bash
Copy code
python manage.py runserver
Open the website in your browser: Visit http://127.0.0.1:8000/ to see the blog website in action.

Usage
Sign Up: Register a new account by navigating to the Sign-Up page.
Log In: Log in to the website with your credentials.
Log Out: Safely log out from your account.
View Blog Posts: Browse all available blog posts on the homepage.
