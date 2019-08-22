Clock.bpm = 120

d1 >> play("X ", room=1)
d2 >> play(" -O- -O  -O- -O  -O- -O  -O-[oO]-O ", room=1)
d3 >> play("_[nn]", rate=(0.5, 0.8), amp=(0.5, 0.6), room=1, amplify=0.8)

b1 >> bass(var([-4, -2, 0, 3, 2, 5, -4, [-6, -2]]), dur=3/4, dist=0.2, amp=0.3, oct=[5, 6])

p1 >> pluck(dur=1/2, sus=0.2, blur=[1, 2], amp=0.6).follow(b1)

k1 >> klank(sus=0.5).follow(b1)
