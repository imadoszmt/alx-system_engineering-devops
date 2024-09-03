#!/usr/bin/python3
"""
This module uses REST API to get the employees data and export them in
CSV file.
"""
import csv
import requests
import sys


def employee_metadata(employee_id):
    """
    Fetches employee data and their tasks from REST API.

    Args:
        user_id (str): ID of the employee.

    Returns:
        tuple: A tuple containing employee and tasks data.
    """
    # Fetch the employee data.
    users_api_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    employee_response = requests.get(users_api_url)
    employee_data = employee_response.json()

    # Fetch the tasks data.
    tasks_api_url = 'https://jsonplaceholder.typicode.com/todos'
    tasks_response = requests.get(f'{tasks_api_url}?userId={employee_id}')
    tasks_data = tasks_response.json()

    return employee_data, tasks_data


def export_to_csv(employee_id, employee_data, tasks_data):
    """
    Exports employee data and tasks to a CSV file.

    Args:
        employee_id (str): The ID of the employee.
        employee_data (dict): The employee data.
        tasks_data (list): The list of tasks.
    """
    csv_name = f'{employee_id}.csv'

    with open(csv_name, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
                        "TASK_TITLE"])

        for task in tasks_data:
            writer.writerow([
                employee_id,
                employee_data['username'],
                task['completed'],
                task['title']
            ])


def main():
    """
    Main function that route fetching employee data and exporting to CSV.

    Usage:
        python3 1-export_to_CSV.py <USER_ID>
    """
    employee_id = sys.argv[1]
    employee_data, tasks_data = employee_metadata(employee_id)
    export_to_csv(employee_id, employee_data, tasks_data)


if __name__ == '__main__':
    main()
