def sqlRowToJsonDict(rows, rowHeaders):
    jsonData = []
    for result in rows:
        jsonData.append(dict(zip(rowHeaders, result)))
    return jsonData