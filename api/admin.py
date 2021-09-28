from django.contrib import admin

# from .models.Greetings import Greeting
from .models import User, Tema, UserFollowing

# Register your models here.

# admin.site.register(Greeting)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    list_display = (
        "pk",
        "username",
        "email",
    )
    list_display_links = (
        "pk",
        "username",
        "email",
    )

    search_fields = [
        "email",
        "username",
        "first_name",
        "list_name",
    ]

    list_filter = [
        "is_active",
        "is_staff",
        "date_joined",
        # "modified",
    ]

    readonly_fields = [
        "fecha_registro",
        # "modified",
    ]


# @admin.register(Tema)
class TemaAdmin(admin.ModelAdmin):
    list_display = ("pk", "categoria_tema", "nombre_tema")
    search_fields = [
        "categoria_tema",
        "nombre_tema",
    ]

    list_filter = [
        "categoria_tema",
    ]

    # fields = ("categoria_tema", "nombre_tema", "imagen_tema")


admin.site.register(Tema, TemaAdmin)

admin.site.register(UserFollowing)
