from flask import Blueprint, render_template

errors = Blueprint('errors', __name__, template_folder="templates")


@errors.app_errorhandler(403)
def forbidden(e):
    return render_template('errors/403.html'), 403


# @errors.app_errorhandler(500)
# def internal_server_error(e):
#     return render_template('errors/500.html'), 500


@errors.app_errorhandler(410)
def resource_deleted(e):
    return render_template('errors/410.html'), 410


# @errors.app_errorhandler(Exception)
# def unhandled_exception(e):
#     return render_template('errors/500.html')
