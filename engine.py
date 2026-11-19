import json,os,sys,urllib.request,urllib.error
U=os.environ.get("MAKEFUN_ENV_URL") or sys.exit("no env")
V=(0,100,320,330,500,900,0)
B=[0]*128;S=1;C=0;E=-1;K=[4,116];ST=[];TT={};KL=[[0,0] for _ in range(128)];N=0;LIM=20000
class A(Exception):pass
def at(q,by):
 for o in ((-15,-17) if by>0 else (15,17)):
  t=q+o
  if 0<=t<128 and not t&136 and B[t]==(1 if by>0 else 7):return 1
 for o in (-33,-31,-18,-14,14,18,31,33):
  t=q+o
  if 0<=t<128 and not t&136 and B[t]==(2 if by>0 else 8):return 1
 for o in (-17,-16,-15,-1,1,15,16,17):
  t=q+o
  if 0<=t<128 and not t&136 and B[t]==(6 if by>0 else 12):return 1
 for o in (-17,-15,15,17):
  t=q+o
  while 0<=t<128 and not t&136:
   v=B[t]
   if v:return 1 if v==(3 if by>0 else 9) or v==(5 if by>0 else 11) else 0
   t+=o
 for o in (-16,-1,1,16):
  t=q+o
  while 0<=t<128 and not t&136:
   v=B[t]
   if v:return 1 if v==(4 if by>0 else 10) or v==(5 if by>0 else 11) else 0
   t+=o
 return 0
def gen(cp):
 M=[]
 for s in range(128):
  if s&136:continue
  c=B[s]
  if not c or (c<7)!=(S>0):continue
  t=c if c<7 else c-6
  if t==1:
   d=16*S;r=s>>4;pr=6 if S>0 else 1;sr=1 if S>0 else 6;q=s+d
   if not B[q]:
    if r==pr:
     for p in (5,2):M.append(s+q*128+p*16384)
    elif not cp:
     M.append(s+q*128)
     if r==sr and not B[q+d]:M.append(s+(q+d)*128)
   for o in (-1,1):
    q=s+d+o
    if q<0 or q>127 or q&136:continue
    v=B[q]
    if (v and (v<7)!=(S>0)) or q==E:
     if r==pr:
      for p in (5,2):M.append(s+q*128+p*16384)
     else:M.append(s+q*128)
  elif t==2 or t==6:
   D=(-33,-31,-18,-14,14,18,31,33) if t==2 else (-17,-16,-15,-1,1,15,16,17)
   for o in D:
    q=s+o
    if q<0 or q>127 or q&136:continue
    v=B[q]
    if not v:
     if not cp:M.append(s+q*128)
    elif (v<7)!=(S>0):M.append(s+q*128)
   if t==6 and not cp:
    if S>0 and s==4:
     if C&1 and not B[5] and not B[6] and B[7]==4 and not at(4,-1) and not at(5,-1) and not at(6,-1):M.append(6*128+4)
     if C&2 and not B[3] and not B[2] and not B[1] and B[0]==4 and not at(4,-1) and not at(3,-1) and not at(2,-1):M.append(2*128+4)
    if S<0 and s==116:
     if C&4 and not B[117] and not B[118] and B[119]==10 and not at(116,1) and not at(117,1) and not at(118,1):M.append(118*128+116)
     if C&8 and not B[115] and not B[114] and not B[113] and B[112]==10 and not at(116,1) and not at(115,1) and not at(114,1):M.append(114*128+116)
  else:
   D=(-17,-15,15,17) if t==3 else (-16,-1,1,16) if t==4 else (-17,-16,-15,-1,1,15,16,17)
   for o in D:
    q=s+o
    while 0<=q<128 and not q&136:
     v=B[q]
     if not v:
      if not cp:M.append(s+q*128)
     else:
      if (v<7)!=(S>0):M.append(s+q*128)
      break
     q+=o
 return M
def mk(m):
 global S,C,E
 f=m&127;t=m>>7&127;p=m>>14;x=B[f];a=x if x<7 else x-6;cap=B[t];cs=-1
 if a==1 and t==E and not cap:cs=t-16*S;cap=B[cs];B[cs]=0
 ST.append((m,cap,cs,C,E,K[0],K[1]));B[t]=x if not p else p+(0 if S>0 else 6);B[f]=0
 if a==6:
  K[0 if S>0 else 1]=t
  if t-f==2:B[t-1]=B[t+1];B[t+1]=0
  elif f-t==2:B[t+1]=B[t-3];B[t-3]=0
  C&=12 if S>0 else 3
 if f==0 or t==0:C&=~2
 if f==7 or t==7:C&=~1
 if f==112 or t==112:C&=~8
 if f==119 or t==119:C&=~4
 E=(f+t)//2 if a==1 and abs(t-f)==32 else -1;S=-S
def un(m):
 global S,C,E
 mm,cap,cs,c0,e0,k0,k1=ST.pop();f=mm&127;t=mm>>7&127;p=mm>>14;S=-S;x=B[t]
 B[f]=x if not p else 1 if S>0 else 7;B[t]=cap
 if cs>=0:B[cs]=cap;B[t]=0
 if (x if x<7 else x-6)==6:
  if t-f==2:B[t+1]=B[t-1];B[t-1]=0
  elif f-t==2:B[t-3]=B[t+1];B[t+1]=0
 C,E,K[0],K[1]=c0,e0,k0,k1
