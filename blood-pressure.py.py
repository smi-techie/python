def check_blood_pressure(systolic, diastolic):  
    """Check blood pressure and provide advice based on the readings."""  
    if systolic < 120 and diastolic < 80:  
        return "😊 Your blood pressure is normal! Keep maintaining a healthy lifestyle!"  
    elif 120 <= systolic < 130 and diastolic < 80:  
        return "🟡 Your blood pressure is elevated. Consider making some lifestyle changes."  
    elif 130 <= systolic < 140 or 80 <= diastolic < 90:  
        return "🟠 This is Hypertension Stage 1. It's a good idea to consult a healthcare provider for advice."  
    elif 140 <= systolic < 180 or 90 <= diastolic < 120:  
        return "🔴 This is Hypertension Stage 2. Please seek medical attention as soon as possible."  
    elif systolic >= 180 and diastolic >= 120:  
        return "🚨 Hypertensive Crisis! This is serious; please seek emergency medical help immediately."  
    else:  
        return "⚠️ It seems the readings are invalid. Please double-check your values."  

# User input  
def get_blood_pressure():  
    """Prompt the user for blood pressure readings and provide feedback."""  
    print("Let's check your blood pressure! Please enter the following values:")  
    try:  
        systolic_input = int(input("Enter systolic pressure (upper number): "))  
        diastolic_input = int(input("Enter diastolic pressure (lower number): "))  
        advice = check_blood_pressure(systolic_input, diastolic_input)  
        print(advice)  
    except ValueError:  
        print("❌ Oops! Please enter valid numeric values for the blood pressure.")  

# Start the user interaction  
if __name__ == "__main__":  
    get_blood_pressure()