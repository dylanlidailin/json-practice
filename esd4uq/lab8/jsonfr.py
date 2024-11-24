import json

# Define the JSON file path and CSV file path
json_file_path = 'data/schacon.repos.json'  # Replace with the correct path
csv_file_path = 'chacon.csv'

# Load the JSON file
try:
    with open(json_file_path, 'r') as file:
        data = json.load(file)
except FileNotFoundError:
    print(f"Error: The file '{json_file_path}' was not found.")
    exit()
except json.JSONDecodeError as e:
    print(f"Error: Failed to decode JSON. {e}")
    exit()

# Open the CSV file and write the output
try:
    with open(csv_file_path, 'w') as csvfile:
        for repo in data[:5]:  # Limit to the first 5 repositories
            # Extract the required fields
            name = repo.get('name', '')
            html_url = repo.get('html_url', '')
            updated_at = repo.get('updated_at', '')
            visibility = repo.get('visibility', '')

            # Format as a comma-separated line
            line = f"{name},{html_url},{updated_at},{visibility}\n"
            csvfile.write(line)
except Exception as e:
    print(f"Error writing to CSV file: {e}")
    exit()

# Read and display the contents of the CSV file
try:
    with open(csv_file_path, 'r') as csvfile:
        print(csvfile.read())
except Exception as e:
    print(f"Error reading the CSV file: {e}")

