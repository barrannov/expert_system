def read_buffer(name_file):
    try:
        with open(name_file, "r") as f:
            return f.read()
    except Exception as e:
        print("Invalid file provided.\n")
        raise