MAIN_CANVAS = """
<!doctype html>
<html>
<head>
    <title>{{title}}</title>
</head>
<body>
    <canvas id="pantograph-canvas"/>
    <script>
        var canvas = document.getElementById("pantograph-canvas")
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    </script>
</body>
</html>
"""
