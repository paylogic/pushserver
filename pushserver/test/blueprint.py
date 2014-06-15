"""Test views."""
from flask import Blueprint, render_template

blueprint = Blueprint('test', __name__, template_folder='templates')


@blueprint.route('')
def test():
    return render_template('test.html')
