========================
    Recurso Usuarios
========================

Recurso LOGIN
-------------

    .. http:post:: /api/users/login/

    Inicia sesión con credenciales de usuario

    * **Campos obligatorios**

        :username: **(string)** Nombre de usuario
        :password: **(string)** Contraseña del usuario

    * **Ejemplo de petición**

        .. host:: http

            POST /api/users/login/
            Content-Type: json

            {
                "username": "usuariosprueba",
                "password": "usuariosprueba"
            }

    * **Ejemplos de respuesta** 

        .. host:: http

            HTTP/1.1 201 CREATED
            Content-Type: json

            {
                "user": {
                        "username": "usuariosabado3",
                        "last_login": "2021-09-18",
                        "email": "usuariosabado3@sabado.com",
                        "fecha_registro": "2021-09-18",
                        "fecha_nacimiento": "2005-01-31",
                        "institucion_educativa": null,
                        "idiomas": [],
                        "ubicacion": null,
                        "facebookurl": null,
                        "twitterurl": null,
                        "youtubeurl": null,
                        "instagramurl": null,
                        "adulto": false,
                        "foto_perfil": null,
                        "following": [],
                        "tutorial_Usuario": []
                },
                "access_token": "3076c51dad376c39984fef4e9ce9a8167e26c6f4"
            }

            HTTP/1.1 400 BAD_REQUEST
            Content-Type: json

            {
                "non_field_errors": [
                    "Credenciales incorrectas"
                ]
            }

Recurso SIGNUP
--------------

    .. http:post:: /api/users/signup/

    Realiza el registro de un usuario

    * **Campos obligatorios**

        :username: **(string)** Nombre de usuario
        :password: **(string)** Contraseña del usuario
        :password_confirmation: **(string)** Verificación de la contraseña del usuario
        :fecha_nacimiento: **(date)** Fecha de nacimiento del usuario en formato yyyy-mm-dd
        :email: **(email)** Correo del usuario en formato usuario@organizacion.tipo

    * **Ejemplo de petición**

        .. host:: http

            POST /api/users/signup/
            Content-Type: json

            {
                "username": "usuario",
                "password": "contraseñausuario",
                "password_confirmation": "contraseñausuario",
                "fecha_nacimiento": "2000-06-01",
                "email": "email@usuario.com"
            }

    * **Ejemplos de respuesta** 

        .. host:: http

            HTTP/1.1 201 CREATED
            Content-Type: json

            {
                "user": {
                    "username": "usuario",
                    "last_login": null,
                    "email": "email@usuario.com",
                    "fecha_registro": "2021-09-24",
                    "fecha_nacimiento": "2000-06-01",
                    "institucion_educativa": null,
                    "idiomas": null,
                    "ubicacion": null,
                    "facebookurl": null,
                    "twitterurl": null,
                    "youtubeurl": null,
                    "instagramurl": null,
                    "adulto": true,
                    "foto_perfil": null,
                    "following": [],
                    "tutorial_Usuario": []  
                },
                "access_token": "0392eec65f1bc00f0deea7dada1c00cf4a753873"
            }

            HTTP/1.1 400 BAD_REQUEST
            Content-Type: json

            {
                "username": [
                    "Este campo debe ser único."
                ],
                "email": [
                    "Este campo debe ser único."
                ]
            }  

