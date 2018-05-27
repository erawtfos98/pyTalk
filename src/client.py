#!/usr/bin/env python3

import asyncio
import websockets
 
async def test():
 
    async with websockets.connect('ws://localhost:8765') as websocket:
 
        await websocket.send("hello ihr ficker!!!")
 
        response = await websocket.recv()
        print(response)
 
asyncio.get_event_loop().run_until_complete(test())
