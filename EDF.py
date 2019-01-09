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
        '''Cette méthode permet de réinsérer la tache que l'on vient d'exécuter au bon endroit dans la liste (après toutes celles qui ont la meme deadline)'''
        if not taskToInsert.done:
            for i in range(0, len(taskList)):
                if taskList[i].deadline > taskToInsert.deadline:
                    taskList.insert(i, taskToInsert)
                    break
