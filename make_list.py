import re

# Path to the input file (with mixed data)
input_file_path = 'input.txt'

# Path to the output file where we will store the IP:Port pairs
output_file_path = 'proxies.txt'

# Regular expression to match IP:Port pairs
ip_port_regex = r'(\d+\.\d+\.\d+\.\d+:\d+)'

# Open the input file for reading
with open(input_file_path, 'r') as file:
    # Open the output file for writing
    with open(output_file_path, 'w') as output_file:
        # Process each line in the input file
        for line in file:
            # Search for IP:Port pattern using regex
            matches = re.findall(ip_port_regex, line)
            for match in matches:
                # Write the found IP:Port to the output file
                output_file.write(match + '\n')

print(f"IP:Port pairs have been saved to {output_file_path}")
