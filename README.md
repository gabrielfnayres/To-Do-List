# To-Do List in Django

I've created this project to help me in my own organization and make my daily tasks more clear and organized, and I hope you enjoy it and use it in your life.

This is a very simple To-Do List in Django framework. It was developed using Django, Bootstrap5 and SQLite for the simple database.

## Functionalities

- Create new tasks.
- Show all the tasks.
- Confirm already done tasks.
- Edit tasks.
- Delete tasks.

## Setup

1. Clone this repository:
2. Install the things in requirements.txt
   ```
   pip install -r requirements.txt
   ```
3. I suggest you to run it in a vitual environment before everything and create a .env file with your SECRET_KEY,
   DEBUG and ALLOWED_HOST
   ```
   python -m venv .venv
   ```
4. Connect to de database and migrate everything to it:
  ```
  python manage.py migrate
  ```

5. To run the application just type this in terminal:

```
python manage.py runserver
```
