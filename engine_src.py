from itertools import count
from collections import namedtuple
qa="2026-packed"
qb="sunfish "+qa
qc={"P":100,"N":280,"B":320,"R":479,"Q":929,"K":60000}
qd={
 'P':(0,0,0,0,0,0,0,0,
   78,83,86,73,102,82,85,90,
   7,29,21,44,40,31,44,7,
  -17,16,-2,15,14,0,15,-13,
  -26,3,10,9,6,1,0,-23,
  -22,9,5,-11,-10,-2,3,-19,
  -31,8,-7,-37,-36,-14,3,-31,
   0,0,0,0,0,0,0,0),
 'N':(-66,-53,-75,-75,-10,-55,-58,-70,
   -3,-6,100,-36,4,62,-4,-14,
   10,67,1,74,73,27,62,-2,
   24,24,45,37,33,41,25,17,
   -1,5,31,21,22,35,2,0,
  -18,10,13,22,18,15,11,-14,
  -23,-15,2,0,2,0,-23,-20,
  -74,-23,-26,-24,-19,-35,-22,-69),
 'B':(-59,-78,-82,-76,-23,-107,-37,-50,
  -11,20,35,-42,-39,31,2,-22,
   -9,39,-32,41,52,-10,28,-14,
   25,17,20,34,26,25,15,10,
   13,10,17,23,17,16,0,7,
   14,25,24,15,8,25,20,15,
   19,20,11,6,7,6,20,16,
   -7,2,-15,-12,-14,-15,-10,-10),
 'R':(35,29,33,4,37,33,56,50,
   55,29,56,67,55,62,34,60,
   19,35,28,33,45,27,25,15,
   0,5,16,13,18,-4,-9,-6,
  -28,-35,-16,-21,-13,-29,-46,-30,
  -42,-28,-42,-25,-25,-35,-26,-46,
  -53,-38,-31,-26,-29,-43,-44,-53,
  -30,-24,-18,5,-2,-18,-31,-32),
 'Q':(6,1,-8,-104,69,24,88,26,
   14,32,60,-10,20,76,57,24,
   -2,43,32,60,72,63,43,2,
   1,-16,22,17,25,20,-13,-6,
  -14,-15,-2,-5,-1,-10,-20,-22,
  -30,-6,-13,-11,-16,-11,-16,-27,
  -36,-18,0,-19,-15,-15,-21,-38,
  -39,-30,-31,-13,-31,-36,-34,-42),
 'K':(4,54,47,-99,-99,60,83,-62,
  -32,10,55,56,56,55,10,3,
  -62,12,-57,44,-67,28,37,-31,
  -55,50,11,-4,-19,13,0,-49,
  -55,-43,-52,-28,-51,-47,-8,-50,
  -47,-42,-43,-79,-64,-32,-29,-32,
   -4,3,-14,-50,-57,-18,13,4,
   17,30,-3,-14,6,-1,40,18),
}
for k,qe in qd.items():
 qf=lambda qg:(0,)+ tuple(x+qc[k]for x in qg)+(0,)
 qd[k]= sum((qf(qe[i*8:i*8+8])for i in range(8)),())
 qd[k]=(0,)* 20+qd[k]+(0,)* 20
