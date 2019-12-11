# (c) @UniBorg
and Lucaco FF apresenta
# Original written by @UniBorg edit by @aidetico

from telethon import events
import asyncio
from collections import deque


@borg.on(events.NewMessage(pattern=r"\.lucaco", outgoing=True))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("Lucaco Ehi Claro Rodando Free Fire!"))
	for _ in range(48):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)
    
