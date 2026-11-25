def answer(question, context=None):
    q = str(question).lower().strip()

    responses = {
        "hello": "Hello! I am DISASTERMATRIX AI, your disaster-management assistant.",
        "hi": "Hi! How can I help you understand disaster preparedness?",
        "flood": "Flooding occurs when water exceeds the capacity of drainage systems, rivers, or other storage areas.",
        "earthquake": "During an earthquake, Drop, Cover and Hold On. Stay away from windows.",
        "cyclone": "During a cyclone, follow official weather alerts, stay indoors and follow evacuation instructions.",
        "rain": "Heavy rainfall can increase surface runoff and flood risk, especially in low-lying areas.",
        "chennai": "Chennai faces urban flooding risks during intense rainfall, particularly where drainage capacity is limited.",
        "pondicherry": "Puducherry is a coastal region that can face heavy-rainfall and cyclone-related hazards.",
        "tiruchirappalli": "Tiruchirappalli can experience heavy-rainfall and river-related flood risks.",
        "trichy": "Tiruchirappalli can experience heavy-rainfall and river-related flood risks.",
        "preparedness": "Keep an emergency kit, follow official warnings, identify safe shelters and prepare a family communication plan."
    }

    for keyword, response in responses.items():
        if keyword in q:
            return response

    return (
        "I am DISASTERMATRIX AI. I can help with floods, "
        "cyclones, earthquakes, rainfall and disaster preparedness. "
        "Please ask a more specific question."
    )
