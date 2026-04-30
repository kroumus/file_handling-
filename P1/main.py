from number_processor import NumberProcessor

def main():
    processor = NumberProcessor('numbers.txt')
    if processor.separate_numbers():
        print("Verified, Files 'even.txt' and 'odd.txt' have been created.")
    else:
        print("Error: numbers.txt' was not found.")

if __name__ == "__main__":
    main()