from flask_wtf import FlaskForm 
from wtforms import SubmitField,TextAreaField,StringField,SelectField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):
    title = StringField("Pitch Title", validators = [Required()])
    category = StringField("What category are you submitting to?",validators=[Required()])
    pitch_content = TextAreaField('What pitch do you want to share?',validators = [Required()] )
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment_content = TextAreaField('Add a comment',validators = [Required()] )
    submit = SubmitField('Submit')

class CategoryForm(FlaskForm):
    category_name = TextAreaField('Add a category', validators=[Required()])
    submit = SubmitField('Submit')