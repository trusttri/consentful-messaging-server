from __future__ import absolute_import
from celery import Celery, shared_task, current_task
from celery.exceptions import Ignore
from website.models import TwitterAccount
from django.utils import timezone
import tweepy


@shared_task
def network_rules(user, sender, access_key, access_secret):
	return False