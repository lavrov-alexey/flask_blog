from blog.app import app

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5005,  # по-умолчанию если не указывать - порт 5000
        debug=True
    )
