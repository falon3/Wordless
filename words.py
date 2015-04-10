from collections import OrderedDict
_END = "_END_"

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
            prev = 'a'
            for line in dictionary:
                # trying to get the first character group
                word = line.split(' ')[0].rstrip('\r\n')
                
                # read once we are past the credits
                if reading:
                    if word.find("'") == -1 and word[0] != word[0].upper() \
                        and len(word) > 2:
                        words.append(word.upper())
                else:
                    # check for end of credits
                    if word[0:3] == "---":
                        reading = True
        #self.dawg = DAWG(words)
        #self.cdawg = CompletionDAWG(wordS)
        self.build_trie(words)
    
    def lookup(self, word):
        # returns None if not in lookup, True if complete, False if incomplete
        #if word in self.dawg:
        #    return True
        #elif word in self.cdawg:
        #    return False
        #return None
        return self.in_trie(word)
        
    def build_trie(self, words):
        root = dict()
        for word in words:
            current_dict = root
            for letter in word:
                current_dict = current_dict.setdefault(letter, {})
            current_dict = current_dict.setdefault(_END, _END)
        self.trie = root
    
    def in_trie(self, word):
        current_dict = self.trie
        for letter in word:
            if letter in current_dict:
                current_dict = current_dict[letter]
            else:
                return None
        return _END in current_dict
        
    def find_long_word(self, graph, tiles, tile):
        R = dict()
        S = [(tile, tile)]
        letters = OrderedDict()
        word=''
        best = ''
        best_value = 0
        while S:
            prev, curr = S.pop()
            if (tuple(letters)) not in R:
                value = 0
                if len(letters):
                    value = letters[next(reversed(letters))]
                value = Letters.calc_add_score(word, value, tiles[curr].text)
                word += tiles[curr].text
                letters[curr] = value
                valid = False
                for n in graph.neighbours(curr):
                    if n not in letters:
                        new_word = word + tiles[n].text
                        # if n + curr is a word add (curr, n)
                        found = self.lookup(new_word) 
                        if found:
                            alt = Letters.calc_add_score(word, value, tiles[n].text)
                            if alt > best_value:
                                best_value = alt
                                best = new_word
                        if found != None:
                            S.append((curr, n))
                            valid = True
                # walk back up graph until we find an open branch
                while S and len(letters) > 1 and not valid:
                    R[tuple(letters)] = prev   
                    letters.popitem()
                    word = word[:-1]
                    curr = next(reversed(letters))
                    value = letters[curr]
                    
                    if S[-1][0] == curr:
                        valid = True  
                    
        return best
        
    def find_longest_word(self, graph, tiles):
        longest = ''
        length = 0
        longest_tile = None
        for tile in graph.vertices():
            word = self.find_long_word(graph, tiles, tile)
            if len(word) > length:
                length = len(word)
                longest = word
                longest_tile = tile
        
        #if longest_tile:
        #    longest_tile.background_color = [1,0,1,1]
        return longest
    
class Letters():
    """A quick class for selecting letters to populate the board with.
    """
    # English letter frequencies reflected down to nearest 1/10 percent
    letters = 'E'*127 + 'T'*91 + 'A'*82 + 'O'*75 + 'I'*70 + 'N'*67 + 'S'*63 \
            + 'H'*61 + 'R'*60 + 'D'*43 + 'L'*40 + 'U'*28 + 'C'*28 + 'M'*24 \
            + 'W'*23 + 'F'*22 + 'YGP'*20 + 'B'*15 + 'V'*10 + 'K'*7 + 'XJ'*2 \
            + 'QZ'
    
    # TODO: these were taken directly from scrabble - replace with own values
    Value = {'A':1,'B':3,'C':3,'D':2,'E':1,'F':4,'G':2,'H':4,'I':1,'J':8,'K':5,\
        'L':1,'M':3,'N':1,'O':1,'P':3,'Q':10,'R':1,'S':1,'T':1,'U':1,'V':4,    \
        'W':4,'X':8,'Y':4,'Z':10}
        
    
    def calc_add_score(word, score, letter):
        score += Letters.Value[letter]
        
        # word length bonus of (addtional letter)/2 times the score
        # for each letter over 3
        length = len(word)
        if 2 < length < 9:
            score += int(score/2)
        elif length >= 9:
            score += int(score/length-7)
            
        return score

