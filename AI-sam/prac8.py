import random

responses = {
    "engine_temp": [
        "Engine temperature is high. Possible turbine overheating detected.",
        "Warning: Elevated engine temperature. Consider reducing thrust."
    ],
    "vibration": [
        "High vibration levels indicate potential turbine imbalance.",
        "Vibration anomaly detected. Recommend immediate inspection."
    ],
    "hydraulic": [
        "Hydraulic pressure low. Possible hydraulic leak detected.",
        "Activate backup hydraulic systems to maintain control."
    ],
    "sensor": [
        "Sensor data noisy or missing. Check sensor health and calibration.",
        "Sensor malfunction suspected. Verify hardware and connections."
    ],
    "fault": [
        "Multiple faults detected. Prioritize turbine and hydraulic issues.",
        "Fault clustering suggests subsystem interdependency."
    ],
    "recommendation": [
        "Reduce thrust and prepare for emergency landing if turbine imbalance confirmed.",
        "Activate backup systems and schedule maintenance after flight."
    ],
    "hello": [
        "Hello! I am ACIDS diagnostic assistant. How can I help you?",
        "Hi there! Describe the aircraft symptom or fault you want diagnosed."
    ],
    "bye": [
        "Goodbye! Fly safe.",
        "Signing off. Take care!"
    ],
    "default": [
        "I'm not sure about that symptom. Could you please rephrase?",
        "Please specify the subsystem or fault, e.g., engine_temp, vibration, hydraulic."
    ]
}


def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(responses["default"])


def acids_chatbot():
    print("ACIDS Bot: Hi! Describe aircraft subsystem symptoms or type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("ACIDS Bot:", random.choice(responses["bye"]))
            break
        response = get_response(user_input)
        print("ACIDS Bot:", response)


if __name__ == "__main__":
    acids_chatbot()