Recurso WATCH
-------------

    .. http:get:: /api/users/watch/?username=<username>

    Ve la información de un usuario

    * **Campos obligatorios**

        :username: **(string)** Nombre de usuario a consultar

    * **Ejemplo de petición**

        .. host:: http

            GET /api/users/watch/?username=usuarioreal
            Content-Type: None
            Parameters: username=usuarioreal

    * **Ejemplos de respuesta** 

        .. host:: http

            HTTP/1.1 200 OK
            Content-Type: json

            {
                "username": "usuarioreal",
                "last_login": "2021-09-18",
                "email": "usuarioreal@realidad.com",
                "fecha_registro": "2021-09-18",
                "fecha_nacimiento": "2000-01-22",
                "institucion_educativa": null,
                "idiomas": null,
                "ubicacion": null,
                "facebookurl": null,
                "twitterurl": null,
                "instagramurl": null,
                "youtubeurl": null,
                "adulto": true,
                "foto_perfil": null,
                "following": [
                    {
                        "following_user_id": 3,
                        "getfollowingusername": "Quetz",
                        "created": "2021-10-31T21:23:17.002124Z"
                    }
                ],
                "temas_seguidos": [
                    3
                ],
                "tutorial_Usuario": [
                    {
                        "id": 5,
                        "titulo": "Cosas",
                        "banner": "/media/tutorials/Quetz2_uCfjJL9.png",
                        "descripcion": "Cosas que se hacen",
                        "nivel": "bas",
                        "sensible": false,
                        "fecha_creacion": "2021-10-19"
                    }
                ]
            }

            HTTP/1.1 301 REDIRECT
            HTTP/1.1 200 OK
            Content-Type: json

            {
                "id": 1,
                "username": "usuarioreal",
                "last_login": "2021-09-18",
                "email": "usuarioreal@realidad.com",
                "fecha_registro": "2021-09-18",
                "fecha_nacimiento": "2000-01-22",
                "institucion_educativa": null,
                "idiomas": null,
                "ubicacion": null,
                "facebookurl": null,
                "twitterurl": null,
                "youtubeurl": null,
                "instagramurl": null,
                "adulto": true,
                "foto_perfil": null,
                "following": [],
                "tutorial_Usuario": [
                    {
                        "id": 1,
                        "titulo": "Cosas",
                        "banner": "/media/tutorials/Quetz2_uCfjJL9.png",
                        "descripcion": "Cosas que se hacen",
                        "nivel": "bas",
                        "sensible": false,
                        "fecha_creacion": "2021-10-19"
                    }
                ]
            }

            HTTP/1.1 400 BAD_REQUEST
            Content-Type: json

            {
                "Error": "Username inválido"
            } 

Recurso PROFILE
---------------

    .. http:get:: /api/users/profile

    Ve la información del usuario activo

    * **Campos obligatorios**

        :Authorization: **(token)** Token del usuario


    * **Ejemplo de petición**

        .. host:: http

            GET /api/users/profile
            Content-Type: None
            Authorization: Token d227f1551ed6e778dc021d14ed85fc5808a131xx

    * **Ejemplos de respuesta** 

        .. host:: http

            HTTP/1.1 200 OK
            Content-Type: json

            {
                "id": 1,
                "username": "usuarioreal",
                "last_login": "2021-09-18",
                "email": "usuarioreal@realidad.com",
                "fecha_registro": "2021-09-18",
                "fecha_nacimiento": "2000-01-22",
                "institucion_educativa": null,
                "idiomas": null,
                "ubicacion": null,
                "facebookurl": null,
                "twitterurl": null,
                "youtubeurl": null,
                "instagramurl": null,
                "adulto": true,
                "foto_perfil": null,
                "following": [
                    {
                        "following_user_id": {
                            "id": 3,
                            "username": "Quetz",
                            "foto_perfil": null
                        },
                        "created": "2021-10-31T21:23:17.002124Z"
                    }
                ],
                "temas_seguidos": [
                    3
                ],
                "tutorial_Usuario": [
                    {
                        "id": 5,
                        "titulo": "Cosas",
                        "banner": "/media/tutorials/Quetz2_uCfjJL9.png",
                        "descripcion": "Cosas que se hacen",
                        "nivel": "bas",
                        "sensible": false,
                        "fecha_creacion": "2021-10-19"
                    }
                ]
            }


            HTTP/1.1 400 BAD_REQUEST
            Content-Type: json

            {
                "Error": "Requiere sesión activa"
            } 

