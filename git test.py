with open("system_log.3.txt") as f:
    with open("out.txt", "w") as f1:
        with open("out2.txt", "w") as f2:    
            for line in f:
                if "adapter" in line:
                    f1.write(line)
                if "breakpoint" in line:
                    f2.write(line)
