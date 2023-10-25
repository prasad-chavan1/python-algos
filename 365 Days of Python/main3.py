'''
Problem :
Bob has a playlist of n songs, each song has a singer associated with it (denoted by an integer)
Favourite singer of Bob is the one whose songs are the most on the playlist.
Count the number of Favourite Singers of Bob.

Input Format :
The first line contains an integer n, denoting the number of songs in Bob's playlist.
The following input contains n integers, i'th integer denoting the singer of the i'th song.

Output Format :
Output a single integer, the number of favourite singers of Bob
'''
from collections import defaultdict
singer_count = defaultdict(int)
name = int(input())
singers = input().split()
final_max_count = 0

for singer in singers:
    singer = int(singer)
    singer_count[singer] += 1

max_c = max(singer_count.values())
for count in singer_count.values():
    if count == max_c:
        final_max_count += 1
print(final_max_count)
