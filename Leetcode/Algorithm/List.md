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
	
* ## [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)
	
