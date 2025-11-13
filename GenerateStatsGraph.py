import numpy as np
import matplotlib.pyplot as plt
import os
import DB_Connect

def generateGraph(userStats, user_name):

        x_Axis = list(userStats.keys())
        y_Axis = list(userStats.values())

        fig = plt.figure(figsize=(5,5))

        # creating the bar plot

        plt.bar(x_Axis, y_Axis, color='maroon',
                width=0.4)

        if ("admin" in user_name):
                plt.xlabel("User IDs")
                file_name="LoginStatsGraph.png"
        else:
                plt.xlabel("Date of Login")
                file_name = user_name + "_LoginStats.png"
        plt.ylabel("No. of Login Attempts")
        plt.title("User Login Statistics")
        my_path=os.path.dirname(__file__)
        print(my_path)
        plt.savefig(my_path + "\\static\images_folder\\" + file_name)
        if os.path.exists(my_path + "\\static\images_folder\\"+ file_name):
                return True
        else:
                return False
        #plt.show()

