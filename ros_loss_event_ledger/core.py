import math
from .common import number,integer,identifier,unique_ids
def run(d):
 events=d['events']
 if len(events)>10000:raise ValueError('events')
 seen={};totals={};duplicates=[];conflicts=[]
 for event in events:
  eid=identifier(event['id']);counts=event['lost'];number(event['time'])
  if not isinstance(counts,dict):raise ValueError('counts')
  clean={identifier(k):integer(v,0,10**9)for k,v in counts.items()}
  if eid in seen:
   if seen[eid]!=clean:conflicts.append(eid)
   else:duplicates.append(eid)
   continue
  seen[eid]=clean
  for topic,count in clean.items():totals[topic]=totals.get(topic,0)+count
 return dict(observed_incremental_losses=totals,duplicate_events=duplicates,conflicting_event_ids=conflicts,complete=not conflicts and d.get('coverage_complete')is True,absence_means_zero=False)
