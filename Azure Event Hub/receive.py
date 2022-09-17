import asyncio
from azure.eventhub.aio import EventHubConsumerClient
from azure.eventhub.extensions.checkpointstoreblobaio import BlobCheckpointStore

async def on_event(partition_context, event):
    # Print the event data.
    print("Received the event: \"{}\" from the partition with ID: \"{}\"".format(event.body_as_str(encoding='UTF-8'), partition_context.partition_id))

    # Update the checkpoint so that the program doesn't read the events
    # that it has already read when you run it next time.
    await partition_context.update_checkpoint(event)

async def main():
    # Create an Azure blob checkpoint store to store the checkpoints.
    checkpoint_store = BlobCheckpointStore.from_connection_string("DefaultEndpointsProtocol=https;AccountName=teststorageaccname;AccountKey=Lpf3kfsOriMMXDpaoQo/YHDrgLK/oABnoxW7/yKEltn5f6XrryXCFDZ0HDmMUnifVgg21BjTyfYA+AStURZrUQ==;EndpointSuffix=core.windows.net", "testcontainername")

    # Create a consumer client for the event hub.
    client = EventHubConsumerClient.from_connection_string("Endpoint=sb://eh-testns.servicebus.windows.net/;SharedAccessKeyName=EHTestPolicyName;SharedAccessKey=Bw2rPoQ64RDxUOqe9W0ekM3l+WGSehG84vbr8TW8AEo=;EntityPath=ehtestname", consumer_group="$Default", eventhub_name="ehtestname", checkpoint_store=checkpoint_store)
    async with client:
        # Call the receive method. Read from the beginning of the partition (starting_position: "-1")
        await client.receive(on_event=on_event,  starting_position="-1")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # Run the main method.
    loop.run_until_complete(main())