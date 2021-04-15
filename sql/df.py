import pandas as pd
import numpy as np

df = pd.DataFrame([])
userid = list(set(df.userid))
eventid = list(set(df.eventid))
query = list(set(df.query))

results = []
for uid in userid:
    for eid in eventid:
        for q in query:
            url = df[df.uid==uid&df.eid==eid&df.query==q].url
            url = url.to_numpy()

            results.append([uid,eid,q,np.sum(url,axis=1)])
results = pd.DataFrame(results)
results.colnames = ['UserId','EventID','Query','URLClick']
