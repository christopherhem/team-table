## Journal requirements:
+ The date of the entry
+ A list of features/issues that you worked on and who you worked with, if applicable
+ A reflection on any design conversations that you had
+ At least one ah-ha! moment that you had during your coding, however small

## October 3, 2022

Today, I worked on:

Organizing and getting files from the startup-repo into our git repository. I also tested and ensured they were properly configured for development on both Mac and Windows. 

Afterwards we then divided and tried to conquer some issues on the git board. I ended up selecting the User microservice and made an attempt to ensure it was in third transitive form before building the api and database. Once completed, the exploration part on third form made slightly more sense. 

I will have to continue to reference back to the explorations when building this Postgres database. However, I feel confident enough to get it started and tackle this issue. Also, I have a very supportive and knowledgeable team to help me as well. 


## October 4, 2022

A slightly stressful day for me. I had some family medical emergencies come up and was having a difficult time focusing. Luckily I was able to re-gain focus and take care Users microservice database connecting it to the rest of the application. I will still need to review all about Postgres once more, it's still a bit cloudy in my mind and having trouble seeing the flow of all things and how they will come together. A bit nervous about learning MongoDB soon because I'm barely getting a grasp on Postgres. Until then... code on. 


## October 5, 2022

I was able to connect the databases and access them through FastAPI. Luckily it wasn't a long fix. We had to modify the ports in our docker compose file and it did the job. I was able to complete a majority of the CRUD except for a specific part when updating a particular entry for the user profile... I was able to get very close but will let this one rest for the night. My brain is fried. I will have to wake up a bit early to tackle this problem again. 

## October 6, 2022

I had a very interesting experience while implementing the JWT OAUTH for User accounts. The frustrating part was having to perform multiple migrations and rebuild with Docker... I was getting different errors that were stating that it was expecting an integer instead of the created email from the user and hash issue with the password. I will let this issue win for tonight... will continue tomorrow. 

## October 7, 2022

No class today. But I was able to solve last night's problem. Hoorah.

