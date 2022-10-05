## October 5, 2022

Today I worked on:
* Paired-programming with Christopher on users_api

Yesterday I got as far as I could on researching and planning how to implement JWTdown into our backend for authentication. The greatest hurdle today was getting our tables to work properly with FastAPI. After writing the files for our queries and routers, we made changes to the docker-compose.yml file to get the tables to finally show up at port 8090. Seeing how the user_api was set up, I think setting up authentication will be simple barring any errors to work through.

## October 4, 2022

Today I worked on:
* Going over foodies.sql example to better understand the file structure
* Researched authentication with JWTdown for FastAPI

I wanted to understand how to create endpoints for Login and Logout functionality for users and how tokens will be used to give permission or lack-there-of for the various microservices and features within them. Once the postgres is set up and models are being created I will be able to start implementing the code to offer these permissions.

## October 3, 2022

Today I worked on:
* Cloning down the GitLab repo and going through the previous exploration

While the other teammates worked on the third form normalized tables, I went back and tried to get a better understanding of how these table relationships work in Postgres.