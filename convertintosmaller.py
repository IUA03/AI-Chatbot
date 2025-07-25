import json

# Function to convert patterns to lowercase, uppercase, and title case
def convert_patterns(intent_data):
    for intent in intent_data:
        updated_patterns = set()  # Use set to avoid duplicates

        # Loop through each pattern in the intent
        for pattern in intent['patterns']:
            updated_patterns.add(pattern.lower())  # Add lowercase
            updated_patterns.add(pattern.upper())  # Add uppercase
            updated_patterns.add(pattern.title())  # Add title case
            updated_patterns.add(pattern.capitalize())
        
        # Update the patterns in the intent with the new variations
        intent['patterns'] = list(updated_patterns)  # Convert set back to list
        
    return intent_data

input_file = r'intents.json'  # Change to the path of your input file
output_file = 'intents_modified.json'  # This will be the output file

# Read the input JSON file
with open(input_file, 'r') as f:
    data = json.load(f)

modified_data = convert_patterns(data['intents'])

with open(output_file, 'w') as f:
    json.dump({"intents": modified_data}, f, indent=2)

print(f"Modified JSON file saved to {output_file}")
