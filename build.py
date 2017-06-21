# Concatenate following dictionaries to create a new one.
# https://app.commit.live/lesson/fsdse-python-assignment-18

# a = {1: 10, 2: 20}
# b = {3: 30, 4: 40}

#a = dict(a.items() + b.items())
#OR
def solution(a, b):
    a.update(b)
    print a
    return a

# dic(a, b)
#DOne, Not Posted =================================================================================
