import datetime
import platform

def main():
    """
    Main function.
    """
    print("Starting speed_racer @ " + str(datetime.datetime.now()))
    print("OS: " + platform.system())
    print("OS Release: " + platform.release())
    print("OS Version: " +  platform.version())

if __name__ == '__main__':
    main()