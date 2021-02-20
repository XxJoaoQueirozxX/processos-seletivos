from flask_migrate import Migrate
from dotenv import load_dotenv
from app import create_app, db
import click

load_dotenv()
app = create_app("dev")
migrate = Migrate(app, db)


@app.before_first_request
def init_db():
    """init the models on database"""
    db.create_all()


@app.shell_context_processor
def shell_context():
    """Make the shell context for flask shell"""
    return dict(db=db)


@app.cli.command()
@click.argument('test_names', nargs=-1)
def test(test_names):
    """Run the unit tests."""
    import unittest
    if test_names:
        tests = unittest.TestLoader().loadTestsFromNames(test_names)
    else:
        tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    app.run()
