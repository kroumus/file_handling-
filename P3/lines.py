class MyLife:
    def __init__(self, file_name="MyLife.txt"):
        self.file_name = file_name

    def write_multiple_lines(self):
        with open(self.file_name, 'w') as file:
            while True:
                line = input("Enter Line: ")
                file.write(line + "\n")

                choice = input("Are there more lines? y/n ").lower()
                if choice != 'y':
                    break
        print(f"Lines saved to {self.file_name}")