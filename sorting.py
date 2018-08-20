def bubble_sort(numbers):
    """Sortuje rosnąco listę liczb przy użyciu sortowania bąbelkowego"""
    while True:
        # Zaczynamy zakładając, że jest posortowana
        is_sorted = True
        # Porównujemy 2 naraz, przeskakujemy do przodu
        node = numbers.begin.next
        while node:
            # Wykonujemy pętlę, porównując węzeł z następnym
            if node.prev.value > node.value:
                # Jeśli następny jest większy, musimy je zamienić
                node.prev.value, node.value = node.value, node.prev.value
                # Ups, wygląda na to, że musimy ponownie skanować
                is_sorted = False
            node = node.next
        # Zresetowanie do początku, ale jeśli niczego nie zamieniliśmy,
        # lista jest posortowana
        if is_sorted:
            break


def count(node):
    count = 0
    while node:
        node = node.next
        count += 1
    return count


def merge_sort(numbers):
    numbers.begin = merge_node(numbers.begin)
    # Okropny sposób, aby pobrać end
    node = numbers.begin
    while node.next:
        node = node.next
    numbers.end = node


def merge_node(start):
    """Sortuje listę liczb, używając sortowania przez scalanie"""
    if start.next is None:
        return start

    mid = count(start) // 2

    # Skanowanie w kierunku środka
    scanner = start
    for i in range(0, mid-1):
        scanner = scanner.next

    # Ustawienie środkowego węzła zaraz po punkcie skanowania
    mid_node = scanner.next
    # Podzielenie w punkcie środkowym
    scanner.next = None
    mid_node.prev = None

    merged_left = merge_node(start)
    merged_right = merge_node(mid_node)

    return merge(merged_left, merged_right)


def merge(left, right):
    """Wykonuje scalanie dwóch list"""
    result = None

    if left is None:
        return right
    if right is None:
        return left

    if left.value > right.value:
        result = right
        result.next = merge(left, right.next)
    else:
        result = left
        result.next = merge(left.next, right)

    result.next.prev = result
    return result


def quicksort_sort(numbers):
    quicksort(numbers, 0, count(numbers.begin)-1)


def quicksort(numbers, lo, hi):
    if lo < hi:
        p = partition(numbers, lo, hi)
        quicksort(numbers, lo, p-1)
        quicksort(numbers, p+1, hi)


def partition(numbers, lo, hi):
    pivot = get_node_by_index(numbers, hi)
    i = lo
    for j in range(lo, hi):
        node_j = get_node_by_index(numbers, j)
        if node_j.value < pivot.value:
            node_i = get_node_by_index(numbers, i)
            node_i.value, node_j.value = node_j.value, node_i.value
            i += 1
    node_i = get_node_by_index(numbers, i)
    node_hi = get_node_by_index(numbers, hi)
    node_i.value, node_hi.value = node_hi.value, node_i.value
    return i


def get_node_by_index(numbers, i):
    node = numbers.begin
    counter = 0
    while node and counter < i:
        node = node.next
        counter += 1
    return node
