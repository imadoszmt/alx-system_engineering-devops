#!/usr/bin/python3
"""
This module uses REST API to get the employees data and export them in
JSON format file.
"""
import json
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


def export_to_json(employee_id, employee_data, tasks_data):
    """
    Exporst employee data and tasks to a JSON file.

    Args:
        employee_id (str): The ID of the employee.
        employee_data (dict): The employee data.
        tasks_data (list): The list of tasks.
    """
    json_file = f'{employee_id}.json'

    # Create the data structure as required
    tasks_list = []
    for task in tasks_data:
        task_info = {
            "task": task['title'],
            "completed": task['completed'],
            "username": employee_data['username']
        }
        tasks_list.append(task_info)

    json_data = {employee_id: tasks_list}

    with open(json_file, mode='w') as file:
        json.dump(json_data, file)


def main():
    """
    Main function that fetches employee data and exports it in JSON format.

    Usage:
        python3 2-export_to_JSON.py <USER_ID>
    """
    employee_id = sys.argv[1]
    employee_data, tasks_data = employee_metadata(employee_id)
    export_to_json(employee_id, employee_data, tasks_data)


if __name__ == '__main__':
    main()
