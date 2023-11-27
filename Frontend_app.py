<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Carbon Footprint Calculator</title>
</head>
<body>
    <h1>Carbon Footprint Calculator</h1>
    <form action="/calculate" method="post">
        <label for="miles">Miles Driven:</label>
        <input type="number" name="miles" required><br>

        <label for="electricity">Electricity Consumed (kWh):</label>
        <input type="number" name="electricity" required><br>

        <label for="waste">Waste Generated (lbs):</label>
        <input type="number" name="waste" required><br>

        <button type="submit">Calculate</button>
    </form>
</body>
</html>

