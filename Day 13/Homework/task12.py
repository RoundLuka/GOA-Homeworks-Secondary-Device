"""მომხმარებელს შემოატანინეთ წელი და შეამოწმეთ ის ნაკიანი არის თუ არა."""

year = int(input("Enter year: "))

if year % 4 == 0:
    print("Not leap year")
else:
    print("Leap year")