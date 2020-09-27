// File: reuseable.js
// Aim: Provide useful reuseable functions in JavaScript

function json2list(json) {
  // Convert [json] into a list,
  // the method can be used to generate d3 useable list structure

  // Get keys
  var keys = [];
  for (var key in json) {
    keys.push(key);
  }
  console.log("Keys are: " + keys.join(", "));

  // Convert [json] into list
  // Each entry of the list is a dict of the keys
  var list = [];
  for (var i in json[keys[0]]) {
    series = [];
    for (var j in keys) {
      key = keys[j];
      series[key] = json[key][i];
    }
    list.push(series);
  }
  console.log("Parsed " + list.length + " entries");

  return [list, keys];
}
