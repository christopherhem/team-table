### LANDING PAGE - CREATE NEW USER!

* Endpoint path: /users
* Endpoint method: POST

* Request shape (form):
    * "username": string,
    * "password": string,
    * "first_name": string,
    * "last_name": string,
    * "email": string,
    * "phone_number": string,
    * "profile_picture": string,

* Response: User Created and a token
* Response shape (JSON):
    ```json
    {
      "account": {
            "username": string,
            "password": string,
            "email": string,
      },
      "token": string
    }
    ```
### LANDING PAGE - USER LOGGED IN

* Endpoint path: /username
* Endpoint method: GET

* Headers:
  * Authorization: Bearer token

* Response: User Logged in information
* Response shape (JSON):
    ```json 
    { 
        "user": { 
            "username": string,
            "password": string,
            "first_name": string,
            "last_name": string,
            "email": string,
            "phone_number": string,
            "profile_picture": string,
        }     
    }
    ```

### LOG IN !
* Endpoint path: /token
* Endpoint method: POST

* Request shape (form):
  * username: string
  * password: string

* Response: Account information and a token
* Response shape (JSON):
    ```json
    {
      "account": {
            "username": string,
            "password": string,
            "email": string,
      },
      "token": string
    }
    ```

### LOG OUT!
* Endpoint path: /token
* Endpoint method: DELETE

* Headers:
  * Authorization: Bearer token

* Response: Always true
* Response shape (JSON):
    ```json
    true
    ```


### User Table Page

* Endpoint path: /users/username/table
* Endpoint method: GET

* Headers:
  * Authorization: Bearer token

* Response: Displays user logged in table
* Response shape (JSON):
    ```json
    {
        "table": {
            "event_objects": [], 
        }
    }
    ```


### Create New Event Page

* Endpoint path: /events
* Endpoint method: POST

* Headers:
  * Authorization: Bearer token

* Request shape (JSON):
    ```json 
    {
        "team_ref": number,
        "team_role": string,
        "start_time": string,
        "end_time": string,
        "username": string,
    }

    ```
* Response: Created an event 
* Response shape (JSON):
    ```json
    {
        "team_ref": number,
        "start_time": string,
        "end_time": string,
    }
    ```

### Create New Swap Page

* Endpoint path: /team/events
* Endpoint method: POST

* Headers:
  * Authorization: Bearer token

* Request shape (JSON):
    ```json
    {
        "event1": {
        },
        "event2": {
        },
    }
    ```
* Response: Created a swap request between users
* Response shape (JSON):
    ```json
    {
        "is_approved": string,
    }
    ```

### Edit Username Profile Page

* Endpoint path: /users/username
* Endpoint method: PUT

* Headers:
  * Authorization: Bearer token

* Request shape (form):
    * "profile_picture": string,
    * "first_name": string,
    * "last_name": string,
    * "email": string,
    * "phone_number": string,
    * "password": string,
   
* Response: User Logged in information
* Response shape (JSON):
    ```json 
    { 
        "user": { 
            "password": string,
            "first_name": string,
            "last_name": string,
            "email": string,
            "phone_number": string,
            "profile_picture": string,
        }     
    }
    ```

### Team Table Page    

* Endpoint path: /team/table
* Endpoint method: GET

* Headers:
  * Authorization: Bearer token

* Response: Team page information
* Response shape (JSON):
    ```json
    {
        "table": {
            "event_objects": [], 
        }
    }
    ```
### Create New Team Page

* Endpoint path: /teams
* Endpoint method: POST

* Request shape (form):
    * "team": string,
    * "description": string,
    * "max_users": number,
    * "is_role_required": boolean,
    * "is_approved_required": boolean,
    * "picture_href": string,
    * "roles": [],

* Response: User created new team 
* Response shape (JSON):
    ```json
    {
        "team": string,
        "description": string,
        "max_users": number,
        "is_role_required": boolean,
        "is_approved_required": boolean,
        "picture_href": string,
        "roles": [],
        "events": [],
        "users": []
    }
    ```