import re

def identify_failed_cells(file_path):
    failed_cells = set()

    # Regular expression to match the cell number after finding "FAIL"
    cell_pattern = re.compile(r"Cell\s+(\d{1,4})\s+Diagnostic\s+FAIL")

    with open(file_path, 'r') as file:
        for line in file:
            stripped_line = line.strip()
            # print(f"Processing line: '{stripped_line}'")
            
            # Check if "FAIL" is in the line
            if "FAIL" in stripped_line:
                # Search for the cell number associated with "FAIL"
                match = cell_pattern.search(stripped_line)
                if match:
                    print(f"Match found: {match.group()}")  # Debugging output
                    cell_number = match.group(1)
                    failed_cells.add(cell_number)
                else:
                    print("FAIL found, but no matching cell number.")  # Debugging output

    return failed_cells

def main():
    # Replace 'events.log' with the path to your event log file
    file_path = '/media/ayden/B0FA5BF1FA5BB278/lander.log'

    failed_cells = identify_failed_cells(file_path)

    if failed_cells:
        print("Failed Cells:")
        for cell in sorted(failed_cells):
            print(f"Cell {cell}")
    else:
        print("No failed cells found.")

if __name__ == "__main__":
    main()
