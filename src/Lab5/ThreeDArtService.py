from Figures.Cube import Cube
import FileService

class ThreeDArtService:
    def __init__(self, size=5, color=0, direction=False):
        self.art = Cube(size)
        self.color = color
        self.direction = direction

    def change_size(self):
        size = input("Enter new size (no less than 3): ")
        if size.isdigit() and int(size) >= 3:
            self.art.side_a = int(size)
        else:
            print("Invalid size. Please try again.")
            self.change_size()

    def set_color(self, color_code):
        self.color = color_code

    def toggle_direction(self):
        self.direction = not self.direction
        print("Direction changed.")

    def get_2d_art(self):
        return self.art.get_two_d_art()

    def get_art(self):
        color_text = f'\033[{self.color}m'
        art = self.art.get_three_d_art() if self.direction else self.art.get_three_d_inverted_art()
        return f"{color_text}{art}\033[0m"

    def display_2d_art(self):
        print(self.get_2d_art())

    def display_art(self):
        print(self.get_art())

    def save_art(self, file_name="lab5/art.txt", is_3d=True):
        art_text = self.get_art() if is_3d else self.get_2d_art()
        FileService.write_into_file(file_name, art_text)
        print(f"Art saved to {file_name} as {'3D' if is_3d else '2D'}.")

    def load_art(self, file_name="lab5/art.txt"):
        try:
            art_text = FileService.read_from_file(file_name)
            print(art_text)
        except FileNotFoundError:
            print(f"No saved art found at {file_name}")
