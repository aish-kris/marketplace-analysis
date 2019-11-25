# Aishwarya Krishnakumar
# kris184@usc.edu
# Thumbtack Analytics Challenge

def main():
    import matplotlib.pyplot as plt
    import numpy as np
    import array as arr

    contact_file = open("Contacts.csv", "r") # Opening both given csv files
    visitor_file = open("Visitorss.csv", "r")

    contact_headerLine = contact_file.readline() # Reading first line of the csv files, they don't contain data values
    visitor_headerLine = visitor_file.readline()

    rating = arr.array('i') # This is necessary to analyze the ratings of the pros
    rating = [0]*100
    rating_no_list = []

    num_of_ratings = arr.array('i') # This is necessary to analyze the # of reviews of the pros
    num_of_ratings = [0]*4000

    print("Loading...") # A file this large takes a while to load!

    for contact_line in contact_file: # This will go through every line in the contacts csv file
        contact_line = contact_line.split(",") # Separating the different data values

        if str(contact_line[3].strip("\n")) == "TRUE": # Checking to see if the pro got hired
            visitor_file = open("Visitorss.csv", "r") # Opens the visitor csv file each time
            visitor_headerLine = visitor_file.readline()

            for visitor_line in visitor_file: # This will go through every line in the visitors csv file
                visitor_line = visitor_line.split(",")

                if int(visitor_line[1]) == int(contact_line[0]):
                    if visitor_line[6] == "":
                        visitor_line[6] = 9

                    rating[int(round(float(visitor_line[6]),0))] += 1 # Sort the people who got hired by their rating

                    if float(visitor_line[6] == 9):
                        rating_no_list.append(visitor_line)

                    num_of_ratings[int(visitor_line[5])] += 1 # Sort the people who got hired by number of reviews

                else:
                    continue
                break
            visitor_file.close()

        else:
            # FALSE means the pro was not hired
            continue

    y = [len(rating_no_list), rating[0], rating[1], rating[2], rating[3], rating[4], rating[5]] # Y values for rating analysis
    x = ["no rating",0,1,2,3,4,5] # X values for rating analysis

    b = [] # Y values for number of reviews analysis
    a = [] # X values for number of reviews analysis
    total_num_of_ratings = 0
    bucket = 0 # Used to bucketize groups of reviews by 100

    for i in range(1000): # Maximum number of reviews a pro has is 1000
        total_num_of_ratings = total_num_of_ratings + num_of_ratings[i] # Adding the number of ratings for each group

        if bucket != int(i/100):
            b.append(total_num_of_ratings)
            bucket = int(i/100)
            total_num_of_ratings = 0

    b.append(total_num_of_ratings) # Insert the added number of ratings into a list for graphing
    a = ("0-99","100-199","200-299","300-399","400-499","500-599","600-699","700-799","800-899","900-999") # 10 Groups of 10 Reviews

    plt.figure(1) # Plotting the first graph, to analyze rating
    y_pos = np.arange(len(x))
    plt.bar(y_pos, y, color='green')
    plt.xlabel("RATINGS")
    plt.ylabel("# OF PROS HIRED")
    plt.title("# OF PROS WITH RATING OF X HIRED")
    plt.ylim(0, 250)
    plt.xticks(y_pos, x)
    for i, v in enumerate(y):
        plt.text(y_pos[i] - 0.15, v + 0.01, str(v))

    plt.figure(2) # Plotting the second graph, to analyze number of reviews
    y_pos = np.arange(len(a))
    plt.bar(y_pos, b, color='blue')
    plt.xlabel("# of REVIEWS")
    plt.ylabel("# OF PROS HIRED")
    plt.title("# OF PROS WITH REVIEWS OF X HIRED")
    plt.ylim(0, 400)
    plt.xticks(y_pos, a)
    for i, v in enumerate(b):
        plt.text(y_pos[i] - 0.15, v + 0.01, str(v))

    plt.show()
    contact_file.close()
    visitor_file.close()
    exit()

main() # Calling the function