import sqlite3
import argparse
import json
import sys,os

class AddAuthorAction(argparse.Action):

    def __init__(self, option_strings, dest, **kwargs):
        super(AddAuthorAction, self).__init__(option_strings, dest, **kwargs)
    def __call__(self, parser, namespace, values, option_string=None):

        conn = sqlite3.connect(os.path.dirname(sys.argv[0])+'/woscopus.db')
        c = conn.cursor()
        dicAuth = json.loads(values)
        cols = dicAuth.keys()
        c.execute("INSERT INTO authors({keys}) VALUES ({vals})".format(
                keys=",".join(cols),vals=",".join(["?"]*len(cols)))
            ,[dicAuth[c] for c in cols])
        conn.commit()
        conn.close() 
        setattr(namespace, self.dest, values)

class SyncAction(argparse.Action):
    def __init__(self, **kwargs):
        super(SyncAction, self).__init__( **kwargs)
    def __call__(self, parser, namespace, values, option_string=None):

        conn = sqlite3.connect(os.path.dirname(sys.argv[0])+'/woscopus.db')
        c = conn.cursor()
        #TODO: ponerle estilo
        print '<table>'
        print '<thead><tr><th>Author Id</th><th>Nombre Completo</th><th>Scopus_id</th><th>WOS id</th></tr></thead>'
        for auid, fullname, scopus_id, wos_id in c.execute("SELECT auid, fullname, scopus_id, wos_id FROM authors"):
            print "<tr><td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td></tr>".format(auid, fullname, scopus_id, wos_id)
        print "</table>"
        #TODO: hacer las sincronizaciones
        conn.close() 

class GetPubsAction(argparse.Action):
    def __init__(self, **kwargs):
        super(GetPubsAction, self).__init__( **kwargs)
    def __call__(self, parser, namespace, values, option_string=None):
        conn = sqlite3.connect(os.path.dirname(sys.argv[0])+'/woscopus.db')
        c = conn.cursor()
        #TODO: ponerle estilo
        print "<ul>"
        #TODO: hacer que se ve bonito
        for auid, pub_id in c.execute("SELECT auid, pub_id FROM authors_pub WHERE auid = ?",(values,)):
            authors,title,year,source,pagerange,indx,volume = list(c.execute("SELECT authors,title,year,source,pagerange,indx,volume FROM pub WHERE pub_id = ?",(pub_id,)))[0]
            print "<li><span>{authors}({year}). {title} <i>{source}</i>, <i>{volume}</i>, {pagerange}. {index}</span></li>".format(
                    authors=authors,
                    year=year,
                    title=title,
                    source=source,
                    volume=volume,
                    pagerange=pagerange,
                    index=", ".join([k+': '+v for k,v in json.loads(indx).items()])
                )
        print "</ul>"
        #TODO: hacer las sincronizaciones
        conn.close() 

if __name__ == '__main__':
    conn = sqlite3.connect(os.path.dirname(sys.argv[0])+'/woscopus.db')
    c = conn.cursor()
    # Create table
    c.execute('''CREATE TABLE IF NOT EXISTS authors
         (auid text NOT NULL UNIQUE,
         fullname text NOT NULL,
         scopus_id text,
         wos_id text,
         CONSTRAINT auid_unique UNIQUE (auid)
         )
         ''')

    c.execute('''CREATE TABLE IF NOT EXISTS pub
        (pub_id INTEGER PRIMARY KEY AUTOINCREMENT,
         authors text NOT NULL,
         title text NOT NULL,
         year INTEGER NOT NULL,
         source text,
         pagerange text,
         indx text, volume INTEGER)''')

    c.execute('''CREATE TABLE IF NOT EXISTS authors_pub
        (auid text NOT NULL, pub_id INTEGER NOT NULL,
        CONSTRAINT rel_unique UNIQUE (auid,pub_id))''')
    """
    c.execute('''INSERT INTO pub(authors, title, year, source, pagerange, indx, volume)
        VALUES (?,?,?,?,?,?,?)''',["Loor, Fernando; Gil-Costa, Veronica; Marin, Mauricio",
    "Processing Collections of Geo-Referenced Images for Natural Disasters",
    2018,
    "JOURNAL OF COMPUTER SCIENCE & TECHNOLOGY"  ,
    "193-202",
    '{"DOI":"10.24215/16666038.18.e22"}',
    18])

    c.execute('''INSERT INTO authors_pub VALUES (?,?)''',["mmarin",1])
    """
    conn.commit()
    conn.close() 

    parser = argparse.ArgumentParser()
    #ex: python main.py -a '{"auid":"nmora","fullname":"Nestor Mora","wos_id":"3352579"}'
    parser.add_argument('-a', '--addauth' , type=str, action=AddAuthorAction)
    parser.add_argument('-s', '--sync' , action=SyncAction)
    parser.add_argument('-g', '--getpubs' , type=str, action=GetPubsAction)
    args = parser.parse_args()
    
    
    
    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
       