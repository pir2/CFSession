from CFSession import cfDirectory
from CFSession import cfSession
import os
if __name__ == "__main__":
    session = cfSession(version_main=114,directory=cfDirectory('./artificialDirectory'))
    res = session.get("https://nowsecure.nl") #A Cloudflare protected site
    print(res.content)
