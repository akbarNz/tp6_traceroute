To run the script, open a terminal and navigate to the directory where `script.py` is located. Then use the following command:

```bash
python3 script.py <host> [-p] [-o <output_file>]
```

Replace `<host>` with the hostname or IP address you want to traceroute. Use the `-p` option if you want to list the output line by line, and use the `-o` option followed by a filename if you want to save the output to a file.

For example:

```bash
python3 script.py example.com -p -o output.txt
```

This command will run a traceroute to `example.com`, list the output line by line, and save the result to `output.txt`.
