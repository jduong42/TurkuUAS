/* 2. JavaScript boolean values. (2 * 0,5 = 1 point)

a. Are the following values true or false in JavaScript? Use a browser console and program an if-else statement to find the answers.

                true, false, 9, -0.7, 0, ‘kissa’, ‘’,”“, null, undefined, {}, [], [0,1] 

b. Why is important to know the truthy values in JavaScript? Give also an example.

    It's important to know the truthy values, because it can affect on the behavior of conditional statements, logical operators and other operations that
    rely on boolean values. For example, if you want to check if a variable has a value, you can use the following code:

    function do_something(value) {
        if (value) {
            console.log("Value is truthy, doing some operation");
        } else {
            console.log("Value is falsy, skippning the operation");
        }
    }

*/

function check_if_true_or_false(value) {
    if (value) {
        console.log(value + " is true");
    } else {
        console.log(value + " is false");
    }
}

check_if_true_or_false(true);       // true
check_if_true_or_false(false);      // false
check_if_true_or_false(9);          // true 
check_if_true_or_false(-0.7);       // true
check_if_true_or_false(0);          // false
check_if_true_or_false('kissa');    // true
check_if_true_or_false('');         // false
check_if_true_or_false("");         // false
check_if_true_or_false(null);       // false
check_if_true_or_false(undefined);  // false
check_if_true_or_false({});         // true
check_if_true_or_false([]);         // true
check_if_true_or_false([0,1]);      // true