//var stdin = process.openStdin();

//console.log("Please enter the ip address of the Node.js server!"); 

//stdin.addListener("data", function(d) {
	// note:  d is an object, and when converted to a string it will
    	// end with a linefeed.  so we (rather crudely) account for that  
    	// with toString() and then substring()
	console.log("You connecting to : [" + process.argv[2] + "]");
	
	var s =  require('net').Socket();
	s.connect(20112, process.argv[2]);

	s.write('Hello');
	s.end();
	
	console.log("connection ended!");
	
	//stdin.end();

//});
