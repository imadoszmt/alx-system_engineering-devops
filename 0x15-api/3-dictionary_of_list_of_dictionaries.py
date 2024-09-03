#!/usr/bin/python3
"""
This module uses REST API to get all employees' data and export them
in JSON format.
"""
import json
import requests


def fetch_all_employees_data():
    """
    Fetches data for all employees and their tasks from REST API.

    Returns:
        dict: A dictionary containing data for all employees.
    """
    # Fetch all employees data.
    users_api_url = 'https://jsonplaceholder.typicode.com/users'
    employees_response = requests.get(users_api_url)
    employees_data = employees_response.json()

    # Fetch all tasks data.
    tasks_api_url = 'https://jsonplaceholder.typicode.com/todos'
    tasks_response = requests.get(tasks_api_url)
    tasks_data = tasks_response.json()

    return employees_data, tasks_data


def export_all_to_json(employees_data, tasks_data):
    """
    Exports all employees' data and tasks to a JSON file.

    Args:
        employees_data (list): The list of all employees' data.
        tasks_data (list): The list of all tasks.
    """
    json_file = 'todo_all_employees.json'

    # Create the data structure as required
    all_employees_tasks = {}
    for employee in employees_data:
        employee_id = str(employee['id'])
        employee_username = employee['username']
        employee_tasks = []

        for task in tasks_data:
            if task['userId'] == employee['id']:
                task_info = {
                    "username": employee_username,
                    "task": task['title'],
                    "completed": task['completed']
                }
                employee_tasks.append(task_info)

        all_employees_tasks[employee_id] = employee_tasks

    with open(json_file, mode='w') as file:
        json.dump(all_employees_tasks, file)


def main():
    """
    Main function that fetches all employees' data and exports it
    in JSON format.

    Usage:
        python3 3-export_to_JSON.py
    """
    employees_data, tasks_data = fetch_all_employees_data()
    export_all_to_json(employees_data, tasks_data)


if __name__ == '__main__':
    main()
