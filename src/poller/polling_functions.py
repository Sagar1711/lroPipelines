from PipelineFactory.pipeline_factory import PipelineFactory
from src.github_libs.github_functions import GitHubFunctions

def poller():
    gitObject = GitHubFunctions()
    gitNotificationResp = gitObject.getNotifications()
    return parser(gitNotificationResp) if gitNotificationResp else None

def parser(responseObject):
    pass
