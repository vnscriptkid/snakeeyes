from flask_wtf import CsrfProtect
from flask_mail import Mail
from flask_debugtoolbar import DebugToolbarExtension


debug_toolbar = DebugToolbarExtension()
mail = Mail()
csrf = CsrfProtect()