def ev():
 s=0;tot=0;nb=[0,0]
 for q in range(128):
  if q&136:continue
  c=B[q]
  if not c:continue
  t=c if c<7 else c-6;w=c<7;f=q&7;r=q>>4;rr=r if w else 7-r;v=V[t];tot+=v;s+=v if w else -v;ce=6-abs(f-3)-abs(rr-3);sg=1 if w else -1
  if t==1:s+=(6*rr+2*(3-abs(f-3)))*sg
  elif t==2:s+=ce*4*sg
  elif t==3:s+=ce*3*sg;nb[0 if w else 1]+=1
  elif t==4:s+=(10 if rr==6 else 0)*sg
  elif t==5:s+=ce*2*sg
 s+=30 if nb[0]==2 else 0;s-=30 if nb[1]==2 else 0
 for i in (0,1):
  q=K[i];f=q&7;r=q>>4;rr=r if i==0 else 7-r;ce=6-abs(f-3)-abs(rr-3);s+=(ce*6-12 if tot<1400 else -ce*3)*(1 if i==0 else -1)
 return s
def ordm(ms,tm,pl):
 def sc(m):
  t=m>>7&127;v=B[t]
  if m==tm:return 999999
  if v:return 10000+V[v if v<7 else v-6]*10-V[B[m&127] if B[m&127]<7 else B[m&127]-6]
  if m==KL[pl][0]:return 9000
  if m==KL[pl][1]:return 8000
  return 0
 return sorted(ms,key=sc,reverse=True)
def qs(a,b,pl):
 global N
 N+=1
 if N>LIM:raise A
 st=ev()*S
 if st>=b:return b
 if st>a:a=st
 if pl>16:return a
 ck=at(K[0 if S>0 else 1],-S);ms=gen(0) if ck else gen(1);lg=0
 for m in ordm(ms,0,pl):
  mk(m)
  if at(K[0 if S<0 else 1],S):un(m);continue
  lg+=1;sc=-qs(-b,-a,pl+1);un(m)
  if sc>a:a=sc
  if a>=b:return a
 if ck and not lg:return -100000+pl
 return a
def sr(d,a,b,pl):
 global N
 N+=1
 if N>LIM:raise A
 if d<=0:return qs(a,b,pl)
 k=bytes(B)+bytes((C,E+1 if E>=0 else 0,0 if S>0 else 1));e=TT.get(k);tm=0;ao=a
 if e and e[0]>=d:
  tm=e[3]
  if e[1]==0:return e[2]
  if e[1]==1 and e[2]>=b:return e[2]
  if e[1]==2 and e[2]<=a:return e[2]
 ms=gen(0);best=-10**9;bm=0;lg=0
 for m in ordm(ms,tm,pl):
  f=m&127;t=m>>7&127;cp=B[t]!=0 or (B[f]==1 or B[f]==7) and t==E
  mk(m)
  if at(K[0 if S<0 else 1],S):un(m);continue
  lg+=1;sc=-sr(d-1,-b,-a,pl+1);un(m)
  if sc>best:best=sc;bm=m
  if sc>a:a=sc
  if a>=b:
   if not cp and m!=KL[pl][0]:KL[pl][1]=KL[pl][0];KL[pl][0]=m
   break
 if not lg:return -100000+pl if at(K[0 if S>0 else 1],-S) else 0
 if len(TT)<150000:TT[k]=(d,best,0 if best<=ao else 1 if best>=b else 2,bm) if best>ao and best<b else (d,best,1 if best>=b else 2,bm)
 return best
def parse(f):
 global B,S,C,E,K
 p=f.split();B=[0]*128;K=[4,116];r=7;fl=0
 for ch in p[0]:
  if ch=='/':r-=1;fl=0
  elif ch.isdigit():fl+=int(ch)
  else:
   c='PNBRQK'.index(ch.upper())+1
   if ch.islower():c+=6
   B[r*16+fl]=c;fl+=1
 S=1 if p[1]=='w' else -1;C=0
 if 'K' in p[2]:C|=1
 if 'Q' in p[2]:C|=2
 if 'k' in p[2]:C|=4
 if 'q' in p[2]:C|=8
 E=-1 if p[3]=='-' else (ord(p[3][0])-97)+(int(p[3][1])-1)*16
 for q in range(128):
  if B[q]==6:K[0]=q
  if B[q]==12:K[1]=q
def root(lg):
 global N,TT,KL
 TT={};KL=[[0,0] for _ in range(128)];N=0;bm=0
 ms=[]
 for u in lg:
  f=(ord(u[0])-97)+(int(u[1])-1)*16;t=(ord(u[2])-97)+(int(u[3])-1)*16;p=0
  if len(u)==5:p={'q':5,'r':4,'b':3,'n':2}[u[4]]
  ms.append(f+t*128+p*16384)
 ms=ordm(ms,0,0);bm=ms[0]
 for d in range(1,7):
  try:
   al=-10**9;cur=bm
   for m in ms:
    mk(m);sc=-sr(d-1,-10**9,-al,1);un(m)
    if sc>al:al=sc;cur=m
   bm=cur
  except A:break
 return bm
def post(p,b):
 req=urllib.request.Request(U+p,data=json.dumps(b).encode(),headers={'content-type':'application/json'})
 try:
  with urllib.request.urlopen(req) as r:return json.load(r)
 except urllib.error.HTTPError as e:sys.exit(f"{p}: HTTP {e.code}")
#---loop---
while True:
 g=post('/game',{})
 if g['status']=='done':break
 while g['status']=='your_move':
  parse(g['fen']);m=root(g['legal_moves']);f=m&127;t=(m>>7)&127;u=chr(97+(f&7))+str((f>>4)+1)+chr(97+(t&7))+str((t>>4)+1)
  if m>>14:u+="  nbrq"[m>>14]
  g=post('/move',{'game':g['game'],'move':u})
 print(f"game {g['game']}: {g['outcome']} by {g['reason']}",file=sys.stderr)
print(f"done: {g.get('wins')} won, {g.get('draws')} drawn, {g.get('losses')} lost",file=sys.stderr)
