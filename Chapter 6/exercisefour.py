# Exercise 4: Stack bar graph ☑️
# In January 2007, a Gallup poll asked 1008 Americans aged 18 and over whether they planned to watch the upcoming Super Bowl. The pollster also asked who planned to watch whether they were looking forward more to watch football games or commercials. The results were summarized in the table

#                    Male	 Female	  Total
# Game		         279	  200	    479
# Commercials	      81	  156	    237
# won’t watch	    132	  160	    292
# Total		        492	  516	    1008

#we import the matplotlib library in order to create visual interfaces such as the requested stack bar graph in the activity
import matplotlib.pyplot as plt

#initializing the figure object
fig = plt.figure()

#defining the necessary data for the bar chart
classes = ['Game','Commercials',"Won't Watch"]
maleData = [279,81,132]
femaleData = [200,156,160]
x_axisLabel = ['Game','Commercials',"Won't Watch"]

plt.bar(classes, maleData, color='skyblue') #classifies the male data and adding the blue hue as its bar
plt.bar(classes, femaleData, bottom=maleData, color='pink') #classifies the female data and adding the pink hue for its bar

plt.title('Super Bowl Views Survey') #creates the title for the bar chart
plt.show() #the .show() function tells the program to display the just created bar chart