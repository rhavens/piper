var http = require('http')
var app = require('http').createServer(handler)
var io = require('socket.io')(app);
var fs = require('fs');
var cookieParser = require('cookie-parser')(app);

app.listen(8001, '127.0.0.1');
app.on('error', function(e){
	console.log("Error: " + e.message);
	console.log(e.stack);
});

var querystring = require('querystring');
 
var redis = require('socket.io/node_modules/redis');
var sub = redis.createClient();
console.log("hello world")
sub.subscribe('chat');

function handler(req, res){
    fs.readFile(__dirname + '/index.html', 
        function(err,data){
            if(err){
                res.writeHead(500);
                return res.end('Error loading index.html');
            }

            res.writeHead(200);
            res.end(data);
        });
}


io.use(function(socket, next) {
    var handshake = socket.request;

    if (!handshake) {
        return next(new Error('[[error:not-authorized]]'));
    }

    cookieParser(handshake, {}, function(err) {
        if (err) {
            return next(err);
        }

        var sessionID = handshake.signedCookies['express.sid'];

        // db.sessionStore.get(sessionID, function(err, sessionData) {
        //     if (err) {
        //         return next(err);
        //     }
        //     console.log(sessionData);

        //     next();
        // });
        next()
    });
});


// io.configure(function(){
//     io.set('authorization', function(data, accept){
//         if(data.headers.cookie){
//             data.cookie = cookie_reader.parse(data.headers.cookie);
//             return accept(null, true);
//         }
//         return accept('error', false);

//     });
//     io.set('log level', 1);

// });
 
 
io.on('connection', function (socket) {

    console.log("in io connection")

    socket.emit('news', {hello:'world'});

    sub.on('message', function(channel, message){
        console.log("do we get into message?");
        socket.send(message);
    });

    socket.on('send_message', function(data){
        console.log("success")
        console.log(data.username)
        values = querystring.stringify({
            username: data.username,
            id: data.id,
            comment: data.message,
            sessionid: 25,
        });

        var options = {
            host: 'piper.link',
            port: 80,
            path: '/node_api',
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Content-Length': values.length
            }
        };

        var req = http.get(options, function(res){
            res.setEncoding('utf8');
            res.on('data', function(message){
                if(message != 'Worked'){
                    console.log('Message: ' + message);
                }
            });
        });

        req.write(values);
    req.end();
  });

});

