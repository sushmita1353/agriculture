def crop_selection():
    region = input("Enter your region (e.g., North, South, East, West): ")
    soil_type = input("Enter the type of soil (e.g., Sandy, Clay, Loamy): ")

    # Example logic for crop recommendation based on region and soil type
    if region.lower() == "south" and soil_type.lower() == "loamy":
        print("\nRecommended Crops for your region and soil type:")
        print("1. Wheat")
        print("2. Rice")
        print("3. Maize")
    else:
        print("\nNo specific recommendations available for your inputs.")
    print("\n------------------------------------------------")
