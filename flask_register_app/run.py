from flask_register_app.main import app


if __name__ == '__main__':
    app.run(
        host='localhost',
        port=8080,
        debug=True
    )
