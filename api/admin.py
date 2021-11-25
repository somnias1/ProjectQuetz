from django.contrib import admin
from admin_views.admin import AdminViews

from django.shortcuts import redirect

# from .models.Greetings import Greeting
from .models import (
    User,
    Tema,
    UserFollowing,
    Tutorial,
    Paso,
    Comentario,
    Respuesta,
    Comunicado,
    ComentarioComunicado,
    NotificacionCreacionTutorial,
    NotificacionComentario,
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


class PasoAdmin(admin.ModelAdmin):
    list_display = ("pk", "tutorial_padre", "numero_paso")
    list_display_links = ("pk", "tutorial_padre", "numero_paso")
    # search_fields = ["tutorial__titulo", "tema__nombre_tema"]

    list_filter = [
        "tutorial_padre__titulo",
    ]


admin.site.register(Paso, PasoAdmin)


class ComentarioAdmin(admin.ModelAdmin):
    list_display = ("pk", "tutorial_padre", "comentador")
    list_display_links = ("pk", "tutorial_padre", "comentador")
    # search_fields = ["tutorial__titulo", "tema__nombre_tema"]

    list_filter = ["tutorial_padre__titulo", "comentador"]


admin.site.register(Comentario, ComentarioAdmin)


class RespuestaAdmin(admin.ModelAdmin):
    list_display = ("pk", "comentario_padre", "comentador_respuesta")
    list_display_links = ("pk", "comentario_padre", "comentador_respuesta")
    # search_fields = ["tutorial__titulo", "tema__nombre_tema"]

    list_filter = ["comentario_padre__comentador", "comentador_respuesta"]


admin.site.register(Respuesta, RespuestaAdmin)


class ComunicadoAdmin(admin.ModelAdmin):
    list_display = ("pk", "comunicador", "fecha_comunicado")
    list_display_links = ("pk", "comunicador", "fecha_comunicado")
    list_filter = ["fecha_comunicado", "comunicador"]


admin.site.register(Comunicado, ComunicadoAdmin)


class ComentarioComunicadoAdmin(admin.ModelAdmin):
    list_display = ("pk", "comunicado_padre", "comentador")
    list_display_links = ("pk", "comunicado_padre", "comentador")
    # search_fields = ["tutorial__titulo", "tema__nombre_tema"]

    list_filter = ["comunicado_padre__comunicador", "comentador"]


admin.site.register(ComentarioComunicado, ComentarioComunicadoAdmin)


class NotificacionTutorialAdmin(admin.ModelAdmin):
    list_display = ("pk", "usuario", "tutorial", "fecha_notificacion")
    list_display_links = ("pk",)


admin.site.register(NotificacionCreacionTutorial, NotificacionTutorialAdmin)


class NotificacionComentarioAdmin(admin.ModelAdmin):
    list_display = ("pk", "autor", "tutorial", "comentario")


admin.site.register(NotificacionComentario, NotificacionComentarioAdmin)
