var app = require('http').createServer(handler)
var io = require('socket.io')(app);
var fs = require('fs');

app.listen(8001);

var cookie_reader = require('cookie');
var querystring = require('querystring');
 
var redis = require('socket.io/node_modules/redis');
var sub = redis.createClient();
 
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


io.configure(function(){
    io.set('authorization', function(data, accept){
        if(data.headers.cookie){
            data.cookie = cookie_reader.parse(data.headers.cookie);
            return accept(null, true);
        }
        return accept('error', false);

    });
    io.set('log level', 1);

});

 
 
io.sockets.on('connection', function (socket) {
  
  sub.on('message', function(channel, message){
    socket.send(message);
  });

  socket.on('send_message', function(message){
    values = querystring.stringify({
        comment: message,
        sessionid: socket.handshake.cookie['sessionid'],
    });

    var options = {
        host: 'localhost',
        port: 8000,
        path: '/node_api'
        method: 'POST'
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

