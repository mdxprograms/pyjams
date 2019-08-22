Samples.addPath('/Users/josh/Desktop')

s1 >> loop('test_break', rate=1.085, dur=8)

s2 >> play("(x[--])xo{-[--][-x]}", amp=0.8)

d1 >> play("X ", sample=6, amp=[[0.5, 1, 0.8, 0.6]])

d2 >> play("  {u,o} ", echo=1/4, room=5, amp=0.2)

ch = [0, 2, 5]

p1 >> pluck(P[0, 0, 2, 5], 
    dur=PDur([3, 8], 8), 
    oct=3, 
    sus=4, 
    room=2, 
    echo=2, 
    amp=[0.3, 0.4,0.7])
    
b1 >> bass(ch, dur=PDur([3, 8], 8), oct=[4,5], room=0.5)

k1 >> sinepad(ch, amp=[0.3, 0.7], room=5, echo=1, dur=PDur([3, 8], 8))