Recurso PROFILEUPDATE
---------------------

    .. http:patch:: /api/users/profileupdate/

    Actualiza la información del usuario activo

    * **Campos obligatorios**

        :Authorization: **(token)** Token del usuario
    
    * **Campos opcionales**
        :email: **(string)** Email del usuario
        :institucion_educativa: **(string)** Institución educativa del usuario
        :idiomas: **(string)** Idiomas del usuario
        :ubicacion: **(string)** Ubicación del usuario
        :facebookurl: **(string)** URL del perfil de Facebook del usuario
        :twitterurl: **(string)** URL del perfil de Twitter del usuario
        :youtubeurl: **(string)** URL del perfil de YouTube del usuario
        :instagramurl: **(string)** URL del perfil de Instagram del usuario
        :foto_perfil: **(file)** Foto de perfil del usuario

    * **Idiomas disponibles**
        :en: Inglés
        :es: "Español
        :fr: "Francés
        :de: "Alemán
        :cn: "Chino
        :jp: "Japonés
        :it: "Italiano
        :pt: "Portugués


    * **Ejemplo de petición**

        .. host:: http

            PATCH /api/users/profileupdate/
            Content-Type: json
            Authorization: Token 0392eec65f1bc00f0deea7dada1c00cf4a753xx

            {
                "email": "perfilde@usuario.com",
                "institucion_educativa": "UTP",
                "idiomas": "cn",
                "ubicacion": "Pereira",
                "instagramurl": "instagram.com/quetzapp01/",
            }

    * **Ejemplos de respuesta** 

        .. host:: http

            HTTP/1.1 200 OK
            Content-Type: json

            {
                "Exito": "Perfil actualizado correctamente"
            }


            HTTP/1.1 400 BAD_REQUEST
            Content-Type: json

            {
                "Error": "Requiere sesión activa"
            }  

Recurso LOGOUT
--------------

    .. http:get:: /api/users/logout/

    Cierra la sesión activa

    * **Campos obligatorios**

        :Authorization: **(token)** Token del usuario

    * **Ejemplo de petición**

        .. host:: http

            GET /api/users/logout/
            Content-Type: None
            Authorization: Token 4bb5315c61eae164656d2765b46a5447073d09b5

    * **Ejemplos de respuesta** 

        .. host:: http

            HTTP/1.1 200 OK
            Content-Type: json

            {
                "Éxito": "Sesión cerrada correctamente"
            }

            HTTP/1.1 401 UNAUTHORIZED
            Content-Type: json

            {
                "detail": "Las credenciales de autenticación no se proveyeron"
            }

Recurso SEGUIR TEMA
-------------------

    .. http:post:: /api/users/followthemes/

    Agrega temas a los seguidos por el usuario

    * **Campos obligatorios**

        :Authorization: **(token)** Token del usuario
        :temas_seguidos: **(intlist)** Lista de temas que el usuario quiere seguir

    * **Ejemplo de petición**

        .. host:: http

            POST /api/users/followthemes/
            Content-Type: json
            Authorization: Token 4bb5315c61eae164656d2765b46a5447073d09b5

            {
                "temas_seguidos": [
                    1, 2
                ]
            }

    * **Ejemplos de respuesta** 

        .. host:: http

            HTTP/1.1 200 OK
            Content-Type: json

            {
                "Éxito": "Temas seguidos correctamente"
            }

            HTTP/1.1 401 UNAUTHORIZED
            Content-Type: json

            {
                "detail": "Las credenciales de autenticación no se proveyeron"
            }

