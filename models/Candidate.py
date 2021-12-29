class UnableToWorkException(Exception):
    def __init__(self):
        self.message = "I’m not hired yet, lol."


try:
    class Candidate:

        def __init__(self, full_name, email, technologies, main_skill, main_skill_grade):
            self.second_name = full_name
            self.email = email
            self.technologies = technologies
            self.main_skill = main_skill
            self.main_skill_grade = main_skill_grade

    raise UnableToWorkException

except UnableToWorkException:
    print("I’m not hired yet, lol.")

s = Candidate("Rid_Onil", "tecnolog", "werrt@gmail.com", "Git", "Java" "Senior")

s.work()
