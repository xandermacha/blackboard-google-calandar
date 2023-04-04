import os

def clean_list(fname):
    original_file = fname
    temp_file = "temp.txt"

    # removes beginning and endlines
    words = ('Upcoming', 'Show', )
    with open(original_file, "r") as input:
        with open("temp.txt", "w") as output:
            # iterate all lines from file
            for line in input:
                # if substring contain in a line then don't write it
                if not line.strip("\n").startswith(words):
                    output.write(line)
    os.replace('temp.txt', fname)

                    
    string_to_delete = ['spring', '2023', 'Due: ', 'Due: ', 'Due Date: ', ',', 'Event', 'Date:', 'Event:']
    with open(original_file, "r") as input:
        with open(temp_file, "w") as output:
            for line in input:
                for word in string_to_delete:
                    line = line.replace(word, "")
                output.write(line)
    # replace file with original name
    os.replace('temp.txt', fname)
    
def spaced(fname):
    content = fname
    # removes extra spaces
    with open(
    fname, 'r') as r, open(
        'temp.txt', 'w') as o:
        for line in r:
            
            #strip() function
            if line.strip():
                o.write(line)
    os.replace('temp.txt', fname)

    # replace file with original name
    