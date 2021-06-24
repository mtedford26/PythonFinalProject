# PythonFinalProject
Code, datasets, and other items for determining whether the movies in the MCU pass the Bechdel Test.

Unfortunately due to time constraints, there's only data for a few movies, so this is really just a sample code for the larger MCU Bechdel test. 
To be fair, there is a majorily female led movie included, a majorily led male movie, and a movie meant to include multiple main characters. 
Captain Marvel, Captain America: the First Avenger, and Avengers: Age of Ultron.

The goal of this project is to review the scripts of as many MCU movies as I can and determine whether or not they pass the Bechdel test.
First, the Input will require the user to enter the name of a Marvel film, which is assigned a script. 
If unavailable, the code will skip to the end and print, "No data for that title, please enter the title of a movie from the MCU with available data"
To determine whether or not a movie does pass, I am analyzing first the names of speakers, (spkr_1) to determine whether or not they are female, and then determining whether or not the second speaker, (spkr_2) is also female. 
(This will require a database of character names within the films to determine a base for "named" female characters.
If both speakers are determined to be female, I will then run the lines of dialogue between those two speakers to look for any male coded language, such as he/him/his pronouns, male titles such as 'sir, mr,' etc., or male proper names, both superhero titles and given names.
These items will also have to be compiled in a list and not sorted through a dictionary because several superhero names are not generally found in common lists of male names, and also several characters are often referred to by last names in dialogue, which could be either gender neutral or could be misconstrued as gendered.
Basically, I will create two tables of coded language and names to compare and assign genders. (first, last, nicknames, superhero titles, villain titles, etc.) as male or female. (since there are currently not any non-binary or non-gendered characters in the MCU)
Then I will run loops to go through the scripts to find dialogue between two female characters and determine if there is any gendered language or male names from my previous table/database.
Then an elif line will be to print, "this movie unfortunately does not pass the Bechdel-test." 