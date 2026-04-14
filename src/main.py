from .application import Application

def main():
    """Serve as the entry point for the application, initializing and running the Application instance.

    Returns:
        None
    """
    app = Application()
    app.run()

if __name__ == "__main__":
    main()
