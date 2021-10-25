# Send to single device.
from pyfcm import FCMNotification
push_service = FCMNotification(api_key="AAAARdOG5cM:APA91bHmILTD_bbxJTT8OzR8MzJcZtsyY56pWpImI1_K3_oN1YSIrz0Panss9wLxjyycVCSmzSUg5UIo3OT73HpRknkwyX4gNOuo2FY411m7CwUQYWIkYazNND0qUS_tiJGlXhZTjCoq")

def send_message(token, message_title, message_body):
    data_message = {
        "Nick" : "Mario",
        "body" : "great match!",
        "Room" : "PortugalVSDenmark"
    }
    result = push_service.notify_single_device(registration_id=token, message_title=message_title,
                                               message_body=message_body, data_message=data_message)


