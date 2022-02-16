import logging

from django_rq import job
from time import sleep

logger = logging.getLogger(__name__)


@job
def run_products_update():
    logger.info("run_products_update is called")
    for _ in range(10):
        sleep(3)
        logger.info("run_products_update step")
    return "Finished"


def some_view_or_function():
    run_products_update.delay()
