from rest_framework.pagination import PageNumberPagination


class UserPaginator(PageNumberPagination):
    """
    Пагинатор для вывода ограниченного количества данных на странице.
    """
    page_size = 5
