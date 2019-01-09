from Task import task
from random import randint
from EDF import *

import time

now = time.time()

taskList = []

for i in range(0, 10):
    taskList.append(task(randint(1, 5) * 1000, "Task " + str(i), False))

orderedTaskList = EDF.sortList(taskList)

while len(orderedTaskList) > 0:
    tempTask = EDF.getTaskToExecute(orderedTaskList)
    tempTask.runTask(10)
    EDF.insertTaskBack(orderedTaskList, tempTask)

