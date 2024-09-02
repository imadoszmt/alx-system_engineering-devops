#!/usr/bin/python3
"""
This module uses REST API to get the employees TODO list progress based
on their ID.
"""
import requests
import sys


def employee_todo_list_progress(employee_id):
    """
    Fetches and displays TODO list progress of employees from a REST API.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    endpoint_url = "https://jsonplaceholder.typicode.com/users"

    # Fetch the employee data.
    employee_response = requests.get(f"{endpoint_url}/{employee_id}")
    employee_data = employee_response.json()
    employee_name = employee_data["name"]

    # Fetch employee's TODO list
    todo_response = requests.get(f"{endpoint_url}/{employee_id}/todos")
    todo_data = todo_response.json()

    # Mesure progress
    all_tasks = len(todo_data)
    finished_tasks = sum(1 for task in todo_data if task['completed'])
    finished_tasks_titles = [task["title"] for task in todo_data if task["completed"]]

    # Print progress
    print(f"Employee {employee_name} is done with tasks({finished_tasks}/{all_tasks}):")
    for title in finished_tasks_titles:
        print(f"    {title}")

#if __name__ == __main__:
    """
    Get employee ID from the command line argument and calls it to print
    the TODO list progress.
    """
    employee_id = int(sys.argv[1])
    employee_todo_list_progress(employee_id)
