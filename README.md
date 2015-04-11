Wordless: a fast-paced word game
Authors: Craig Cmgraff, Falon Scheers Cmput275 LBL B2, LBL EB1

Required software/environment: Kivy 1.9.0
To run the game click on the Wordless.py file and 'open with' kivy-3.4.bat


Required modules/files:
         -binary_heap.py
         -board.py
                Most of the game play is done in this module, the board updates
                and animations as well as calls to the timer and score functions.
                Also the ending game function and screen are handled here.   
         -graph_v2.py
                Our graph class used to distinguish which tiles are connected
                to eachother
         -tile.py
                Algorithms regarding building and updating the tiles are found here
                as well as calculating the scores and deciding if the letters selected
                are a word or not
         -us_cad_dict.txt:
                A large list of all of the words in Canadian and United States
                dictionary, plus any Hacker words
         -Wordless.kv
                DONT KNOW WHAT TO CALL THIS ONE.... KIVY ORGANIZATIONAL FILE HOLDING MOST OF 
                CLASS DEFINITIONS
         -Wordless.py
                Main file that runs the game app
         -words.py

Code references:
     - Graph Class and Binary heap code and functionality from class notes
     - dictionary file generated by http://app.aspell.net/create
     -

Complex Algorithms to bring attention to:
        SEARCHWORD
        GRAPH RE-BUILD
        TRIE STUFF
        ect....

        Efficiency and running time of these


High-level Game Play description:

Wordless is a word game with the main screen as a board with a grid-like array
 of 7x9 tiles with letters and their score value on them similar to Scrabble tiles.
 The object of the game is to get the highest score possible before the time runs 
out to zero. 

The game begins at level zero and waits until you accumulate 30 points to start 
counting down. As you get more points these points directly add to the timer to 
increase your playing time. At 100, 200, 300, 400, excetera points you level up 
to the next level of the game by which the timer counts down a bit faster each 
level. There are score bonuses for each additional letter over 3. 

The largest possible scoring word on the board at any given time, or the 'Search Word' 
is displayed at the bottom of the screen after the first 15 points are scored. As a 
player you can choose to find the search word for extra big score bonuses or make up 
your own words from the tiles on the board. While holding the cursor down over a 
series of connected letter the tiles light up to be yellow if there exists a word 
from the combination of letters selected, and the tiles go red if there exists no word 
in the game dictionary that starts with what is selected. Tiles are green when a valid 
word is selected. 

Upon running out of time the user is prompted for their name and if their score is among 
the top 5 highest then it is saved to the high_scores.txt file and displayed on the screen.

