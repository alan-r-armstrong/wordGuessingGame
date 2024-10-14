# wordGuessingGame
Adding color from colorama to output was easy enough but initially would color everything after it was called.  Resetting the style output to normal required a lot of debugging until I found the autoreset feature and enabled it.  

Another problem was when the random word returned from the capitals list contained multiple words, such as Salt Lake City, I was unable to find a way to allow the player to enter a " " character.  I spent a few hours troubleshooting this before deciding to comment out any words that were two or more words in length.  

Proper syntax was another problem with this assignment.  Calling my functions in my wordlists.py file correctly took a lot of trial and error before I got the syntax correct.  

Finally I had to spend some time in google sheets to properly format the words in my columns to concatenate them into a list that python would recognize when I copied them into my lists.
