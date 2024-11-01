import sys
from ThreeDArtService import *
from Menu import Menu

def main():
    art_service = ThreeDArtService()

    main_menu_options = {
        "1": ("Display 3D Cube", art_service.display_art),
        "2": ("Display 2D Cube", art_service.display_2d_art),
        "3": ("Change Color", lambda: color_menu.show()),
        "4": ("Change Size", art_service.change_size),
        "5": ("Toggle Direction", art_service.toggle_direction),
        "6": ("Save 3D Art", lambda: art_service.save_art(is_3d=True)),
        "7": ("Save 2D Art", lambda: art_service.save_art(is_3d=False)),
        "8": ("Load and Display Saved Art", art_service.load_art),
        "9": ("Exit", sys.exit),
    }
    main_menu = Menu(main_menu_options)

    color_menu_options = {
        "1": ("White", lambda: art_service.set_color(0)),
        "2": ("Red", lambda: art_service.set_color(91)),
        "3": ("Blue", lambda: art_service.set_color(94)),
    }
    color_menu = Menu(color_menu_options)

    while True:
        main_menu.show()

if __name__ == "__main__":
    main()
