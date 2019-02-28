import json

import models as db
import requests
__author__ = "Brandon Duke"

__version__ = ""
__email__ = "http://bduke.net"


insert = []

r = requests.get("https://www.thebluealliance.com/api/v3/event/2019ohmv/teams", headers={"X-TBA-Auth-Key" : "vOi134WDqMjUjGslV08r9ElOGoiWAU8LtSMxMBPziTVertNPmsdUqBOY8cYnyb7u"})
r = json.loads(r.text)

for t in r:
    #insert.append(db.team(team_no=t['team_number'], team_nm=t['nickname']))

    insert.append(db.event_team_xref(team_no=t['team_number'], event_id=4))

#insert.append(db.event(event_nm='Miami Valley Regional', date_st='2019-03-06', date_end='2019-03-09'))

for i in insert:
    i.save(force_insert=True)
    print(i)


