import datetime
from flask import current_app
from flask_script import Command
from app import db
from app.user_models import User, Role

# app-specific
# from app.member.models import LoanStatus

# to use: python manage init_db


class InitDbCommand(Command):
    """Initialize the database."""

    def run(self):
        init_db()


def init_db():
    """Initialize the database."""

    # db creation is done with alembic
    #   flask db migrate; flask db upgrade

    # db.drop_all()
    # db.create_all()
    create_users()


def create_users():
    """Create users."""
    # Create all tables
    # db.create_all()

    # Adding roles
    admin_role = find_or_create_role('admin', 'Admin')
    find_or_create_role('member', 'Member')
    processor_role = find_or_create_role('processor', 'Processor')

    # Add users
    find_or_create_user('admin', 'admin@example.com', 'Password1', admin_role)
    find_or_create_user('member', 'member@example.com', 'Password1')

    # Add app-specific users
    find_or_create_user('processor', 'processor@example.com', 'Password1',
                        processor_role)

    # app specific

    # Save to DB
    db.session.commit()

# app specific


# standard functions
def find_or_create_role(name, label):
    """Find existing role or create new role."""
    role = Role.query.filter(Role.name == name).first()
    if not role:
        role = Role(name=name, label=label)
        db.session.add(role)
        print(f"'{name}' role created.")
    else:
        print(f"'{name}' role found.")
    return role


def find_or_create_user(username, email, password, role=None):
    """Find existing user or create new user."""
    user = User.query.filter(User.email == email).first()
    if not user:
        user = User(username=username,
                    email=email,
                    password=current_app.user_manager.hash_password(password),
                    active=True,
                    email_confirmed_at=datetime.datetime.utcnow())
        if role:
            user.roles.append(role)
        print(f"'{username}' user created.")
        db.session.add(user)
    else:
        print(f"'{username}' user found.")
    return user
