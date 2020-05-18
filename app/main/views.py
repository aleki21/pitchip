from flask import render_template,request,redirect,url_for,abort  #takes the name of a template file as the first argument and searches and loads the file
from .import main
from ..models import Review, User, Pitch
from .forms import PitchReviewForm,UpdateProfile,PitchForm
from .. import db,photos
from flask_login import login_required,current_user



# all views below
@main.route('/')
def index():
    '''
    This is the view root function that returns the index page and its data
    '''
    
    title = 'Pitch Perfect, the best pitching website.'
    return render_template('index.html', title = title)

@main.route('/categories')
def categories():
    '''
    View categories function that returns the categories and various pitches in the category
    '''
    categories = categories()

    return render_template('categories.html')

@main.route('/user/<uname>')
def profile(uname):
    '''
    View function to display the profile of a logged in user
    '''
    user = User.query.filter_by(username = uname).first()
    pitches = Pitch.query.filter_by(user_id = user.id).order_by(Pitch.posted.desc())
    if user is None:
        abort(404)

    return render_template('profile/profile.html', user = user,pitches = pitches)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)
@main.route('/comments')
def comments():
    '''
    This is the view function to display the comments and reviews.
    '''
    
    reviews = Review.get_reviews(id)

    return render_template('pitch.html',reviews = reviews)

@main.route('/pitch/review/new', methods = ['GET','POST'])
@login_required
def new_review(pitch_id):
    '''
    View function for the reviews and comments
    '''
    form = PitchReviewForm()

    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        new_review = review(title,review)
        new_review.save_review()

    return render_template('/review.html',pitch_review_form = form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/pitches/<category>')
def pitches(category):
    pitches = Pitch.query.filter_by(category = category).order_by(Pitch.posted.desc())

    return render_template("pitches.html", pitches = pitches, category = category)


@main.route('/user/<uname>/pitch',methods= ['GET','POST'])
@login_required
def new_pitch(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = PitchForm()
    pitch = Pitch()

    if form.validate_on_submit():
        pitch.category = form.category.data
        pitch.title = form.title.data
        pitch.pitch_statement = form.pitch.data
        pitch.likes = 0
        pitch.dislikes = 0
        pitch.user_id = current_user.id

        db.session.add(pitch)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('new_pitch.html',uname=uname, user = user, PitchForm = form)
