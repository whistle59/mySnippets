/*
This example was taken from https://javascript.info/constructor-new
Thanks to Ilya for that awsome course!!

FUNCTIONALITY:
Create a constructor function Calculator that creates “extendable” calculator objects.

Step1: implement the method calculate(str) that takes a string like "1 + 2"
in the format “NUMBER operator NUMBER” (space-delimited) and returns the result.
 Should understand plus + and minus -.

Step 2: add the method addOperator(name, func) that teaches the calculator
 a new operation. It takes the operator name and the two-argument function
 func(a,b) that implements it.

*/

function Calculator() {
  let methods = {
    "+": (a,b) => a + b,
    "-": (a,b) => a - b
  };

  this.addMethod = function(name, func) {
    methods[name] = func;
    console.log(methods);
  };

  this.calculate = function(str) {
    let split = str.split(" "),
    a = +split[0],
    op = split[1],
    b = +split[2];

    if(!methods[op] || isNaN(a) || isNaN(b)) {
      return NaN;
    }

    return methods[op](a,b);
  };
}

let calc = new Calculator();
console.log(calc.calculate("2 + 3"));
console.log(calc.calculate("4 - 3"));

let powerCalc = new Calculator();
powerCalc.addMethod("*", (a, b) => a * b);
console.log(powerCalc.calculate("2 * 3"));

powerCalc.addMethod("**", (a, b) => a ** b);
console.log(powerCalc.methods);

let otro = powerCalc.calculate;
console.log(otro);
console.log(otro("2 * 3"));
