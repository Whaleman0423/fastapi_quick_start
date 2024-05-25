from models.person import Person

class Male(Person):

    def do_habit(self):
        habit = "男生的興趣是打籃球"
        
        print(habit)
        return {"habit":habit}
