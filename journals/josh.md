## 10/3/2022
mapped tables for team microservice, tried to follow third normalization protocols.
Added starting issues for the project
I had several AHA moments while making the map that made me reconsider how we may want to design the models for the project. Will discuss with team.


## 10/4/2022
helped troubleshoot/looked into how migrations for fastapi work and did bug fixing with louise and siers for a few hours.
set up all of the tables for team microservice, will get them migrated tomorrow

## 10/5/2022
I spent a lot of time re watching the fasapi videos because I have felt lost. I then worked on my endpoints for teams and did some reworking of the tables.

## 10/6/2022
We went over our bounded contexts with curtis, then I pair programmed with Louise to finish all the models for teams and get started on the routes and endpoints for the teams database

## 10/10/2022
We continued working on endpoints, queries, and models for the teams microservice. We reconsidered some of the variables and removed unneccessary data for some of the models as we worked. We should finish the endpoints and queries tomorrow for the teams microservice and then we will decide how to do the pub/sub for events-> eventsVO

## 10/11/2022
I made a pub sub from scratch that should be able to handle pub sub for events->eventVO's and Teams->teamVOs. I had to review the docs for requests and do a little bit of research into how pub sub works but it should be effective after we test it and get rid of any small bugs.