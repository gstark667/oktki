from flask import Blueprint, render_template, abort, redirect, url_for

from ..models.pages import Page, EditPageForm

blueprint = Blueprint('Pages', __name__, template_folder='templates/pages', url_prefix='/pages')

@blueprint.route('/')
def index():
    return render_template('pages/index.html'), 200


@blueprint.route('/page/<title>')
def page(title):
    page = Page.get(title)
    return render_template('pages/page.html', page=page), 200


@blueprint.route('/create/<title>')
def create(title):
    page = Page.create(title)
    return redirect(url_for('Pages.page', title=page.title))


@blueprint.route('/edit/<title>', methods=('GET', 'POST'))
def edit(title):
    page = Page.get(title)
    form = EditPageForm()
    if form.validate_on_submit():
        page.update(form.body.data)
        return redirect(url_for('Pages.page', title=page.title))
    form.body.data = page.body
    return render_template('pages/edit.html', page=page, form=form), 200

