from django.urls import path

from habits.apps import HabitsConfig
from habits.views import HabitsListAPIView, HabitCreateAPIView, HabitUpdateAPIView, HabitDetailAPIView, \
    HabitDeleteAPIView

app_name = HabitsConfig.name

urlpatterns = [
    path("", HabitsListAPIView.as_view(), name="habits_list"),
    path("create/", HabitCreateAPIView.as_view(), name="habit_create"),
    path("update/<int:pk>/", HabitUpdateAPIView.as_view(), name="habit_update"),
    path("detail/<int:pk>/", HabitDetailAPIView.as_view(), name="habit_detail"),
    path("delete/<int:pk>/", HabitDeleteAPIView.as_view(), name="habit_delete"),
]
