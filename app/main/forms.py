from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class PitchReviewForm(FlaskForm):
    title = StringField('Review title', validators=[Required()])
    review = TextAreaField('Pitch review', validators=[Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us more about yourself',validators = [Required()])
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):
    category = SelectField('Category', choices=[('', ''), ('comical', 'Comical pitches'), ('innovation', 'Innovation pitches'), ('technology', 'Technology pitches'), ('product', 'Product pitches'), ('marketing', 'Marketing pitches')], validators = [Required()])
    title = StringField('Pitch title', validators = [Required()])
    pitch = TextAreaField('Pitch', validators = [Required()])
    submit = SubmitField('Submit')