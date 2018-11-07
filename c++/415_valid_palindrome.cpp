/*
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.

Example
"A man, a plan, a canal: Panama" is a palindrome.

"race a car" is not a palindrome.

Challenge
O(n) time without extra memory.
*/

#include "helper.h"

class Solution {
public:
    /**
     * @param s: A string
     * @return: Whether the string is a valid palindrome
     */
    bool isPalindrome(const string &s) {
        // write your code here
        if (s.empty()) {
            return true;
        }
        int i = 0, j = s.length() - 1;
        while (i < j) {
            if (!isalnum(s[i])) {
                i++;
                continue;
            }
            if (!isalnum(s[j])) {
                j--;
                continue;
            }
            if (toupper(s[i]) != toupper(s[j])) {
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
};

int main() {
    Solution s;
    cout << s.isPalindrome(string("")) << endl;
    cout << s.isPalindrome(string("A man, a plan, a canal: Panama")) << endl;
    cout << s.isPalindrome(string("race a car")) << endl;
}

