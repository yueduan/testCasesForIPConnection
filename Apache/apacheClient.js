var http = require('http');

//var stdin = process.openStdin();
//console.log("Please enter the ip address of the apache server!");


//stdin.addListener("data", function(d) {
//	console.log("you entered: [" + d.toString().trim() + "]");


//{
  	console.log("You connecting to : [" + process.argv[2] + "]");
	var options = { 
        	host: process.argv[2], 
        	path: '/' 
	};

	
	callback = function(response) {
		var str = '';
		//another chunk of data has been recieved, so append it to `str`
		response.on('data', function (chunk) {
			str += chunk;
		});
	
		//the whole response has been recieved, so we just print it out here
		response.on('end', function () {
			console.log(str);
		});
	}

	http.request(options, callback).end();

	console.log("connection ended!");

	//stdin.end();
//});

