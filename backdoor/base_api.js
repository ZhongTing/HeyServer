var server_url = "http://140.124.181.195:8000/api/";
var access_token = "test";

var rest = require('restler');

function api(method, path, data, need_token, callback) {
    method = method.toLowerCase();
    path = server_url + path;

    var headers = {};
    if (need_token)
        headers["Authorization"] = access_token;

    var options = {
        headers: headers,
    };
    if (Object.keys(data).length > 0)
        options["data"] = data;

    rest[method](path, options).on('complete', function(data, response) {
        console.log("API => [" + method.toUpperCase() + "]", path);
        if (response.statusCode == 200)
            callback(data);
        else
            console.log("ERROR =>", response.rawEncoded);
    });
}

module.exports = api;
