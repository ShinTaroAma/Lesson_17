""" Домашка + самост. задание  """


class Employee:

    def __init__(self, name, second_name, mobile_number, email, payment_per_one_day):
        f = open("text.txt", "r")
        f.close()
        self.name = name
        self.second_name = second_name
        self.email = email
        self.mobile_number = mobile_number
        self.payment_per_one_day = payment_per_one_day
        self.write_email()

    def write_email(self):
        emails = []
        f = open("text.txt", "r")
        for line in f:
            emails.append(line)

        if self.email + '\n' in emails:
            raise ValueError()
        else:
            f = open('txt.txt', 'a')
            f.write(self.email + '\n')
            f.close()

    @staticmethod
    def work(self):
        print("I come to the office")


    @staticmethod
    def check_salary(self, work_days, payment_per_one_day, no_payment_days):
        self.payment_per_one_day = payment_per_one_day
        return (work_days - no_payment_days) * payment_per_one_day


class Recruiter(Employee):
    hired_this_month = 0

    def work(self):
        return "I come to the office and start hiring"

    def __str__(self):
        return f"Должность:{self.name} {self.second_name}"


class Programmer(Employee):
    tech_stack = ""
    closed_this_month = 0

    def work(self):
        return "I come to the office and start coding"

    def __str__(self):
        return f"Должность:{self.name} {self.second_name}"







prog1 = Employee("Nin","Nan", "0938473546", "asdffg@gmail.com", 500 )
prog2 = Employee("Nin","Nan", "0938473546", "assdffg@gmail.com", 500 )