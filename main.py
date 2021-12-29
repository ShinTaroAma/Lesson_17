import datetime
import traceback


def main():

    class UnableToWorkException(Exception):
        def __init__(self):
            self.message = "I’m not hired yet, lol."


    class Employee:
        def __init__(self, email: str):

            with open('emails.txt', 'r') as emails_file:
                if email in emails_file.read():
                    raise ValueError('Error')

            with open('emails.txt', 'a') as emails_file:
                emails_file.write(f'{email}\n')

            self.email = email


    programmer = Employee('abc@abc.com')
    hr = Employee('hr@hr.com')


if __name__ == '__main__':
    try:
        main()
    except Exception as exception:
        with open('logs.txt', 'a') as logs:
            logs.write(f'{datetime.datetime.now()}\n'
                       f'{type(exception).__name__}\n'
                       f'{traceback.format_exc()}\n')
