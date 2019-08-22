ch = var(4, [4,5])

b2 >> play("X ")
b3 >> play("-------{r,=}", dist=1)
b4 >> play(["  t ", "  tt", " V v"], dist=[0.2, 1])
b5 >> play(P[ch].amen(), echo=1.5, amplify=[0, 0.4])
b5.stop()
p1 >> play(P["x-o-"].amen())
