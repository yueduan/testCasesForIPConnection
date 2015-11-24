
var server = require('net').createServer(function (socket) {
	console.log("connected");
	
	socket.on('data', function (data) {
        	console.log(data.toString());
		var fs = require("fs");

		console.log("Going to write into a file: result.txt");
		fs.writeFile('result.txt', data.toString(),  function(err) 
		{
			if (err) {
				return console.error(err);
			}
		});

		socket.destroy();
        	server.close();
	
    	});
})
.listen(20112);
