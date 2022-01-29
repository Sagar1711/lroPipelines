import abc

class AbsPipeline(abc.ABC):

    @abc.abstractclassmethod
    def initializePipeline(self):
        pass

    @abc.abstractclassmethod
    def runPipeline(self):
        pass
