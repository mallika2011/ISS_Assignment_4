var table = document.getElementById('table');
// console.log(table);

// for (var x = 0; x < 2; x++) {
    for (var i = 1; i < table.rows.length; i++) {
        table.rows[i].onclick = function () {
            // rIndex = this.rowIndex;
            $(table).css("background-color","red");
            var x = this.cells[1].innerHTML;
            console.log(x);
            $.ajax({
                url: "/", // Path of the python script to do the processing
                method: "POST", // Method to submit the HTTP request as, usually either POST or GET
                data: { // These are the POST parameters passed to the backend script
                    binary1: x,
                },
                success: function (returned_data) { // Function to run if successful, with the function parameter being the output of the url script
                    alert('Here is the output: ' + returned_data);
                },
                error: function () { // Function to run if unsuccessful
                    alert('An error occured');
                }
            });




            
        };
    }

    for (var i = 1; i < table.rows.length; i++) {
        table.rows[i].onclick = function () {
            // rIndex = this.rowIndex;
            var x2 = this.cells[1].innerHTML;
            console.log(x2);
            $.ajax({
                url: "/", // Path of the python script to do the processing
                method: "POST", // Method to submit the HTTP request as, usually either POST or GET
                data: { // These are the POST parameters passed to the backend script
                    binary2: x,
                },
                success: function (returned_data) { // Function to run if successful, with the function parameter being the output of the url script
                    alert('Here is the output: ' + returned_data);
                },
                error: function () { // Function to run if unsuccessful
                    alert('An error occured');
                }
            });


        };
    }



