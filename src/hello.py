from datetime import datetime


def main():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Hello! The current date and time is {now}")


if __name__ == "__main__":
    main()
