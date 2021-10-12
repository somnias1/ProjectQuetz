========================
    Recurso Pasos
========================

recurso POST
------------

    .. http:post:: /api/tutorials/<pk>/steps

    Crea un paso en un tutorial

    * **Campos obligatorios**

        :Authorization (HEADER): **(token)** Token del usuario creador
        :numero_paso: **(int)** Número del paso
        :descripcion: **(string)** Una descripcion del paso, puede ser tan extensa como se requiera

    * **Campos opcionales**

        :imagen: **(file)** Imagen descriptiva del paso
        :adjunto: **(URL)** URL de referencia en caso de que el usuario considere que se necesite mayor profundidad

    * **Ejemplo de petición**

        .. host:: http

            POST /api/tutorials/5/steps/
            Authorization: Token TokenRealMuyReal100
            Content-Type: json

            {
                "numero_paso": 1,
                "imagen": null,
                "descripcion": "Para hacer cosas primero hay que entender el concepto, así pues, imaginemos que hay una esfera",
                "adjunto": "https://youtu.be/dQw4w9WgXcQ"
            }

    * **Ejemplos de respuesta**

        .. host:: http

            HTTP/1.1 201 CREATED
            Content-Type: json

            {
                "numero_paso": 1,
                "imagen": null,
                "descripcion": "Para hacer cosas primero hay que entender el concepto, así pues, imaginemos que hay una esfera",
                "adjunto": "https://youtu.be/dQw4w9WgXcQ"
            }

            HTTP/1.1 400 BAD_REQUEST
            Content-Type: json

            {
                "numero_paso": ["Introduzca un número entero válido."]
            }

            HTTP/1.1 401 UNAUTHORIZED
            Content-Type: json

            {
                "detail": "Las credenciales de autenticación no se proveyeron"
            }

Recurso GET
-----------
    .. http:get:: /api/tutorials/<pk>/steps

    Recibe la lista de pasos de un tutorial específico

    * **Ejemplo de petición**

        .. host:: http

        GET /api/tutorials/8/steps
        Content-Type: None

    * **Ejemplos de respuesta**

        .. host:: http

            HTTP/1.1 200 OK
            Content-Type: json

            [
                {
                    "numero_paso": 1,
                    "imagen": null,
                    "descripcion": "Para hacer cosas primero hay que entender el concepto, así pues, imaginemos que hay una esfera",
                    "adjunto": "https://youtu.be/dQw4w9WgXcQ"
                }
            ]         

        .. http:get:: /api/tutorials/<pk>/steps/<numero_paso>

            Recibe la información de un paso en específico

            * **Ejemplo de petición**

                .. host:: http

                GET /api/tutorials/8/steps/1
                Content-Type: None

            * **Ejemplos de respuesta**

                .. host:: http

                    HTTP/1.1 200 OK
                    Content-Type: json

                    {
                        "numero_paso": 1,
                        "imagen": null,
                        "descripcion": "Para hacer cosas primero hay que entender el concepto, así pues, imaginemos que hay una esfera",
                        "adjunto": "https://youtu.be/dQw4w9WgXcQ"
                    }

                    HTTP/1.1 404 NOT FOUND
                    Content-Type: json

                    {
                        "detail": "No encontrado."
                    }

recurso DELETE
------------

    .. http:delete:: /api/tutorials/<pk>/steps/<numero_paso>

    Elimina un paso previamente creado

    * **Campos obligatorios**

        :Authorization (HEADER): **(token)** Token del usuario creador

    * **Ejemplo de petición**

        .. host:: http

            DELETE /api/tutorials/5/steps/2
            Authorization: Token TokenRealMuyReal100
            Content-Type: None

    * **Ejemplos de respuesta**

        .. host:: http

            HTTP/1.1 204 NO CONTENT
            Content-Type: None

            HTTP/1.1 404 NOT FOUND
                Content-Type: json

                {
                    "detail": "No encontrado."
                }


recurso PATCH
------------

    .. http:patch:: /api/tutorials/<pk>/steps/<numero_paso>/

    Actualiza parcialmente un paso creado

    * **Campos obligatorios**

        :Authorization (HEADER): **(token)** Token del usuario creador

    * **Campos opcionales**

        :numero_paso: **(int)** Número del paso
        :descripcion: **(string)** Una descripcion del paso, puede ser tan extensa como se requiera
        :imagen: **(file)** Imagen descriptiva del paso
        :adjunto: **(URL)** URL de referencia en caso de que el usuario considere que se necesite mayor profundidad

    * **Ejemplo de petición**

        .. host:: http

            PATCH /api/tutorials/8/steps/1/
            Authorization: Token TokenRealMuyReal100
            Content-Type: json

            {
                "descripcion": "Para hacer cosas primero hay que entender el concepto, así pues, imaginemos que hay un cubo"
            }

    * **Ejemplos de respuesta**

        .. host:: http

            HTTP/1.1 200 OK
            Content-Type: json

            {
                "numero_paso": 1,
                "imagen": null,
                "descripcion": "Para hacer cosas primero hay que entender el concepto, así pues, imaginemos que hay un cubo",
                "adjunto": "https://youtu.be/dQw4w9WgXcQ"
            }

            HTTP/1.1 401 UNAUTHORIZED
            Content-Type: json

            {
                "detail": "Las credenciales de autenticación no se proveyeron"
            }

            HTTP/1.1 404 NOT FOUND
                Content-Type: json

                {
                    "detail": "No encontrado."
                }

recurso PUT
------------

    .. http:put:: /api/tutorials/<pk>/steps/<numero_paso>/

    Actualiza completamente un paso creado

    * **Campos obligatorios**

        :Authorization (HEADER): **(token)** Token del usuario creador
        :numero_paso: **(int)** Número del paso
        :descripcion: **(string)** Una descripcion del paso, puede ser tan extensa como se requiera

    * **Campos opcionales**

        :imagen: **(file)** Imagen descriptiva del paso
        :adjunto: **(URL)** URL de referencia en caso de que el usuario considere que se necesite mayor profundidad

    * **Ejemplo de petición**

        .. host:: http

            PUT /api/tutorials/<pk>/steps
            Authorization: Token TokenRealMuyReal100
            Content-Type: json

            {
                "numero_paso": 2,
                "imagen": null,
                "descripcion": "Para hacer cosas primero hay que entender el concepto, así pues, imaginemos que hay una esfera",
                "adjunto": "https://youtu.be/dQw4w9WgXcQ"
            }

    * **Ejemplos de respuesta**

        .. host:: http

            HTTP/1.1 200 OK
            Content-Type: json

            {
                "numero_paso": 2,
                "imagen": null,
                "descripcion": "Para hacer cosas primero hay que entender el concepto, así pues, imaginemos que hay una esfera",
                "adjunto": "https://youtu.be/dQw4w9WgXcQ"
            }

            HTTP/1.1 400 BAD_REQUEST
            Content-Type: json

            {
                "Nombre_de_Campo": "Este campo es requerido"
            }

            HTTP/1.1 401 UNAUTHORIZED
            Content-Type: json

            {
                "detail": "Las credenciales de autenticación no se proveyeron"
            }

            HTTP/1.1 404 NOT FOUND
            Content-Type: json

            {
                "detail": "No encontrado."
            }


:status 200: Petición completada
:status 201: paso creado
:status 204: Eliminación del paso completada
:status 400: Valores inválidos
:status 401: Token de autorización inválido
:status 404: Paso no encontrado



