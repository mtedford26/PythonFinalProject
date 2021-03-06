# PythonFinalProject
Code, datasets, and other items for determining whether the movies in the MCU pass the Bechdel Test.

Due to time constraints, there's only data for a few movies, so this is really just a sample code for the larger MCU Bechdel test. 

For the purpose of equality, there is a majorily female led movie included, a majorily led male movie, and a movie meant to include multiple main characters. A "team up" if you will.  
Captain Marvel, Captain America, and Avengers: Age of Ultron.

The goal of this project is to review the scripts of as many MCU movies as I can and determine whether or not they pass the Bechdel test.

Basically, I will create two tables of coded language and names to compare and assign genders. (first, last, nicknames, superhero titles, villain titles, etc.) as male or female. (since there are currently not any non-binary or non-gendered characters in the MCU)

Then I will run loops to go through the scripts pulled by the input requested to find dialogue between two female characters and determine if there is any gendered language or male names from my previous table/database.

First, the Input will require the user to enter the name of a Marvel film, which is assigned a script. 
If a movie title that does not have available data for the Input requested, a line will print, "this movie title is unavailable in this dataset, please enter the title of another MCU film."

Then a For loop will check for available data. 

If available, proceed with another For loop.

To determine whether or not a movie does pass, I am analyzing the speakers line by line to see if they are a named female character, and then determining whether or not the speaker of the following line is also a named female. This analysis will come from the table of female character names. 

If both speakers are determined to be female, I will then run the lines of dialogue between those two speakers to look for any male coded language, such as he/him/his pronouns, male titles such as 'sir, mr,' etc., or male proper names, both superhero titles and given names.

These items will also have to be compiled in a list and not sorted through a dictionary because several superhero names are not generally found in common lists of male names, and also several characters are often referred to by last names in dialogue, which could be either gender neutral or could be misconstrued as gendered.



If there is no gendered language detected, and/or no items from my table of male gendered language/titles/names, the output will be, "YES, this MCU film DOES pass the Bechdel test!"

If gendered language/titles/names are detected, the else: code will skip to the end and print, "this movie unfortunately does not pass the Bechdel-test."

This overall is very rough code and does not account for scene changes, group conversations, and other complicating factors. 
It is only meant to be a basic set-up to give the general idea for if a film will or will not pass the Bechdel-test. As time goes on, I believe I can put more personal time into this project and really flesh it out for more accuracy. 
