'''
You are on a flight and wanna watch two movies during this flight.
You are given int[] movie_duration which includes all the movie duration.
You are also given the duration of the flight which is d in minutes.
Now, you need to pick two movies and the total duration of the two movies is less than or equal to (d - 30min).

Find the pair of movies with the longest total duration. If multiple found, return the pair with the longest movie.

Similar to Two Sum less than K
'''
class Solution:
    def twoSumLessThanK(self, a, K):
        K = K - 30
        a.sort()
        s, e = 0, len(a) - 1
        max_sum = float('-inf')
        
        res = []
        while s < e:
            if a[s] + a[e] <= K:
                if a[s] + a[e] > max_sum:
                    max_sum = a[s] + a[e]
                    res = [a[s], a[e]]
                s += 1
            else:
                e -= 1
        
        return res if max_sum != float('-inf') else []
