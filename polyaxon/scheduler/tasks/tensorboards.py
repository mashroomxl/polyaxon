import logging

from constants.jobs import JobLifeCycle
from db.getters.projects import get_valid_project
from polyaxon.celery_api import app as celery_app
from polyaxon.settings import SchedulerCeleryTasks
from scheduler import tensorboard_scheduler

_logger = logging.getLogger(__name__)


@celery_app.task(name=SchedulerCeleryTasks.PROJECTS_TENSORBOARD_START, ignore_result=True)
def projects_tensorboard_start(project_id):
    project = get_valid_project(project_id=project_id)
    if not project or not project.tensorboard:
        _logger.warning('Project does not have a tensorboard.')
        return None

    if project.tensorboard.last_status == JobLifeCycle.RUNNING:
        _logger.warning('Tensorboard is already running.')
        return None
    tensorboard_scheduler.start_tensorboard(project.tensorboard)


@celery_app.task(name=SchedulerCeleryTasks.PROJECTS_TENSORBOARD_STOP, ignore_result=True)
def projects_tensorboard_stop(project_id):
    project = get_valid_project(project_id=project_id)
    if not project:
        return None
    tensorboard_scheduler.stop_tensorboard(project.tensorboard, update_status=True)
