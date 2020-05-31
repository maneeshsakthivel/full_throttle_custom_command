from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from multiprocessing import Process, Pool
import time


def get_user_activity(request):
    """
    View for multiprocessing using process method
    :param request:
    :return:
    """
    from .models import ActivityPeriod, User
    all_users = User.objects.all()
    members_arr = []
    for user in all_users:
        activity_arr = ActivityPeriod.objects.filter(user=user)
        user_activity_dict_arr = []
        for activity in activity_arr:
            user_activity_dict_arr.append({
                'start_time': activity.login_time.strftime("%b %d %Y, %I:%M %p"),
                'end_time': activity.logout_time.strftime("%b %d %Y, %I:%M %p")
            })

        members_arr.append({
            'id': user.id,
            'real_name': user.first_name + " " + user.last_name,
            'tz': user.timezone,
            'activity_periods': user_activity_dict_arr
        })

    return JsonResponse(data={"ok": True, 'members': members_arr})

