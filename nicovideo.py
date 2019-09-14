import sqlite3
from contextlib import closing
import tempfile
from glob import glob
import shutil, os
from os.path import expanduser, join
from datetime import datetime
import pandas as pd

def search_nicovideo():
    dbfilelist = [expanduser("~/AppData/Local/Google/Chrome/User Data/Default/History")]
    dbfilelist += glob(expanduser("~/AppData/Local/Google/Chrome/User Data/Profile */History"))
    print(dbfilelist)
    ls = []
    with tempfile.TemporaryDirectory() as t:
        for filefrom in dbfilelist:
            fileto = join(t, 'temp.db')
            shutil.copyfile(filefrom, fileto)
            join(fileto, 'temp.db')
            with closing(sqlite3.connect(fileto)) as conn:
                c = conn.cursor()
                key = "http%://%nicovideo.jp/watch/%"
                for x in c.execute('select * from urls where url like ?', [key]):
                    time_ = datetime.fromtimestamp(x[-2] / 1000000 - 11644473600)
                    url = x[1].split('?')[0]
                    ls.append([
                        url, time_, x[2], x[3], url.split('/')[-1]
                    ])
    # ls.sort(key=lambda x:x[1], reverse=True)
    def drop(d):
        res = d.values.tolist()[0]
        res[3] = d[3].sum()
        return res
    df = pd.DataFrame(ls).groupby(0, as_index=False).apply(drop)
    return df.values.tolist()