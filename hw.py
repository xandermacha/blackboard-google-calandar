import linecache

class_name = []
assn_date = []
item = []
due_date = []

def make_task(_file):
    content = _file
    with open(content, 'r') as fp:
        num_lines = sum(1 for line in fp if line.rstrip())
        
        print(f"Total Assignments: {num_lines/4}")  
        
    # adds all parameters to item list
    i = 1
    n = 0
    while i<= num_lines:
        _class = linecache.getline(content, i)
        _date = linecache.getline(content, 1+i)
        _item = linecache.getline(content, 2+i)
        _due = linecache.getline(content, 3+i)
        class_name.insert(n,_class)
        assn_date.insert(n,_date)
        item.insert(n,_item)
        due_date.insert(n,_due)
        i+=4
        n+=1
def numline():
    _length = len(item)
    return _length

def summary():
    Class = []
    for i in range(len(item)):
        Class.append(item[i])
    return Class
def desc():
    Class = []
    for i in range(len(class_name)):
        Class.append(class_name[i])
    return Class
def due():
    Class = []
    for i in range(len(due_date)):
        Class.append(due_date[i])
    return Class
def assign():
    Class = []
    for i in range(len(assn_date)):
        Class.append(assn_date[i])
    return Class
        
