class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        memo = {}
		#tracking the max popular video count
        overall_max_popular_video_count = -1
        #looping over the creators
        for i in range(len(creators)):
            if creators[i] in memo:
                #Step 1: update number of views for the creator
                memo[creators[i]][0] += views[i]
                #Step 2: update current_popular_video_view and id_of_most_popular_video_so_far
                if memo[creators[i]][2] < views[i]:
                    memo[creators[i]][1] = ids[i]
                    memo[creators[i]][2] = views[i]
                #Step 2a: finding the lexicographically smallest id as we hit the current_popularity_video_view again!
                elif memo[creators[i]][2] == views[i]:
                    memo[creators[i]][1] = min(memo[creators[i]][1],ids[i])
            else:
			#adding new entry to our memo
			#new entry is of the format memo[creator[i]] = [total number current views for the creator, store the lexicographic id of the popular video, current popular view of the creator]
                memo[creators[i]] = [views[i],ids[i],views[i]]
			#track the max popular video count
            overall_max_popular_video_count = max(memo[creators[i]][0],overall_max_popular_video_count)
        
        result = []
        for i in memo:
            if memo[i][0] == overall_max_popular_video_count:
                result.append([i,memo[i][1]])
        return result
        