https://amoffat.github.io/sh/

from sh import ifconfig 
print(ifconfig("wlan0"))


pip install sh

sh.ls("-l", "/tmp", color="never")
sh.ls(_out="/tmp/dir_contents")

with open("/tmp/dir_contents", "w") as h:
    sh.ls(_out=h)

from io import StringIO
buf = StringIO()
sh.ls(_out=buf)

# equivalent
sh.git("show", "HEAD")
sh.git.show("HEAD")

