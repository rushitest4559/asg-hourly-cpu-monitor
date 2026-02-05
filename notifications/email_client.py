import boto3
from botocore.exceptions import ClientError
from utils.logger import get_logger

logger = get_logger(__name__)

class EmailClient:
    def __init__(self, region_name="us-east-1", sender=None):
        """
        Initializes the SES client. 
        Note: Boto3 will automatically look for AWS_ACCESS_KEY_ID 
        and AWS_SECRET_ACCESS_KEY environment variables.
        """
        self.client = boto3.client('ses', region_name=region_name)
        self.sender = sender

    def send_email(self, to_email, subject, html_body):
        try:
            response = self.client.send_email(
                Source=self.sender,
                Destination={
                    'ToAddresses': [to_email],
                },
                Message={
                    'Subject': {'Data': subject, 'Charset': 'UTF-8'},
                    'Body': {
                        'Html': {'Data': html_body, 'Charset': 'UTF-8'}
                    }
                }
            )
            logger.info(f"Email sent! Message ID: {response['MessageId']}")

        except ClientError as e:
            logger.error(f"Failed to send email to {to_email}: {e.response['Error']['Message']}")
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")