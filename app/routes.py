from flask import render_template, redirect, url_for, flash
from app import app 
from app.forms import Contact


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contacts', methods=["GET", "POST"])
def add_contact():
    form = Contact()
    if form.validate_on_submit():
        first_name = form.first.data
        last_name = form.last.data
        phone_num = form.phone.data
        home = form.home.data
        print(first_name,last_name,phone_num,home)

        flash(f"{first_name} {last_name} \n residing at {home}\n has been added to your contacts.", "success")
        return redirect(url_for('index.html'))
    return render_template('contacts.html', form=form)