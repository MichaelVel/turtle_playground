from letters import *
                
class Word:
    def __init__(self, word, startx, starty):
        self.letters = [] 

        for n,l in enumerate(word):
            offset = n*(W+SPACE)
            self.letters.append(Letter(l, startx+offset, starty))
 
    def draw(self):
        for letter in self.letters:
            letter.draw()

if __name__ == "__main__":
    test = Word("FELIZ", 0, 0)
    test.draw()

  
  

