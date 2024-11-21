from db import create_app
from flask_login import LoginManager, UserMixin, login_user, login_required

app = create_app()


if __name__ == '__main__':
    app.run(debug=True)
