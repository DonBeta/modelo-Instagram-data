import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False, unique=True)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(100), nullable=False)
    email = Column(String(50), nullable=False, unique=True)


class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user_to_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user_from = relationship("Users", foreign_keys=[user_from_id])
    user_to = relationship("Users", foreign_keys=[user_to_id])


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("Users")


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(300), nullable=False)
    author_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    post_id = Column(Integer, ForeignKey("post.id"), nullable=False)
    author = relationship("Users")
    post = relationship("Post")


class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    url = Column(String(250), nullable=True)
    post_id = Column(Integer, ForeignKey("post.id"), nullable=False)
    post = relationship("Post")

    def to_dict(self):
        return {}

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
render_er(Base, 'diagram.png')
