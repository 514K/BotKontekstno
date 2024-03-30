import requests
def getRoomLink(id: str):
    # resp = requests.post("https://xn--80aqu.xn--e1ajbkccewgd.xn--p1ai/create_room?user_id=3490b742-56b3-443e-bc16-9eaac4222d74&is_public=false&challenge_type=random")

    return "https://контекстно.рф/room/" + id #resp.json()["room_id"]

def getRoomId():
    resp = requests.post("https://xn--80aqu.xn--e1ajbkccewgd.xn--p1ai/create_room?user_id=3490b742-56b3-443e-bc16-9eaac4222d74&is_public=false&challenge_type=random")

    return resp.json()["room_id"]

def isRoomComplete(id: str):
    resp = requests.get("https://xn--80aqu.xn--e1ajbkccewgd.xn--p1ai/get_room", {"room_id" : id})
    # print("debug api start")
    # print(resp.json()["completed"])
    # print(True if resp.json()["completed"] == True else False)
    # print(True if resp.json()["completed"] == "true" else False)
    # print(True if resp.json()["completed"] == "True" else False)
    # print((True if resp.json()["completed"] == "True" else False))
    # print("debug api stop")

    return True if resp.json()["completed"] == True else False