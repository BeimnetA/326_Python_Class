from db_user import create_tables
from gui import create_gui

def main():
    # Initializes the database by creating all the necessary tables
    create_tables()

    # Launch the GUI
    create_gui()

if __name__ == "__main__":
    main()