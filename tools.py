class tools:
    @staticmethod
    def sort(taskList):
        ordered = []
        lowestTask = taskList[0]
        lowestTaskIndex = 0
        while len(taskList) > 0:
            for i in range(0, len(taskList)):
                if taskList[i].deadline <= lowestTask.deadline:
                    lowestTaskIndex = i
                    lowestTask = taskList[i]
            ordered.append(lowestTask)
            if (len(taskList) > lowestTaskIndex):
                del taskList[lowestTaskIndex]
            if len(taskList) >= 1:
                lowestTask = taskList[0]
                lowestTaskIndex = 0
        return ordered
