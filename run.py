from src.main.server.server import app
from src.models.connection.connectio_handler import db_connection_handler

if __name__ == "__main__":
    db_connection_handler.connect_to_db()
    app.run(host="0.0.0.0", port=5000)
