def diagnose(symptoms):
    # Basic logic for diagnosis
    if "fever" in symptoms and "body ache" in symptoms and "fatigue" in symptoms:
        return "You might have the flu."
    elif "fever" in symptoms or "fatigue" in symptoms:
        return "You might have a cold."
    else:
        return "It seems like a mild condition or no cold/flu symptoms."


def main():
    print("Welcome to the Cold Vs Flu Diagnosis")
    print("Please answer the following questions with 'yes' or 'no'")

    questions = {
        "fever": "Do you have a fever?",
        "body ache": "Are you experiencing body pain?",
        "fatigue": "Do you feel fatigued or tired?",
        "runny nose": "Do you have a runny nose?",
        "sneezing": "Are you sneezing?",
        "sore throat": "Do you feel a sore throat?"
    }

    user_symptoms = []

    for symptom, question in questions.items():
        response = input(question + " ").strip().lower()
        if response == 'yes':
            user_symptoms.append(symptom)

    result = diagnose(user_symptoms)
    print("\nDiagnosis Result:")
    print(result)


if __name__ == "__main__":
    main()
