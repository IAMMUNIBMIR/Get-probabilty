import copy
from operator import index
import random


class Hat:

    def __init__(self,**kwargs):

        self.contents = []

        for key,value in kwargs.items():
            for itr in value:
                self.contents.append(key)
            
    def draw(self,numofballstodraw):
        
        draw_list = []

        if numofballstodraw > len(self.contents):
                return self.contents

        for i in range(numofballstodraw):

          Ballchoice = self.contents.pop(random.randrange(len(self.contents)))
          draw_list.append(Ballchoice)
        
        return draw_list


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    numoftimesitworked = 0

    for i in range(num_experiments):
        
        Hatcopy = copy.deepcopy(hat)
        Listofballs = Hatcopy.draw(num_balls_drawn)
        success = True

        for key,value in expected_balls.items():
            
            if Listofballs.count(key) < value:
                success = False
                break

        if success == True:
            numoftimesitworked += 1

        return numoftimesitworked/num_experiments

