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
        choices=[
            (1, "Easy"),
            (2, "Boring"),
            (3, "Hard!"),
        ],
        validators=[InputRequired()],
    )
    submit = SubmitField("Send")
