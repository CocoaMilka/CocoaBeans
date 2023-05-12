from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user

from .models import Commission
from . import db
# 

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():

    if request.method == 'POST':
        title = request.form.get('title')
        price = request.form.get('price')
        description = request.form.get('description')

        if len(title) < 1:
            flash('Title cannot be empty!', category='error')
        elif len(description) < 1:
            flash('Description cannot be empty!', category='error')
        else:
            new_commission = Commission(title=title, price=price, commissioner=current_user.id, description=description)
            db.session.add(new_commission)
            db.session.commit()
            flash('Commission added!', category='success')

    return render_template("index.html", user=current_user)