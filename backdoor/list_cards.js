var api = require('./base_api');

api("GET", "issue/fetch", {}, true, function(result) {
    console.log(result);
});
