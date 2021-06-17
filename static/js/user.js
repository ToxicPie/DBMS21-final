document.addEventListener("DOMContentLoaded", event => {
    const scoreDiv = document.querySelector("div.scoreboard");
    //Build an array containing Customer records.
    var orderTable = new Array();
    orderTable.push(["User id", "Fetch on", "Amount", "Price Per Unit", "Orders"]);
    orderTable.push(["apple", "6/6", 100, 3, 2]);
    orderTable.push(["apple", "6/6", 125, 2, 5]);
    orderTable.push(["apple", "6/6", 10, 7, 9]);
    orderTable.push(["apple", "6/6", 1000, 6, 1]);

    //Create a HTML Table element.
    var table = document.createElement("TABLE");
    table.border = "1";
    table.setAttribute('class', 'table table-dark');

    //Get the count of columns.
    var columnCount = orderTable[0].length;

    //Add the header row.
    var row = table.insertRow(-1);
    for (var i = 0; i < columnCount; i++) {
        var headerCell = document.createElement("TH");
        headerCell.innerHTML = orderTable[0][i];
        row.appendChild(headerCell);
    }

    //Add the data rows.
    for (var i = 1; i < orderTable.length; i++) {
        row = table.insertRow(-1);
        for (var j = 0; j < columnCount; j++) {
            var cell = row.insertCell(-1);
            cell.innerHTML = orderTable[i][j];
        }
        var cell = row.insertCell(-1);
        var del_btn = document.createElement("button");
        del_btn.setAttribute('class', 'btn btn-outline-danger my-2 my-sm-0');
        del_btn.setAttribute('type', 'button');
        del_btn.innerHTML = "Delete";
        cell.appendChild(del_btn);
    }

    var dvTable = document.getElementById("buyTable");
    dvTable.innerHTML = "";
    dvTable.appendChild(table);
});
