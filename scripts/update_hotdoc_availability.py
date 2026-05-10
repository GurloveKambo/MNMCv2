#!/usr/bin/env python3
import json, re, datetime, pathlib, sys
from urllib.request import Request, urlopen
HOTDOC_URL='https://www.hotdoc.com.au/medical-centres/mount-nelson-TAS-7007/mt-nelson-medical-centre/doctors'
OUT=pathlib.Path('assets/hotdoc-availability.json')
DOCTOR_ALIASES={'Dr Jasmeen Kaur':['Dr Jasmeen Kaur'],'Dr Harpreet Kaur':['Dr. Harpreet Kaur','Dr Harpreet Kaur'],'Dr Huma Nadeem Iftikhar':['Dr Huma Iftikhar','Dr Huma Nadeem Iftikhar'],'Dr Shea Phillip Thrift':['Dr Shea Phillip Thrift','Dr Shea Thrift'],'Dr Abdul Ahmed Hussain':['Dr Abdul Ahmed Hussain','Dr Ahmed Abdul Hussain'],'Dr Christopher Roy-Chowdhury':['Dr Christopher Roy-Chowdhury']}
def clean(html):
    text=re.sub(r'<script[\s\S]*?</script>|<style[\s\S]*?</style>',' ',html,flags=re.I); text=re.sub(r'<[^>]+>',' ',text); return re.sub(r'\s+',' ',text)
def extract(text,aliases):
    for alias in aliases:
        pat=re.escape(alias)+r'.{0,400}?Appointments available from:\s*((?:Today|Tomorrow|Mon|Tue|Wed|Thu|Fri|Sat|Sun|\d{1,2}\s+[A-Z][a-z]{2,8})[^D]{0,60}?(?:am|pm))'
        m=re.search(pat,text,flags=re.I)
        if m: return re.sub(r'\s+',' ',m.group(1)).strip(' ,')
    return 'Check HotDoc'
def main():
    old={}
    if OUT.exists():
        try: old=json.loads(OUT.read_text())
        except Exception: old={}
    try:
        html=urlopen(Request(HOTDOC_URL,headers={'User-Agent':'Mozilla/5.0'}),timeout=30).read().decode('utf-8','ignore')
        text=clean(html); doctors={d:{'next':extract(text,a),'bookingUrl':HOTDOC_URL} for d,a in DOCTOR_ALIASES.items()}
        OUT.write_text(json.dumps({'source':HOTDOC_URL,'lastUpdated':datetime.datetime.now(datetime.timezone.utc).astimezone().isoformat(timespec='minutes'),'timezone':'Australia/Hobart','doctors':doctors},indent=2))
    except Exception as e:
        old['lastUpdated']='Refresh failed: '+datetime.datetime.utcnow().isoformat(timespec='minutes')+'Z'; old.setdefault('source',HOTDOC_URL); old.setdefault('doctors',{}); OUT.write_text(json.dumps(old,indent=2)); print(e,file=sys.stderr)
if __name__=='__main__': main()
