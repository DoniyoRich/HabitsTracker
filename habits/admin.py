from django.contrib import admin

from habits.models import Habit, HabitLinked, Award


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "activity", "award", "linked", "is_public")
    list_filter = ("id", "user", "activity", "is_public")
    search_fields = ("id", "user", "activity", "is_public")


@admin.register(HabitLinked)
class HabitLinkedAdmin(admin.ModelAdmin):
    list_display = ("id", "activity",)
    list_filter = ("id", "activity",)
    search_fields = ("activity",)


@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ("id", "award",)
    list_filter = ("id", "award",)
    search_fields = ("award",)
