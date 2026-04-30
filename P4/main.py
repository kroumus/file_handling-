from integer_processor import IntegerProcessor

def main():
    source_file = 'integers.txt'
    processor = IntegerProcessor(source_file)
    print(f"Starting process for {source_file}...")
    processor.process_numbers()
    print("Process complete. Check double.txt and triple.txt for results.")

if __name__ == "__main__":
    main()