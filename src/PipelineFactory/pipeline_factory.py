from inspect import  getmembers, isclass, isabstract
import pipelines

class PipelineFactory(object):

    pipelines = {}

    def __init__(self) -> None:
        self.load_pipelines()

    def load_pipelines(self):
        classes = getmembers(
            pipelines,
            lambda m: isclass(m) and not isabstract(m)
        )
        for name, _type in classes:
            if isclass(_type) and issubclass(_type, pipelines.AbsPipeline):
                self.pipelines.update({name, _type})
        
    def create_instance(self, pipeline_name):
        if pipeline_name in self.pipelines:
            return self.pipelines[pipeline_name]()
        else:
            raise ValueError(f"Pipeline not found: {pipeline_name}")

