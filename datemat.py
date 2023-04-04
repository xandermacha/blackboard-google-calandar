from datetime import datetime

def format_dates(dates):
    
    for i in len(dates):
        d = dates[i]
        d = d.strip()# remove the newline character
        date_object = datetime.strptime(d, '%m/%d/%y %I:%M %p')
        dates[i] = (date_object)
    return dates