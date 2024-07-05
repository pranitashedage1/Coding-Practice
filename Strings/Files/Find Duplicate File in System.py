'''
Given a list paths of directory info, including the directory path, 
and all the files with contents in this directory, return all the duplicate files in the file system in
 terms of their paths. You may return the answer in any order.

A group of duplicate files consists of at least two files that have the same content.

A single directory info string in the input list has the following format:
"root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ... fn.txt(fn_content)"
It means there are n files (f1.txt, f2.txt ... fn.txt) with content 
(f1_content, f2_content ... fn_content) respectively in the directory "root/d1/d2/.../dm". 
Note that n >= 1 and m >= 0. If m = 0, it means the directory is just the root directory.

The output is a list of groups of duplicate file paths. For each group, it contains all the file 
paths of the files that have the same content. 
A file path is a string that has the following format:
"directory_path/file_name.txt"
 

Example 1:
Input: paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
Output: [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]

Example 2:
Input: paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)"]
Output: [["root/a/2.txt","root/c/d/4.txt"],["root/a/1.txt","root/c/3.txt"]] 
'''
from collections import defaultdict
class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        # Map to store file content as key and list of file paths as value
        content_map = defaultdict(list)

        for path in paths:
            split_path = path.split(" ")# Split the path by spaces
            dir_path = split_path[0] # First part is the directory path
            for i in range(1, len(split_path)):
                file_path = split_path[i]
                start = file_path.index('(')
                file_name = file_path[:start]
                content = file_path[start+1:-1] #Extract content inside parentheses
                # Add the file path to the map
                content_map[content].append('{}/{}'.format(dir_path, file_name))

         # Collect the result: only include lists with more than one file path
        result = [files for files in content_map.values() if len(files)>1]

        return result

