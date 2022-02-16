from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def homework_index(request):
    value = request.GET.get("name")
    logger.info(value)
    return HttpResponse("Python the best")
