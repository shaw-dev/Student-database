# Student Database

A simple web application for managing student records built with Flask. This application allows you to add, view, and delete student records. It uses SQLite as the database and provides a clean interface to interact with the data.

## Features

- Add new student records.
- View a list of all students.
- Delete student records.
- Bootstrap-based styling for a responsive design.

## Technologies Used

- **Flask**: A lightweight WSGI web application framework for Python.
- **SQLite**: A lightweight database used for storing student records.
- **Bootstrap**: A front-end framework for developing responsive and mobile-first websites.
- **Jinja2**: A templating engine for rendering HTML pages.

## Installation

To set up the project on your local machine, follow these steps:

1. **Clone the Repository**

   ```sh
   git clone https://github.com/yourusername/Student-database.git
   cd Student-database

2. **to create a virtual env**:

   ```sh
   python -m venv venv
3. ** to activate**:

   ```sh
   source venv/bin/activate or venv\Scripts\activate
4. **dependencies**

   ```sh
   pip install -r requirements.txt
5. **setup**
   flask db upgrade  and then run at flask run.
6. **run**

   ```sh
   python app.py
   

**The application will be available at http://127.0.0.1:5000/.**
