# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Try programiz.pro")

def solution(commands):
    current_bucket = None
    buckets = {}
    max_bucket = None
    max_files = -1

    for command in commands:
        parts = command.split()
        action = parts[0]
        
        if action == 'goto':
            current_bucket = parts[1]
            if current_bucket not in buckets:
                buckets[current_bucket] = []
        elif action == 'create':
            if current_bucket:
                file_name = parts[1]
                buckets[current_bucket].append(file_name)
                
              
                if len(buckets[current_bucket]) > max_files:
                    max_files = len(buckets[current_bucket])
                    max_bucket = current_bucket
        else:
            print(f"Unknown command: {command}")
    
    return buckets, max_bucket

commands = [
    'goto bucketA',
    'create fileA',
    'create fileB',
    'goto bucketB',
    'create fileA',
    'create fileB',
    'create filec'
]

buckets, max_bucket = solution(commands)
print(f"\nBucket with maximum files: {max_bucket}")
