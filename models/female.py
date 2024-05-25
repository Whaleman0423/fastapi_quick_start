from models.person import Person

class Female(Person):

    def do_habit(self):
        habit = "女生的興趣是逛街"
        
        print("女生的興趣是逛街")
        return {"habit":habit}