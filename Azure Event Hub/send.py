import asyncio
from azure.eventhub.aio import EventHubProducerClient
from azure.eventhub import EventData


async def run():
    # Create a producer client to send messages to the event hub
    producer = EventHubProducerClient.from_connection_string(conn_str="Endpoint=sb://eh-testns.servicebus.windows.net/;SharedAccessKeyName=EHTestPolicyName;SharedAccessKey=Bw2rPoQ64RDxUOqe9W0ekM3l+WGSehG84vbr8TW8AEo=;EntityPath=ehtestname", eventhub_name="ehtestname")
    async with producer:
        # Create a batch.
        event_data_batch = await producer.create_batch()

        # Add events to the batch.
        event_data_batch.add(EventData('This is First event '))
        event_data_batch.add(EventData('This is Second event'))
        event_data_batch.add(EventData('This is Third event'))

        # Send the batch of events to the event hub.
        await producer.send_batch(event_data_batch)
        
loop = asyncio.get_event_loop()
loop.run_until_complete(run())