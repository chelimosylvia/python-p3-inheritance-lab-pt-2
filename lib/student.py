class Student:
    '''Class representing a Student'''

    def hello(self):
        '''Prints out a greeting message'''
        print("Hey there! I'm so excited to learn stuff.")

    def raise_hand(self):
        '''Prints out a message indicating raising hand'''
        print("Pick me!")


class ChattyStudent(Student):
    '''Class representing a Chatty Student'''

    def hello(self):
        '''Augments the hello method to be more chatty'''
        super().hello()
        print("How are you doing today? I'm okay, but I'm kind of tired. "
              "Did you watch The Walking Dead last night? You didn't?! "
              "Oh man, it was so crazy! What, you don't want any spoilers? "
              "Okay well let me just tell you who died...")

    def raise_hand(self):
        '''Overrides raise_hand to print "Pick me!" ten times'''
        for _ in range(10):
            super().raise_hand()
