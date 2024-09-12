import csv
from collections import defaultdict
from protocol_nums import protocol_map

def load_lookup_table(lookup_file):
    """
    Load the lookup table from a CSV file into a dictionary.
    return lookup_dict which map (dstport, protocol) tuple to a tag.
    """
    lookup_dict = {}
    with open(lookup_file, mode='r', newline='') as file:
        # Read and skip the header
        header = file.readline()
        
        # Process each line in the lookup file
        for line in file:
            fields = line.split(',')
            if len(fields) < 3: 
                continue
            
            dstport = fields[0].strip()
            protocol = fields[1].strip().lower()
            tag = fields[2].strip()
            
            key = (dstport, protocol)
            lookup_dict[key] = tag
            
    return lookup_dict

def process_flow_logs(flow_log_file, lookup_dict):
    """
    Process the flow log file and count occurrences of each tag and port/protocol combination.
    """
    tag_counts = defaultdict(int)
    port_protocol_counts = defaultdict(int)
    
    with open(flow_log_file, mode='r') as file:
        # Process each line in the lookup file
        for line in file:
            fields = line.split()
            if len(fields) < 14:
                continue
            
            # Extract relevant fields from the flow log record
            dstport = fields[6]
            protocol = protocol_map[fields[7]]
            
            key = (dstport, protocol)
            tag = lookup_dict.get(key, 'untagged')
            
            # Update counts
            tag_counts[tag] += 1
            port_protocol_counts[key] += 1
    
    return tag_counts, port_protocol_counts

def write_output(tag_counts, port_protocol_counts, output_tag_file, output_port_protocol_file):
    """
    Write the counts of tags and port/protocol combinations to separate output files.
    """
    # Write tag counts to output file
    with open(output_tag_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Tag', 'Count'])
        for tag, count in tag_counts.items():
            writer.writerow([tag, count])
    
    # Write port/protocol counts to output file
    with open(output_port_protocol_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Port', 'Protocol', 'Count'])
        for (port, protocol), count in port_protocol_counts.items():
            writer.writerow([port, protocol, count])

def main():    
    lookup_file = 'look_up.txt'
    flow_log_file = 'flow_logs.txt'
    output_tag_file = './output/tag_counts.txt'
    output_port_protocol_file = './output/port_protocol_counts.txt'
    
    # Load the lookup table into a dictionary map of  (dstport, protocol) to tag.
    lookup_dict = load_lookup_table(lookup_file)

    # # Process the flow logs and get counts
    tag_counts, port_protocol_counts = process_flow_logs(flow_log_file, lookup_dict)

    # Write the results to output files
    write_output(tag_counts, port_protocol_counts, output_tag_file, output_port_protocol_file)

if __name__ == '__main__':
    main()
