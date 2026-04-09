#!/usr/bin/env python3

ip_dict = {}
endpoint_dict = {}

def get_value(item):
    return item[1]

def sort_dict_change_tuple(target):
    return sorted(target.items(), key=get_value, reverse=True)

def target_counter(dict_name, target):
    if target not in dict_name:
        dict_name[target] = 1
    else:
        dict_name[target] += 1
    return dict_name

def print_top_ten_failures(label, sorted_tuple):
    print(f"\nTop 10 failing {label}s:")
    for target, connection_amount in sorted_tuple[:10]: # ip=index0 connection_amount=index1
        print(f"{label}: {target}, failures: {connection_amount}")
print("\n#############################################")
print("Filtering HTTP 4xx error logs from access.log")
with open("access.log") as file:
    for line in file:
        line = line.strip() # remove new line
        fields = line.split()

        if len(fields) != 12:
            continue # skip malformed lines

        try:
            status_code = int(fields[8])
        except ValueError:
            continue

        ip = fields[0]
        date = fields[3]
        path = fields[6]
        response_size = fields[9]
        method = fields[11]

        if 400 <= status_code < 500:
            print(
f"""
Status code:       {status_code}
URL path:          {path}
Connection method: {method[1:-1]}
Response size:     {response_size}
IP:                {ip}
Date:              {date[1:]}"""
)

        ip_dict = target_counter(ip_dict, ip)
        endpoint_dict = target_counter(endpoint_dict, path)

sorted_ip_tuple = sort_dict_change_tuple(ip_dict)
sorted_endpoint_tuple = sort_dict_change_tuple(endpoint_dict)

print_top_ten_failures("IP", sorted_ip_tuple)
print_top_ten_failures("Endpoint", sorted_endpoint_tuple)
