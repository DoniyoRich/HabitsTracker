from rest_framework import status
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.response import Response

from habits.models import Award, Habit
from habits.paginators import HabitPaginator
from habits.serializers import AwardSerializer, HabitSerializer
from habits.services import create_habit_schedule
from users.permissions import IsModerator, IsOwner


# Набор API для полезных привычек
class AllPublicHabitsListAPIView(ListAPIView):
    """
    Список всех публичных привычек в системе.
    """
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator

    def get_queryset(self):
        return Habit.objects.filter(is_public=True)


class UserHabitsListAPIView(ListAPIView):
    """
    Список всех привычек определенного пользователя.
    """
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator

    def get_queryset(self):
        return Habit.objects.filter(owner=self.request.user)


class HabitCreateAPIView(CreateAPIView):
    """
    Создание привычки.
    """
    serializer_class = HabitSerializer
    permission_classes = [IsOwner]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        habit = serializer.save()

        # Создаем расписание
        try:
            create_habit_schedule(
                owner=request.user,
                habit=habit
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            habit.delete()
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class HabitDetailAPIView(RetrieveAPIView):
    """
    Просмотр привычки.
    """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsModerator | IsOwner]


class HabitUpdateAPIView(UpdateAPIView):
    """
    Редактирование привычки.
    """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner]


class HabitDeleteAPIView(DestroyAPIView):
    """
    Удаление привычки.
    """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsModerator | IsOwner]


# Набор API для вознаграждений
class AwardListAPIView(ListAPIView):
    """
    Список всех вознаграждений.
    """
    serializer_class = AwardSerializer
    queryset = Award.objects.all()
    pagination_class = HabitPaginator


class AwardCreateAPIView(CreateAPIView):
    """
    Создание вознаграждения.
    """
    serializer_class = AwardSerializer
    permission_classes = [IsOwner]


class AwardDetailAPIView(RetrieveAPIView):
    """
    Просмотр вознаграждения.
    """
    serializer_class = AwardSerializer
    queryset = Award.objects.all()
    permission_classes = [IsModerator | IsOwner]


class AwardUpdateAPIView(UpdateAPIView):
    """
    Редактирование вознаграждения.
    """
    serializer_class = AwardSerializer
    queryset = Award.objects.all()
    permission_classes = [IsOwner]


class AwardDeleteAPIView(DestroyAPIView):
    """
    Удаление вознаграждения.
    """
    serializer_class = AwardSerializer
    queryset = Award.objects.all()
    permission_classes = [IsModerator | IsOwner]
