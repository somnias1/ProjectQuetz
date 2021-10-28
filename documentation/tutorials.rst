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
        :nivel: **(string)** Nivel de dificultad del tutorial, las 3 opciones son bas, med, adv}
        :temas_tutorial: **(intlist)** Lista de temas del tutorial, dirigirse a la documentación de temas para más información
        :paso_Tutorial: **(Dictlist)** Lista de diccionarios con los pasos del tutorial, ver documentación de pasos para más información


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
                "nivel": "bas",
                "temas_tutorial": [2],
                "paso_Tutorial":
                [
                    {
                        "numero_paso":1,
                        "descripcion": "Primero se debe calcular cuanta aguapanela queremos",
                        "adjunto": "google.com"
                    },
                    {
                        "numero_paso":2,
                        "descripcion": "Despues cortaremos trozos iguales",
                        "imagen": "panelapartida.png"
                    }
                ]
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
                "temas_tutorial": [2],
                "paso_Tutorial":
                [
                    {
                        "numero_paso":1,
                        "descripcion": "Primero se debe calcular cuanta aguapanela queremos",
                        "adjunto": "google.com"
                    },
                    {
                        "numero_paso":2,
                        "descripcion": "Despues cortaremos trozos iguales",
                        "imagen": "panelapartida.png"
                    }
                ]
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
    .. http:get:: /api/tutorials

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
                    "id": 1,
                    "autor": {
                        "id": 3,
                        "username": "Quetz",
                        "foto_perfil": null
                    },
                    "titulo": "Creación de un buen tutorial",
                    "banner": "http://127.0.0.1:8000/media/tutorials/Quetz2.png",
                    "descripcion": "En este tutorial aprenderemos cómo se crea un tutorial apropiadamente",
                    "nivel": "bas",
                    "sensible": false,
                    "temas_tutorial": [
                        {
                            "id": 2,
                            "categoria_tema": "prgm",
                            "nombre_tema": "Angular",
                            "imagen_tema": "https://quetz.s3.us-east-2.amazonaws.com/themes/angular.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVLDANIIR5O6TFGCH%2F20211028%2Fus-east-2%2Fs3%2Faws4_request&X-Amz-Date=20211028T012213Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=a49d29d1f5b5ed374191b2125bbec2513b6943237c3edc450b5ab6413634846b"
                        }
                    ],
                    "fecha_creacion": "2021-10-19"
                },
                {
                    "id": 5,
                    "autor": {
                        "id": 1,
                        "username": "usuarioreal",
                        "foto_perfil": null
                    },
                    "titulo": "Cosas",
                    "banner": "http://127.0.0.1:8000/media/tutorials/Quetz2_uCfjJL9.png",
                    "descripcion": "Cosas que se hacen",
                    "nivel": "bas",
                    "sensible": false,
                    "temas_tutorial": [3],
                    "fecha_creacion": "2021-10-20"
                },
                {
                    "id": 8,
                    "autor": {
                        "id": 3,
                        "username": "Quetz",
                        "foto_perfil": null
                    },
                    "titulo": "Como hacer aguapanela",
                    "banner": "http://127.0.0.1:8000/media/tutorials/aguapanela.jpg",
                    "descripcion": "Te enseñaré paso a paso como realizar una deliciosa aguapanela",
                    "nivel": "bas",
                    "sensible": false,
                    "temas_tutorial": [
                        {
                            "id": 1,
                            "categoria_tema": "tmsc",
                            "nombre_tema": "Lectura de partituras",
                            "imagen_tema": "https://quetz.s3.us-east-2.amazonaws.com/themese/PFP.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVLDANIIR5O6TFGCH%2F20211028%2Fus-east-2%2Fs3%2Faws4_request&X-Amz-Date=20211028T012214Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=301f717b6340fe6354d86b7fe12c82e8f918cb372964a78795b3801a34e1f969"
                        }
                    ],
                    "fecha_creacion": "2021-10-20"
                }
            ]

    .. http:get:: /api/tutorials/?[Query]=value

    Realiza una consulta de los tutoriales que hay
        :search: **(string)** Busca por título o contenido del autor
        :nivel: **(string)** Busca por nivel de dificultad
        :temas_tutorial: **(int)** Busca por id del tema
        :autor: **(int)** Busca por id del autor

    * **Ejemplo de petición**

        .. host:: http

            GET /api/tutorials/
            Query-Param: nivel: bas
            Content-Type: None

    * **Ejemplos de respuesta**

        .. host:: http

            HTTP/1.1 200 OK
            Content-Type: json

            {
                "id": 1,
                "autor": {
                        "id": 3,
                        "username": "Quetz",
                        "foto_perfil": null
                },
                "titulo": "Creación de un buen tutorial",
                "banner": "http://127.0.0.1:8000/media/tutorials/Quetz2.png",
                "descripcion": "En este tutorial aprenderemos cómo se crea un tutorial apropiadamente",
                "nivel": "bas",
                "sensible": false,
                "temas_tutorial": [
                        {
                            "id": 2,
                            "categoria_tema": "prgm",
                            "nombre_tema": "Angular",
                            "imagen_tema": "https://quetz.s3.us-east-2.amazonaws.com/themes/angular.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVLDANIIR5O6TFGCH%2F20211028%2Fus-east-2%2Fs3%2Faws4_request&X-Amz-Date=20211028T012213Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=a49d29d1f5b5ed374191b2125bbec2513b6943237c3edc450b5ab6413634846b"
                        }
                    ],
                "fecha_creacion": "2021-10-18"
            }

            HTTP/1.1 400 BAD_REQUEST
            Content-Type: json

            {
                "nivel": [
                    "Escoja una opción válida. bas1 no es una de las opciones disponibles."
                ]
            }


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
                "autor": {
                        "id": 3,
                        "username": "Quetz",
                        "foto_perfil": null
                },
                "titulo": "Creación de un buen tutorial",
                "banner": "http://127.0.0.1:8000/media/tutorials/Quetz2.png",
                "descripcion": "En este tutorial aprenderemos cómo se crea un tutorial apropiadamente",
                "nivel": "bas",
                "sensible": false,
                "temas_tutorial": [
                        {
                            "id": 2,
                            "categoria_tema": "prgm",
                            "nombre_tema": "Angular",
                            "imagen_tema": "https://quetz.s3.us-east-2.amazonaws.com/themes/angular.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVLDANIIR5O6TFGCH%2F20211028%2Fus-east-2%2Fs3%2Faws4_request&X-Amz-Date=20211028T012213Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=a49d29d1f5b5ed374191b2125bbec2513b6943237c3edc450b5ab6413634846b"
                        }
                    ],
                "paso_Tutorial": [
                    {
                        "numero_paso": 1,
                        "imagen": "http://localhost:8000/media/steps/12-222683488_9hl70gr.jpg",
                        "descripcion": "Para la creación de un tutorial es importante saber que cada paso es importante, no debes correr antes de caminar, ni apresurar las acciones que deben ser tomadas\r\nIntenta que cada paso sea específico, centrado en lo que debe hacerse en ese instante, si consideras que un paso es demasiado grande, intenta partirlo en múltiples pasos más pequeños",
                        "adjunto": null
                    }
                ]
                "comentario_Tutorial": [
                    {
                        "id": 1,
                        "comentador": {
                            "id": 1,
                            "username": "usuarioreal",
                            "foto_perfil": "https://quetz.s3.us-east-2.amazonaws.com/users/E9ww4s2UcAIWCB-.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVLDANIIR5O6TFGCH%2F20211021%2Fus-east-2%2Fs3%2Faws4_request&X-Amz-Date=20211021T012601Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=062e7b79c8d9b3a94682f2644f8d944568e573753a832ab9a5e8ee0bdd88fc70"
                        },
                        "fecha_comentario": "2021-10-03",
                        "texto_comentario": "Un gran tutorial, aprendí a hacer mis propios tutoriales gracias a Quetz"
                    }
                ],
                "fecha_creacion": "2021-10-20"
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
        :temas_tutorial: **(intlist)** Lista de temas del tutorial, dirigirse a la documentación de temas para más información

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
                "temas_tutorial": []
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
        :temas_tutorial: **(intlist)** Lista de temas del tutorial, dirigirse a la documentación de temas para más información

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
                "temas_tutorial": [2],
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
                "temas_tutorial": [2],
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



