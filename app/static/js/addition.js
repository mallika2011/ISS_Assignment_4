var table = document.getElementById('table');
var x1=-1,x2=-1,x;
var ind,i1,i2;
var count=0;

    $('#add').click(
        function(){
            if(x1==-1 || x2==-1)
                alert("Select integers");
        }
    );


    for (var i = 1; i < table.rows.length; i++) {

        


        table.rows[i].onclick = function () {
            // rIndex = this.rowIndex;
            ind =this.rowIndex;
            console.log(ind)
            x = this.cells[1].innerHTML;
            document.getElementById(ind).style.backgroundColor ="#ff5959";

            if(count==0)
            {
                x1=x; console.log("case1");
                i1=ind;
                count++;          

            }
            else if(count==1)
            {
                x2=x; console.log("case2");
                i2=ind;
                count++;          

            }
            else if(count==2)
            {
                x1=x2;
                x2=x;
                document.getElementById(i1).style.backgroundColor = "";
                i1=i2;
                i2=ind;


                console.log("case3");
            }
            
            console.log(ind);
            console.log(i1);
            console.log(i2);

            $('#add').click(
                function compute(){
                if(x1==-1 || x2 ==-1)
                    alert("Select integers");    
                    
                var param={'x1':x1,'x2':x2};


                $.ajax({
                    url:"/answer",
                    type:"POST",
                    data: JSON.stringify(param),
                    contentType: 'application/json; charset=utf-8',
                    datatype:'json',
                    
                    success:function(value)
                    {
                        console.log("THIS WAS SUCCESSFUL")
                        console.log(value);

                        $('#resbinary').html(value['res']);
                        $('#restwo').html(value['two']);
                        $('#resone').html(value['one']);
                        $('#resunsigned').html(value['un']);
                        $('#ressigned').html(value['sign']);

                        bin=value['bin'];

                        two=value['two'];
                        one=value['one'];
                        un=value['un'];
                        sign=value['sign'];

                        console.log(two);

                        var arr=[];
                        arr[1]=bin;
                        arr[2]=two;
                        arr[3]=one;
                        arr[4]=un;
                        arr[5]=sign;


                        var t=document.getElementById("table");
                        for(var i=0, row; row=t.rows[i]; i++)
                        {
                            for(var j=0, col; col=row.cells[j]; j++)
                            {
                                $(col).css('background-color','')
                                var value=col.innerHTML;
                                if(value==arr[j])
                                    $(col).css('background-color', '#a4f6a5');

                            }
                        }
    

                        


                    }

                });

            });

        }
    
    
    
    
    
    }

    









