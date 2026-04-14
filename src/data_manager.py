import datetime

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
