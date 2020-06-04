# Your code here



def finder(files, queries):
    result = []
    paths_by_file = {}
    for path in files:
        f = path.split('/')[-1]
        # Need to account for multiple paths to same file; wrap first path in a list
        if f not in paths_by_file:
            paths_by_file[f] = [path]
        else:
            paths_by_file[f].append(path)
    for q in queries:
        if q in paths_by_file:
            result.extend(paths_by_file[q])
    return result


if __name__ == "__main__":
    files = []

    for i in range(500000):
        files.append(f"/dir{i}/file{i}")

    for i in range(500000):
        files.append(f"/dir{i}/dirb{i}/file{i}")

    queries = []

    for i in range(1000000):
        queries.append(f"nofile{i}")

    queries += [
        "file3490",
        "file256",
        "file999999",
        "file8192"
    ]

    result = finder(files, queries)
    print(result)
    result.sort()
