"""Plan text chunks within an approximate token budget."""
from __future__ import annotations
def estimate(text:str,chars_per_token:int=4)->int:return (len(text)+chars_per_token-1)//chars_per_token
def plan(chunks:list[str],budget:int,chars_per_token:int=4)->dict:
 selected=[];used=0
 for index,chunk in enumerate(chunks):
  cost=estimate(chunk,chars_per_token)
  if used+cost<=budget:selected.append(index);used+=cost
 return {'selected':selected,'used':used,'remaining':budget-used,'skipped':len(chunks)-len(selected)}
if __name__=='__main__':
 import json,sys;p=json.load(sys.stdin);print(json.dumps(plan(p['chunks'],p['budget'],p.get('chars_per_token',4)),indent=2))
