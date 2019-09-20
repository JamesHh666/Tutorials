# List

* ## [203. Remove Linked List Elements](https://leetcode.com/problems/linked-list-cycle/)
	Remove all elements from a linked list of integers that have value **val**.

	```python
	def removeElements(self, head: ListNode, val: int) -> ListNode:
        head_fake, head_fake.next = ListNode(-1), head
        p = head_fake
        while p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
	        p = p.next
        return head_fake.next
	```
	
	### Summary:
	* Create a **`head_fake`** linked to `head`.
	* Use a pointer `p` to track iteration.
	* Return `head_fake.next`
	
* ## [82. Remove Duplicates from Sorted List II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/)
	* 暴力解法：
	
		Set two pointers `cur` and `p`:
		* `cur` points to current non-duplicated node in the list 
		* `p` points to the duplicated nodes and is used to skip those nodes
	
		```python
		def deleteDuplicates(self, head: ListNode) -> ListNode:
			fake_head = ListNode(-1)
			fake_head.next = head
			p = cur = fake_head
			while cur.next:
				if not cur.next.next:
					break
				if cur.next.val == cur.next.next.val:
					p = cur.next
					while p.next and p.next.val == p.val:
						p = p.next
					cur.next = p.next
				else:
					cur = cur.next

			return fake_head.next
		```
	
	
* ## [876. Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)
	* 暴力解法
		```python
		def middleNode(self, head: ListNode) -> ListNode:
			l = []
			p = head
			while p:
				l.append(p.val)
				p = p.next
			idx = (len(l) // 2) if len(l)%2 == 1 else ((len(l)+1) // 2)
			del l

			i = 0
			ans = head
			while i!= idx:
				ans = ans.next
				i += 1
			return ans
		```
	* **time:** `O(N)`, **space:**`O(N)`:
	
		find all nodes and return the middle one.
		```python
		def middleNode(self, head: ListNode) -> ListNode:
			l = [head]
			while l[-1].next:
				l.append(l[-1].next)
			return l[len(l) // 2]
		```
	* **time:** `O(N)`, **space:**`O(1)`:
	
		use two pointers `tmp` and `head` to track the process, if `tmp` find the end of the linked list, then `head` is in the middle of the list.
		```python
		def middleNode(self, head: ListNode) -> ListNode:
			tmp = head
			while tmp and tmp.next:
				head = head.next
				tmp = tmp.next.next
			return head
		```
	
* ## [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

	Reverse a singly linked list.
	* 暴力解法 (TOO redundant)
		```python
		def reverseList(self, node: ListNode) -> ListNode:
			if not node or not node.next:
				return node
			curr = node
			head = curr.next
			curr.next = None
			while 1:
				temp = head.next
				head.next = curr
				if not temp:
					break
				else:
					curr, head = head, temp
			return head
		```
		
	* [A better one ](https://leetcode.com/problems/reverse-linked-list/discuss/140916/Python-Iterative-and-Recursive-(206))
		```python
		def reverseList(self, node: ListNode) -> ListNode:
			prev = None
			while node:
				curr = node
				node = node.next
				curr.next = prev
				prev = curr
			return prev
		```
	


