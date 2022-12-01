# TeamTable

<p align="center">
	<img alt="Team Table logo" src="https://i.imgur.com/9v1W8Ct.png">
</p>

## Sample Images 

![Landing Page](https://i.imgur.com/1EgoyEA.png)
![User Dashboard Page](https://i.imgur.com/liZ7s5p.png)
![Team Dashboard Page](https://i.imgur.com/hsEJAwF.png)
![Create Swap Event](https://i.imgur.com/m73gSAv.png)
![Create Cover Event](https://i.imgur.com/CoEUobA.png)

# Module 3 Project Gamma

# Authors
  - Louise Vermaelen
  - Christopher Hem
  - Josh Hilsberg

# Introduction to TeamTable
TeamTable is a team management app designed to help members of large teams coordinate and plan for shift swaps and shift covers. Members of a team can post their needed shift swaps and the times they are available to cover a shift in return and the system can automatically find shift swaps or people willing to cover their shift if they exist. Members can also post cover events which allow them to cover other peoples shifts for the purpose of getting more hours. If a users shift is covered in this way then their availability is automatically turned into a cover event so that they can "pay it forward" and help someone else get the time off they need.

## User Dashboard
The user dashboard displays the users posted shift swap requests and cover availabilities as well as notifications informing them if one of their shifts has been covered which includes the dates and times they will need to cover in return. Users can be a member of multiple teams (such as the popular imaginary fast food chains, Burger Monarch and McDimwalds), and the events will not interact with one another. For example, a user could not pick up a shift at Burgur Monarch in exchange for a shift at McDimwalds. 

## Team Dashboard
The team dashboard displays the information for an individual team, including all the requested swaps on the team, members, and roles. This allows users to view a team dashboard and see shifts they might be interested in picking up, they can then post an availability during that time and request the swap. 

## Setup
  - clone the repository
  - You will need a pg-admin and a postgres-data volume, as well as a top level .env file
    - docker volume create pg-admin
    - docker volume create postgres-data
    - create a top level env file and paste this into it: TEAM_DATABASE_URL=postgresql://teams:password@postgres/teams
  - docker-compose build
  - docker-compose up
  - website hosted locally on localhost:3000

## Tests
  - unit tests can be run in docker console for monoservice or teams service using the following commands
    - pip install pytest
    - pytest
  - pipeline currently only has one stage; Test, which successfully runs the tests on gitlab
    - you are welcome to make a comment somewhere in the code, save, add, commit, and push to test this functionality
  - tests are located in the 'test' folders in both the monoservice and the teams service.
  
## MVP
  - Front page
    - Signup page on nav bar
    - Login Page on nav bar
  - User dashboard redirect on login
    - user dashboard displays all user's events and notifications
    - user can carry out shift swaps and shift covers on dashboard
    - user can create shift swap and shift cover events on dashboard
    - user can mark notifications as seen (green checkmark)
    - side navigation bar lists users teams in a drop down menu
  - team dashboard
    - team dashboard displays buttons to invite team members and add roles to the team
    - displays team members
    - displays all team swap and cover events for the team
    - user can navigate back to dashboard by clicking "my home" on the side navbar
  - Please Note:
    - We are still working on and adding to this project and many pieces of code we still have intentions of using are currently commented out for the sake of grading. We apologize for the mess but hope you understand.

## Stretch
  - button to pick up a shift on team dashboard - automatically covers the event for the other user and sends correct notifications
  - Permissions functionality (ability to add members restricted by "can_invite", and the ability to require approval for shift swaps "can_approve")
  - number of teams/events displays correctly on side nav bar
  - deploy to heroku
  - Different team types for social use rather than just shift management
  - mobile app to interact with backend
  - true shift management functionality
  - darkmode?
  - messaging
  - display events on a calendar

