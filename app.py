from flask import Flask, render_template

from config import Config
from models import db, Article, Video, LifeMoment


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app


app = create_app()


@app.route("/")
def index():
    articles = Article.query.order_by(Article.created_at.desc()).limit(5).all()
    videos = Video.query.order_by(Video.created_at.desc()).limit(5).all()
    moments = LifeMoment.query.order_by(LifeMoment.created_at.desc()).limit(10).all()
    return render_template("index.html", articles=articles, videos=videos, moments=moments)


if __name__ == "__main__":
    app.run(debug=True)
