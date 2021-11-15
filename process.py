log_file = open("um-server-01.txt")


def sales_reports(log_file):
    for line in log_file:
        line = line.rstrip()
        day = line[0:3]
        if day == "Tue":
            print(line)


sales_reports(log_file)


#def sales_reports(log_file): - this line defines the function and the parameter.

    #for line in log_file: - this line is a for loop that is iterating over the (log_file) sequence.
    
        #line = line.rstrip() - In this line, you're creating a new string with the stripped content before printing.
        
        #day = line[0:3] - This line assignes the varible.
        
        #if day == "Tue": This line reassigns the varble and looks for lines that are equal to "Tue".
            #print(line) - This line prints out the results of for loop.
            
#sales_reports(log_file)

def sales_reports(log_file):
    for line in log_file:
        line = line.rstrip
        fruit = line[0:3]
        if fruit = "Melon":
            print(line)
            