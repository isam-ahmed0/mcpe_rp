import time
from pypresence import Presence
from pypresence.types import ActivityType

RPC = Presence("1568313132722561165")
RPC.connect()
RPC.update(
    activity_type=ActivityType.PLAYING,
    state="Mincraft Bedrock",
    # state_url="https://github.com/isam-ahmed0",
    details="Playing Minecraft Bedrock on mcpelauncher",
    # details_url="",
    # large_image="logo",
    # large_url="https://project-website.com",
    # buttons=[
    #     {"label": "View Project", "url": "https://github.com/username/project"},
    #     {"label": "Documentation", "url": "https://docs.project.com"}
    # ]
)


choice = input("Enter to exit")
RPC.close()
if KeyboardInterrupt:
    RPC.close()