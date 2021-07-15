from utilities.configuration import getQuery


def addbook_payload(isbn, aisle):
    body = {
        "name": "Learn Software Testing",
        "isbn": isbn,
        "aisle": aisle,
        "author": "Advay Modak"
    }
    return body


def payload_DB(query):
    addBody = {}
    tp = getQuery(query)
    addBody['name']: tp[0]
    addBody['isbn']: tp[1]
    addBody['aisle']: tp[2]
    addBody['author']: tp[3]
    return addBody



