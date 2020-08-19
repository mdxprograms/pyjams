Clock.bpm = 93

d1 >> play(var(["x ", "    [x,x]"], dur=0.5), room=0.5, compress=1)

d2 >> play("--o---o---o---o-", room=0.3, compress=0.5)

b1 >> bass(var([-6, -6, -4, -2], dur=4), chop=[2,[3,4],2,[0,3]], compress=0.5, dist=0.2)

c1 >> pluck(var([-6, -6, -4, -2], dur=4), compress=0.5, amp=0.5)

