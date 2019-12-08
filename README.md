# Recreating-VLabs-CSO-Experiment
Experiment- Representation of Integers and their arithmetic

<h1 align="center"> Representation of Integers and their Arithmetic </h1> <br>

<p align="center">

  <a href="http://cse11-iiith.vlabs.ac.in/Introduction.html">
    <img alt="CSO" title="Computer Stucture and Architecture" src="./CSO.png" width="450">
  </a>
</p>

<p align="center" >

  Know the representation the binary numbers in various forms.
</p>

<p align="center">
  Brought to you by
</p>
<p align="center">
  <a href="http://www.vlab.co.in/">
    <img alt="VLabs" title="VLabs" src="./logo.jpg" width="450">
  </a>
</p>

## Table of Contents

  Getting Started
- [Prerequisites](#prerequisites)
- [Browser Support](#browser-support)
- [Installing](#installing)
  
Running the tests
- [Break down into end to end tests](#break-down-into-end-to-end-tests)
  
Theory
- [Introduction](#introduction)
- [Unsigned Integers](#unsigned-integers)
- [Signed Integers](#signed-integers)
- [Unsigned versus 2's complement addition](#unsigned-versus-2's-complement-addition)
- [References](#references)
  
Coding Style
- [Built With](#built-with)

  
- [Contributing](#contributing)
- [Authors](#authors)
- [Acknowledgments](#acknowledgments)

## Getting Started

This Experiment is mainly to give you an understanding on the representation of binary numbers in varios forms like Unsigned, Signed, One's complement etc.

Follow the given instructions to run the project on your local machine.

### Prerequisites

Things you need to install before running the project.

```
Python3
Flask
SQLAlchemy
```

### Browser Support

 <img src="https://user-images.githubusercontent.com/1215767/34348387-a2e64588-ea4d-11e7-8267-a43365103afe.png" alt="Chrome" width="16px" height="16px" /> Chrome | <img src="https://user-images.githubusercontent.com/1215767/34348590-250b3ca2-ea4f-11e7-9efb-da953359321f.png" alt="IE" width="16px" height="16px" /> Internet Explorer | <img src="https://user-images.githubusercontent.com/1215767/34348380-93e77ae8-ea4d-11e7-8696-9a989ddbbbf5.png" alt="Edge" width="16px" height="16px" /> Edge | <img src="https://user-images.githubusercontent.com/1215767/34348394-a981f892-ea4d-11e7-9156-d128d58386b9.png" alt="Safari" width="16px" height="16px" /> Safari | <img src="https://user-images.githubusercontent.com/1215767/34348383-9e7ed492-ea4d-11e7-910c-03b39d52f496.png" alt="Firefox" width="16px" height="16px" /> Firefox |
| :---------: | :---------: | :---------: | :---------: | :---------: |
| Yes | 10+ | Yes | Yes | Yes |

### Installing

Step by step series to run the development env.



First, Clone the Repository

```
git clone https://github.com/mallika2011/Recreating-VLabs-CSO-Experiment.git
```

Go to the folder containing the run.py

```
cd Recreating-VLabs-CSO-Experiment/app/
```
Run the python file using python3

```
python3 run.py
```
Open any browser. Go to below described page to view this experiment and its components

```
http://localhost:5000/introduction
```
To directly view the experiment page, go to this link

```
http://localhost:5000/experiment
```


Select the Bitmode you want to use.
Select any two binary numbers and press the 'ADD' button. The result will be displayed in the bottom left table.
The result is also show by the highlighted green cells in the table. If there is an overflow on adding the two numbers, no cell of the table is highlighted, rather the answer is displayed in the results table.

Eg: Select 1010 and 1101.
    You will see the 1's complement and signed answers highlighted in green in the table (However the 2's complement and unsigned arithmetic results in an overflow).
    The results are also displayed in the bottom left table (Including the ones which have resulted in an overflow).

If you want to restart the experiment with other inputs, click the 'RESET' button.

If you want to change the Bitmode, click the 'SWITCH TO 5-BIT' button. This button can be used to toggle between the Bitmodes.

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Run the given python code your local machine

```
python3 tester.py
```
This test case checker will check the results of some random (built-in) test cases and try to match the results with the original answers and show whether the test cases have passed or failed.

## Theory

### INTRODUCTION

What does the 8-bit string 11100000 represent? It could mean 224, -96, -31 and -32 when treated as an unsigned integer, sign-magnitude integer, one’s complement integer and two’s complement integer respectively. Or it could be mean the ASCII character α. So what a bit string means depends on the semantics or the definition we associate with it. In this write-up we shall study binary representation of unsigned and signed integers which is a primitive data structure supported by all modern processors.

### UNSIGNED INTEGERS

Consider the bijective function B2Uw:{0,1}w→ {0,· · ·,2w−1} which maps w-bit binary strings to unsigned integers as follows.
<a href="https://www.codecogs.com/eqnedit.php?latex=\&space;B2U_{w}(\vec{b})&space;=&space;\sum_{i=0}^{w-1}\&space;b_{i}\2^{i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\&space;B2U_{w}(\vec{b})&space;=&space;\sum_{i=0}^{w-1}\&space;b_{i}\2^{i}" title="\ B2U_{w}(\vec{b}) = \sum_{i=0}^{w-1}\ b_{i}\2^{i}"/></a>

For example B2U4(0101) = 5 and B2U4(1101) = 13. You can observe that the function B2Uw and its inverse are efficiently computable. In other words, we can easily compute the binary representation of an unsigned integer in the range of the function making it a viable representation.

In C-language all variables of type unsigned integers are allocated a fixed number of bytes (or equivalent number of bits) for storage which is typically 4 bytes or 32 bits. You can check this by running the following C-program on your machine.

```
#include <stdio.h>
main()
{
    printf("Size of Unsigned Integer: %d\n", sizeof(unsignedint));
}
```
Having represented unsigned integers in binary, we would like to figure out how to perform addition and multiplication operations. Let us just focus on addition operation in our discussion and the relevant ideas can be applied to multiplication operations too with suitable modifications.  We presume that you know the algorithm to add two binary numbersas illustrated in the Figure 11.  We also know the analogous algorithm for addition in the unsigned integer domain.  Now the beauty of the mapping function  <a href="https://www.codecogs.com/eqnedit.php?latex=B2U_{w}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?B2U_{w}" title="B2U_{w}" /></a> is that it shows the isomorphic structure between the unsigned integers and their binary representation with respect to the addition operation (and also multiplication operation). 

To elaborate more on this idea let us define the w-bit addition of two numbers as the regular binary addition except that we ignore the carry-out bit from the MSB if at all there is one. With this definition, when we add two w-bit numbers, the result is always a w-bitnumber. 

The key claim here is whether we do addition of two unsigned integers in decimal notation which we are familiar with or we do addition of their respective w-bit binary representations, the net result is just the same except for the difference in their notational representation. This claimis true so far as the result of the addition operation does cause an overflow, in other words the result would fit into w-bits. Consider the following Table 1 with three columns. If we want to add 1 and 4, whether we carry out addition in column 2 or in column 3, the respective results would fall in Row 5. However if we want to add 4 and 5, then the result wouldn’t fall in the range in the column 2 and the result in the column 3 would fall in Row-1 (recall how w-bit additionis defined). 

It can be observed though that there is isomorphism between (mod2w) addition of decimal numbers and w-bit addition of binary numbers without worrying about overflow at allsince it would never happen in modular arithmetic. It has to be noted here that we can use any other function (preferably bijective) from the w-bit strings to unsigned numbers and createa isomorphism between the decimal domain and the binary domain by appropriately defining the addition operations in the binary domain. We leave it to you to ponder whether such an alternate function has any utility. It is easy to note here that the addition of two w-bit unsigned numbers would cause an overflow if and only if the carry-out bit is 1.

### SIGNED INTEGERS

The following are three different ways of representing signedintegers.

1. Sign-Magnitude Representation. The mapping function here is:
   <a href="https://www.codecogs.com/eqnedit.php?latex=B2S_{w}(b_{w-1}...b_{0})&space;=&space;(-1)^{b_{w-1}}*(2^{w-2}*b_{w-2}&plus;...&plus;2^0*b_{0})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?B2S_{w}(b_{w-1}...b_{0})&space;=&space;(-1)^{b_{w-1}}*(2^{w-2}*b_{w-2}&plus;...&plus;2^0*b_{0})" title="B2S_{w}(b_{w-1}...b_{0}) = (-1)^{b_{w-1}}*(2^{w-2}*b_{w-2}+...+2^0*b_{0})" /></a>

2. 1’s Complement Representation. The mapping function here is:
<a href="https://www.codecogs.com/eqnedit.php?latex=B2O_{w}(b_{w-1}...b_{0})&space;=&space;-b_{w-1}*(2^{w-1}-1)&space;&plus;&space;b_{w-2}*2^{w-2}&plus;...&plus;b_{0}*2_{0}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?B2O_{w}(b_{w-1}...b_{0})&space;=&space;-b_{w-1}*(2^{w-1}-1)&space;&plus;&space;b_{w-2}*2^{w-2}&plus;...&plus;b_{0}*2_{0}" title="B2O_{w}(b_{w-1}...b_{0}) = -b_{w-1}*(2^{w-1}-1) + b_{w-2}*2^{w-2}+...+b_{0}*2_{0}" /></a>

3. 2’s Complement Representation. The mapping function here is:
<a href="https://www.codecogs.com/eqnedit.php?latex=B2T_{w}(b_{w-1}...b_{0})&space;=&space;-b_{w-1}*2^{w-1}&space;&plus;&space;b_{w-2}*2^{w-2}&plus;...&plus;b_{0}*2_{0}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?B2T_{w}(b_{w-1}...b_{0})&space;=&space;-b_{w-1}*2^{w-1}&space;&plus;&space;b_{w-2}*2^{w-2}&plus;...&plus;b_{0}*2_{0}" title="B2T_{w}(b_{w-1}...b_{0}) = -b_{w-1}*2^{w-1} + b_{w-2}*2^{w-2}+...+b_{0}*2_{0}" /></a>

Pretty much all systems use 2’s complement representation for signed integers. We shall see the rationale behind such a choice in the following discussion. First you can verfiy that among the 3 mapping functions only the B2Tw function corresponding to 2’s complement representation is bijective.

Let us stick to our definition of w-bit addition of binary numbers and we shall see that there is an isomorphic structure between signed integers and their 2’s complement representation with respect to addition. It has to be noted that this isomorphism holds if and only if the results of addition does not cause overflow or underflow.

Sign-magnitude and 1’s complement representation of signed integers doesn’t carry this isomorphic structure with respect to the canonical binary addition rules.  It is worth noting that we can create an isomorphic structure even with these representations by suitable modifying the rules of binary addition.

However it can be verified that as long as there is no overflow there is a perfect isomorphism with respect to addition between binary and two’s complement representation of numbers.

### UNSIGNED versus 2's COMPLEMENT ADDITION

From the previous discussion it could have been noted that the rules of binary addition for both Unsigned and 2’s Complement Addition is exactly the same. It means that we could use the same k-bit ripple carry to add any 2 unsigned or 2’s complement numbers and we need not tell the k-bit ripple adder whether we are doing signed arithmetic or unsigned arithmetic.

To illustrate this point further let us assume that I have a k-bit adder circuit with me, some of the students in the class want to do 2’s complement addition and some of you may want to perform unsigned addition over k-bit numbers using my k-bit adder circuit. But you don’t want to reveal to me whether you have performed signed or unsigned arithmetic. It is no big deal for the k-bit adder circuit as the rules of addition remains the same for both signed and unsigned numbers. However there is a catch here. The catch is that overflow conditions for signed and unsigned arithmetic are different.


## CODING STYLE

This Project is written using Flask, Database and python fullstack for back-end and HTML, CSS, Javascript, JQuery and AJAX for front-end.

In the Front-end, Javascript uses AJAX and sends POST request to the back-end server where it uses the python files to return a JSON object containing the sum of inputs selected.

```
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
            }
```

and the returned json object look like

```json

{ 
    'res':binary(input1+input2),
    'two':two's complement(input1)+two's complement(input2),
    'one':one's complement(input1)+one's complement(input2),
    'un':input1+input2,
    'sign':signed(input1)+signed(input2)
}

```

The quiz section of this project was implemented using a database which sent the selected options into the database on clicking the submit button. All the resources for the file are self-contained in the "static" folder and is loaded from the server side.


### REFERENCES


Computer Systems: A Programmer's Perspective, Second Edition (CS:APP2e) Randal E. Bryant and David R. O'Hallaron  Prentice Hall, 2011 (ISBN 0 13-610804-0) 

## Built With

* [Flask](http://flask.pocoo.org/) - The web framework used
* [Python](https://www.python.org/) - To bring the project together
* HTML,CSS and JS - For all the web development aspects

## Contributing

Intrested!

Contribute to this project through Vlabs

<http://www.vlab.co.in/>


## Authors

* **Mallika Subramanian** - [Mallika Subramanian](https://github.com/mallika2011)

* **Sachin Kumar** - [Sachin Kumar](https://github.com/SachinKumar105)
 

## Acknowledgments

* Our Teaching Assistant Anubhab Sen who helped us at every step of this project.
* Inspiration : The CSO course.

