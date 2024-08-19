def soil_management():
    soil_ph = float(input("Enter your current soil pH level (e.g., 5.5, 6.0): "))

    # Example logic for soil management recommendation
    if soil_ph < 6.0:
        print("\nRecommended soil treatment:")
        print("- Add lime to increase soil alkalinity")
        print("- Use organic compost to improve soil fertility")
    else:
        print("\nYour soil pH is within the optimal range.")
    print("\n------------------------------------------------")
