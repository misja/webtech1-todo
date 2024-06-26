from models import TaskType
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired
from wtforms import StringField, BooleanField, SelectField, DateField, SubmitField


class TaskForm(FlaskForm):
    title = StringField("Title", validators=[InputRequired()])
    description = StringField("Description")
    deadline = DateField("Deadline")
    completed = BooleanField("Completed")
    type = SelectField(
        "Type",
        # wtf is dated and doesn't know enums, convert to a list of options
        choices=[(choice.name, choice.value) for choice in TaskType],
        validators=[InputRequired()],
    )
    submit = SubmitField("Send")
