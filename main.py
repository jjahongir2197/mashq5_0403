class Member:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.workouts = []
        self.fitness_score = 0

    def add_workout(self, workout_type, duration):
        self.workouts.append({"type": workout_type, "duration": duration})
        self.fitness_score += duration * 1.5

    def average_workout(self):
        if not self.workouts:
            return 0
        total = sum(w["duration"] for w in self.workouts)
        return total / len(self.workouts)

    def info(self):
        print(f"Name: {self.name}, Age: {self.age}")
        print(f"Workouts: {len(self.workouts)}, Avg Duration: {self.average_workout():.2f}")
        print(f"Fitness Score: {self.fitness_score:.2f}")

class Gym:
    def __init__(self):
        self.members = []

    def add_member(self, member):
        self.members.append(member)

    def remove_member(self, name):
        self.members = [m for m in self.members if m.name != name]

    def top_member(self):
        if not self.members:
            return None
        return max(self.members, key=lambda m: m.fitness_score)

    def show_all_members(self):
        for m in self.members:
            m.info()
            print("----------------")

def gym_demo():
    gym = Gym()
    m1 = Member("Ali", 20)
    m2 = Member("Vali", 22)
    m3 = Member("Hasan", 19)

    workouts = [("Cardio", 30), ("Boxing", 45), ("Weight", 60)]
    for w in workouts:
        m1.add_workout(*w)
        m2.add_workout(w[0], w[1] + 10)
        m3.add_workout(w[0], w[1] - 5)

    gym.add_member(m1)
    gym.add_member(m2)
    gym.add_member(m3)

    gym.show_all_members()

    top = gym.top_member()
    if top:
        print("Top Member:")
        top.info()

gym_demo()
