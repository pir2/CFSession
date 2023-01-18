import CFSession
from CFSession import cfDirectory
import os

if __name__ == "__main__": 
    session = CFSession.cfSession(directory=cfDirectory(chromedriver_path=os.path.join(os.path.dirname(__file__), "bin/chromedriver108.exe")))
    print(os.path.join(os.path.dirname(__file__), "bin","chromedriver108.exe"))
    res = session.get("https://nowsecure.nl") #A Cloudflare protected site
    print(res.content)

    #Context Manager
    with CFSession.cfSession() as session:
        res = session.get("https://nowsecure.nl")
        print(res.content)

