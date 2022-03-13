# Take in a number
# split tip/calculate the tip per person
# has to be a large enough number
# code must work properly
# must ask whats the total of bill
# must ask how many people
# must return a tip per person

# num3 = num1/num2
# make this more precise500

# calculate tip percentage
# create new bill total 
# divide new bill total by number of people

bill_total = int(float(input(' what is the total of the bill: ')))

print(bill_total)
total_amount_of_people = int(float(input(' how many people were serviced: ')))

print(total_amount_of_people)

tip = bill_total * 0.15
print(tip)

new_total = tip + bill_total
print(new_total)

amount_per_person = new_total/total_amount_of_people
print(amount_per_person)

tip_per_person = tip / total_amount_of_people
print(tip_per_person)



# this is a basic tip calculator which creates a new bill with the tip included and then divides the bill first, before dividing the tip per person.
# Thank you for your patience!




