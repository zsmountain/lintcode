#include <iostream>
#include <ostream>
#include <sstream>
#include <vector>
#include <iterator>
#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>
#include <stack>
#include <queue>
#include <iomanip>
#include <algorithm>
#include <utility>

using namespace std;

/*********************************************** List *****************************************************************/
struct ListNode {
    int val;
    ListNode *next;

    explicit ListNode(int x) : val(x), next(nullptr) {}
};

ListNode *buildList(vector<int> &values) {
    if (values.empty()) {
        return nullptr;
    }
    ListNode *head = new ListNode(values[0]);
    ListNode *cur;
    ListNode *pre = head;
    for (int i = 1; i < values.size(); ++i) {
        cur = new ListNode(values[i]);
        pre->next = cur;
        pre = cur;
    }
    return head;
}

void printList(ListNode *head) {
    while (head) {
        cout << head->val << "->";
        head = head->next;
    }
    cout << "NULL" << endl;
}

ListNode *mergeTwoLists(ListNode *l1, ListNode *l2) {
    ListNode dummy(0);
    ListNode *p1 = l1, *p2 = l2, *p = &dummy;
    while (p1 && p2) {
        if (p1->val > p2->val) {
            p->next = p2;
            p2 = p2->next;
        } else {
            p->next = p1;
            p1 = p1->next;
        }
        p = p->next;
    }
    if (p1) {
        p->next = p1;
    }
    if (p2) {
        p->next = p2;
    }
    return dummy.next;
}

ListNode* sortList(ListNode* head) {
    if (!head || !head->next) {
        return head;
    }
    ListNode *fast = head, *slow = head;
    while (fast->next && fast->next->next) {
        fast = fast->next->next;
        slow = slow->next;
    }
    fast = slow->next;
    slow->next = nullptr;

    ListNode* p1 = sortList(head);
    ListNode* p2 = sortList(fast);

    return mergeTwoLists(p1, p2);
}

// return the last node after reverse
ListNode *reverse(ListNode *pre, ListNode *end) {
    ListNode *cur = pre->next;
    while (cur->next != end) {
        ListNode *tmp = cur->next;
        cur->next = tmp->next;
        tmp->next =pre->next;
        pre->next = tmp;
    }
    return cur;
}

struct List {
    ListNode *head;

    explicit List(ListNode *head) : head(head) {}

    explicit List(vector<int> &values) : head(buildList(values)) {}

    List() : head(nullptr) {}

    void print() {
        printList(head);
    }

    void free() {
        while (head) {
            ListNode* tmp = head;
            head = head->next;
            delete tmp;
        }
    }

    void remove(ListNode *pre) {
        if (pre && pre->next) {
            ListNode *removedNode = pre->next;
            pre->next = pre->next->next;
            delete removedNode;
        }
    }

    void removeHead() {
        if (head) {
            ListNode *removedNode = head;
            head = head->next;
            delete removedNode;
        }

    }

};

/**********************************************************************************************************************/

/************************************************ Tree ****************************************************************/

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;

    explicit TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}

    void insert(bool left, int val) {
        left ? this->left = new TreeNode(val) : this->right = new TreeNode(val);
    }

    void print(int indent = 0) {
        if (this == nullptr) {
            return;
        }
        if (this->left) {
            this->left->print(indent + 4);
        }
        if (this->right) {
            this->right->print(indent + 4);
        }
        if (indent) {
            cout << std::setw(indent) << ' ';
        }
        cout << this->val << endl;
    }
};

TreeNode *build(vector<int> &preorder, int s1, int e1, vector<int> &inorder, int s2, int e2) {
    if (s1 > e1 || s2 > e2) {
        return nullptr;
    }
    TreeNode *root = new TreeNode(preorder[s1]);
    int index = -1;
    for (int i = s2; i <= e2; ++i) {
        if (inorder[i] == root->val) {
            index = i;
            break;
        }
    }
    if (index == -1) {
        return nullptr;
    }
    int leftSize = index - s2;
    root->left = build(preorder, s1 + 1, s1 + leftSize, inorder, s2, index - 1);
    root->right = build(preorder, s1 + leftSize + 1, e1, inorder, index + 1, e2);
    return root;
}

TreeNode *buildTree(vector<int> &preorder, vector<int> &inorder) {
    if (preorder.empty() || inorder.empty()) {
        return nullptr;
    }

    return build(preorder, 0, preorder.size() - 1, inorder, 0, inorder.size() - 1);
}

/**********************************************************************************************************************/

/*********************************************** Print Utils **********************************************************/

template<typename T>
ostream &operator<<(ostream &out, const vector<T> &v) {
    if (!v.empty()) {
        out << '[';
        std::copy(v.begin(), v.end(), std::ostream_iterator<T>(out, ", "));
        out << "\b\b]";
    } else {
        out << "[]";
    }
    return out;
}

template<typename T>
ostream &operator<<(ostream &out, const vector<vector<T>> &v) {
    out << '[' << endl;
    for (int i = 0; i < v.size(); ++i) {
        out << "\t" << v[i] << endl;
    }
    out << "]" << endl;
    return out;
}

template<typename T1, typename T2>
ostream &operator<<(ostream &out, const map<T1, T2> &m) {
    if (m.empty()) {
        out << "{}";
    }
    for (auto it = m.begin(); it != m.end(); ++it) {
        out << it->first << ":" << it->second << ";";
    }
    return out;
}

template<typename T1, typename T2>
ostream &operator<<(ostream &out, const unordered_map<T1, T2> &m) {
    if (m.empty()) {
        out << "{}";
    }
    for (auto it = m.begin(); it != m.end(); ++it) {
        out << it->first << ":" << it->second << ";";
    }
    return out;
}

/**********************************************************************************************************************/
