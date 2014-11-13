function getOctet() {
    return Math.round(Math.random()*255);
}

methods = ["GET", "POST"]
actions = ["VIEW", "DOWNLOAD", "SUBMIT"]

for (var i = 1; i <= 25000; i++) {
    db.statistics.insert({
        "request_ip": getOctet() + '.' + getOctet() + '.' + getOctet() + '.' + getOctet(),
        "owner": ObjectId(),
        "request_date": ISODate(),
        "request_method": methods[Math.floor(methods.length * Math.random())],
        "request_uri": "api.myapplication.com/v1/document/" + i,
        "action": actions[Math.floor(actions.length * Math.random())],
        "request_time_milliseconds": 379,
        "loc": [-121.89,37.3378],
        cookies: ['generated']
   })
}
