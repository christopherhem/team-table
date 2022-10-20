## 10/18/2022

* I spent today writing out the redux endpoints for the events queries

I took a break from the backend today. I really needed some relief from banging my head against the wall with the pubsub. I got all the the redux endpoints flushed out for the events queries. The only thing I am waiting on is the ability to pass the user's token through each endpoint. Chris has been having a bug in the login that is preventing the token from being returned. We have asked for help but no one has figured out what's going on. Good news is that Josh was able to finalize the teamsvo pubsub and its up and running pefectly!

## 10/17/2022

* I spent today trying to work on the teamsvo pub sub

Today was a big blocker day. I tried to ge the teamsvo pubs sub up and running to no avail. We had too many other issues with our routers and queries that were hindering the progress. I tried to get all of the events q/r working while Josh worked on the teams q/r. We didnt end up finishing today and I am really starting to worry that we are not going to make our MVP on time due to being only 3 members now.

## 10/14/2022

* I spent today fixing all of our endpoints and finished getting our pubsub set up to send events to the teams service

I spent most of my day going through our enpoints on the evvents mircoservice to make sure they all worked. I am currently stuck on how to get teh current user for creating a new event.

## 10/13/2022

* I spent today helping josh with the pub sub.

The pub sub is for the most part ready to be tested but we had a quite a few spaghetti code erors that we had to work through and fix today. I am hoping that we will get it up and running tomorrow. If we can't get it running by tomorrow night we are going to make it a monolith and try to do microservices as a stretch goal.

## 10/12/2022

* I helped josh for most of the day trying to get the pub/sub to start working

I spent most of the day with josh trying to get the pub/sub up and running. We are close but not quite there yet.

## 10/11/2022

* I worked on refactoring the events migration, queries, and routers

I worked with Josh and Christoher today to modify the events service to be fit our needs. We had a small blocker on how to list all of the different events together because they don't have the same fields. We won't know if it works until we have the pub/sub set up to get the teamVO from the teams service.

## 10/10/2022
* I worked on the queries and routers for event_types and teams_types

I worked on these queries today and had to get some help from Josh and Chris to figure out to how do the many-to-many relationship between them. I was not able to get to redoing the event migration file so I will have to work on that tomorrow with my teammates to get it set up correctly. Right now it is not set up for the teams microservice to use and definitely needs to be modified

## 10/06/2022

* I pair coded with Josh to work on the the queries and routers for the teams service

The beginning of the day was spent refactering our file structure on the advice of Curtis to bring our user and event services together and leaving the teams service as its own microservice. Me and Josh spent the rest of the day working on the quries and routers. We figured out that we would need to separate these into individual files for each base table because the files were getting pretty long.

## 10/05/2022

* I fixed my tables and created the routers and queries.

I spent my day modify my tables and getting my routers and queries setup. I had a blocker with getting my FastAPI docs page to show up but Curtis and Jaylon helped me figure it out. Curtis also told me we should not be using multiple FastAPI projects because our project is one bounded context. I talked with part of my team about it, but we weren't all available so I will bring it up tomorrow morning.

## 10/04/2022

* I created the tables for the events microservice in the postgres database

I spent nearly the whole day trying to figure out how the tables connect to the database. I had help from multiple SEIRs (Chad was really helpful!) and my whole team because we did not have adequete information on how to set up the multiple postgres databases and link them with our files that create the tables. I wish we would just focus on the way we are suppose to be structuring our files and writing them it in lectures instead have them set up differently in every lecture.

I was eventually able to get my migrations working and the tables showing up in pg-admin once I figured out how to write the DATABASE_URL in the docker compose and once Conner let me know the difference command I had to use for the docker compose build.

## 10//03/2022

* I created a excalidraw of the events relational database at the 3 form of mormalization

I went over my excalidraw with the team to make sure it all looked correct.

I used the rest of my time to research and better understand how joining tables in sequel actually works and on the exploration. I feel like I definitely havea better understand of their functionality and use cases