Recurso NOTIFICACIONES
----------------------

    .. http:get:: /api/users/notifications/

    Visualiza las notificaciones del usuario 

    * **Campos obligatorios**

        :Authorization: **(token)** Token del usuario

    * **Explicación grupos**

        :notificacioncreaciontutorial_set: Notificaciones de tutoriales creados por los usuarios seguidos
        :followers: Notificaciones de seguidores nuevos
        :notificacioncreacioncomunicado_set: Notificaciones de comunicados creados por los usuarios seguidos
        :autor_tutorial_comentado: Notificaciones de comentarios en los tutoriales propios
        :comunicador_comunicado_comentado: Notificaciones de comentarios en los comunicados propios
        :comentador_comentario: Notificaciones de respuestas en los comentarios propios
        :notificacionplumatutorial_autor: Notificaciones de plumas en los tutoriales propios
        :notificacionplumacomunicado_comunicador: Notificaciones de plumas en los comunicados propios
        :notificacionplumacomentario_comentador: Notificaciones de plumas en los comentarios proios

    * **Ejemplo de petición**

        .. host:: http

            GET /api/users/notifications/
            Content-Type: None
            Authorization: Token 4bb5315c61eae164656d2765b46a5447073d0

    * **Ejemplos de respuesta** 

        .. host:: http

            HTTP/1.1 200 OK
            Content-Type: json

            {
                "notificacioncreaciontutorial_set": [
                {
                    "tutorial": {
                        "id": 35,
                        "autor": {
                            "id": 3,
                            "username": "Quetz",
                            "foto_perfil": null
                        },
                        "titulo": "Tutorial con notificaciones"
                    },
                    "fecha_notificacion": "2021-11-24T21:03:45.894016Z"
                }
                ],
                "followers": [
                    {
                    "user_id": {
                        "id": 2,
                        "username": "ni monda perez",
                        "foto_perfil": "https://quetz.s3.us-east-2.amazonaws.com/users/basic.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVLDANIIR5O6TFGCH%2F20211125%2Fus-east-2%2Fs3%2Faws4_request&X-Amz-Date=20211125T185840Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=6fbecc682d69eab455020055ff94d385fb3697d7b71d674f9ba54f0aa2f7430a"
                    },
                    "created": "2021-09-28T19:16:32.623156Z"
                }
                ],
                "notificacioncreacioncomunicado_set": [
                    {
                        "comunicado": {
                            "id": 4,
                            "comunicador": {
                                "id": 3,
                                "username": "Quetz",
                                "foto_perfil": null
                            }
                        },
                        "fecha_notificacion": "2021-11-25T20:42:23.086684Z"
                    }
                ],
                "autor_tutorial_comentado": [
                    {
                        "tutorial": 1,
                        "titulo_tutorial": "Creación de un buen tutorial",
                        "comentario": {
                            "id": 9,
                            "comentador": {
                                "id": 32,
                                "username": "usuario",
                                "foto_perfil": null
                            }
                        },
                        "fecha_notificacion": "2021-11-25T21:49:03.900756Z"
                    }
                ],
                "comunicador_comunicado_comentado": [
                    {
                        "comunicado": 4,
                        "titulo_tutorial": "Creación de un buen tutorial",
                        "comentario": {
                            "id": 3,
                            "comentador": {
                                "id": 32,
                                "username": "usuario",
                                "foto_perfil": null
                            }
                        },
                        "fecha_notificacion": "2021-11-25T22:25:33.359139Z"
                    }
                ],
                "comentador_comentario": [
                    {
                        "tutorial": 5,
                        "comentario": 4,
                        "respuesta": {
                            "id": 9,
                            "comentador_respuesta": {
                                "id": 32,
                                "username": "usuario",
                                "foto_perfil": null
                            }
                        },
                        "fecha_notificacion": "2021-11-26T21:53:01.946795Z"
                    }
                ],
                "notificacionplumatutorial_autor": [
                    {
                        "tutorial": 1,
                        "emplumador": {
                                "id": 32,
                                "username": "usuario",
                                "foto_perfil": null
                            },
                        "fecha_notificacion": "2021-11-28T15:29:22.436254Z"
                    }
                ],
                "notificacionplumacomunicado_comunicador": [
                    {
                        "comunicado": 1,
                        "emplumador": {
                                "id": 32,
                                "username": "usuario",
                                "foto_perfil": null
                            },
                        "fecha_notificacion": "2021-11-28T15:57:54.544313Z"
                    }
                ],
                "notificacionplumacomentario_comentador": [
                    {
                        "tutorial": 5,
                        "comentario": 4,
                        "emplumador": {
                                "id": 32,
                                "username": "usuario",
                                "foto_perfil": null
                            },
                        "fecha_notificacion": "2021-11-28T16:22:12.313457Z"
                    }
                ]

            }

            HTTP/1.1 400 BAD REQUEST
            Content-Type: json

            {
                "detail": "Requiere sesión activa"
            }

            HTTP/1.1 401 UNAUTHORIZED
            Content-Type: json

            {
                "detail": "Token inválido."
            }


:status 200: Petición completada
:status 201: Usuario o token creado
:status 301: Redirigido debido a una solicitud de watch con una URL mal escrita
:status 400: Valores inválidos
:status 401: Token de autorización inválido
