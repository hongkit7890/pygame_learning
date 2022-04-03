from random import randint
import pygal
import webbrowser
import os

class Die():
    """A class representing a single die."""
    def __init__(self, num_sides=6):
        """Assume a six-sided die."""
        self.num_sides = num_sides
    def roll(self):
        """"Return a random value between 1 and number of sides."""
        return randint(1, self.num_sides)


die_1 = Die()
die_2 = Die(10)

# Make some rolls, and store results in a list.
results = []
ran = 1000000
for roll_num in range(ran):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
  frequency = results.count(value)
  frequencies.append(frequency)

# Visualize the results.
hist = pygal.Bar()
hist.title = "Results of rolling a D6 and a D10 "+str(ran)+" times."
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
'13', '14', '15', '16']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6 + D10', frequencies)

hist.render_to_file('die_visual.svg')

url = 'die_visual.svg'
firefox = webbrowser.Mozilla("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
firefox.open_new_tab(os.getcwd()+"\\"+url)


