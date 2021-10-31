========================
    Recurso Seguidores
========================

Recurso POST
------------

    .. http:post:: /api/users/social/

    Sigue a un usuario

    * **Campos obligatorios**

        
        :Authenticated: **(token)** Información de autenticación del usuario
        :following_user_id: **(integer)** Id del usuario a seguir
        

        * **Ejemplo de petición**

            .. host:: http

                POST /api/users/social
                Content-Type: json

                {
                    "following_user_id": 4
                }

        * **Ejemplos de respuesta**

            .. host:: http http

                HTTP/1.1 201 CREATED
                Content-Type: json

                {
                    "following_user_id": 27,
                    "getfollowingusername": "usuarioadulto",
                    "created": "2021-09-28T20:50:27.973518Z"
                }

                HTTP/1.1 401 UNAUTHORIZED
                Content-Type: json
                {
                    "detail": "Las credenciales de autenticación no se proveyeron."
                }
