"""
This Module provides a context manager implementation for a database connection
"""

class DatabaseConnection:
    """connects upon creation and desconnects upon exiting"""
    def __init__(self, connection_string: str) -> None:
        self.connection_string = connection_string
        self.is_connected = False

    def __enter__(self):
        print(f"Connecting to database: {self.connection_string}")
        self.is_connected = True
        return self

    def __exit__(self,
                 exc_type: type[BaseException] | None,
                 exc_value: BaseException | None,
                 traceback: object | None) -> None:
        print("Disconnecting from database")
        self.is_connected = False

with DatabaseConnection("localhost") as db_connection:
    raise ValueError
