from rest_framework.pagination import PageNumberPagination


class HabitPaginator(PageNumberPagination):
    """
    Пагинатор для вывода ограниченного количества данных на странице.
    """
    page_size = 2
