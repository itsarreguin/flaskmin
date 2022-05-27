"""All models for Flaskmin project"""

from datetime import datetime

from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from werkzeug.security import (generate_password_hash,
    check_password_hash
    )

from flask_login import UserMixin

from db.engine import Base


class Admin(Base, UserMixin):
    __tablename__ = 'admins'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=True)
    username = Column(String(20), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)
    password_hash = Column(String(100))

    admin = relationship('Employee', backref='admin')
    
    def __init__(self, firstname, lastname, username, email, password) -> None:
        self.first_name = firstname
        self.last_name = lastname
        self.username = username
        self.email = email
        self.password_hash = password

    def __repr__(self) -> str:
        return self.username
    
    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute')
    
    @password.setter
    def password(self, password: str):
        self.password_hash = generate_password_hash(password)
    
    def confirm_password(self, password: str):
        return check_password_hash(self.password_hash, password)


class Employee(Base):
    __tablename__ = 'employees'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    username = Column(String(20), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)
    created_at = Column(DateTime(), default=datetime.utcnow())
    
    # One to many relationship
    admin_id = Column(Integer, ForeignKey('admins.id'))
    
    def __init__(self, firstname, lastname, username, email) -> None:
        self.first_name = firstname
        self.last_name = lastname
        self.username = username
        self.email = email

    def __repr__(self) -> str:
        return self.first_name