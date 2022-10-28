## 10/28/2022
Started the day helping chris with back end bug resolution for forms he was working on, the endpoints were working as expected but redux was causing problems sending the data in the format that the back end was expecting. We ended up changing the routes to make the information that needed to be sent simpler which seemed to resolve the issue. I then started work on a python function that could be called to populate databases for testing purposes, but decided to focus on other things as I began to encounter problems and louise and chris still needed help with some bugs. Helped louise with some troubleshooting of her unit test and continued to help chris with forms issues. Then pair programmed with louise to get cover functionality working and have events display correctly on the team dashboard. 

## 10/27/2022
I started work again on CICD and unit tests, did bug resolution and traced back what was causing errors including environmental variables that needed to be included. Stopped this to make and test some endpoints that louise needed for the front end. Pair programmed with louise to get the swap functionality working on the front end for our MVP. I learned more about how much I hate redux. Finished CICD and got pipeline working for valid tests - both my test and chris' test are working in pipeline.

## 10/26/2022
Spent a few hours looking into unit tests and CICD after I finished fully resolving all the issues with swap internal messaging and data transfer between services. After I got a good grasp on CICD and started implementing tests (trying to anyway) I went over everything I learned with louise and chris, then spent the rest of the day pair programming with louise on the front end to try to implement swaps

## 10/25/2022
Finished all logic for swaps and began troubleshooting. Logic works for queries to get valid swaps and covers, and logic works on main service to swap events and covers but does not yet update through the pub sub properly. Will continue to resolve issues to get this working.

## 10/24/2022
Completed members pub sub and bug fixed/fully tested it, made necessary changes to roles model and endpoints, and started work on the comparison logic for creating swap lists. Ran into trouble with date time object comparisons but figured out I was causing an error in a different way, I learned that timestamp objects from sql automatically get imported as datetime objects to python. I also helped with smaller bug fixes/questions that louise and christopher had about backend stuff.

## 10/20/2022
I finished the base code for the members pub sub though I did not bug test it. I created a few more endpoints for front end requests and then tackled most of the redux endpoint queries for the teams microservice so that those are available for use, though since we have not tried to use them yet we may need to do some troubleshooting/bug fixes.

## 10/19/2022
I spent the day polishing endpoints and adding a few new ones as louise and chris made progress on the front end and needed functionality we had not originally thought of. I bagan work on a pub sub for members in the team microservice that should update the relational table in the monoservice that indexes user's connections to team VO's

## 10/18/2022
I finished the paths and logic for pub sub in the Teams->teamsVO direction. I had to rewrite a few of the endpoints and models to accept the data correctly as well as fix early syntax errors from our early attempts at SQL table manipulation. I also wrote a query to get the teams related to a given user, which required a many to many table that had to be implemented into the teamVO creation to autopopulate. We will also need to create a path for members pub sub to populate the many to many table in monoservice when a member is added to a team. I also added functionality for updating a user so the new password will hash correctly and require authentication.

## 10/17/2022
Louise and I got Pub sub publishing and posting working correctly with two direction authentication for the event->eventVO paths. Creation of an event in fastapi docs on the main monoservice successfully creates that event on the teams microservice as a VO. I refactored the file names for the monoservice to match the style of the teams microservice and be more readable. Also slightly adjusted some models, as well as relocated the models file and updated appropriate imports. I started working on the logic and routes to make a list of events that have availability and shift overlap

## 10/14/2022
Pub sub requests are working with insomnia! We had to get curtis' help with getting auth to pass through the pub sub correctly, but it is working now, we only need to get all the endpoints working perfectly now and we will be done with the hardest part of the back end. 

## 10/13/2022
I worked to get pub sub requests working, ended up needing to work on a long chain of endpoints to get the teams model working so we could test TeamVO pubsub.

## 10/12/2022
I 'finished' the pub sub and related endpoints, set up endpoints to use the new get user functionality chris made so we can create models correctly and utilize authentication. 

## 10/11/2022
I made a pub sub from scratch that should be able to handle pub sub for events->eventVO's and Teams->teamVOs. I had to review the docs for requests and do a little bit of research into how pub sub works but it should be effective after we test it and get rid of any small bugs.

## 10/10/2022
We continued working on endpoints, queries, and models for the teams microservice. We reconsidered some of the variables and removed unneccessary data for some of the models as we worked. We should finish the endpoints and queries tomorrow for the teams microservice and then we will decide how to do the pub/sub for events-> eventsVO

## 10/6/2022
We went over our bounded contexts with curtis, then I pair programmed with Louise to finish all the models for teams and get started on the routes and endpoints for the teams database

## 10/5/2022
I spent a lot of time re watching the fasapi videos because I have felt lost. I then worked on my endpoints for teams and did some reworking of the tables.

## 10/4/2022
helped troubleshoot/looked into how migrations for fastapi work and did bug fixing with louise and siers for a few hours.
set up all of the tables for team microservice, will get them migrated tomorrow

## 10/3/2022
mapped tables for team microservice, tried to follow third normalization protocols.
Added starting issues for the project
I had several AHA moments while making the map that made me reconsider how we may want to design the models for the project. Will discuss with team.





























