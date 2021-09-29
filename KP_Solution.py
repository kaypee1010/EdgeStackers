import json
import datetime
from dateutil import tz

# Converts UTC to AEST


def covertUTCToAest(inp):

    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()

    utc = datetime.datetime.fromtimestamp(inp / 1e3)
    utc = utc.replace(tzinfo=from_zone)

    central = utc.astimezone(to_zone)

# Gets Event Details


def getEventDetails(events):

    eventList = []
    for event in events:
        eventList.append({
            "eventIDs": event["id"],
            "eventRaceNumbers": event["raceNumber"],
            "eventLinks": event["httpLink"],
            "eventDistance": event["distance"] if "distance" in event else None,
            "startTime": covertUTCToAest(event["startTime"])
        })

    return eventList


# Entry Point
def extract(jsonFile):

    out = []

    with open('response.json') as f:
        data = json.load(f)

        for race in data['dates'][0]['sections']:

            for meeting in race['meetings']:
                eventList = getEventDetails(meeting['events'])
                for eventInfo in eventList:
                    out.append({
                        "meeting_id":  meeting['id'],
                        "meeting_name": meeting['name'],
                        "race_number": eventInfo['eventRaceNumbers'],
                        "race_link": eventInfo['eventLinks'],
                        "event_id": eventInfo['eventIDs'],
                        "distance": eventInfo['eventDistance'],
                        "startTime": eventInfo['startTime']
                    })

    return out
