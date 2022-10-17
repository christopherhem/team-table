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

## 10/12/2022
I 'finished' the pub sub and related endpoints, set up endpoints to use the new get user functionality chris made so we can create models correctly and utilize authentication. 

## 10/13/2022
I worked to get pub sub requests working, ended up needing to work on a long chain of endpoints to get the teams model working so we could test TeamVO pubsub.

## 10/14/2022
Pub sub requests are working with insomnia! We had to get curtis' help with getting auth to pass through the pub sub correctly, but it is working now, we only need to get all the endpoints working perfectly now and we will be done with the hardest part of the back end. 

## 10/17/2022
Louise and I got Pub sub publishing and posting working correctly with two direction authentication for the event->eventVO paths. Creation of an event in fastapi docs on the main monoservice successfully creates that event on the teams microservice as a VO. I refactored the file names for the monoservice to match the style of the teams microservice and be more readable. Also slightly adjusted some models, as well as relocated the models file and updated appropriate imports. 