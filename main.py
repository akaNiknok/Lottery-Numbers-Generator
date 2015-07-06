"""Generates 6 random numbers

   Author: Austin G. Imperial
File Name: main.py

 Problem: You have 1 in 28,989,675 chance of winning the lottery (Philippine
          Lottery). How can we improve the chance of winning in the lottery?

Solution: Making a program that eliminates rare combinations by
          setting some rules.

*Rules*
    1. It should generate 6 random numbers from 1-55
    2. It should generate numbers from Low (1-28) and High (29-55) with this
       ratios:
        3:3  4:2  2:4
    3. It should generate Odd and Even numbers with the same ratio as above
    4. It should not generate 6 numbers from all of 5 groups
    5. The sum of the 6 numbers should be from 104 - 239
    6. Every list should not be generated twice or more (Not working on this
       version)

*Groups*
    1 --  1-11
    2 -- 12-22
    3 -- 23-33
    4 -- 34-44
    5 -- 45-55
"""

__version__ = "1.0"

import random
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout


# Initialize groups
GROUP1_ODD = range(1, 12, 2)
GROUP2_ODD = range(13, 23, 2)
GROUP3_ODD = range(23, 34, 2)
GROUP4_ODD = range(35, 45, 2)
GROUP5_ODD = range(45, 56, 2)
GROUP1_EVEN = range(2, 12, 2)
GROUP2_EVEN = range(12, 23, 2)
GROUP3_EVEN = range(24, 34, 2)
GROUP4_EVEN = range(34, 45, 2)
GROUP5_EVEN = range(46, 56, 2)

GROUP1 = [GROUP1_ODD, GROUP1_EVEN]
GROUP2 = [GROUP2_ODD, GROUP2_EVEN]
GROUP3 = [GROUP3_ODD, GROUP3_EVEN]
GROUP4 = [GROUP4_ODD, GROUP4_EVEN]
GROUP5 = [GROUP5_ODD, GROUP5_EVEN]

groups = [GROUP1, GROUP2, GROUP3, GROUP4, GROUP5]


class MainWidget(BoxLayout):

    def rule(self):

        # Initialize variables
        odd = random.randint(2, 4)
        high_max = random.randint(2, 4)
        low_max = 6 - high_max
        generated = []
        high = 0
        low = 0

        random.shuffle(groups)  # Shuffle the groups

        # The total sum of the generated list should be 104 - 239
        while sum(generated) < 104 or sum(generated) > 239:

            # Generate 6 numbers
            for i in range(6):

                # Checks if we need to generate an odd or an even number
                if i <= odd - 1:
                    odd_or_even = 0
                else:
                    odd_or_even = 1

                # Get a random group from the first four groups
                current_group = groups[random.randint(0, 3)]

                # Get either an odd or even number from the chosen group
                num = random.choice(current_group[odd_or_even])

                # Checks if num is already generated or if it is a High/Low
                # number and the max number of High/Low number is already
                # achieved
                while (num in generated or (high >= high_max and num >= 29) or
                        (low >= low_max and num < 29)):
                    current_group = groups[random.randint(0, 3)]
                    num = random.choice(current_group[odd_or_even])

                # Checks whether the generated number is part of the High or
                # Low numbers
                if num >= 29:
                    high += 1
                else:
                    low += 1

                generated.append(num)  # Append the num

        generated.sort()  # Sort the list
        return str(generated)

    def generate(self):

        # Get the IDs of the GUI elements
        label = self.ids.label
        toggle_1 = self.ids.toggle_1
        toggle_5 = self.ids.toggle_5

        # If the first radio button is highlighted,
        if toggle_1.state == "down":
            label.text = self.rule()  # generate 1 combination

        # If the second radio button is highlighted,
        elif toggle_5.state == "down":
            nums = ''
            for i in range(5):        # generate 5 combinations
                nums += self.rule()
                nums += "\n"
            label.text = nums

        # If the third radio button is highlighted,
        else:
            nums = ''
            for i in range(10):       # generate 10 combinations
                nums += self.rule()
                nums += "\n"
            label.text = nums


# Make a Kivy App
class LotteryNumbersGenerator(App):
    def build(self):
        return MainWidget()

# Run the App
if __name__ == "__main__":
    LotteryNumbersGenerator().run()
