========================
    Recurso Comunicados
========================


recurso POST
------------

    .. http:post:: /api/announces/

    Crea un comunicado

    * **Campos obligatorios**

        :Authorization (HEADER): **(token)** Token del usuario creador
        :contenido: **(string)** Contenido del comunicado

    * **Ejemplo de petición**

        .. host:: http

            POST /api/announces/
            Authorization: Token TokenRealMuyReal100
            Content-Type: json

            {
                "contenido": "Ahora podrán estar al tanto de nuestros anuncios de comunidad. Espérenlos"
            }   

    * **Ejemplos de respuesta**

        .. host:: http

            HTTP/1.1 201 CREATED
            Content-Type: json

            {
                "contenido": "Ahora podrán estar al tanto de nuestros anuncios de comunidad. Espérenlos",
                "fecha_comunicado": "2021-11-14"
            }

            HTTP/1.1 400 BAD_REQUEST
            Content-Type: json

            {
                "contenido": [
                    "Este campo es requerido."
                ]
            }

            HTTP/1.1 401 UNAUTHORIZED
            Content-Type: json

            {
                "detail": "Las credenciales de autenticación no se proveyeron"
            }


Recurso GET
-----------
    .. http:get:: /api/announces/

    Recibe la lista de anuncios

    * **Campos obligatorios**

        :Authorization (HEADER): **(token)** Token de usuario

    * **Ejemplo de petición**

        .. host:: http

            GET /api/announces/
            Authorization: Token TokenRealMuyReal100
            Content-Type: None

    * **Ejemplos de respuesta**

        .. host:: http

            HTTP/1.1 200 OK
            Content-Type: json

            [
                {
                    "id": 1,
                    "comunicador": {
                        "id": 3,
                        "username": "Quetz",
                        "foto_perfil": null
                    },
                    "fecha_comunicado": "2021-11-14",
                    "plumas_comunicados": []
                }
            ]

            HTTP/1.1 401 UNAUTHORIZED
            Content-Type: json

            {
                "detail": "Las credenciales de autenticación no se proveyeron"
            }


recurso DELETE
--------------

    .. http:delete:: /api/announces/<pk>

    Elimina un anuncio previamente creado

    * **Campos obligatorios**

        :Authorization (HEADER): **(token)** Token del usuario creador

    * **Ejemplo de petición**

        .. host:: http

            DELETE /api/announces/2
            Authorization: Token TokenRealMuyReal100
            Content-Type: None

    * **Ejemplos de respuesta**

        .. host:: http

            HTTP/1.1 204 NO CONTENT
            Content-Type: None

            HTTP/1.1 401 UNAUTHORIZED
            Content-Type: json

            {
                "detail": "Las credenciales de autenticación no se proveyeron"
            }

            HTTP/1.1 403 FORBIDDEN
            Content-Type: json

            {
                "detail": "Usted no tiene permiso para realizar esta acción."
            }

            HTTP/1.1 404 NOT FOUND
            Content-Type: json

            {
                "detail": "No encontrado."
            }


recurso EMPLUMAR
----------------


    .. http:post:: /api/announces/feathers/emplumar/

    Añade una pluma a un comunicado

    * **Campos obligatorios**

        :Authorization (HEADER): **(token)** Token del usuario
        :comunicado: **(int)** ID del comunicado a emplumar

    * **Ejemplo de petición**

        .. host:: http

            POST /api/announces/feathers/emplumar/
            Authorization: Token TokenRealMuyReal100
            Content-Type: json

            {
                "comunicado": 1
            }

    * **Ejemplos de respuesta**

        .. host:: http

            HTTP/1.1 200 OK
            Content-Type: json

            {
                "Exito": "Comunicado emplumado correctamente"
            }

            HTTP/1.1 400 BAD_REQUEST
            Content-Type: json

            {
                "Error": "Comunicado inválido"
            }

            HTTP/1.1 401 UNAUTHORIZED
            Content-Type: json

            {
                "Error": "Requiere sesión activa"
            }

recurso DESPLUMAR
-----------------


    .. http:post:: /api/announces/feathers/desplumar/

    Añade una pluma a un comunicado

    * **Campos obligatorios**

        :Authorization (HEADER): **(token)** Token del usuario
        :tutorial: **(int)** ID del comunicado a desplumar

    * **Ejemplo de petición**

        .. host:: http

            POST /api/announces/feathers/desplumar/
            Authorization: Token TokenRealMuyReal100
            Content-Type: json

            {
                "comunicado": 1
            }

    * **Ejemplos de respuesta**

        .. host:: http

            HTTP/1.1 200 OK
            Content-Type: json

            {
                "Exito": "Comunicado desplumado correctamente"
            }

            HTTP/1.1 400 BAD_REQUEST
            Content-Type: json

            {
                "Error": "Comunicado inválido"
            }

            HTTP/1.1 401 UNAUTHORIZED
            Content-Type: json

            {
                "Error": "Requiere sesión activa"
            }


