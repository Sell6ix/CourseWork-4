from project.config import config
from project.models import Genre, Movie, User

from project.server import create_app, db

app = create_app(config)




if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)