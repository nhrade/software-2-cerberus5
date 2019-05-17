

class HookCollectionManager:

    def __init__(self):
        self.hookCollectionList = []

    def addHookCollection(self, hookCollection):
        self.hookCollectionList.append(hookCollection)

    def removeHookCollection(self, hookCollection):
        self.hookCollectionList.remove(hookCollection)

    def getHookCollection(self, name):
        for hookCollection in self.hookCollectionList:
            if hookCollection.name == name:
                return hookCollection
        return None