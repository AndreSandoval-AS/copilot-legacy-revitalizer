from .data_manager import DataManager
from .authenticator import Authenticator
from .data_persistence import DataPersistence

class Application:
    """Orchestrates the application by integrating data management, authentication, and persistence."""

    def __init__(self):
        """Initialize the Application with instances of DataManager, Authenticator, and DataPersistence, and load existing data."""
        self.data_manager = DataManager()
        self.authenticator = Authenticator()
        self.persistence = DataPersistence()
        # Load existing data on startup
        self.data_manager.data = self.persistence.load()

    def run(self):
        """Execute the main application loop, handling user authentication and commands.

        Returns:
            None
        """
        username = input("User: ")
        password = input("Pass: ")

        if self.authenticator.authenticate(username, password):
            print("Welcome")
            while True:
                cmd = input("What to do? (add/show/save/exit): ")
                if cmd == "exit":
                    break
                elif cmd == "add":
                    value = input("Value: ")
                    self.data_manager.add_item(value)
                elif cmd == "show":
                    self.data_manager.show_items()
                elif cmd == "save":
                    self.persistence.save(self.data_manager.get_items())
                else:
                    print("Invalid command.")
        else:
            print("Wrong!")
