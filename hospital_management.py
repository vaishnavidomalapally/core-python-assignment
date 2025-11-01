def search_by_disease(patients, disease):
    result = [p["Name"] for p in patients if p["Disease"] == disease]
    return result

patients = [
    {"Name": "Alice", "Age": 30, "Disease": "Flu"},
    {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},
    {"Name": "Charlie", "Age": 35, "Disease": "Flu"}
]

search_disease = "Flu"
print("Patients with", search_disease + ":", search_by_disease(patients, search_disease))
