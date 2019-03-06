from flask_wtf import Form
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length


class CommentForm(Form):
    title = StringField(
        'Title',
        validators=[DataRequired(), Length(max=255)]
    )
    text = TextAreaField(u'Comment', validators=[DataRequired()])


class PostForm(Form):
    title = StringField('Title', [DataRequired(), Length(max=255)])
    text = TextAreaField('Content', [DataRequired()])