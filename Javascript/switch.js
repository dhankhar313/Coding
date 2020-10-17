function input_value(num){
    switch(num){
        case 1:
            console.log('Case 1');
            break;
        case 2:
            console.log('Case 2');
            break;
        case 'x':
            console.log('Case 3');
            break;
        default:
            console.log('Default');
            break;
    }
}

input_value(1)
input_value(2)
input_value(3)
input_value('x')
input_value(6)