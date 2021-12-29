
class Recruiter:
    hired_this_month = 0

    def __init__(self, name, second_name, mobile_number, email, payment_per_one_day):
        self.name = name
        self.second_name = second_name
        self.mobile_number = mobile_number
        self.email = email
        self.payment_per_one_day = payment_per_one_day

    def __str__(self):
        return f"Должность:{self.name} {self.second_name}"

    @staticmethod
    def work():
        return "I come to the office and start hiring"


assert Recruiter.work() == "I come to the office and start hiring"