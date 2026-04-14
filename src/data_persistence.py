import json

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
