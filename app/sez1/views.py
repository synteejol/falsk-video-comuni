from flask import Blueprint, render_template, request, redirect
from flask_login import login_required, fresh_login_required
from models.models import Sezioni, Video

sez1_bp = Blueprint('sez1_bp', __name__,
    template_folder='templates')

@sez1_bp.route("/sez/<int:id>")
@fresh_login_required
def view_home(id):
    
    return render_template("index.html", sezioni = Sezioni.query.all(), videos= Video.query.filter_by(sez=id).all(), \
        last = Video.query.filter_by(sez=id).order_by(Video.id.desc()).first())