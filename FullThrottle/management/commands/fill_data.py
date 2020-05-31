from django.core.management.base import BaseCommand
from FullThrottle.models import User, ActivityPeriod
import random
import string
import time
from randomtimestamp import randomtimestamp


class Command(BaseCommand):
    help = "Command to fill up dummy data"

    def handle(self, *args, **options):
        """
        Fill up dummy data
        :param args:
        :param options:
        :return:
        """
        usr_arr = []
        for i in range(100):
            new_usr = User(first_name=random_string(6), last_name=random_string(4), timezone=time.tzname)
            usr_arr.append(new_usr)
        User.objects.bulk_create(usr_arr)
        all_users = User.objects.all()
        activity_arr = []
        for i in range(200):
            usr = all_users[random.randint(0, len(all_users) - 1)]
            new_activity = ActivityPeriod(login_time=randomtimestamp(2010, False),
                                          logout_time=randomtimestamp(2010, False),
                                          user=usr)
            activity_arr.append(new_activity)

        ActivityPeriod.objects.bulk_create(activity_arr)


def random_string(string_length=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_length))