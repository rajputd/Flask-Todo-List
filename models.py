import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class TodoList(db.Model):
    __tablename__ = "todo_lists"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    tasks = db.relationship('Task', backref="todo_list", lazy=True)

    def addTask(self, task_content):
        task = Task(content=task_content, list_id=self.id)
        db.session.add(task)
        db.session.commit()


class Task(db.Model):
    __tablename__ = "tasks"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(300), nullable=False)
    date = db.Column(db.DateTime)
    list_id = db.Column(db.Integer, db.ForeignKey("todo_lists.id"), nullable=False)


if __name__ == "__main__":
    """Create all database tables for each model"""
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)


    db.create_all(app=app)

