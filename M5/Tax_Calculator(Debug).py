#define the formula to calculate sales tax 
def sales_tax(total):
    tax = 0.06
    sales_tax = total * tax 
    return sales_tax
# def the introduction to the program and giving the input to the user, after that the total after tax will be calculated by adding both the total and the sales_tax together, after that it is rounded and printed as the output
def main():
    print("Sales Tax Calculator\n")
    total = float(input("Enter total: "))
    total_after_tax = round(total + sales_tax(total), 2)
    print("Total after tax: ", total_after_tax)
 #calles the function main()   
if __name__ == "__main__":
    main()