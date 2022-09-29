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


### LANDING PAGE - USER LOGGED IN

* Endpoint path: /users/??????? WHAT WILL THIS BE?
* Endpoint method: GET

* Headers:
  * Authorization: Bearer token

* Response: User Logged in information?
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

### SCHEDULE PAGE - USER EVENT OBJECTS

* Endpoint path: /user/<int:pk>/schedule
* Endpoint method: GET

* Headers:
  * Authorization: Bearer token

* Response: Displays user logged in schedule
* Response shape (JSON):
    ```json
    {
        "schedule": {
            "event_objects": [], 
    }
}
    ```


### NEW EVENT ON SCHEDULE PAGE - PLEASE REVIEW.. 

* Endpoint path: /user/<int:pk>/event
* Endpoint method: POST

* Headers:
  * Authorization: Bearer token

* Request shape (JSON):
    ```json 
    {
        "collaboration_ref": number,
        "collaboration_role": string,
        "start_time": string,
        "end_time": string,
    }

    ```
* Response: Created an event 
* Response shape (JSON):
    ```json
    {
        "collaboration_ref": number,
        "start_time": string,
        "end_time": string,
    }
    ```


### NEW SWAP REQUEST ON SCHEDULE PAGE

* Endpoint path: /user/<int:pk>/swap
* Endpoint method: POST

* Headers:
  * Authorization: Bearer token

* Request shape (JSON):
    ```json
    «JSON-looking thing that has the
    keys and types in it»
    ```

* Response: «Human-readable description
            of response»
* Response shape (JSON):
    ```json
    «JSON-looking thing that has the
    keys and types in it»
    ```


### EDIT ACCOUNT PROFILE PAGE

* Endpoint path: /users/<int:pk>
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
   
* Response: User Logged in information?
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


### Collaboration Page    

* Endpoint path: /collaboration/<int:pk>/users/
* Endpoint method: GET

* Headers:
  * Authorization: Bearer token

* Response: Collaboration page information
* Response shape (JSON):
    ```json
    {
        {
            "users": [],
        }

    }
    ```