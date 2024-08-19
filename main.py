from crop_selection import crop_selection
from soil_management import soil_management
from disease_identification import disease_identification
from weather_forecast import weather_forecast
from sustainable_farming_tips import sustainable_farming_tips

def main():
    while True:
        print("------------------------------------------------")
        print("Welcome to the Crop and Soil Management System")
        print("------------------------------------------------")
        print("Theme: Agriculture")
        print("Goal: Zero Hunger")
        print("------------------------------------------------\n")

        print("1. Crop Selection")
        print("2. Soil Management")
        print("3. Disease Identification")
        print("4. Weather Forecast")
        print("5. Sustainable Farming Tips")
        print("6. Exit")

        choice = input("\nPlease select an option (1-6): ")

        if choice == '1':
            crop_selection()
        elif choice == '2':
            soil_management()
        elif choice == '3':
            disease_identification()
        elif choice == '4':
            weather_forecast()
        elif choice == '5':
            sustainable_farming_tips()
        elif choice == '6':
            print("\nThank you for using the Crop and Soil Management System!")
            print("------------------------------------------------")
            break
        else:
            print("\nInvalid option. Please try again.")
            print("------------------------------------------------")

if __name__ == "__main__":
    main()
