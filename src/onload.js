// File: onload.js
// Aim: Run on load of the html

console.log("Onload .js is running.");

function create_colors_table(list, keys) {
  console.log("Creating colors table in #colorsDiv");
  let div = d3.select("#colorsDiv");
  let table = div.append("table");
  let thead = table.append("thead");
  let tbody = table.append("tbody");

  thead
    .append("tr")
    .selectAll("th")
    .data(keys)
    .enter()
    .append("th")
    .text((d) => {
      return d;
    });

  tbody
    .selectAll("tr")
    .data(list)
    .enter()
    .append("tr")
    .selectAll("td")
    .data((d) => {
      return [d.Name, d.Hex, d.RGB, d.HSV, d.CMYK];
    })
    .enter()
    .append("td")
    .text((d) => {
      return d;
    })
    .attr("style", (d) => {
      return "width: " + d.length * 10 + "px;";
    });
}

d3.json("http://localhost:8000/src/colors.json").then(function (data) {
  console.log("Data is loaded:");
  console.log(data);
  var parsed = json2list(data);
  var list = parsed[0];
  var keys = parsed[1];
  create_colors_table(list, keys);
});
