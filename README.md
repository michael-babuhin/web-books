# Web-Books: Educational Django Project



## Installation

Follow the instructions below to install and run the project on your local machine.

### Requirements

To install and run the project, you will need:

- Python 3.6+
- Installed pip (Python package installer)
- Git (for cloning the project repository)

### Install Dependencies

Before installing dependencies, create a virtual environment for the project. Then, activate the virtual environment and execute the following command to install dependencies from the requirements.txt file:
```
pip install -r requirements.txt
```

### Clone the Project

You can clone the project from GitHub by running the following command:
```
git clone https://github.com/michael-babuhin/web-books.git
```

### Run the Project

After installing dependencies and cloning the project, navigate to the project directory and execute the following commands:

```
python manage.py migrate
python manage.py runserver
```

The Web-Books site will be available at http://localhost:8000/ in your web browser.

## Project Description

Web-Books allows registered users to add new books and authors to the site, as well as modify existing information using forms. The project also includes user registration and authentication, password reset via simulated email sending, and administrative panel functionality.

The project is created for educational purposes and can be used as a base for developing more complex web applications using Django. Enjoy!
