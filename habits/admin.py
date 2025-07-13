from django.contrib import admin

from habits.models import Award, Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ("id", "owner", "activity", "location", "time", "award", "linked", "is_public")
    list_filter = ("id", "owner", "activity", "location", "time", "award", "linked", "is_public")
    search_fields = ("id", "owner", "activity", "location", "time", "award", "linked", "is_public")


@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ("id", "award",)
    list_filter = ("id", "award",)
    search_fields = ("award",)
