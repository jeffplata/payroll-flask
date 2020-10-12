# Scaffolding App 

Hello. Welcome to the Scaffolding App.

Modify this README.md as necessary.

Enjoy!

**Steps:**

1. Fine-tune the User model (user_models.py)
1. Setup the database
    1. Adjust DATABASE_URL in (.env)
    1. flask db init
    1. flask db upgrade
    1. flask db migrate
1. Define initial user data
    1. Fine-tune >/commands/init_db.py
    1. python manage.py init_db