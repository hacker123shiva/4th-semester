#  Linux shell script program to add two numbers.

    
    #!/bin/bash
    # Path: main.sh
    #  Linux shell script program to add two numbers.
    
    echo "Enter first number"
    read a
    echo "Enter second number"
    read b
    c=`expr $a + $b`
    echo "Sum = $c"