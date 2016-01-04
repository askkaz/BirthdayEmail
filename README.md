## Synopsis
This app allows doctors to write a personalized birthday greeting to a patient, which is then sent on the patient's birthday. This allows the doctor to write the message while details of the patient are fresh in their mind, making for a more personal touch.  This was a project to both learn django and begin playing with the interface to the [drchrono API](https://www.drchrono.com/api/).  I also used Bootstrap and Javascript.

## Status
I'm currently hosting this at [Python Anywhere](http://adamkaz.pythonanywhere.com/), which was a pretty simple way to get this published.  You'll need a username and password to play with the sample account - feel free to email me at drchronobirthday (at) gmail.com to get one.

Emails are currently sent to my personal email address (with the real email address denoted in the message).  I didn't want to be spamming people if these were actual email addresses in the drchrono sample account set up.

## What It Does
The first step in using this app is to give permission for the app to use details from a drchrono account.  The way that the API works, only one account can be linked for an unpublished app (mine).  The app manages the authentication with drchrono and updates access tokens when they are within 30 min of expiration.

After succesfully creating an account, the user is presented with a list of patients.  These patients are in 1 of 4 color categories based on their status:
* Patients in red are not selectable, because they are either missing an email or a birthday within drchrono.  (I originally planned to create a modal to add these details, but it's either not possible or I wasn't able to figure out how to modify patient details from the API).
* Patients in blue have handcrafted emails just waiting to be sent to them.  Their birthday just hasn't passed yet.  These emails can still be edited or deleted.
* Patients in green have had amazingly curated messages sent to them on their birthday (within the past month).  These emails can be deleted if the doctor wants to get cracking on next year's message.
* Patients in gray have no messages queued and can be selected to begin writing a birthday greeting.

Emails are sent twice daily, based on whether the date has passed.  There is a command on the server that will send all the emails regardless of date, which is why there may be some sent messages that don't make sense.

## Reflections
We currently use Laravel at work for our back end. One difference I noticed was the way that migrations are handled.  In Django, you define what the model should look like, and Django takes care of the migrations for you.  In Laravel, you define what migrations you want done (changes to the model), and Laravel makes the model for you. In the end, the migrations files end up looking the same, but its nice to have everything all in one place for each model in Django.

Overall, even though it has been a little while since I've used Python, Django was really straightforward to pick up.  This is greatly helped by the large community using it.