#!/usr/bin/node

// Define the addMeMaybe function and export it
exports.addMeMaybe = function addMeMaybe (number, theFunction) {
  theFunction(number + 1);
};
