#javaScript Objects, Scopes, and Closures

This JavaScript project focuses on objects, scopes, and closures, helping you deepen your understanding of these concepts. 

## Table of Contents

- [General Info](#general-info)
- [Project Tasks](#project-tasks)
- [Requirements](#requirements)
- [Usage](#usage)
- [License](#license)

## Geneneral.

By completing these tasks, you will be able to:

- Understand the basics of JavaScript programming.
- Create and work with objects in JavaScript.
- Learn about the `this` keyword and its significance.
- Handle variable types and scope.
- Gain knowledge about closures and prototypes.
- Inherit objects from one another.

## Project Tasks

This project consists of several tasks, each designed to help you practice and explore different aspects of JavaScript. Here is a brief overview of the tasks:

1. **Rectangle #0**: Create an empty class called Rectangle using the class notation.

2. **Rectangle #1**: Create a class called Rectangle with a constructor that takes two arguments (width and height) and initializes instance attributes accordingly.

3. **Rectangle #2**: Create a class called Rectangle with a constructor that takes two arguments (width and height) and initializes instance attributes accordingly. If either width or height is 0 or not a positive integer, create an empty object.

4. **Rectangle #3**: Extend the Rectangle class to include an instance method `print()` that prints the rectangle using the character 'X'.

5. **Rectangle #4**: Extend the Rectangle class further to include two more instance methods: `rotate()` (exchanges width and height) and `double()` (multiplies width and height by 2).

6. **Square #0**: Create a class called Square that inherits from the Rectangle class. The Square class takes one argument (size) in its constructor and calls the Rectangle constructor using `super()`.

7. **Square #1**: Extend the Square class to include an instance method `charPrint(c)` that prints the square using the character `c`. If `c` is undefined, use the character 'X'.

8. **Occurrences**: Write a function `nbOccurences` that returns the number of occurrences of a given element in a list.

9. **Esrever**: Write a function `esrever` that returns a reversed version of a list without using the built-in `reverse` method.

10. **Log me**: Write a function `logMe` that prints the number of arguments already printed and the new argument value in a specific format.

11. **Number conversion**: Write a function `converter` that converts a number from base 10 to another base passed as an argument.

## Requirements

- Editor: vi, vim, emacs
- Operating System: Ubuntu 20.04 LTS
- Node.js version 14.x
- Installation of `semistandard` for code style checking (Use `sudo npm install semistandard --global`)

## Usage

1. Clone the repository to your local machine.

2. Navigate to the specific task directory.

3. Run the JavaScript files using Node.js to test and verify your solutions.

For example:

```bash
$ node 0-main.js
```

Make sure that your code adheres to the specified coding style and requirements mentioned in each task.

## License

This project is licensed under the terms of the [MIT License](LICENSE).
