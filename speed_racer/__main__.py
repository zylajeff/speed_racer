import datetime
import platform
from robot.app import app

def main():
    """
    Main function.
    """
    print("Starting speed_racer @ " + str(datetime.datetime.now()))
    print("OS: " + platform.system())
    print("OS Release: " + platform.release())
    print("OS Version: " +  platform.version())

    app()

if __name__ == '__main__':
    main()