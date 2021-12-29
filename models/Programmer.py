class Programmer:
    tech_stack = ""
    closed_this_month = 0

    def __init__(self, name, second_name, mobile_number, email, payment_per_one_day):
        self.name = name
        self.second_name = second_name
        self.mobile_number = mobile_number
        self.email = email
        self.payment_per_one_day = payment_per_one_day

    @staticmethod
    def work():
        return "I come to the office and start coding"

    def __str__(self):
        return f"Должность:{self.name} {self.second_name}"


programmer = Programmer('darova', 'poka', 'ne dam', 'ne skazhu', 1500)
assert programmer.work() == "I come to the office and start coding"
