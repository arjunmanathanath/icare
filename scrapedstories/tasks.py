from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
#from photos.utils import save_latest_flickr_image
from .myscrapercrawler import scraper
from .models import SeedUrlDefiner

logger = get_task_logger(__name__)


@periodic_task(
    run_every=(crontab(minute='*/5')),
    name="task_save_scraped_data",
    ignore_result=True
)
def task_save_scraped_data():
    """
    code here
    """

    scraper(["https://www.parsehub.com/", "https://www.entrepreneur.com/article/287583"], 2)
    #save_latest_flickr_image()
    logger.info("Saved image from Flickr")
