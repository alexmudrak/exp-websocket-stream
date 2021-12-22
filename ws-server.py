import websockets
import asyncio
import base64

PORT = 5050

print(f"Server listening in Port {PORT}")
connected = set()

async def echo(webs, path):
    print('A client is connected')
    connected.add(webs)
    try:
        async for message in webs:
            for conn in connected:
                if conn != webs:
                    print('\n\nReceived msg from cliend: \n', message)
                    await conn.send(message)
    except websockets.exceptions.ConnectionClosed as e:
        print("A client just disconnected.")
    finally:
        connected.remove(webs)

start_server = websockets.serve(echo, "0.0.0.0", PORT)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
