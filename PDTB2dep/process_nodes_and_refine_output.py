# process_nodes_and_refine_output.py
# This script processes nodes and refines the output.

def test():
    comp = 0
    order = 0
    sets = []
    sentid4span = {}
    Span4end = {}
    Order4end = {}

    with open("mytempout.txt", 'r') as F:
        for line in F:
            line = line.strip()
            array = line.split('\t')
            order += 1
            start, end = int(array[1]), int(array[2])
            span = array[0]
            if end - start <= 6:
                sentid4span[span] = 0
                continue
            sets.append(span)
            if start <= comp:
                pass
            if end >= comp:
                comp = end
            Span4end[comp] = span
            Order4end[comp] = order

    return sets, sentid4span, Span4end, Order4end

def check_inclusion(a, aSpan, sets):
    me = list(map(int, aSpan.split('..')))
    myresults = []

    for i1 in range(a):
        items = list(map(int, sets[i1].split('..')))
        result = is_inclusion(me[0], me[1], aSpan, items[0], items[1], sets[i1])
        if result:
            myresults.append(result)

    for i1 in range(a + 1, len(sets)):
        items = list(map(int, sets[i1].split('..')))
        result = is_inclusion(me[0], me[1], aSpan, items[0], items[1], sets[i1])
        if result:
            myresults.append(result)
        if items[0] > me[1]:
            break

    return myresults

def is_inclusion(a1, a2, aa, b1, b2, bb):
    if a1 <= b1 + 6 and a2 >= b2 - 6:
        return bb
    else:
        return None

if __name__ == "__main__":
    sets, sentid4span, Span4end, Order4end = test()
    # Additional processing can be added here

