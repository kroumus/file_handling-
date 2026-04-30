class NumberProcessor:
    def __init__(self, input_file):
        self.input_file = input_file
    
    def separate_numbers(self):
        try:
            with open(self.input_file, 'r') as file:
                nums =[int(n) for n in file.read().split()]
        
        even_nums = [str(n) for n in nums if n % 2 == 0]
        odd_nums= [str(n) for n in nums if n % 2 != 0]

        self.write_to_file('even.txt', even_nums)
        self.write_to_file('odd.txt', odd_nums)

        