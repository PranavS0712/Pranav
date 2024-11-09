import json
import sys

# Step 1: Ensure UTF-8 encoding for output
sys.stdout.reconfigure(encoding='utf-8')

# Step 2: Open and read the JSONL file with UTF-8 encoding
with open('expense report.jsonl', 'r', encoding='utf-8') as file:
    # Step 3: Read the file line by line
    for line in file:
        # Step 4: Parse each line as a JSON object
        expense_Report_obj = json.loads(line)
        
        # Step 5: Access the expenses in the 'data' dictionary and print them
        for expense in expense_Report_obj['data']['expenses']:
            print(expense['customFields'])
