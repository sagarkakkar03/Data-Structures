class Solution:
	# @param A : list of strings
	# @param B : integer
	# @return a list of strings
	def fullJustify(self, A, B):
        ans = []
        arr = []
        string = 0
        i = 0
        ans_string = ''
        while i < len(A):
            # print(i, ans, string)
            if arr == []:
                arr.append(A[i])
                string += len(A[i])
                i += 1
            else:
                if 1 + string + len(A[i]) <=B:
                    arr.append(A[i])
                    string += 1 
                    string += len(A[i])
                    i += 1
                else:
                    if len(arr) == 1:
                        ans.append(arr[0]+(B-len(arr[0]))*' ')
                    else:
                        spacing = (B - string)//(len(arr) - 1)
                        extra = B - spacing*(len(arr)-1) - string 
                        ans_string = ''
                        for j in range(len(arr)):
                            ans_string += arr[j]
                            if j != len(arr)-1:
                                ans_string += (spacing + 1)*' '
                                if extra > 0:
                                    ans_string += ' '
                                    extra -= 1
                        ans.append(ans_string)
                    arr = []
                    string = 0
        string = ''
        for i in range(len(arr)):
            string += arr[i]
            if i != len(arr)-1:
                string += ' '
        if string != '':
            ans.append(string + (B-len(string))*' ')
        return ans
