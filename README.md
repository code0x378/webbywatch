----

**NOTE**

Project moved to source hut:
https://git.sr.ht/~code0x378/webbywatch

----

WebbyWatch is a simple web page change notifier.  It just watches web pages then sends an email (and logs) 
when keywords are no longer included in the page content.  I use it to be notified when products are available again.

# Requirements

* python 3

# Installation

Rename settings.example.py to settings.py and edit the content as needed

```
python -m venv venv
. venv/bin/activate
pip install -r requirements.txt
python webbywatch.py
```


