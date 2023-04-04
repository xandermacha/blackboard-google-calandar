import hw 
from datetime import datetime, timedelta
from quickstart import get_calendar_service


def main():
   # creates one hour event tomorrow 10 AM IST
   service = get_calendar_service()

   d = datetime.now().date()
   tomorrow = datetime(d.year, d.month, d.day, 10)+timedelta(days=1)
   start = tomorrow.isoformat()
   end = (tomorrow + timedelta(hours=1)).isoformat()

   event_result = service.events().insert(calendarId='primary',
       body={
           "summary": 'Automating calendar',
           "description": 'This is a tutorial example of automating google calendar with python',
           "start": {"dateTime": start, "timeZone": 'Asia/Kolkata'},
           "end": {"dateTime": end, "timeZone": 'Asia/Kolkata'},
       }
   ).execute()

   print("created event")
   print("id: ", event_result['id'])
   print("summary: ", event_result['summary'])
   print("starts at: ", event_result['start']['dateTime'])
   print("ends at: ", event_result['end']['dateTime'])

def mevent(num_event):
   summary = hw.summary()
   desc = hw.desc()
   dates = hw.due()
   for i in range(len(dates)):
    date_string = dates[i]
    date = date_string.strip()
    d = datetime.strptime(date, '%m/%d/%y %I:%M %p')
    dates[i] = d
  
   summ = summary[num_event]
   des = desc[num_event]
   d = dates[num_event]
   start = d.isoformat()
   end = (d + timedelta(hours=1)).isoformat()
   
   service = get_calendar_service()
   event_result = service.events().insert(calendarId='primary',
       body={
           "summary": summ,
           "description": des,
           "start": {"dateTime": start, "timeZone": 'America/New_York'},
           "end": {"dateTime": end, "timeZone": 'America/New_York'},
       }
   ).execute()

   print("created event")
   print("id: ", event_result['id'])
   print("summary: ", event_result['summary'])
   print("starts at: ", event_result['start']['dateTime'])
   print("ends at: ", event_result['end']['dateTime'])
if __name__ == '__main__':
    mevent()
