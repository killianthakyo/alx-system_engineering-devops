import requests
import sys

# Check if an employee ID is provided as a command-line argument
if len(sys.argv) != 2:
    print("Usage: python todo_progress.py <employee_id>")
    sys.exit(1)

employee_id = sys.argv[1]

# Define the API URL to fetch user information
user_api_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"

try:
    # Send an HTTP GET request to the user API
    user_response = requests.get(user_api_url)

    # Check if the user request was successful (status code 200)
    if user_response.status_code == 200:
        user_data = user_response.json()
        employee_name = user_data['name']

        # Define the API URL to fetch the list of TODO item IDs for the user
        todo_ids_api_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

        # Send an HTTP GET request to retrieve the list of TODO item IDs
        todo_ids_response = requests.get(todo_ids_api_url)

        # Check if the TODO item IDs request was successful (status code 200)
        if todo_ids_response.status_code == 200:
            todo_ids = [todo['id'] for todo in todo_ids_response.json()]

            # Display progress information for each TODO item
            print(f"Employee {employee_name} is done with tasks:")

            for todo_id in todo_ids:
                # Define the API URL for each individual TODO item
                todo_item_api_url = f"https://jsonplaceholder.typicode.com/todos/{todo_id}"

                # Send an HTTP GET request to retrieve the TODO item details
                todo_item_response = requests.get(todo_item_api_url)

                # Check if the TODO item request was successful (status code 200)
                if todo_item_response.status_code == 200:
                    todo_item_data = todo_item_response.json()

                    # Check if the TODO item is completed
                    if todo_item_data['completed']:
                        print(f"\t{todo_item_data['title']}")

        else:
            print(f"Failed to retrieve TODO item IDs. Status code: {todo_ids_response.status_code}")

    else:
        print(f"Failed to retrieve user data. Status code: {user_response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

