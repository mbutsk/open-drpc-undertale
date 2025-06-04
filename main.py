import configparser
import pathlib

def setup():
    return [391540]

path = pathlib.Path("~/.config/UNDERTALE/undertale.ini").expanduser()

locations = {
    range(4, 44): ["Ruins", "https://static.wikia.nocookie.net/undertale/images/7/70/Ruins_location_entrance.png/revision/latest?cb=20200201200339"],
    range(44, 78): ["Snowdin", "https://static.wikia.nocookie.net/undertale/images/f/fe/Snowdin_location.png/revision/latest?cb=20160212141711"],
    range(81, 136): ["Waterfall", "https://static.wikia.nocookie.net/undertale/images/6/6c/Waterfall_location_Shyren_room.png/revision/latest?cb=20160211163540"],
    range(136, 188): ["Hotland", "https://static.wikia.nocookie.net/undertale/images/6/60/Hotland_location.png/revision/latest?cb=20160211164015"],
    range(188, 216): ["Core", "https://static.wikia.nocookie.net/undertale/images/8/84/CORE_location_lobby.png/revision/latest?cb=20211118153743&path-prefix=ru"],
    range(216, 239): ["New home", "https://static.wikia.nocookie.net/undertale/images/c/cb/New_Home_location.png/revision/latest?cb=20160211164902"],
    range(242, 264): ["True lab", "https://static.wikia.nocookie.net/undertale/images/7/72/True_Lab_location.png/revision/latest?cb=20160211165335"],
    range(264, 265): ["Secret", "https://upload.wikimedia.org/wikipedia/commons/a/a5/Undertale.png"]
}

config = configparser.ConfigParser()


def game_data(game):
    config.read(str(path))
    room_id = int(config.get("General", "Room", fallback="0").replace('"', "").split(".")[0])
    love = config.get("General", "Love", fallback="Unknown").replace('"', "").split(".")[0]
    location = None
    for room_range, info in locations.items():
        if room_id in room_range:
            location = info
            break
    
    if not location:
        location = ["Unknown", "https://upload.wikimedia.org/wikipedia/commons/a/a5/Undertale.png"]
    

    game['description'] = f"In {location[0]}. Love: {love}"
    game['header_image'] = location[1]
    return game