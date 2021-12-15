from models.Programmer import Programmer
from models.Recruiter import Recruiter
from models.Vacancy import Vacancy
from models.Candidate import Candidate

HR = Recruiter("Ana", "Conda", 38039845345, "anaconda@gmail.com", 300)
Prog_1 = Programmer("Simba", "King", 3803256789, "SimbaKing@gmail.com", 500)
Prog_2 = Programmer("Leon", "Sniper", 38034834953, "LeonSniper@gmail.com", 500)
Cand_1 = Candidate("Donatello_Artist", "Donatello_Artist@gmail.com", "Frontend", "Js, HTML, CSS", "Senior")
Cand_2 = Candidate("Michelangelo_Artist", "Mikelangelo_Artist@gmail.com", "Frontend", "Js, HTML, CSS", "Senior")
Cand_3 = Candidate("Raphael_Artist", "Raphael_Artist@gmail.com", "Backend", "Java, Python, C#, GO, Ruby", "Senior")
Vac_1 = Vacancy("DevOps", "Js, HTML, CSS, Java, Python, C#, GO, Ruby", "Senior")
Vac_2 = Vacancy("QA_Automation", "Python, QA_test_knowledge, Python_test_lybs", "Senior")
