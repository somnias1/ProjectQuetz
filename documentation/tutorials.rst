========================
    Recurso Tutoriales
========================

recurso POST
------------

    .. http:post:: /api/tutorials/

    Crea un tutorial base, al que luego se añadirán pasos

    * **Campos obligatorios**

        :Authorization (HEADER): **(token)** Token del usuario creador
        :titulo: **(string)** Título del tutorial
        :banner: **(file)** Imagen que representará el tutorial
        :descripcion: **(string)** Una descripcion corta de los temas que se cubrirán en el tutorial
        :nivel: **(string)** Nivel de dificultad del tutorial, las 3 opciones son bas, med, adv

    * **Campos opcionales**

        :sensible: **(boolean)** Atributo de restricción de edad (Falso si no se selecciona)

    * **Ejemplo de petición**

        .. host:: http

            POST /api/tutorials/
            Authorization: Token TokenRealMuyReal100
            Content-Type: json

            {
                "titulo": "Como hacer aguapanela",
                "banner": "aguapanela.png"
                "descripcion: "Te enseñaré paso a paso cómo realizar una deliciosa aguapanela"
                "nivel": "bas"
            }

    * **Ejemplos de respuesta**

        .. host:: http

            HTTP/1.1 201 CREATED
            Content-Type: json

            {
                "titulo": "Como hacer aguapanela",
                "banner": "http://127.0.0.1:8000/media/tutorials/aguapanela.jpg"
                "descripcion: "Te enseñaré paso a paso cómo realizar una deliciosa aguapanela"
                "nivel": "bas",
                "sensible": false,
                "paso_Tutorial": []
            }

            HTTP/1.1 400 BAD_REQUEST
            Content-Type: json

            {
                "banner": "No se envió ningún archivo"
            }

            HTTP/1.1 401 UNAUTHORIZED
            Content-Type: json

            {
                "detail": "Las credenciales de autenticación no se proveyeron"
            }

Recurso GET
-----------
    .. http:get:: /api/tutorials/

    Recibe la lista de tutoriales 

    * **Ejemplo de petición**

        .. host:: http

            GET /api/tutorials/
            Content-Type: None

    * **Ejemplos de respuesta**

        .. host:: http

            HTTP/1.1 200 OK
            Content-Type: json

            [
                {
                    "titulo": "Creación de un buen tutorial",
                    "banner": "http://127.0.0.1:8000/media/tutorials/Quetz2.png",
                    "descripcion": "En este tutorial aprenderemos cómo se crea un tutorial apropiadamente",
                    "nivel": "bas",
                    "sensible": false,
                    "paso_Tutorial": [
                        {
                            "numero_paso": 1,
                            "imagen": "http://localhost:8000/media/steps/12-222683488_9hl70gr.jpg",
                            "descripcion": "Para la creación de un tutorial es importante saber que cada paso es importante, no debes correr antes de caminar, ni apresurar las acciones que deben ser tomadas\r\nIntenta que cada paso sea específico, centrado en lo que debe hacerse en ese instante, si consideras que un paso es demasiado grande, intenta partirlo en múltiples pasos más pequeños",
                            "adjunto": null
                        }
                    ]
                },
                {
                    "titulo": "Cosas",
                    "banner": "http://127.0.0.1:8000/media/tutorials/Quetz2_uCfjJL9.png",
                    "descripcion": "Cosas que se hacen",
                    "nivel": "bas",
                    "sensible": false,
                    "paso_Tutorial": []
                },
                {
                    "titulo": "Como hacer aguapanela",
                    "banner": "http://127.0.0.1:8000/media/tutorials/aguapanela.jpg",
                    "descripcion": "Te enseñaré paso a paso como realizar una deliciosa aguapanela",
                    "nivel": "bas",
                    "sensible": false,
                    "paso_Tutorial": []
                }
            ]


    .. http:get:: /api/tutorials/<pk>

    Recibe la información de un tutorial en específico

    * **Ejemplo de petición**

        .. host:: http

            GET /api/tutorials/1
            Content-Type: None

    * **Ejemplos de respuesta**

        .. host:: http

            HTTP/1.1 200 OK
            Content-Type: json

            {
                "titulo": "Creación de un buen tutorial",
                "banner": "http://127.0.0.1:8000/media/tutorials/Quetz2.png",
                "descripcion": "En este tutorial aprenderemos cómo se crea un tutorial apropiadamente",
                "nivel": "bas",
                "sensible": false,
                "paso_Tutorial": [
                    {
                        "numero_paso": 1,
                        "imagen": "http://localhost:8000/media/steps/12-222683488_9hl70gr.jpg",
                        "descripcion": "Para la creación de un tutorial es importante saber que cada paso es importante, no debes correr antes de caminar, ni apresurar las acciones que deben ser tomadas\r\nIntenta que cada paso sea específico, centrado en lo que debe hacerse en ese instante, si consideras que un paso es demasiado grande, intenta partirlo en múltiples pasos más pequeños",
                        "adjunto": null
                    }
                ]
            }

            HTTP/1.1 404 NOT FOUND
            Content-Type: json

            {
                "detail": "No encontrado."
            }

