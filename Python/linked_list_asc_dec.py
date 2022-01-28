def is_continuous(LL):
    curr = LL.head
    ascending = True
    descending = True

    while curr.next and (ascending or descending):
        if curr.next.value <= curr.value:
            ascending = False
        if curr.next.value >= curr.value:
            descending = False
        curr = curr.next
    return ascending or descending

