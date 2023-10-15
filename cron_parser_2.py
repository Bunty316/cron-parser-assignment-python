import sys

def parse_cron(cron_str):
    fields = ['minute', 'hour', 'day of month', 'month', 'day of week', 'command']
    cron_parts = cron_str.split(' ')
    cron_dict = dict(zip(fields, cron_parts))

    ranges = {
        'minute': range(0, 60),
        'hour': range(0, 24),
        'day of month': range(1, 32),
        'month': range(1, 13),
        'day of week': range(0, 7)
    }

    output = []
    for field in fields:
        if field == 'command':
            output.append(f"{field:14} {cron_dict[field]}")
        else:
            if cron_dict[field] == '*':
                output.append(f"{field:14} {' '.join(str(i) for i in ranges[field])}")
            elif ',' in cron_dict[field]:
                output.append(f"{field:14} {cron_dict[field].replace(',', ' ')}")
            elif '-' in cron_dict[field]:
                start, end = map(int, cron_dict[field].split('-'))
                output.append(f"{field:14} {' '.join(str(i) for i in range(start, end + 1))}")
            elif '/' in cron_dict[field]:
                step = int(cron_dict[field].split('/')[1])
                output.append(f"{field:14} {' '.join(str(i) for i in ranges[field] if i % step == 0)}")
            else:
                output.append(f"{field:14} {cron_dict[field]}")

    return '\n'.join(output)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: Please provide a cron string as a command-line argument.")
        sys.exit(1)
    print(parse_cron(sys.argv[1]))