# print("Day 1")
# the_file = open("um-deliveries-20140519.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print("Delivered {} {}s for total of ${}".format(
#         count, melon, amount))
# the_file.close()


# print("Day 2")
# the_file = open("um-deliveries-20140520.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print("Delivered {} {}s for total of ${}".format(
#         count, melon, amount))
# the_file.close()


#Create function, set parameter
def melon_delivery_report(date, the_file):
      
    # print file name, for reference, idk how to just print date of file name
    print("Date:", date)
    #Search through each line in file and Tokenize words
    for line in the_file:
        line = line.rstrip()
        words = line.split("|")

        #Assign variable to tokens
        melon = words[0]
        count = words[1]
        amount = words[2]
        #output each line
        print("Delivered {} {}s for a total of ${}".format(
            count, melon, amount))
    #close the file (don't know why?)    
    the_file.close()

#call the function, pass in argument as open file

melon_delivery_report("2014-05-19", open("um-deliveries-20140519.txt"))
melon_delivery_report("2014-05-20", open("um-deliveries-20140520.txt"))
melon_delivery_report("2014-05-21", open("um-deliveries-20140521.txt"))

