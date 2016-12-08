from app import app
from flask import render_template,request,redirect,url_for
from model import ToDo
from app import db
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from datetime import datetime

@app.route('/',methods=['GET','POST'])
def index():
    form = AddForm()
    if form.validate_on_submit():
        content = form.content.data
        todo = ToDo(content=content,time=datetime.utcnow().strftime("%H:%M %d-%m-%Y"))
        db.session.add(todo)
        db.session.commit()

        return redirect(url_for('index'))


    todos = ToDo.query.order_by(ToDo.time.desc())
    return render_template('index.html',todos=todos,form=form)


class AddForm(Form):
    content = StringField(validators=[Required()])
    submit = SubmitField('add')

@app.route('/operate/<op>/<int:id>',methods=['GET','POST'])
def operate(id,op):
    todo = ToDo.query.get_or_404(id)
    if op=='done':
        todo.status=1
    elif op =='undone':
        todo.status=0
    elif op=='delete':
        db.session.delete(todo)

    return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
