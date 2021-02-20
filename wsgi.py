from app import create_app
from dotenv import load_dotenv


load_dotenv()
app = create_app("dev")


@app.route("/")
def index():
    return f"<h1>Home</h1>"


if __name__ == '__main__':
    app.run()
