def serialize(items):
    output = []
    for item in items:
        output.append(item.serialize())
    return output
