from app import create_app

application = create_app('development')

if __name__ == "__main__":
    application.run(host='127.0.0.1', port=8000)
