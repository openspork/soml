from flask_login import LoginManager
from soml.models import User
from soml.app import app 

#login settings
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_message = 'pls log in'
login_manager.login_view = 'login_mod.login'

@login_manager.user_loader
def load_user(user_id):
	return User.get(User.id == int(user_id))

#login settings
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_message = 'pls log in'
login_manager.login_view = 'login_mod.login'

@login_manager.user_loader
def load_user(user_id):
	sq = User.select().where(User.id == int(user_id))
	if sq.exists():
		return User.get(User.id == int(user_id))