"""დაწერეთ პროგრამა, რომელიც იღებს მომხმარებლისგან მთელ რიცხვს და დაბეჭდავს მის 
გამრავლების ცხრილს 10-ის ჩათვლით. მაგ: x, x2, x3 ... x*10."""

num = int(input("Enter a number: "))

for i in range(1,10 + 1):
    print(num * i)