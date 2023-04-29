priceOfBook1=499
priceOfBook2=855
priceOfBook3=645  #let us consider b1,b2,b3 are the 3 books
c1=int(input())   #no.of b1 books to purchase
c2=int(input())   #no.of b2 books to purchase
c3=int(input())   #no.of b3 books to purchase
d1=c1*priceOfBook1    
d2=c2*priceOfBook1
d3=c3*priceOfBook1
sum=d1+d2+d3
amount=(sum * 12/100) + 250 + sum       #adding GST and delivery charge to the total books purchase cost.
print(amount)