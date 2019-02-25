import logging 

from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver

from .models import Book


logger = logging.getLogger(__name__)

@receiver(pre_save, sender=Book)
def log_update_or_create(sender, instance, **kwargs):
    if instance.__dict__.get('id', None):
        logger.info('Updated data for {}'.format(instance.__dict__.get('title', None)))
    else:
        logger.info('Creted new book item: {}'.format(instance.__dict__.get('title', None)))

@receiver(pre_delete, sender=Book)
def log_delete(sender, instance, **kwargs):
    logger.info('Deleted book item: {}'.format(instance.__dict__.get('title', None)))