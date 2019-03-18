import json
import datetime
import peewee

import models as db
import requests
__author__ = "Brandon Duke"

__version__ = ""
__email__ = "http://bduke.net"


insert = []
now = datetime.datetime.now()
r = requests.get("https://www.thebluealliance.com/api/v3/team/frc3492/events/" + str(now.year), headers={"X-TBA-Auth-Key": "vOi134WDqMjUjGslV08r9ElOGoiWAU8LtSMxMBPziTVertNPmsdUqBOY8cYnyb7u"})
r = json.loads(r.text)

for e in r:
    print(e)
    insert.append(db.event(event_nm=e['name'], date_st=e['start_date'], date_end=e['end_date'], event_cd=e['key']))

    s = requests.get("https://www.thebluealliance.com/api/v3/event/" + e['key'] + "/teams", headers={"X-TBA-Auth-Key": "vOi134WDqMjUjGslV08r9ElOGoiWAU8LtSMxMBPziTVertNPmsdUqBOY8cYnyb7u"})
    s = json.loads(s.text)
    print(s)

    for t in s:
        insert.append(db.team(team_no=t['team_number'], team_nm=t['nickname']))
        insert.append(db.event_team_xref(team_no=t['team_number'], event_id=(db.event.select(db.event.event_id).where(db.event.event_cd == e['key']))))


for i in insert:
    try:
        i.save(force_insert=True)
    except peewee.IntegrityError:
        print("already in there")
    print(i)
