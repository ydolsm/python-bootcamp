# Add more country codes and test this code
country_codes = {
	"PH": "Philippines",
	"US": "United States",
    "UK": "United Kingdom",
    "ES": "Spain",
    "JP": "Japan",
    "SK": "South Korea",
    "TH": "Thailand",
    "VN": "Vietnam",
    "ID": "Indonesia",
    "IT": "Italy"
}

code = input("Enter country code: ")

if code not in country_codes:
    print("Country not found!")
else:
    print(f"{code} -> {country_codes[code]}")