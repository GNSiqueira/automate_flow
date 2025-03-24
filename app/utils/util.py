from app import app

def screen_center(larg, alt):
    locate = app.primaryScreen().geometry()
    center_x = (locate.width() - larg) // 2
    center_y = (locate.height() - alt) // 2

    return center_x + locate.x(), center_y + locate.y()
