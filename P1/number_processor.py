class NumberProcessor:
    def __init__(self, input_file):
        self.input_file = input_file
    
    def separate_numbers(self):
        try:
            with open(self.input_file, 'r') as file:
                nums =[int(n) for n in file.read().split()]