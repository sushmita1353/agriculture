def disease_identification():
    crop_name = input("Enter crop name (e.g., Wheat, Rice): ")
    symptoms = input("Enter visible symptoms (e.g., yellowing leaves, brown spots): ")
    if crop_name.lower() == "wheat" and "yellowing leaves" in symptoms.lower():
        print("\nPossible Disease: Leaf Rust")
        print("Recommended Action:")
        print("- Apply fungicide recommended for Leaf Rust")
        print("- Ensure proper crop rotation")
    else:
        print("\nNo specific disease identified for your inputs.")
    print("\n------------------------------------------------")
