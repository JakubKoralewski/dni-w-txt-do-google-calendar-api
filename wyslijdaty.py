"""Dodaje daty z pliku zdobadzdaty.py do kalendarza Google"""
from __future__ import print_function
import datetime
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# zdobadz variable daty ze zdobadzdaty.py
from zdobadzdaty import daty

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/calendar'


def jakiMiesiac(miesiac):
    if not isinstance(miesiac, str):
        return 'miesiac nie jest stringiem'
    miesiac = miesiac.lower()
    if miesiac == 'stycznia':
        return 1
    elif miesiac == 'lutego':
        return 2
    elif miesiac == 'marca':
        return 3
    elif miesiac == 'kwietnia':
        return 4
    elif miesiac == 'maja':
        return 5
    elif miesiac == 'czerwca':
        return 6
    elif miesiac == 'lipca':
        return 7
    elif miesiac == 'sierpnia':
        return 8
    elif miesiac == 'września':
        return 9
    elif miesiac == 'października':
        return 10
    elif miesiac == 'listopada':
        return 11
    elif miesiac == 'grudnia':
        return 12
    else:
        return '{} to nie miesiac'.format(miesiac)


def main():
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('calendar', 'v3', http=creds.authorize(Http()))
    for data in daty:
        miesiac = data[1]
        dzien = data[0]
        miesiac = jakiMiesiac(data[1])
        if int(miesiac) < 10:
            miesiac = '0'+str(miesiac)
        else:
            miesiac = str(miesiac)

        event = {
            'summary': 'Twój tytuł.',
            'description': 'By Jakub Koralewski xD',
            'start': {
                'date': "2018-{month}-{day}".format(month=miesiac, day=dzien),
            },
            'end': {
                'date': "2018-{month}-{day}".format(month=miesiac, day=dzien),
            },
        }
        print(event)
        event = service.events().insert(calendarId='primary', body=event).execute()
        print('Event created: {}'.format(event.get('htmlLink')))


if __name__ == '__main__':
    main()