qh,qi=qd["K"],tuple(qc["K"]+ 70
- 10 *(abs(2 *(i//10)- 11)+ abs(2 *(i%10)- 9))for i in range(120))
qj=60000-13*929
qk=60000+10*929
A1,H1,A8,H8=91,98,21,28
ql =(
 "         \n"
 "         \n"
 " rnbqkbnr\n"
 " pppppppp\n"
 " ........\n"
 " ........\n"
 " ........\n"
 " ........\n"
 " PPPPPPPP\n"
 " RNBQKBNR\n"
 "         \n"
 "         \n"
)
N,E,S,W=-10,1,10,-1
qm={
 "P":(N,N+N,N+W,N+E),
 "N":(N+N+E,E+N+E,E+S+E,S+S+E,S+S+W,W+S+W,W+N+W,N+N+W),
 "B":(N+E,S+E,S+W,N+W),
 "R":(N,E,S,W),
 "Q":(N,E,S,W,N+E,S+E,S+W,N+W),
 "K":(N,E,S,W,N+E,S+E,S+W,N+W)
}
QS=40
QS_A=140
EVAL_ROUGHNESS=15
qn=40
qo=60
TABLE_SIZE=10**6
qp=dict(
 QS =(0,300),
 QS_A =(0,300),
 EVAL_ROUGHNESS =(0,50),
 TABLE_SIZE =(10**4,10**8),
)
qq=namedtuple("Move","i j prom")
class qr(namedtuple("qr","board score wc bc ep kp")):
 def __hash__(qs):
  return hash((qs.board,qs.wc,qs.bc,qs.ep,qs.kp))
 def __eq__(qs,o):
  return(qs.board == o.board and qs.ep == o.ep and qs.kp == o.kp
    and qs.wc == o.wc and qs.bc == o.bc)
 def __ne__(qs,o):
  return not qs.__eq__(o)
 def gen_moves(qs):
  for i,p in enumerate(qs.board):
   if p not in "PNBRQK":
    continue
   for d in qm[p]:
    for j in count(i+d,d):
     q=qs.board[j]
     if q in " \nPNBRQK":
      break
     if p == "P":
      if d in(N,N+N)and q != ".":break
      if d == N+N and(i<A1+N or qs.board[i+N]!= "."):break
      if(
       d in(N+W,N+E)
       and q == "."
       and j not in(qs.ep,qs.kp,qs.kp-1,qs.kp+1)
      ):
       break
      if A8 <= j <= H8:
       for prom in "NBRQ":
        yield qq(i,j,prom)
       break
     yield qq(i,j,"")
     if p in "PNK" or q in "pnbrqk":
      break
     if i == A1 and qs.board[j+E]== "K" and qs.wc[0]:
      yield qq(j+E,j+W,"")
     if i == H1 and qs.board[j+W]== "K" and qs.wc[1]:
      yield qq(j+W,j+E,"")
 def rotate(qs,nullmove=False):
  return qr(
   qs.board[::-1].swapcase(),-qs.score,qs.bc,qs.wc,
   119-qs.ep if qs.ep and not nullmove else 0,
   119-qs.kp if qs.kp and not nullmove else 0,
  )
 def move(qs,move):
  i,j,prom=move
  p,q=qs.board[i],qs.board[j]
  qt=lambda board,i,p:board[:i]+ p+board[i+1:]
  board=qs.board
  wc,bc,ep,kp=qs.wc,qs.bc,0,0
  score=qs.score+qs.value(move)
  board=qt(board,j,board[i])
  board=qt(board,i,".")
  wc =(wc[0]and i != A1,wc[1]and i != H1)
  bc =(bc[0]and j != H8,bc[1]and j != A8)
  if p == "K":
   wc =(False,False)
   if abs(j-i)== 2:
    kp =(i+j)// 2
    r=A1 if j<i else H1
    board=qt(board,r,".")
    board=qt(board,kp,"R")
  if p == "P":
   if A8 <= j <= H8:
    board=qt(board,j,prom)
   if j-i == 2*N:
    ep=i+N
   if j == qs.ep:
    board=qt(board,j+S,".")
  return qr(board[::-1].swapcase(),-score,bc,wc,
      119-ep if ep else 0,119-kp if kp else 0)
 def value(qs,move):
  i,j,prom=move
  p,q=qs.board[i],qs.board[j]
  score=qd[p][j]- qd[p][i]
  if q in "pnbrqk":
   score += qd[q.upper()][119-j]
  if abs(j-qs.kp)< 2:
   score += qd["K"][119-j]
  if p == "K" and abs(i-j)== 2:
   score += qd["R"][(i+j)// 2]
   score -= qd["R"][A1 if j<i else H1]
  if p == "P":
   if A8 <= j <= H8:
    score += qd[prom][j]- qd["P"][j]
   if j == qs.ep:
    score += qd["P"][119 -(j+S)]
  return score
 def king_capture(qs):
  return next((m for m in qs.gen_moves()
     if qs.board[m.j]== "k" or abs(m.j-qs.kp)< 2),None)
class qu(Exception):pass
qv=namedtuple("Entry","lower upper")
class qw:
 def __init__(qs):
  qs.tp_score,qs.tp_move,qs.history={},{},set()
  qs.nodes,qs.deadline=0,1 << 63
  qs.node_cap=1<<62
 def bound(qs,qx,qy,qz,root=False):
  qs.nodes += 1
  if qs.nodes%2048 == 0 and qs.nodes>qs.node_cap:raise qu
  qz=max(qz,0)
  if qx.score <= -qj:
   return -qk
  if not root:
   qba=qs.tp_score.get((qx,qz),qv(-qk,qk))
   if qba.lower >= qy:return qba.lower
   if qba.upper<qy:return qba.upper
   if qz>0 and qx in qs.history:return 0
  def qbb():
   qbc=qs.tp_move.get(qx)
   if not root and qz>2 and abs(qx.score)< 500 and any(c in qx.board for c in "RBNQ"):
    score=-qs.bound(qx.rotate(nullmove=True),1-qy,qz-3)
    qbd=score >= qy and(qs.tp_move.get(qx)or qx.king_capture())
    if qbd and qx.value(qbd)>= qj:
     yield qbd,qk
    elif score<qy or qs.bound(qx.rotate(nullmove=True),
      1-qj,qz-3)>= 1-qj:
     yield None,score
   if qz == 0:
    yield None,qx.score
   if not qbc and qz>2:
    qs.bound(qx,qy,qz-3,root=True)
    qbc=qs.tp_move.get(qx)
   qbe=QS-qz*QS_A
   if qbc and qx.value(qbc)>= qbe:
    yield qbc,-qs.bound(qx.move(qbc),1-qy,qz-1)
   for qbf,(qbg,move)in enumerate(sorted(((v,m)for m in qx.gen_moves()
         if(v:=qx.value(m))>= qbe),reverse=True)):
    if qz <= 1 and qx.score+qbg<qy:
     yield(move,qk)if qbg >= qj else(None,qx.score+qbg)
     break
    qbh=qo and qz>2 and qbf>2 and qbg<qo
    score=-qs.bound(qx.move(move),1-qy,qz-2 if qbh else qz-1)
    if qbh and score >= qy:
     score=-qs.bound(qx.move(move),1-qy,qz-1)
    yield move,score
  qbi,qbj=-qk,False
  for move,score in qbb():
   qbi=max(qbi,score)
   qbj |= move is not None and score>-qk
   if qbi >= qy:
    if move is not None and qz:
     qs.tp_move[qx]= move
     if len(qs.tp_move)> TABLE_SIZE:
      del qs.tp_move[next(k for k in qs.tp_move if k != qs.root)]
    break
  if qz and not qbj and all(
    qx.move(m).king_capture()for m in qx.gen_moves()):
   qbi=-qj if qx.rotate(nullmove=True).king_capture()else 0
  if not root:
   qs.tp_score[qx,qz]= qv(qbi,qba.upper)if qbi >= qy else qv(qba.lower,qbi)
  if len(qs.tp_score)> TABLE_SIZE:
   del qs.tp_score[next(iter(qs.tp_score))]
  return qbi
 def search(qs,history):
  qs.nodes,qs.history=0,set(history)
  qs.tp_score.clear()
  qx=qs.root=history[-1]
  qbk=sum(c.isupper()for c in qx.board)== 1 or sum(c.islower()for c in qx.board)== 1
  qd["K"]= qi if qbk else qh
  qy=0
  for qz in range(1,1000):
   lower,upper,qbl=1-qk,qk,0
   while lower<upper-EVAL_ROUGHNESS:
    score=qs.bound(qx,qy,qz,root=True)
    if score >= qy:lower=max(lower,score)
    else:upper=min(upper,score)
    qbl += 1
    yield qz,qy,score,qs.tp_move.get(qx)
    if lower>upper or qbl>qn:
     break
    qy =(lower+upper+1)// 2
def qbm(c):return A1+ord(c[0])- ord("a")- 10 *(int(c[1])- 1)
def qbn(i):return chr((i-A1)%10+ord("a"))+ str(1 -(i-A1)//10)
def qbo(board,wc=(True,True),bc=(True,True),ep=0,kp=0):
 score=sum(qd[p][i]if p.isupper()else -qd[p.upper()][119-i]
    for i,p in enumerate(board)if p.isalpha())
 return qr(board,score,wc,bc,ep,kp)
qbp =[qbo(ql)]
qbq=50000
import json as _json,urllib.request as _u,os as _os
def qbr(qbs,qbt):
 qbu=_u.Request(_os.environ["MAKEFUN_ENV_URL"]+ qbs,data=_json.dumps(qbt).encode(),headers={"content-type":"application/json"})
 with _u.urlopen(qbu)as qbv:
  return _json.load(qbv)
def qbw(qbx):
 qby=qbx.split()
 qbz=qby[0].split("/")
 qca=9*" "+chr(10)
 def qcb(r):
  qcc=""
  for ch in r:
   if ch.isdigit():
    qcc += "."*int(ch)
   else:
    qcc += ch
  return " "+qcc
 if qby[1]== "w":
  board=qca+qca+chr(10).join(qcb(r)for r in qbz)+ chr(10)+ qca+qca
 else:
  qcd =[qcb(r)[1:][::-1].swapcase()for r in qbz[::-1]]
  board=qca+qca+chr(10).join(qcb(r)for r in qcd)+ chr(10)+ qca+qca
 if qby[1]== "w":
  wc =("K" in qby[2],"Q" in qby[2])
  bc =("k" in qby[2],"q" in qby[2])
 else:
  wc =("k" in qby[2],"q" in qby[2])
  bc =("K" in qby[2],"Q" in qby[2])
 return qbo(board,wc,bc,0,0),qby[1]== "w"
def qce(qx):
 qbz=qx.board.split(chr(10))
 upper=sum(ch.isupper()for ch in chr(10).join(qbz[2:6]))
 lower=sum(ch.isupper()for ch in chr(10).join(qbz[6:10]))
 return lower >= upper
def qcf(qx,qcg,qch):
 qci=qcg
 if not qci:
  i0,j0=qbm(qch[:2]),qbm(qch[2:4])
  i,j=119-i0,119-j0
 else:
  i,j=qbm(qch[:2]),qbm(qch[2:4])
 prom=qch[4:].upper()
 return qx.move(qq(i,j,prom)),not qcg
qcj=qw()
qck={}
qcl={}
while True:
 g=qbr("/game",{})
 if g["status"]== "done":
  break
 qbb =[u for u in g.get("moves",[])if len(u)>= 4]
 n=g["game"]
 if n not in qck:
  p,qcg=qbw(g["fen"])
  qck[n]=[p,len(qbb)]
  qcl[n]= qcg
 else:
  p,qcm=qck[n]
  qcg=qcl[n]
  for u in qbb[qcm:]:
   p,qcg=qcf(p,qcg,u)
  qck[n]=[p,len(qbb)]
 if g["status"]== "your_move":
  qcj.node_cap=qbq
  qbi=qcn=None
  try:
   for qz,qy,score,move in qcj.search([qck[n][0]]):
    if qbq and qcj.nodes >= qbq and qcn:
     break
    if score >= qy:
     ii,jj=move.i,move.j
     if not qcl[n]:
      ii,jj=119-ii,119-jj
     qcn=qbn(ii)+ qbn(jj)+ move.prom.lower()
  except qu:
   pass
  mv=qcn
  if not mv:
   break
  g=qbr("/move",{"game":n,"move":mv})
  p,qco=qcf(qck[n][0],qcl[n],mv)
  qcl[n]= qco
  qcp =[u for u in g.get("moves",[])if len(u)>= 4]
  qcm=qck[n][1]
  for u in qcp[qcm+1:]:
   p,qco=qcf(p,qco,u)
  qcl[n]= qco
  qck[n]=[p,len(qcp)]
