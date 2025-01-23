import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

class DBConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = 'mongodb://{}:{}@{}:{}/?authSource=admin'.format(
            os.getenv("MONGO_USER"),
            os.getenv("MONGO_PASSWORD"),
            os.getenv("MONGO_HOST"),
            os.getenv("MONGO_PORT")
        )
        self.__database_name = "delivery_db"
        self.__client = None
        self.__db_connection = None

    def connect_to_db(self):
        self.__client = MongoClient(self.__connection_string)
        self.__db_connection = self.__client[self.__database_name]

    def get_db_connection(self):
        return self.__db_connection

db_connection_handler = DBConnectionHandler()