recurso DELETE
--------------

    .. http:delete:: /api/tutorials/<pk>

    Elimina un tutorial previamente creado

    * **Campos obligatorios**

        :Authorization (HEADER): **(token)** Token del usuario creador

    * **Ejemplo de petición**

        .. host:: http

            DELETE /api/tutorials/10
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

recurso PATCH
-------------

    .. http:patch:: /api/tutorials/<pk>/

    Actualiza parcialmente un tutorial creado

    * **Campos obligatorios**

        :Authorization (HEADER): **(token)** Token del usuario creador

    * **Campos opcionales**

        :titulo: **(string)** Título del tutorial
        :banner: **(file)** Imagen que representará el tutorial
        :descripcion: **(string)** Una descripcion corta de los temas que se cubrirán en el tutorial
        :nivel: **(string)** Nivel de dificultad del tutorial, las 3 opciones son bas, med, adv
        :sensible: **(boolean)** Atributo de restricción de edad (Falso si no se selecciona)

    * **Ejemplo de petición**

        .. host:: http

            PATCH /api/tutorials/1/
            Authorization: Token TokenRealMuyReal100
            Content-Type: json

            {
                "titulo": "Cómo hacer aguapanela"
            }

    * **Ejemplos de respuesta**

        .. host:: http

            HTTP/1.1 200 OK
            Content-Type: json

            {
                "titulo": "Cómo hacer aguapanela",
                "banner": "http://127.0.0.1:8000/media/tutorials/aguapanela.jpg"
                "descripcion: "Te enseñaré paso a paso cómo realizar una deliciosa aguapanela"
                "nivel": "bas",
                "sensible": false,
                "paso_Tutorial": []
            }

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

recurso PUT
-----------

    .. http:put:: /api/tutorials/<pk>/

    Actualiza completamente un tutorial creado

    * **Campos obligatorios**

        :Authorization (HEADER): **(token)** Token del usuario creador
        :titulo: **(string)** Título del tutorial
        :banner: **(file)** Imagen que representará el tutorial
        :descripcion: **(string)** Una descripcion corta de los temas que se cubrirán en el tutorial
        :nivel: **(string)** Nivel de dificultad del tutorial, las 3 opciones son bas, med, adv

    * **Campos opcionales**

        :sensible: **(boolean)** Atributo de restricción de edad (Falso si no se selecciona)

    * **Ejemplo de petición**

        .. host:: http

            PUT /api/tutorials/8/
            Authorization: Token TokenRealMuyReal100
            Content-Type: json

            {
                "titulo": "Cómo hacer aguapanela",
                "banner": "aguapanela2.png"
                "descripcion: "Te enseñaré paso a paso, el cómo realizar una deliciosa aguapanela"
                "nivel": "bas"
                "sensible": True,
                "paso_Tutorial": []
            }

    * **Ejemplos de respuesta**

        .. host:: http

            HTTP/1.1 200 OK
            Content-Type: json

            {
                "titulo": "Cómo hacer aguapanela",
                "banner": "aguapanela2.png"
                "descripcion: "Te enseñaré paso a paso, el cómo realizar una deliciosa aguapanela"
                "nivel": "bas"
                "sensible": true,
                "paso_Tutorial": []
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


:status 200: Petición completada
:status 201: Tutorial creado
:status 204: Eliminación del tutorial completada
:status 400: Valores inválidos
:status 401: Token de autorización inválido
:status 403: Permisos insuficientes para realizar una acción
:status 404: Tutorial no encontrado



