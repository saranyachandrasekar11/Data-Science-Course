class Robot:
    def __init__(self, name, task):
        self.name = name
        self.task = task

    def introduce(self):
        print(f"Hello! I am {self.name}.")
        print(f"My main job is: {self.task}.\n")

# Creating the robot objects
bot1 = Robot("MediBot", "Helping doctors")
bot2 = Robot("ScrubBot", "Cleaning floors")

# Running the introductions
bot1.introduce()
bot2.introduce()
