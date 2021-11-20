from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Member
import logging

logger = logging.getLogger(__name__)



logger = logging.getLogger(__name__)

@receiver(pre_save, sender=Member)
def reduce_image_quality(sender, instance, **kwargs):
    logger.info(f"Compressing photograph  '{instance.firstname}'")
    instance.compress_img(instance.passport)