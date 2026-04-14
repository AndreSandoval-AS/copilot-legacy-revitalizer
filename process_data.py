import datetime
import json

class DataManager:
    """Manages a collection of data items, providing operations to add, retrieve, and display them."""

    def __init__(self):
        """Initialize the DataManager with an empty list of data items."""
        self.data = []

    def add_item(self, value):
        """Add a new item to the data collection with a timestamp.

        Args:
            value (str): The value to store in the new item.

        Returns:
            None
        """
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        item = {'id': len(self.data) + 1, 'val': value, 'date': timestamp}
        self.data.append(item)
        print("Added.")

    def get_items(self):
        """Retrieve the current list of data items.

        Returns:
            list: A list of dictionaries representing the data items.
        """
        return self.data

    def show_items(self):
        """Display all data items in a formatted manner to the console.

        Returns:
            None
        """
        for item in self.data:
            print(f"Item: {item['id']} - {item['val']} at {item['date']}")

class Authenticator:
    """Handles user authentication using predefined credentials."""

    def __init__(self):
        """Initialize the Authenticator with hardcoded credentials."""
        self.credentials = {"u": "admin", "p": "12345"}

    def authenticate(self, username, password):
        """Verify if the provided username and password match the stored credentials.

        Args:
            username (str): The username to check.
            password (str): The password to check.

        Returns:
            bool: True if credentials are valid, False otherwise.
        """
        return username == self.credentials["u"] and password == self.credentials["p"]

class DataPersistence:
    """Manages saving and loading of data items to and from a JSON file."""

    def __init__(self, filename="data.txt"):
        """Initialize the DataPersistence with a specified filename.

        Args:
            filename (str): The path to the file for data persistence. Defaults to 'data.txt'.
        """
        self.filename = filename

    def save(self, data):
        """Save the provided data list to the file in JSON format.

        Args:
            data (list): The list of data items to save.

        Returns:
            None

        Raises:
            Prints error messages for file or serialization issues.
        """
        try:
            with open(self.filename, "w") as f:
                json.dump(data, f, indent=4)
            print("Saved.")
        except (OSError, IOError) as e:
            print(f"Error saving data: {e}")
        except (TypeError, ValueError) as e:
            print(f"Error serializing data: {e}")

    def load(self):
        """Load the data list from the file.

        Returns:
            list: The loaded list of data items, or an empty list if loading fails.

        Raises:
            Prints error messages for file or parsing issues.
        """
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
            return data
        except FileNotFoundError:
            print("Data file not found, starting with empty data.")
            return []
        except (OSError, IOError) as e:
            print(f"Error reading data: {e}")
            return []
        except (json.JSONDecodeError, ValueError) as e:
            print(f"Error parsing data file: {e}")
            return []

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

def main():
    """Serve as the entry point for the application, initializing and running the Application instance.

    Returns:
        None
    """
    app = Application()
    app.run()

if __name__ == "__main__":
    main()
