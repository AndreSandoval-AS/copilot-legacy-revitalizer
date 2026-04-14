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
