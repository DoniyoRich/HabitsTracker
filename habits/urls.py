from django.urls import path

from habits.apps import HabitsConfig
from habits.views import HabitsListAPIView, HabitCreateAPIView, HabitUpdateAPIView, HabitDetailAPIView, \
    HabitDeleteAPIView, HabitsLinkedListAPIView, HabitLinkedCreateAPIView, HabitLinkedUpdateAPIView, \
    HabitLinkedDetailAPIView, HabitLinkedDeleteAPIView, AwardListAPIView, AwardCreateAPIView, AwardUpdateAPIView, \
    AwardDetailAPIView, AwardDeleteAPIView

app_name = HabitsConfig.name

urlpatterns = [
    # эндпойнты для полезных привычек
    path("", HabitsListAPIView.as_view(), name="habits_list"),
    path("create/", HabitCreateAPIView.as_view(), name="habit_create"),
    path("update/<int:pk>/", HabitUpdateAPIView.as_view(), name="habit_update"),
    path("detail/<int:pk>/", HabitDetailAPIView.as_view(), name="habit_detail"),
    path("delete/<int:pk>/", HabitDeleteAPIView.as_view(), name="habit_delete"),

    # эндпойнты для связанных привычек
    path("habits_linked/", HabitsLinkedListAPIView.as_view(), name="habits_linked_list"),
    path("habits_linked/create/", HabitLinkedCreateAPIView.as_view(), name="habit_linked_create"),
    path("habits_linked/update/<int:pk>/", HabitLinkedUpdateAPIView.as_view(), name="habit_linked_update"),
    path("habits_linked/detail/<int:pk>/", HabitLinkedDetailAPIView.as_view(), name="habit_linked_detail"),
    path("habits_linked/delete/<int:pk>/", HabitLinkedDeleteAPIView.as_view(), name="habit_linked_delete"),

    # эндпойнты для вознаграждений
    path("awards/", AwardListAPIView.as_view(), name="awards_list"),
    path("awards/create/", AwardCreateAPIView.as_view(), name="award_create"),
    path("awards/update/<int:pk>/", AwardUpdateAPIView.as_view(), name="award_update"),
    path("awards/detail/<int:pk>/", AwardDetailAPIView.as_view(), name="award_detail"),
    path("awards/delete/<int:pk>/", AwardDeleteAPIView.as_view(), name="award_delete"),
]
