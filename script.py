import argparse
import subprocess

def run_traceroute(host, progressive, output_file):
    command = ['traceroute', host]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    output_lines = []
    try:
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                output_lines.append(output.strip())
                if progressive:
                    input("Press Enter to see the next line...")
                print(output.strip())
    except KeyboardInterrupt:
        process.kill()
        print("\nTraceroute interrupted by user.")
    
    if output_file:
        with open(output_file, 'w') as f:
            for line in output_lines:
                f.write(line + '\n')

def main():
    parser = argparse.ArgumentParser(description='Traceroute script with subprocess and argparse.')
    parser.add_argument('host', help='Host name or IP address to traceroute.')
    parser.add_argument('-p', '--progressive', action='store_true', help='List line by line the execution of traceroute using Enter on the keyboard.')
    parser.add_argument('-o', '--output_file', help='Output file name to save the result of the traceroute.')

    args = parser.parse_args()
    run_traceroute(args.host, args.progressive, args.output_file)

if __name__ == '__main__':
    main()