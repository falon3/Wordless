# cmgraff, scheers cmput275 LBL B2, LBL EB1
'''
Wordless
================

A word search game created with kivy.

TODO: add game description here, including specifics of assignment 
    (e.g. where to look for interesting algorithms)
'''

import kivy
kivy.require('1.8.0')

from kivy.properties import StringProperty, ObjectProperty, NumericProperty
# from kivy.animation import Animation
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

from collections import OrderedDict
from random import randint
import string

from graph_v2 import Graph

TILE_COLUMNS = 8   # number of columns in the game board
TILE_ROWS = 6       # number of rows in the game board

class Dictograph():
    """A word list used for checking words and populating the board.
    
    
    NOTE: work in progress
    
    """
    def __init__(self, filename):
        words = []
        # meant to process a list generated by http://app.aspell.net/create
        #
        # read all strictly aphabetic words that are longer than 4 characters
        # into list 'words'
        with open(filename, newline='') as dictionary:
            # skip the opening credits of the file
            reading = False
            count = 0
            for line in dictionary:
                # trying to get the first character group
                word = line.split(' ')[0].rstrip('\r\n')
                
                # read once we are past the credits
                if reading:
                    if word.find("'") == -1 and word[0] != word[0].upper() \
                        and len(word) > 3:
                        words.append(word)
                else:
                    # check for end of credits
                    if word[0:3] == "---":
                        reading = True
        """
        letter = None
        position = 0
        line = 0
        start = 0
        same = []
        edges = []
        while line < len(words): # probably needs a better end condition
            # if the current letter doesn't match the previous letter
            if words[line][position] != letter:
                # process list of words that are the same to this point
                # having the current letter/position point to all next adjacent letter/positions
                letter
                for word in same:
                    # if letter
                    edges.append(
        """
        self.words = set(words) # make it a set
        
        # build a list of all words that share the same letter at the same position
        
            # add an edge from that letter/position to all next adjacent letters/positions
            # repeat
class Letters():
    """A quick class for selecting letters to populate the board with.
    """
    
    letters = "AEIOUAEIOUAEIOUBCDFGHJKLMNPQRSTVWXYYZ"
    
    # TODO: these were taken directly from scrabble - replace with own values
    Value = {'A':1,'B':3,'C':3,'D':2,'E':1,'F':4,'G':2,'H':4,'I':1,'J':8,'K':5,\
        'L':1,'M':3,'N':1,'O':1,'P':3,'Q':10,'R':1,'S':1,'T':1,'U':1,'V':4,    \
        'W':4,'X':8,'Y':4,'Z':10}
    
