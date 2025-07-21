from django.test import override_settings
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from habits.models import Award, Habit
from users.models import CustomUser


@override_settings(
    REST_FRAMEWORK={
        'DEFAULT_AUTHENTICATION_CLASSES': [],
        'DEFAULT_PERMISSION_CLASSES': [],
    }
)
class HabitTestCase(APITestCase):
    """
    Класс тестирования привычек.
    """

    def setUp(self):
        self.user = CustomUser.objects.create(email="admin@mail.com")

        self.award1 = Award.objects.create(award="Выпить сока")
        self.award2 = Award.objects.create(award="Посмотреть сериальчик")
        self.award3 = Award.objects.create(award="Съесть печенюшку")

        self.habit1 = Habit.objects.create(
            owner=self.user, activity="Сделать пробежку утром", time="07:00",
            location="Вокруг дома", is_pleasant=False, linked=None,
            award=self.award1, frequency=1, implementation_time=120, is_public=True
        )

    def test_get_list_public_habits(self):
        """
        Тест на получение списка публичных привычек.
        """
        self.client.force_authenticate(self.user)
        self.url = reverse("habits:all_public_habits_list")
        response = self.client.get(self.url)
        total_public_habits = Habit.objects.filter(is_public=True).count()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

        self.assertEqual(total_public_habits, 1)

    def test_create_habit(self):
        """
        Тест на создание привычки.
        """
        self.client.force_authenticate(self.user)
        count_before = Habit.objects.count()
        self.url = reverse("habits:habit_create")
        self.data = {
            "owner": self.user.id,
            "activity": "Сделать пробежку вечером",
            "time": "22:00",
            "location": "Вокруг дома",
            "is_pleasant": False,
            "linked": "",
            "award": self.award2.id,
            "frequency": 1,
            "implementation_time": 120,
            "is_public": False
        }
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.count(), count_before + 1)
        self.assertEqual(response.json()["activity"], "Сделать пробежку вечером")

    def test_detail_habit(self):
        """
        Тест на просмотр привычки.
        """
        self.client.force_authenticate(self.user)
        self.url = reverse("habits:habit_detail", args=(self.habit1.pk,))

        response = self.client.get(self.url)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

    def test_update_habit(self):
        """
        Тест на обновление привычки.
        """
        self.client.force_authenticate(self.user)
        self.url = reverse("habits:habit_update", args=(self.habit1.pk,))
        self.data = {
            "activity": "Почитать про нейросети",
            "is_pleasant": True
        }
        response = self.client.patch(self.url, self.data)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            response.json()["activity"], "Почитать про нейросети"
        )
        self.assertEqual(
            response.json()["is_pleasant"], True
        )

    def test_delete_lesson(self):
        """
        Тест на удаление привычки.
        """
        self.client.force_authenticate(self.user)
        self.url = reverse("habits:habit_delete", args=(self.habit1.pk,))
        response = self.client.delete(self.url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
