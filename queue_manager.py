import json

from monday_code import QueueApi, PublishMessageParams


class MondayQueueManager:
    def __init__(self):
        self.queue_manager = QueueApi()

    async def publish(self, queue: str, message: dict):
        message = {
            "queue": queue,
            "message": message
        }
        self.queue_manager.publish_message(publish_message_params=PublishMessageParams(message=json.dumps(message)),
                                           _request_timeout=10)


queue_manager = MondayQueueManager()
