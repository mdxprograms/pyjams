ch = var(4, [4,5])

b2 >> play("X ", dist=0.2)

b3 >> play("-------{r,=}", dist=[0, 0.3, 0.5])

b4 >> play(["  t ", "  tt", " {V,d} v"], dist=[0, 0.3, 0.5])

b5 >> play(P[ch].amen(), echo=1.5, amplify=[0, 0.3])

p1 >> play(P["v-o-"].amen())

p2 >> sinepad([4, -2, [2,3]], oct=3, dur=[6/8], room=10, dist=[0.3, 0.4])
