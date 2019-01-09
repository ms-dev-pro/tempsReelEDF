from tools import *

class EDF:

    @staticmethod
    def sortList(taskList):
        return tools.sort(taskList)

    @staticmethod
    def getTaskToExecute(taskList):
        myTask = taskList.pop(0)
        return myTask

    @staticmethod
    def insertTaskBack(taskList, taskToInsert):
        if not taskToInsert.done:
            for i in range(0, len(taskList)):
                if taskList[i].deadline > taskToInsert.deadline:
                    taskList.insert(i, taskToInsert)
                    break
