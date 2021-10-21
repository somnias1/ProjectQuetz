========================
    Recurso Comentarios
========================

recurso POST
------------

    .. http:post:: /api/comments/

    Crea un paso en un tutorial

    * **Campos obligatorios**

        :Authorization (HEADER): **(token)** Token del usuario
        :tutorial_padre: **(int)** ID del tutorial a comentar
        :texto_comentario: **(string)** Contenido del comentario

    * **Ejemplo de petición**

        .. host:: http

            POST /api/comments/
            Authorization: Token TokenRealMuyReal100
            Content-Type: json

            {
                "tutorial_padre": 5,
                "texto_comentario": "El equipo Quetz está ansioso de hacer sus propias galletas"
            }

    * **Ejemplos de respuesta**

        .. host:: http

            HTTP/1.1 201 CREATED
            Content-Type: json

            {
                "tutorial_padre": 5,
                "fecha_comentario": "2021-10-21",
                "texto_comentario": "El equipo Quetz está ansioso de hacer sus propias galletas"
            }

            HTTP/1.1 400 BAD_REQUEST
            Content-Type: json

            {
                "texto_comentario": "Este campo es requerido"
            }

            HTTP/1.1 401 UNAUTHORIZED
            Content-Type: json

            {
                "detail": "Las credenciales de autenticación no se proveyeron"
            }


recurso DELETE
--------------

    .. http:delete:: /api/comments/<pk>/

    Elimina un paso previamente creado

    * **Campos obligatorios**

        :Authorization (HEADER): **(token)** Token del usuario creador

    * **Ejemplo de petición**

        .. host:: http

            DELETE /api/comments/3/
            Authorization: Token TokenRealMuyReal100
            Content-Type: None

    * **Ejemplos de respuesta**

        .. host:: http

            HTTP/1.1 204 NO CONTENT
            Content-Type: None

            HTTP/1.1 403 FORBIDDEN
            Content-Type: json

            {
                "detail": "Usted no tiene permiso para realizar esta acción."
            }



:status 201: comentario creado
:status 204: Eliminación del comentario completada
:status 400: Valores inválidos
:status 401: Token de autorización inválido
:status 403: Token de autorización no proveído