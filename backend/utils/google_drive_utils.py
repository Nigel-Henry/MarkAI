import logging
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from googleapiclient.errors import HttpError

# Constants
SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = 'service-account.json'

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def upload_to_drive(file_path, folder_name):
    """
    Upload a file to Google Drive inside a specified folder.

    Args:
        file_path (str): The path to the file to be uploaded.
        folder_name (str): The name of the folder to create and upload the file into.

    Returns:
        str: The ID of the uploaded file.
    """
    try:
        # Authenticate and build the service
        creds = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        service = build('drive', 'v3', credentials=creds)

        # Create a folder in Google Drive
        folder_metadata = {
            'name': folder_name,
            'mimeType': 'application/vnd.google-apps.folder'
        }
        folder = service.files().create(body=folder_metadata, fields='id').execute()
        folder_id = folder.get('id')
        logger.info(f"Folder '{folder_name}' created with ID: {folder_id}")

        # Upload the file to the folder
        file_metadata = {
            'name': file_path.split('/')[-1],
            'parents': [folder_id]
        }
        media = MediaFileUpload(file_path, resumable=True)
        file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        file_id = file.get('id')
        logger.info(f"File '{file_path}' uploaded with ID: {file_id}")

        return file_id

    except HttpError as error:
        logger.error(f"An error occurred: {error}")
        return None