# backend/app/features/tasks/service.py
from datetime import datetime, timezone

class TaskService:
    @staticmethod
    def create_task(user_id: int, title: str) -> dict:
        """
        Create a new task with the given user ID and title.

        Args:
            user_id (int): The ID of the user to whom the task is assigned.
            title (str): The title of the task.

        Returns:
            dict: A dictionary containing the task details.
        """
        return {
            "id": 1,
            "title": title,
            "created_at": datetime.now(timezone.utc),
            "assigned_to": user_id
        }