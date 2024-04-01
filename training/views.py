from django.shortcuts import render
from .models import User, Activity, UserActivityLog, do_training

# Create your views here.
def index(request):
    activity_list = Activity.objects.all()
    users_list = User.objects.filter(is_staff=False)
    users=[]
    for user in users_list:
        user_activity = UserActivityLog.objects.filter(user_activity__user__username=user.username)
        score = 0
        for activity in user_activity:
            score += activity.score
        userProfile={}
        userProfile["username"] = user.username
        userProfile["score"] = score
        users.append(userProfile)
    users.append({"username": "Dyonisia", "score": 640})
    users = sorted(users, key=lambda x: x["score"], reverse=True)
    context = {"activity_list": activity_list, "users": users}
    return render(request, "training/index2.html", context)

def train(request):
    training_score = do_training
    return render(request, "training/train.html", {"score": training_score})