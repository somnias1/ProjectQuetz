========================
    Recurso Respuestas
========================

recurso POST
------------

    .. http:post:: /api/replies/

    Crea una respuesta en un comentario

    * **Campos obligatorios**

        :Authorization (HEADER): **(token)** Token del usuario
        :comentario_padre: **(int)** ID del comentario a responder
        :texto_respuesta: **(string)** Contenido de la respuesta

    * **Ejemplo de petición**

        .. host:: http

            POST /api/replies/
            Authorization: Token TokenRealMuyReal100
            Content-Type: json

            {
                "comentario_padre": 1,
                "texto_respuesta": "Claro, ya está en curso"
            }

    * **Ejemplos de respuesta**

        .. host:: http

            HTTP/1.1 201 CREATED
            Content-Type: json

            {
                "comentario_padre": 1,
                "fecha_respuesta": "2021-10-28",
                "texto_respuesta": "Claro, ya está en curso"
            }

            HTTP/1.1 400 BAD_REQUEST
            Content-Type: json

            {
                "texto_respuesta": "Este campo es requerido"
            }

            HTTP/1.1 401 UNAUTHORIZED
            Content-Type: json

            {
                "detail": "Las credenciales de autenticación no se proveyeron"
            }


recurso DELETE
--------------

    .. http:delete:: /api/replies/<pk>/

    Elimina una respuesta previamente creada

    * **Campos obligatorios**

        :Authorization (HEADER): **(token)** Token del usuario creador

    * **Ejemplo de petición**

        .. host:: http

            DELETE /api/replies/3/
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



:status 201: Respuesta creada
:status 204: Eliminación de la respuesta completada
:status 400: Valores inválidos
:status 401: Token de autorización inválido
:status 403: Token de autorización no proveído