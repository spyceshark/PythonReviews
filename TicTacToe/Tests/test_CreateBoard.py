#Unit tests for the creation of the game table to user/game specs

#Imports
import unittest
from Main.CreateBoard import user_input, full_board_builder, row_creation

#Tests
class TestBoardCreationMethods(unittest.TestCase):
    
    def test_user_input(self):
        self.assertEquals()


    def test_full_board_builder(self):
        self.assertEquals(full_board_builder(3, 3), )


    #redundancy test - full board builder test will test this
    def test_row_creation(self):
        self.assertEquals()

