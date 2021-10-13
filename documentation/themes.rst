========================
    Recurso Temas
========================

recurso POST
------------

    .. http:post:: /api/themes/

    Crea un tema en una de las categorías disponibles
    :instmsc: Instrumento musical
    :tmsc: Teoría musical
    :prgm: Programación
    :dbj: Dibujo
    :art: Artesanías
    :mnga: Manga - Anime
    :ltr: Literatura
    :coci: Cocina
    :mrk: Marketing
    :dsgn: Diseño
    :otrs: Otros

    * **Campos obligatorios**

        :Authorization (HEADER): **(token)** Token de Administrador
        :categoria_tema: **(string)** Categoría a la que pertenece el tema
        :nombre_tema: **(string)** Nombre del tema
        :imagen_tema: **(file)** Imagen representativa del tema


    * **Ejemplo de petición**

        .. host:: http

            POST /api/themes/
            Authorization: Token TokenRealMuyReal100
            Content-Type: json

            {
                "categoria_tema": "tmsc",
                "nombre_tema": "Lectura de partituras",
                "imagen_tema": "PFP_Partituras.jpg"
            }

    * **Ejemplos de respuesta**

        .. host:: http

            HTTP/1.1 201 CREATED
            Content-Type: json

            {
                "categoria_tema": "tmsc",
                "nombre_tema": "Lectura de partituras",
                "imagen_tema": "PFP_Partituras.jpg"
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

Recurso GET
-----------
    .. http:get:: /api/themes/

    Recibe la lista de temas

    * **Ejemplo de petición**

        .. host:: http

            GET /api/themes/
            Content-Type: None

    * **Ejemplos de respuesta**

        .. host:: http

            HTTP/1.1 200 OK
            Content-Type: json

            [
                {
                    "categoria_tema": "tmsc",
                    "nombre_tema": "Lectura de partitura",
                    "imagen_tema": "http://localhost:8000/media/themese/PFP.jpg"
                }
            ]


    .. http:get:: /api/tutorials/<pk>

    Recibe la información de un tema en específico

    * **Ejemplo de petición**

        .. host:: http

            GET /api/themes/1
            Content-Type: None

    * **Ejemplos de respuesta**

        .. host:: http

            HTTP/1.1 200 OK
            Content-Type: json

            {
                "categoria_tema": "tmsc",
                "nombre_tema": "Lectura de partitura",
                "imagen_tema": "http://localhost:8000/media/themese/PFP.jpg"
            }

            HTTP/1.1 404 NOT FOUND
            Content-Type: json

            {
                "detail": "No encontrado."
            }

recurso DELETE
--------------

    .. http:delete:: /api/themes/<pk>

    Elimina un tema previamente creado

    * **Campos obligatorios**

        :Authorization (HEADER): **(token)** Token de administración

    * **Ejemplo de petición**

        .. host:: http

            DELETE /api/themes/10
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

recurso PATCH
-------------

    .. http:patch:: /api/themes/<pk>/

    Actualiza parcialmente un tema creado

    * **Campos obligatorios**

        :Authorization (HEADER): **(token)** Token de Administrador

    * **Campos opcionales**

        :categoria_tema: **(string)** Categoría a la que pertenece el tema
        :nombre_tema: **(string)** Nombre del tema
        :imagen_tema: **(file)** Imagen representativa del tema

    * **Ejemplo de petición**

        .. host:: http

            PATCH /api/themes/1/
            Authorization: Token TokenRealMuyReal100
            Content-Type: json

            {
                "nombre_tema": "Lectura de partituras"
            }

    * **Ejemplos de respuesta**

        .. host:: http

            HTTP/1.1 200 OK
            Content-Type: json

            {
                "categoria_tema": "tmsc",
                "nombre_tema": "Lectura de partituras",
                "imagen_tema": "http://localhost:8000/media/themes/PFP_Partituras.jpg"
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

    .. http:put:: /api/themes/<pk>/

    Actualiza completamente un tutorial creado

    * **Campos obligatorios**

        :Authorization (HEADER): **(token)** Token de Administrador
        :categoria_tema: **(string)** Categoría a la que pertenece el tema
        :nombre_tema: **(string)** Nombre del tema
        :imagen_tema: **(file)** Imagen representativa del tema

    * **Ejemplo de petición**

        .. host:: http

            POST /api/themes/1/
            Authorization: Token TokenRealMuyReal100
            Content-Type: json

            {
                "categoria_tema": "tmsc",
                "nombre_tema": "Lectura de partituras",
                "imagen_tema": "http://localhost:8000/media/themes/PFP_Partituras2.jpg"
            }

    * **Ejemplos de respuesta**

        .. host:: http

            HTTP/1.1 200 OK
            Content-Type: json

            {
                "categoria_tema": "tmsc",
                "nombre_tema": "Lectura de partituras",
                "imagen_tema": "http://localhost:8000/media/themes/PFP_Partituras2.jpg"
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


:status 200: Petición completada
:status 201: Tema creado
:status 204: Eliminación del tema completada
:status 400: Valores inválidos
:status 401: Token de autorización inválido
:status 403: Permisos insuficientes para realizar una acción
:status 404: Tema no encontrado



