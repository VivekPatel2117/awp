def diagnose(crop, symptoms):
    # Sample rule-based diagnosis
    if crop == "tomato":
        if "yellow spots on leaves" in symptoms and "wilting" in symptoms:
            return {
                "disease": "Bacterial Wilt",
                "treatment": "Apply Streptocycline 200 ppm",
                "prevention": "Use crop rotation, sterilize tools"
            }
        elif "brown spots on leaves" in symptoms and "leaf drop" in symptoms:
            return {
                "disease": "Early Blight",
                "treatment": "Spray Mancozeb 2g/litre",
                "prevention": "Remove infected leaves, avoid overhead watering"
            }

    elif crop == "rice":
        if "yellowing leaves" in symptoms and "brown lesions on stem" in symptoms:
            return {
                "disease": "Rice Blast",
                "treatment": "Use Tricyclazole at 0.6 g/litre",
                "prevention": "Maintain proper spacing, avoid excess nitrogen"
            }

    elif crop == "brinjal":
        if "holes in leaves" in symptoms and "fruit damage" in symptoms:
            return {
                "disease": "Fruit and Shoot Borer",
                "treatment": "Spray Neem oil 5%",
                "prevention": "Destroy affected shoots and fruits"
            }

    return {
        "disease": "Unknown or no major disease detected",
        "treatment": "Consult an agricultural expert",
        "prevention": "Ensure good farming practices and monitor regularly"
    }


def main():
    print("🌾 Welcome to AgroDoc: Crop Disease Diagnosis System")
    print("Please answer the following questions.")

    crop = input("Enter the crop name (e.g., tomato, rice, brinjal): ").strip().lower()

    symptom_questions = {
        "yellow spots on leaves": "Do you see yellow spots on the leaves?",
        "wilting": "Is the plant wilting?",
        "brown spots on leaves": "Are there brown spots on the leaves?",
        "leaf drop": "Are leaves falling off?",
        "yellowing leaves": "Are the leaves turning yellow?",
        "brown lesions on stem": "Are there brown lesions on the stem?",
        "holes in leaves": "Do the leaves have holes?",
        "fruit damage": "Is the fruit damaged or showing signs of pest attack?"
    }

    user_symptoms = []
    for symptom, question in symptom_questions.items():
        response = input(question + " (yes/no): ").strip().lower()
        if response == "yes":
            user_symptoms.append(symptom)

    result = diagnose(crop, user_symptoms)

    print("\n Diagnosis Result:")
    print(f"Disease: {result['disease']}")
    print(f"Treatment: {result['treatment']}")
    print(f"Prevention: {result['prevention']}")


if __name__ == "__main__":
    main()
