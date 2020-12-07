from models.models import Sezioni, Video
from flask import Blueprint, render_template, request, redirect
from flask_login import current_user, UserMixin,  LoginManager, login_user, logout_user, login_required, fresh_login_required, confirm_login
from app import db

video_bp = Blueprint('video_bp', __name__,
    template_folder='templates')

@video_bp.route('/video', methods=['GET', 'POST'])
@fresh_login_required
def video():

    if request.method == 'POST':
        try:
            db.session.add(Video(codice=request.form['codice'], sez=request.form['sez'], desc=request.form['desc']))
            db.session.commit()
            return redirect('/video')
        except:
            return "There was a problem adding new stuff."
    else:
        
        return render_template('video.html', videos = Video.query.all(), sezioni = Sezioni.query.all(), sez=Sezioni)

@video_bp.route('/delete/<int:id>')
@fresh_login_required
def delete(id):
    video = Video.query.get_or_404(id)

    try:
        db.session.delete(video)
        db.session.commit()
        return redirect('/video')
    except:
        return "There was a problem deleting data."