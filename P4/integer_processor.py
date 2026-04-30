class IntegerProcessor:
    def __init__(self, file_name):
        self.file_name = file_name
    
    def process_numbers(self):
        try:
            with open(self.file_name, 'r') as file:
                data = file.readlines()
            
            with open('double.txt', 'w') as double, open ('triple.txt', 'w') as triple:
                for line in data:
                    try:
                        value = int(line.strip())
                        if value % 2 == 0:
                            double.write(f"{value**2}\n")
                        else:
                            triple.write(f"{value**3}\n")
                    except ValueError:
                        print(f"Skipping invalid data: {line.strip()}")
        
        except Exception as error:
            print(f"An unexpected error occurred: {error}")