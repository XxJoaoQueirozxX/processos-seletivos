from flask_migrate import Migrate
from dotenv import load_dotenv
from app import create_app, db


load_dotenv()
app = create_app("dev")
migrate = Migrate(app, db)


@app.before_first_request
def init_db():
    db.create_all()


@app.shell_context_processor
def shell_context():
    return dict(db=db)


@app.route("/")
def index():
    return f"<h1>Home</h1>"


if __name__ == '__main__':
    app.run()
