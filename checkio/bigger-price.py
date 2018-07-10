from operator import itemgetter
def bigger_price(limit, data):
    strng = ""
    newlist = sorted(data, key=itemgetter('price'), reverse=True)
    return [newlist[i] for i in range(limit)]
