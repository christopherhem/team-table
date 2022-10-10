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
