counter=1
        for i in range(1,len(nums)):
            if(nums[i]!=nums[i-1]):
                nums[counter]=nums[i]
                counter+=1
                
        del nums[counter+1:]
        return counter
