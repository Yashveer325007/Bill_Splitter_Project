print("Welcome to the Bill Splitter")
#asking for the toatal bill amount
Total_bill=float(input("What was the total bill ?"))
#tip percent you want to give
Tip=int(input("what percent tip will you like to give [10%,12%,15%]"))
#asking for total persons to split up the bill into
Total_persons=int(input("How many people to split the bill into ?"))
#tip amount 
tip_amount=Total_bill*(Tip/100)
#Final bill afer adding tip
New_total_bill=(Total_bill+tip_amount)
split=round(New_total_bill/Total_persons,2)
print(f"Each person has to pay:{split} ")
