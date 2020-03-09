from flask import Blueprint, render_template, request, url_for, redirect
from webapp.main.forms import SearchForm
from scraper import get_page

main = Blueprint('main', __name__)

@main.route("/")
def default():
    return redirect(url_for("main.home"))

@main.route("/home", methods=['GET', 'POST'])
def home():
    form = SearchForm()
    if form.validate_on_submit():
        get_page(form.url.data)
        print(form.url.data)
    return render_template("home.html", form=form)
