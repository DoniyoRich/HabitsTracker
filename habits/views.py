from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView


class HabitsListAPIView(ListAPIView):
    pass


class HabitCreateAPIView(CreateAPIView):
    pass


class HabitDetailAPIView(RetrieveAPIView):
    pass


class HabitUpdateAPIView(UpdateAPIView):
    pass


class HabitDeleteAPIView(DestroyAPIView):
    pass
