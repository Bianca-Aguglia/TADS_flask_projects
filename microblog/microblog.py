from app import app
import config

app.config['SECRET_KEY'] = config.SECRET_KEY

if __name__ == '__main__':
    app.run()