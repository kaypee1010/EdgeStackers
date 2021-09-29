# EdgeStackers
To extract the race details for each Australian horse racing racing on the day, pass Location of json as input.

To call the function,
  Syntax - extract(location_of_json)
    where extract is the function call.


 Each meeting has multiple events.
 Each event has multiple race.
 
Returns a dictionary with

- meeting_id
- meeting_name - race_number
- race_link
- event_id
- distance
- start_time ( in AEST iso format )
