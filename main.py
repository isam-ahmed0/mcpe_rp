import time
from pypresence import Presence
from pypresence.types import ActivityType

RPC = Presence("1568313132722561165")
RPC.connect()
RPC.update(
    activity_type=ActivityType.PLAYING,
    state="Mincraft Bedrock",
    # state_url="https://github.com/isam-ahmed0/mcpe_rp",
    details="Playing Minecraft Bedrock on mcpelauncher",
    # details_url="",
    # large_image="logo",
    # large_url="https://project-website.com",
    # buttons=[
    #     {"label": "View Project", "url": "https://github.com/isam-ahmed0/mcpe_rp"},
    #     {"label": "Documentation", "url": "https://github.com/isam-ahmed0/mcpe_rp"}
    # ]
)

try:
    choice = input("Enter to exit")
except KeyboardInterrupt:
    pass
finally:
    RPC.close()
    print("Closed")