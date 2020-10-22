// File: add_colors.js
// Aim: Run on load of the html, add colors components
//      The colors components will be inserted into #colorsDiv

console.log("Onload .js is running.");

function find_color() {
  // Find colors based on input of #colorPicker
  var str = document.getElementById("colorPicker").value;

  // Filter colors
  console.log("Select colors starting with [" + str + "]");
  str = "_c_" + str;

  // Start filter
  let trs = document.getElementsByClassName("color_tr");

  // Count found colors and toggle their visibility
  var count = 0;
  for (var i = 0; i < trs.length; i++) {
    tr = trs[i];
    if (tr.id.startsWith(str)) {
      // Match, show it
      count += 1;
      if (is_hidden(tr)) {
        toggle_visible(tr);
      }
    } else {
      // Not match, hide it
      if (!is_hidden(tr)) {
        toggle_visible(tr);
      }
    }
  }

  console.log("Found " + count + "colors");
  document.getElementById("colorsCount").innerText =
    "Found " + count + " colors";
}

function create_colors_table(list, keys) {
  // Create table of colors
  console.log("Creating colors table in #colorsDiv");
  // Prepare DOMs
  // Init div container
  let div = d3.select("#colorsDiv").append("div").attr("class", "container");
  // Init table
  let table = div.append("table");
  // Init thead of the table
  let thead = table.append("thead");
  // Init tbody of the table
  let tbody = table.append("tbody");

  // Fill thead
  thead
    .append("tr")
    .selectAll("th")
    // Five columns Name, Block, Hex, RGB, HSV, CMYK
    .data([keys[0], "Block", keys[1], keys[2], keys[3], keys[4]])
    .enter()
    .append("th")
    .text((d) => {
      return d;
    });

  // Fill tbody
  tbody
    .selectAll("tr")
    .data(list)
    .enter()
    // Append <tr>
    .append("tr")
    .attr("class", "color_tr")
    .attr("id", (d) => {
      return "_c_" + d.Name.toLowerCase();
    })
    // Append 5 <td> in <tr>
    .selectAll("td")
    .data((d) => {
      return [d.Name, "_block", d.Hex, d.RGB, d.HSV, d.CMYK];
    })
    .enter()
    .append("td")
    .text((d) => {
      return d;
    })
    .attr("style", (d) => {
      return "width: " + d.length * 10 + "px;";
    })
    .attr("class", (d) => {
      if (d == "_block") {
        return "color_block";
      }
      return undefined;
    });

  // Fill the blocks with color
  tbody
    .selectAll(".color_block")
    .data(list)
    .text(undefined)
    .append("div")
    .attr("style", (d) => {
      return "background-color: " + d.Hex;
    })
    .attr("class", "color_block");

  // .text((d) => {
  //   return d.Hex;
  // });
}

d3.json("http://127.0.0.1:5000/colors.json").then(function (data) {
  console.log("Data is loaded:");
  console.log(data);
  var parsed = json2list(data);
  var list = parsed[0];
  var keys = parsed[1];
  create_colors_table(list, keys);
  find_color();
});
