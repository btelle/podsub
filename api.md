FORMAT: 1A
HOST: http://podsub.btelle.me/

# podsub

A REST API to subscribe to podcast feeds and retrieve feed entries. Useful as a backing microservice to a podcast app or multi-platform service.

## register [/register]

### Register an account [POST]

+ Request

        {
            "email": "luvpod7235424@gmail.com",
            "password": "a6bd8166d2c3873d"
        }

+ Response 200 (application/json)

        {
            "ok": true,
            "token": "54ec94aeaa644dc1ba6e12850be667f2"
        }

## login [/login]

### Login to an account [POST]

+ Request

        {
            "email": "luvpod7235424@gmail.com",
            "password": "a6bd8166d2c3873d"
        }

+ Response 200 (application/json)

        {
            "ok": true,
            "token": "60178f6e9e404569b844d67614160206"
        }

## podcasts [/podcasts?limit,page]

### Get a list of podcasts [GET]

+ Parameters 
    + limit - maximum number of results to return
    + page - page number

+ Response 200 (application/json)

        {
            "podcasts": [
                {
                    "id": "5b94bd10-4434-4857-a08a-963d74c7ae81",
                    "explicit": true,
                    "description": "The show's description",
                    "image": "https://cdn.stitcher.com/asdf.jpg",
                    "title": "The Podcast Show",
                    "url": "https://stitcher.com/shows/asdf",
                }
            ]
        }

### Add a new podcast subscription [POST]

+ Request

        {
            "url": "https://stitcher.com/asdf"
        }

+ Response 200 (application/json)

        [
            {
                "ok" true, 
                "podcast": 
                {
                    "id": "5b94bd10-4434-4857-a08a-963d74c7ae81",
                    "explicit": true,
                    "description": "The show's description",
                    "image": "https://cdn.stitcher.com/asdf.jpg",
                    "title": "The Podcast Show",
                    "url": "https://stitcher.com/shows/asdf",
                    "episodes": 
                    [
                        {
                            "id": "98y43uiwey-98769yueh-12823",
                            "guid": "asdfsieehuods",
                            "url": "https://cdn.stitcher.com/asdf.mp3",
                            "release_date": "2016-06-27T23:48:05-700",
                            "duration": 2640,
                            "status": "new",
                            "progress": 0
                        }
                    ]
                }
            }
        ]

## podcasts/{id} [/podcasts/{id}]

### Get a podcast [GET]

+ Parameters
    + id -- ID of the podcast to fetch

+ Response 200 (application/json)

        {
            "podcast": [
                {
                    "id": "5b94bd10-4434-4857-a08a-963d74c7ae81",
                    "explicit": true,
                    "description": "The show's description",
                    "image": "https://cdn.stitcher.com/asdf.jpg",
                    "title": "The Podcast Show",
                    "url": "https://stitcher.com/shows/asdf",
                    "episodes": 
                    [
                        {
                            "id": "98y43uiwey-98769yueh-12823",
                            "guid": "asdfsieehuods",
                            "url": "https://cdn.stitcher.com/asdf.mp3",
                            "release_date": "2016-06-27T23:48:05-700",
                            "duration": 2640,
                            "status": "new",
                            "progress": 0
                        }
                    ]
                }
            ]
        }

### Delete a podcast subscription [DELETE]

+ Parameters
    + id -- ID of the podcast to delete

+ Response 200 (application/json)

        {
            "ok": true,
            "message": "Deleted podcast"
        }

## episodes [/episodes?limit,since,page]

### Get recent episodes [GET]

+ Parameters 
    + limit - maximum number of results to return
    + since - minimum timestamp results were created at
    + page - page number

+ Response 200 (application/json)

        [
            {
                "id": "98y43uiwey-98769yueh-12823",
                "guid": "12332",
                "url": "https://cdn.stitcher.com/asdf/12332.mp3",
                "release_date": "2016-06-28T14:17:44-700",
                "duration": 1769,
                "status": "new",
                "progress": 0,
                "podcast":
                {
                    "id": "5b94bd10-4434-4857-a08a-963d74c7ae81",
                    "explicit": true,
                    "description": "The show's description",
                    "image": "https://cdn.stitcher.com/asdf.jpg",
                    "title": "The Podcast Show",
                    "url": "https://stitcher.com/shows/asdf"
                }
            }
        ]

## episodes/{id} [/episodes/{id}]

### Update episode status [PUT]

+ Parameters
    + id -- ID of the episode to update

+ Request

        {
            "status": "in_progress",
            "progress": 774
        }

+ Response 200 (application/json)

        {
            "ok": true,
            "message": "Updated episode"
        }

### Delete episode [DELETE]

+ Parameters
    + id -- ID of the podcast to delete

+ Response 200 (application/json)

        {
            "ok": true,
            "message": "Deleted episode"
        }
