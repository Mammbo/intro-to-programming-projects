#Project 7-5: Email List Clearner 
#Daniel Alvarez 
#3/7/24 

import csv
# define function that formats csv files
def csv_clean(inpath, outpath):
  # open csv file
    #define headeer
    outfile = open(outpath, "w")
    outfile_header = "First_Name,Last_Name,email\n"
    #write to the cleaned file
    outfile.write(outfile_header)
    #open original file 
    with open(inpath, 'r') as infile: 
        reader = csv.reader(infile, delimiter=",")
        #loop through all lists and sort them via first last and emial and format them 
        for row in reader:
          first_name = row[0].title().strip()
          last_name = row[1].title().strip()
          email = row[2].lower().strip()
          #write to cleaned file 
          line = "{},{},{}\n".format(first_name, last_name, email)
          outfile.write(line)

    outfile.close()
#welcome message 
print("Welcome to the Email Cleaner")

#asks for source list 
inpath = input("Source List: ") 
#asks for cleaned list
outpath = input("Cleaned List: ")
csv_clean(inpath, outpath)

print(f"Congratulations! Your list has been cleaned!: {outpath}")