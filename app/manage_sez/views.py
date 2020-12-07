from models.models import Sezioni
from flask import Blueprint, render_template, request, redirect
from flask_login import current_user, UserMixin,  LoginManager, login_user, logout_user, login_required, fresh_login_required, confirm_login
from app import db

sezioni_bp = Blueprint('sezioni_bp', __name__,
    template_folder='templates')

@sezioni_bp.route('/sezioni', methods=['GET', 'POST'])
@fresh_login_required
def sezioni():

    if request.method == 'POST':
        try:
            db.session.add(Sezioni(nome=request.form['nome']))
            db.session.commit()
            return redirect('/sezioni')
        except:
            return "There was a problem adding new stuff."
    else:
        
        return render_template('sezioni.html', sezioni = Sezioni.query.all())

@sezioni_bp.route('/delete/<int:id>')
@fresh_login_required
def delete(id):
    sezioni = Sezioni.query.get_or_404(id)

    try:
        db.session.delete(sezioni)
        db.session.commit()
        return redirect('/sezioni')
    except:
        return "There was a problem deleting data."

# @rinnovi_bp.route('/update/<int:id>', methods=['GET', 'POST'])
# @fresh_login_required
# def update(id):
#     rinnovi = Rinnovi.query.get_or_404(id)
#     tecnici = Tecnici.query.all()
#     punti = Punto.query.all()
#     piani = Piani.query.all()

#     if request.method == 'POST':
#         rinnovi.nome = request.form['name']
#         #rinnovi.tec_app = request.form['tec']
#         rinnovi.punto_aff = request.form['aff']
#         #rinnovi.piano = request.form ['piano']

#         try:
#             db.session.commit()
#             return redirect('/')
#         except:
#             return "There was a problem updating data."

#     else:
#         title = "Update Data"
#         return render_template('update.html', title=title, rinnovi=rinnovi, punti=punti)