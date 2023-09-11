# 0x12 - JavaScript Warm-up

## Introduction
Welcome to the "0x12 - JavaScript Warm-up" project. In this project, you will explore the fundamentals of JavaScript by completing a series of tasks. By the end of this project, you'll have a solid understanding of JavaScript basics, including variables, functions, loops, and more.

## Prerequisites
Before you start working on the tasks, make sure you have the following set up:
- Node.js (version 14.x) installed. If not, you can install it with the following commands:
  ```shell
  $ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
  $ sudo apt-get install -y nodejs
  ```
- Semi-Standard style for JavaScript. You can install it globally with:
  ```shell
  $ sudo npm install semistandard --global
  ```

## Tasks

### 0. First constant, first print
- Create a script that prints "JavaScript is amazing" using a constant variable called `myVar`.
- Use `console.log(...)` to print the output.
- Do not use `var`.

### 1. 3 languages
- Write a script that prints three lines: "C is fun", "Python is cool", and "JavaScript is amazing".
- Use `console.log(...)` to print the output.
- Do not use `var`.

### 2. Arguments
- Write a script that prints a message depending on the number of arguments passed:
  - If no arguments are passed, print "No argument".
  - If only one argument is passed, print "Argument found".
  - Otherwise, print "Arguments found".
- Use `console.log(...)` to print the output.
- Do not use `var`.
- Reference: `process.argv`

### 3. Value of my argument
- Write a script that prints the first argument passed to it:
  - If no arguments are passed, print "No argument".
- Use `console.log(...)` to print the output.
- Do not use `var`.
- Do not use `length`.

### 4. Create a sentence
- Write a script that prints two arguments passed to it in the format: "<arg1> is <arg2>".
- Use `console.log(...)` to print the output.
- Do not use `var`.

### 5. An Integer
- Write a script that prints "My number: <arg>" if the argument can be converted to an integer:
  - If the argument can't be converted to an integer, print "Not a number".
- Use `console.log(...)` to print the output.
- Do not use `var`.
- Do not use try/catch.

### 6. Loop to languages
- Write a script that prints the same lines as task 1 but using an array of strings and a loop.
- Use `console.log(...)` to print the output.
- Do not use `var`.
- Do not use any if/else statement.
- Use only one `console.log`.
- Use a loop (while, for, etc.).

### 7. I love C
- Write a script that prints "C is fun" x times, where x is the first argument of the script:
  - If the first argument can't be converted to an integer, print "Missing number of occurrences".
- Use `console.log(...)` to print the output.
- Do not use `var`.
- Use only two `console.log`.
- Use a loop (while, for, etc.).

### 8. Square
- Write a script that prints a square made of the character 'X':
  - The first argument is the size of the square.
  - If the first argument can't be converted to an integer, print "Missing size".
- Use `console.log(...)` to print the output.
- Use the character 'X' to print the square.
- Do not use `var`.
- Use a loop (while, for, etc.).

### 9. Add
- Write a script that prints the addition of two integers:
  - The first argument is the first integer.
  - The second argument is the second integer.
- Define a function with the prototype: `function add(a, b)`.
- Use `console.log(...)` to print the output.
- Do not use `var`.

### 10. Factorial
- Write a script that computes and prints the factorial of a given integer:
  - The first argument is an integer used for computing the factorial.
  - The factorial of NaN is 1.
- Implement the computation recursively.
- Define a function for this task.
- Use `console.log(...)` to print the output.
- Do not use `var`.

### 11. Second biggest!
- Write a script that searches for the second biggest integer in the list of arguments.
- If no argument is passed, print 0.
- If only one argument is passed, print 0.
- Use `console.log(...)` to print the output.
- Do not use `var`.

### 12. Object
- Update the script to replace the value 12 with 89 in the `myObject` constant.
- You are not allowed to use `var`.

### 13. Add file
- Write a function that returns the addition of two integers.
- The function must be visible from outside and named `add`.
- You are not allowed to use `var`.

## Conclusion
This project is designed to help you become familiar with JavaScript fundamentals and common coding practices. Completing these tasks will enhance your understanding of variables, functions, loops, and more. Happy coding!
