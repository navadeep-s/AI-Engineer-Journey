import calculations

def main():
    total =calculations.calculate_total(20,3)
    print("Subtotal:", total)

    tax = calculations.calculate_tax(total,0.08)
    print("Tax:", tax)

    final_price = total+tax
    print("Final price:", final_price)

if __name__ == "__main__":
    main()