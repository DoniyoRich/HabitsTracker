from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from habits.models import Habit, HabitLinked, Award
from habits.serializers import HabitSerializer, HabitLinkedSerializer, AwardSerializer
from users.permissions import IsModerator, IsOwner

# Набор API для полезных привычек
class HabitsListAPIView(ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitCreateAPIView(CreateAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsOwner]


class HabitDetailAPIView(RetrieveAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsModerator | IsOwner]


class HabitUpdateAPIView(UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner]


class HabitDeleteAPIView(DestroyAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsModerator | IsOwner]


# Набор API для связанных привычек
class HabitsLinkedListAPIView(ListAPIView):
    serializer_class = HabitLinkedSerializer
    queryset = HabitLinked.objects.all()


class HabitLinkedCreateAPIView(CreateAPIView):
    serializer_class = HabitLinkedSerializer
    permission_classes = [IsOwner]


class HabitLinkedDetailAPIView(RetrieveAPIView):
    serializer_class = HabitLinkedSerializer
    queryset = HabitLinked.objects.all()
    permission_classes = [IsModerator | IsOwner]


class HabitLinkedUpdateAPIView(UpdateAPIView):
    serializer_class = HabitLinkedSerializer
    queryset = HabitLinked.objects.all()
    permission_classes = [IsOwner]


class HabitLinkedDeleteAPIView(DestroyAPIView):
    serializer_class = HabitLinkedSerializer
    queryset = HabitLinked.objects.all()
    permission_classes = [IsModerator | IsOwner]


# Набор API для вознаграждений
class AwardListAPIView(ListAPIView):
    serializer_class = AwardSerializer
    queryset = Award.objects.all()


class AwardCreateAPIView(CreateAPIView):
    serializer_class = AwardSerializer
    permission_classes = [IsOwner]


class AwardDetailAPIView(RetrieveAPIView):
    serializer_class = AwardSerializer
    queryset = Award.objects.all()
    permission_classes = [IsModerator | IsOwner]


class AwardUpdateAPIView(UpdateAPIView):
    serializer_class = AwardSerializer
    queryset = Award.objects.all()
    permission_classes = [IsOwner]


class AwardDeleteAPIView(DestroyAPIView):
    serializer_class = AwardSerializer
    queryset = Award.objects.all()
    permission_classes = [IsModerator | IsOwner]