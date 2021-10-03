from django.contrib import admin
from admin_views.admin import AdminViews

from django.shortcuts import redirect

# from .models.Greetings import Greeting
from .models import (
    User,
    Tema,
    UserFollowing,
    TemaUsuario,
    Tutorial,
    Pluma,
    TemaTutorial,
    Paso,
    Comentario,
    Respuesta,
)

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
        "last_name",
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
    list_display_links = ("pk", "categoria_tema", "nombre_tema")
    search_fields = [
        "categoria_tema",
        "nombre_tema",
    ]

    list_filter = [
        "categoria_tema",
    ]

    # fields = ("categoria_tema", "nombre_tema", "imagen_tema")


admin.site.register(Tema, TemaAdmin)


class UserFollowingAdmin(admin.ModelAdmin):
    list_display = ("pk", "user_id", "following_user_id")
    list_display_links = ("pk", "user_id", "following_user_id")
    search_fields = [
        "user_id",
        "following_user_id",
    ]

    list_filter = [
        "user_id",
        "following_user_id",
    ]


admin.site.register(UserFollowing, UserFollowingAdmin)


class TemaUsuarioAdmin(admin.ModelAdmin):
    list_display = ("pk", "tema", "usuario")
    list_display_links = ("pk", "tema", "usuario")
    search_fields = [
        "tema",
        "usuario",
    ]

    list_filter = [
        "tema",
    ]


admin.site.register(TemaUsuario, TemaUsuarioAdmin)


class TutorialAdmin(admin.ModelAdmin):
    list_display = ("pk", "titulo", "autor", "sensible")
    list_display_links = ("pk", "titulo", "autor")
    search_fields = [
        # "autor",
        "titulo",
        "nivel",
    ]

    list_filter = ["nivel", "sensible", "autor"]


admin.site.register(Tutorial, TutorialAdmin)


class PlumaAdmin(admin.ModelAdmin):
    list_display = ("pk", "tutorial", "user")
    list_display_links = ("pk", "tutorial", "user")
    search_fields = [
        "tutorial__titulo",
        # "user"
    ]

    list_filter = ["tutorial__titulo", "tutorial__autor", "user"]


admin.site.register(Pluma, PlumaAdmin)


class TutorialTemaAdmin(admin.ModelAdmin):
    list_display = ("pk", "tutorial", "tema")
    list_display_links = ("pk", "tutorial", "tema")
    search_fields = ["tutorial__titulo", "tema__nombre_tema"]

    list_filter = ["tutorial__titulo", "tema__nombre_tema"]


admin.site.register(TemaTutorial, TutorialTemaAdmin)


class PasoAdmin(admin.ModelAdmin):
    list_display = ("pk", "tutorialpadre", "paso")
    list_display_links = ("pk", "tutorialpadre", "paso")
    # search_fields = ["tutorial__titulo", "tema__nombre_tema"]

    list_filter = [
        "tutorialpadre__titulo",
    ]


admin.site.register(Paso, PasoAdmin)


class ComentarioAdmin(admin.ModelAdmin):
    list_display = ("pk", "tutorialpadre", "comentador")
    list_display_links = ("pk", "tutorialpadre", "comentador")
    # search_fields = ["tutorial__titulo", "tema__nombre_tema"]

    list_filter = ["tutorialpadre__titulo", "comentador"]


admin.site.register(Comentario, ComentarioAdmin)


class RespuestaAdmin(admin.ModelAdmin):
    list_display = ("pk", "comentariopadre", "comentadorrespuesta")
    list_display_links = ("pk", "comentariopadre", "comentadorrespuesta")
    # search_fields = ["tutorial__titulo", "tema__nombre_tema"]

    list_filter = ["comentariopadre__comentador", "comentadorrespuesta"]


admin.site.register(Respuesta, RespuestaAdmin)
