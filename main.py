x=int (input("enter number"),16)

team1 = {
    0b0000_0000:"Al Ahli ", 0b0000_0001:"Al Ettifaq" ,0b0000_0010:"Al Fateh",0b0000_0011:"Al Fayha" ,
    0b0000_0100:"Al Hazem ",0b0000_0101:"Al Hilal",0b0000_0110:"Al Ittihad",0b0000_0111:"Al Khaleej",
    0b0000_1000:"Al Kholood", 0b0000_1001:"Al Najmah",0b0000_1010:"Al Nassr",0b0000_1011:"Al Okhdood",
    0b0000_1100:"Al Qadsiah ",0b0000_1101:"Al Riyadh",0b0000_1110:"Al Shabab"
}

team2 = {
    0b0000_0000:"Al Ahli ", 0b0000_0001:"Al Ettifaq" ,0b0000_0010:"Al Fateh",0b0000_0011:"Al Fayha" ,
    0b0000_0100:"Al Hazem ",0b0000_0101:"Al Hilal",0b0000_0110:"Al Ittihad",0b0000_0111:"Al Khaleej",
    0b0000_1000:"Al Kholood", 0b0000_1001:"Al Najmah",0b0000_1010:"Al Nassr",0b0000_1011:"Al Okhdood",
    0b0000_1100:"Al Qadsiah ",0b0000_1101:"Al Riyadh",0b0000_1110:"Al Shabab"
}


score = {
    0b0000_0000:"match canceled", 0b0000_0001:"right team won",0b0000_0010:"left team won",0b0000_0011:"draw"
}
league = {
    0b0000_0000:"Roshan Saudi League", 0b0000_0001:"Saudi Super Cup",
    0b0000_0010:"Crown Prince Cup",0b0000_0011:"King's Cup"
}
home = {
    0b0000_0000:"Left team's home",0b0000_0001:"Right team's home"
}
judge = {
    0b0000_0000:"Foreign",0b0000_0001:"Saudi"
}

A=x & 0b0001_1111
if A in team1:
    
    print(team1[A])
    
else:
    print("no such team")
    
B= x & 0b1111_1000
B= B>>5
if B in team2:
    
    print(team2[B])
    
else:
    print("no such team")
    
c= x & 0b1100_0000_0000
c= c>>10
if c in score:
    
    print(score[c])
    
else:
    print("no such score")
    
D= x & 0b1_0000_0000_0000
D= D>>13
if D in home:
    
    print(home[D])
    
else:
    print("no such answer")
    
E= x & 0b110_0000_0000_0000
E= E>>14
if E in league:
    
    print(league[E])
    
else:
    print("no such league")
    
F= x & 0b1_1000_0000_0000_0000
F= F>>17
if F in judge:
    
    print(judge[F])
    
else:
    print("no answer")