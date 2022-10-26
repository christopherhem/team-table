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

## October 10, 2022

Today I was able to provide some back-end support for the Team's Microservice and worked on the Roles and Permission routers and endpoints. We had a discussion on the complexity of all of these models referencing each other and if implementing a NoSQL database for this situation were a better solution. Despite how tedious setting up the routers/queries with Postgres, we're hoping that in the long run it'll pay off and be beneficial for our application. Nonetheless, it's definitely giving us some repetitions for SQL coding. We all agreed that we're ready for the back-end portion of this application to be done *crosses-fingers*. Definitely ready to start on the front-end with React. 

## October 11, 2022

Worked with Louise and Josh to do some tri-programming for our back-end portion for events and teams. I'm currently stuck on figuring out how to use the JWT for the teams microservice to connect with it. I was able to find a couple of documentation to support this issue but difficulty making those connections. I ended up giving it a rest and started to begin the front-end portion of user forms, specifically signup. 

## October 12, 2022

 It's been nearly 15+ hours invested in this JWT/Teams connection problem... I was able to implement code from the FastAPI/Triaglo docs still couldn't get it to work... So we finally threw in the towel and reached out to Curtis to provide some life-support. Because I was defeated and my team was out brain-power as well. Curtis came in and helped us solve the issue within 30 minutes with probably three lines of code! Amazing. Overall, glad I was on the right track.

## October 13, 2022

Today I was able to focus a bit more on design and front end tasks. Definitely a different pace compared to back-end programming, which is kind of nice. We were in the talks of possibly converting to a monolith but thankfully Louise and Josh have been very diligent and hardworking on trying to make all the connections. Currently running with a 3 person team appears to be a challenge the past couple days, but we're pushing along! Onwards! 

## October 14, 2022

Starting to feel somewhat the pressure of whether or not we're on track with our project, I was having difficult deciding on what kind of approach to go with our front-end. I initially was thinking a carousel would be nice, but I was able to find more of a scrolling style page that may provide a clean and simple experience. I'm currently implementing more CSS for the Home page just because I want to improve CSS skills a bit. It is definitely a head banger activity. 

## October 17, 2022

I finally completed the landing page, forms for signing in and create an account, clean up some of the bigger issues that I came across a couple of days ago. At this moment, currently having a difficulty logging in on the front end as well as small routing issues. Hopefully they will be solved by tomorrow and we can continue on to completing the Dashboard of the application. 

## October 18, 2022

I have finally completed the user login that creates a token for them. It took me nearly all day to finally get it up and running... My brain is once again fried. Not sure how much mental energy I have left to work for the remainder of the evening... I hope tomorrow is a better day. 

## October 19, 2022

More front-end frenzy. Dashboard is slowly coming together, I was able to get some modal forms up and running. Currently having issues with the endpoints. But overall looks pretty cool. Today was a better today. I hope tomorrow is an even better day. Onwards. 


## October 20, 2022

Today was a day full of BUGS. We were finally able to access the teams query and events in order to create both Cover and Swaps! Tomorrow Louise and I will have to grind it out to beautify this product because it's looking quite dull at the moment. Hopefully we dont break anything major again... 

## October 24, 2022

I worked on the dashboard and was able to finally complete it when a user logs in it will redirect them to their User page. I also worked on creating multiple forms such as adding member, adding role, and add team. The endpoints still need work on connecting and rendering into the modal. Overall, learning more and more everyday about React.

## October 25, 2022

Today we found a bug within the dashboard that dealt with a user still logged in. I was able to implement a code that would check if a token was valid for a user that is logged and if it was true, it would render the User's Dashboard otherwise it would display the main landing page. I'm still occasionally making small tweaks to try to beautify the application. Still have a bunch of other stuff we need to add to make it function time is going by so fast...Trying to be better at managing certain problems and not spending so much time on them. 

## October 26, 2022

