from django.urls import path

from habits.apps import HabitsConfig
from habits.views import (AllPublicHabitsListAPIView, AwardCreateAPIView,
                          AwardDeleteAPIView, AwardDetailAPIView,
                          AwardListAPIView, AwardUpdateAPIView,
                          HabitCreateAPIView, HabitDeleteAPIView,
                          HabitDetailAPIView, HabitUpdateAPIView,
                          UserHabitsListAPIView)

app_name = HabitsConfig.name

urlpatterns = [
    # эндпойнты для полезных привычек
    path("public-habits/", AllPublicHabitsListAPIView.as_view(), name="all_public_habits_list"),
    path("user-habits/", UserHabitsListAPIView.as_view(), name="user_habits_list"),
    path("create/", HabitCreateAPIView.as_view(), name="habit_create"),
    path("update/<int:pk>/", HabitUpdateAPIView.as_view(), name="habit_update"),
    path("detail/<int:pk>/", HabitDetailAPIView.as_view(), name="habit_detail"),
    path("delete/<int:pk>/", HabitDeleteAPIView.as_view(), name="habit_delete"),

    # эндпойнты для вознаграждений
    path("awards/", AwardListAPIView.as_view(), name="awards_list"),
    path("awards/create/", AwardCreateAPIView.as_view(), name="award_create"),
    path("awards/update/<int:pk>/", AwardUpdateAPIView.as_view(), name="award_update"),
    path("awards/detail/<int:pk>/", AwardDetailAPIView.as_view(), name="award_detail"),
    path("awards/delete/<int:pk>/", AwardDeleteAPIView.as_view(), name="award_delete"),
]