class Board():   
    """Represents the game board.
    
    Currently this class encompasses both the data for the board and the  
    display for the same. 
    
    TODO: We may want to break this functionality up into
    a couple different classes for easier development and maintenance.
    
    Attributes:
      _highlighted (OrderedDict): An ordered collection of highlighted tiles.
      _dictionary (Dictograph): A word list used for checking words 
        and populating the board.
    
    
    """    
    Score = None
    score = '0'
    _highlighted = OrderedDict()
    _dictionary = Dictograph("us_cad_dict.txt")
    
    def highlight(tile, highlight=[0,1,1,1]):    
        # if not highlighted
        if tile not in Board._highlighted:
            last = None
            if Board._highlighted:
            # get the last element added to highlighted
                last = next(reversed(Board._highlighted))
            
            # if last exists, get neighbors
            if last:
                neighbours = Board._board.neighbours(last)
            # allow highlighting if first tile or adjacent tile
            if not last or tile in neighbours:                
                Board._highlighted[tile] = len(Board._highlighted)
                tile.background_color = highlight
        
        # if already highlighted
        elif Board._highlighted[tile] == len(Board._highlighted) - 2:
            # unhighlight last tile if going backward
            last = Board._highlighted.popitem(last=True)
            last[0].background_color = [1,1,1,1]
                
    
    def build_board():
        # declare the widget for the app to display
        layout = BoxLayout(orientation = 'vertical')
        tiles = []
        Header = BoxLayout(orientation = 'horizontal')
        layout.add_widget(Header)
        Score = Label()   
        Board.Score = Score 
        Score.text = "SCORE: " + Board.score   
        Header.add_widget(Score)
        
        
        # add all the tiles to the board
        for i in range(TILE_COLUMNS * TILE_ROWS):
            if i % TILE_COLUMNS == 0:
                row = BoxLayout(orientation = 'horizontal')
                if i % (2 * TILE_COLUMNS) == 0:                    
                    row.pos_hint = {'right': .975}       
                else:                              
                    row.pos_hint = {'right': .92}       
                    
                row.size_hint_x = 0.9                    
                layout.add_widget(row)

            tile = Tile(i)
            tiles.append(tile)
            row.add_widget(tile)
            
        
        # fill out edges of graph
        edges = []
        
        # check if at board boundaries
        
        for i in range(len(tiles)):           
            
            left = i % TILE_COLUMNS == 0
            right = i % TILE_COLUMNS == TILE_COLUMNS - 1 
            top = i // TILE_COLUMNS == 0
            bottom = i // TILE_COLUMNS == TILE_ROWS - 1
            
            
            # offset == 1 for odd rows, 0 for even
            offset = (i // TILE_COLUMNS) % 2
            # even == True if offset == 0
            even = offset == 0
                        
            # NOTE: effectively the two values above are identical, but 
            #       I've given them different names because they are
            #       used for different purposes
            
            # not left of the board
            if not left:
                edges.append((tiles[i], tiles[i-1]))
                
            # not right of the board
            if not right:
                edges.append((tiles[i], tiles[i+1]))
            
            # not top of the board
            if not top:      
                if not right:
                    edges.append((tiles[i], tiles[i-TILE_COLUMNS + 1 - offset]))  
                elif not even:  # right and odd
                    edges.append((tiles[i], tiles[i-TILE_COLUMNS]))            
                if not left: 
                    edges.append((tiles[i], tiles[i-TILE_COLUMNS - offset]))  
                elif even:  # left and even
                    edges.append((tiles[i], tiles[i-TILE_COLUMNS]))         
            
                
            # not bottom of the board
            if not bottom:
                if not right:
                    edges.append((tiles[i], tiles[i+TILE_COLUMNS + 1 - offset]))
                elif not even:  # right and odd
                    edges.append((tiles[i], tiles[i+TILE_COLUMNS]))                      
                if not left:
                    edges.append((tiles[i], tiles[i+TILE_COLUMNS - offset]))   
                elif even:  # left and even
                    edges.append((tiles[i], tiles[i+TILE_COLUMNS]))    
        
            # create graph representing the board
            Board._board = Graph(set(tiles), edges)
        
        # return the widget for the app to display
        
        
        return layout

    
class Tile(Button):
    """ Represents a tile in the game board.
    """    
    
    def __repr__(self):
        return self.text
    
    def __init__(self, tilenumber=-1, **kwargs):
        """
        
        """
        # initialize base class
        super().__init__(**kwargs)     
        
        
        # populate board with random letters
        # TODO: consider populating board with words and partial words
        
        # set the text of this tile
        rand = randint(0, len(Letters.letters)-1)
    
        letter = Letters.letters[rand]
        self.text = letter
        self.lscore.text = str(Letters.Value[letter])
        self.font_size = 50
                
    def on_touch_down(self, touch):  
        """Base kivy method inherited from Button.
        
        This method is called on all buttons at once, so we need to 
        return True for only the currently touched button.

        Note:
          We are not currently passing this up to super(), but 
          we could consider doing so.

        Args:
          touch: A kivy motion event

        Returns:
          True if for currently touched button, False otherwise.

        """      
        
        if touch.is_touch or touch.button == 'left':
            if self.collide_point(touch.x, touch.y):
                Board.highlight(self)
                
                # set grab to catch release off of tiles
                touch.grab(self)
                return True
        return False
            
    def on_touch_move(self, touch):        
        """Base kivy method inherited from Button.
        
        This method is called on all buttons at once, so we need to 
        return True for only the currently touched button.

        Note:
          We are not currently passing this up to super(), but 
          we could consider doing so.

        Args:
          touch: A kivy motion event

        Returns:
          True if for currently touched button, False otherwise.

        """
        
        if touch.is_touch or touch.button == 'left':
            if self.collide_point(touch.x, touch.y):
                Board.highlight(self)
                return True
        return False
            
    def on_touch_up(self, touch):        
        """Base kivy method inherited from Button.
        
        This method is called on all buttons at once, so we need to 
        return True for only the currently touched button.

        Note:
          We are not currently passing this up to super(), but 
          we could consider doing so.

        Args:
          touch: A kivy motion event

        Returns:
          True if for currently touched button, False otherwise.

        """
        if touch.is_touch or touch.button == 'left':
            if touch.grab_current is self:
                # release grab
                touch.ungrab(self)
                score = 0
                word = ''
                for tile in Board._highlighted:
                    letter = tile.text
                    score = score + Letters.Value[letter]
                    word = word + letter
                    
                if word.lower() in Board._dictionary.words:
                    print("SUCCESS!")
                    Board.score = str(int(Board.score) + score)
                    Score = Board.Score 
                    Score.text = "SCORE: " + Board.score
                    
                    #save score somewhere
                    #remove tiles 
                else:
                    for tile in Board._highlighted:
                        tile.background_color = [1,1,1,1]
                        
                #xclear highlighted list
                Board._highlighted.clear()
                    
                return True
        return False
        
        
        
    """ just keeping this around as an example animation for when we add them
    
    def animate(self, instance):
        # create an animation object. 
        animation = Animation(pos=(100, 100), t='out_bounce')
        animation += Animation(pos=(200, 100), t='out_bounce')
        animation += Animation(pos=(self.pos[0], self.pos[1]), t='out_bounce')

        # apply the animation on the button, passed in the "instance" argument
        animation.start(instance) 
    """
        
class Wordless(App):
    """Base kivy application for game.
    
    """
    def build(self):                    
        layout = Board.build_board()
        
        return layout

    
if __name__ == '__main__':
    
    Wordless().run()
