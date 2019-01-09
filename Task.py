from time import sleep
import random

class task:
    def __init__(self, deadline, name, done):
        self.done = done
        self.name = name
        self.deadline = deadline

    def __str__(self):
        return self.name + "\nDeadline : " + str(self.deadline) + "\n"

    def runTask(self, duration):
        self.done = bool(random.getrandbits(1))
        print("Running task : " + self.name + " with deadline : " + str(self.deadline) + " for : " + str(
            duration) + "ms. Will be done ? " + str(self.done))
        sleep(float(duration) / float(1000))
