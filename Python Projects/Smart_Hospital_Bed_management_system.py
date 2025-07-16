age = int(input("Enter Age: "))
severity = int(input("Enter Severity level (1-10): "))
fever = input("Do you have fever (yes/no): ").lower()
fracture = input("Do you have fracture (yes/no): ").lower()
breathing_difficulty = input("Do you have breathing issues (yes/no): ").lower()
insured = input("Do you have insurance (yes/no): ").lower()
comorbidity = input("Comorbidity (yes/none): ").lower()

department = ""
urgency = ""
billing = ""
bed_allotted = "No"


if severity > 8 or breathing_difficulty == "yes":
    department = "ICU"
    urgency = "Critical"

elif fracture == "yes" and severity >= 5:
    department = "ER"
    urgency = "High"

elif age > 70 and comorbidity == "yes":
    if severity >= 5:
        department = "ICU"
        urgency = "High"
    else:
        department = "ER"
        urgency = "High"

elif fever == "yes":
    if severity < 3:
        department = "General"
        urgency = "Low"
    elif severity > 5 and comorbidity == "yes":
        department = "ER"
        urgency = "Medium"
    else:
        department = "General"
        urgency = "Medium"

else:
    department = "Referral"
    urgency = "Low"

if insured == "yes":
    billing = "Private"
elif insured == "no" and (age < 18 or age > 65):
    billing = "Govt Scheme"
else:
    billing = "NGO Support"

if department == "ICU" or department == "ER":
    bed_allotted = "Yes"
elif department == "General":
    if urgency == "Medium" or urgency == "High":
        bed_allotted = "Yes"
    else:
        bed_allotted = "No"
elif department == "Referral":
    bed_allotted = "No"

print("\n--- Patient Triage Result ---")
print("Department:", department)
print("Urgency Level:", urgency)
print("Billing Type:", billing)
print("Bed Allotted:", bed_allotted)

