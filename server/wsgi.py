from app import app
from settings import DEBUG, HOST, PORT

if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=DEBUG, ssl_context=("server/cert.pem", "server/key.pem"))
