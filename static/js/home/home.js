// Access the team name
var teamName = team_data.team;

// Access player data
var players = team_data.players;

// Process player data and create a table
var tableHTML = "<table><tr><th>Name</th><th>Year</th><th>Team</th><th>Points</th><th>Rebounds</th><th>Assists</th></tr>";
for (var playerName in players) {
    var playerData = players[playerName];
    for (var year in playerData) {
        var yearData = playerData[year];
        tableHTML += "<tr><td>" + playerName + "</td><td>" + year + "</td><td>" + yearData.team + "</td><td>" + yearData.pts + "</td><td>" + yearData.reb + "</td><td>" + yearData.ast + "</td></tr>";
    }
}
tableHTML += "</table>";

// Insert the table into your HTML (you should have a div with id="table-container" or similar)
document.getElementById("table-container").innerHTML = tableHTML;