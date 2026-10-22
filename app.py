# ACCT 411: Playable Pong Game inside a Google Colab Cell
# REPAIRED & REMIXED NEON VERSION: Fixed text string quote and applied custom color theme!

from IPython.display import HTML

pong_game_code = """
<!DOCTYPE html>
<html>
<head>
    <style>
        /* CSS: Style the game frame and court layout */
        #pongCanvas {
            /* Neon navy and dark purple color palette background mix */
            background: linear-gradient(135deg, #0b112c, #230c33);
            display: block;
            margin: 0 auto;
            border: 4px solid #ff007f; /* Kept the hot pink neon boundary line color */
            box-shadow: 0px 0px 20px #ff007f; /* Pink neon glow effect */
            cursor: none; /* Hide standard cursor pointer over the court */
        }
        .game-container {
            text-align: center;
            font-family: 'Courier New', Courier, monospace;
            color: #00ffff; /* Neon cyan text header decoration */
            background-color: #060814; /* Deep dark frame wrap */
            padding: 15px;
            border-radius: 12px;
            width: 630px;
            margin: 0 auto;
            border: 2px solid #b5179e;
            box-shadow: 0px 0px 15px #b5179e;
        }
    </style>
</head>
<body>
    <div class="game-container">
        <h2>⚡ DIANA'S RETRO NEON PONG ⚡</h2>
        <p style="color: #00f5d4;">Slide your trackpad smoothly up and down to play!</p>
        <canvas id="pongCanvas" width="600" height="400"></canvas>
    </div>

    <script>
        const canvas = document.getElementById("pongCanvas");
        const ctx = canvas.getContext("2d");

        // Game Objects with Your Custom Requested Colors
        const ball = { x: 300, y: 200, radius: 10, speedX: 5, speedY: 5, color: "#ffff00" }; // Glowing neon yellow ball
        const userPaddle = { x: 15, y: 160, width: 12, height: 80, score: 0, color: "#b5179e" }; // Custom Neon Purple
        const aiPaddle = { x: 573, y: 160, width: 12, height: 80, score: 0, color: "#00f5d4" };  // Custom Neon Aqua

        // Event Listener: Tracks mouse movement smoothly relative to game court frame
        canvas.addEventListener("mousemove", function(e) {
            const rect = canvas.getBoundingClientRect();
            const relativeY = e.clientY - rect.top;
            userPaddle.y = relativeY - (userPaddle.height / 2);
        });

        function resetBall() {
            ball.x = canvas.width / 2;
            ball.y = canvas.height / 2;
            ball.speedX = -ball.speedX;
        }

        // Object shapes rendering logic
        function drawRect(x, y, w, h, color) {
            ctx.fillStyle = color;
            ctx.fillRect(x, y, w, h);
        }

        function drawCircle(x, y, r, color) {
            ctx.fillStyle = color;
            ctx.fillStyle = color;
            ctx.beginPath();
            ctx.arc(x, y, r, 0, Math.PI * 2, false);
            ctx.closePath();
            ctx.fill();
        }

        function drawText(text, x, y, color) {
            ctx.fillStyle = color;
            ctx.font = "bold 36px 'Courier New'";
            ctx.fillText(text, x, y);
        }

        // Main game frame update loop calculations
        function update() {
            ball.x += ball.speedX;
            ball.y += ball.speedY;

            // Smoothly track ball position with AI opponent
            aiPaddle.y += (ball.y - (aiPaddle.y + aiPaddle.height / 2)) * 0.09;

            // Bounce ball off horizontal bounds
            if (ball.y + ball.radius > canvas.height || ball.y - ball.radius < 0) {
                ball.speedY = -ball.speedY;
            }

            // Detect matching horizontal bounce zone contacts
            let player = (ball.x < canvas.width / 2) ? userPaddle : aiPaddle;

            if (ball.x - ball.radius < player.x + player.width &&
                ball.x + ball.radius > player.x &&
                ball.y > player.y &&
                ball.y < player.y + player.height) {
                ball.speedX = -ball.speedX;
            }

            // Score conditions bounds checking
            if (ball.x - ball.radius < 0) {
                aiPaddle.score++;
                resetBall();
            } else if (ball.x + ball.radius > canvas.width) {
                userPaddle.score++;
                resetBall();
            }
        }

        // Draw loop clear and redraw commands
        function render() {
            // Re-render our custom linear color background grid
            let grad = ctx.createLinearGradient(0, 0, canvas.width, canvas.height);
            grad.addColorStop(0, "#0b112c"); // Neon Navy mix
            grad.addColorStop(1, "#230c33"); // Dark Purple mix
            ctx.fillStyle = grad;
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            // Dotted net separator line
            ctx.strokeStyle = "rgba(255, 255, 255, 0.08)";
            ctx.beginPath();
            ctx.setLineDash([5, 15]);
            ctx.moveTo(canvas.width / 2, 0);
            ctx.lineTo(canvas.width / 2, canvas.height);
            ctx.stroke();

            // Render live neon game asset elements on top of the layout
            drawText(userPaddle.score, canvas.width / 4, canvas.height / 4, "#b5179e"); // Purple score font
            drawText(aiPaddle.score, 3 * canvas.width / 4, canvas.height / 4, "#00f5d4"); // Aqua score font

            drawRect(userPaddle.x, userPaddle.y, userPaddle.width, userPaddle.height, userPaddle.color); // User Paddle shape
            drawRect(aiPaddle.x, aiPaddle.y, aiPaddle.width, aiPaddle.height, aiPaddle.color); // AI Paddle shape

            drawCircle(ball.x, ball.y, ball.radius, ball.color); // Glowing neon yellow match ball
        }

        function gameLoop() {
            update();
            render();
            requestAnimationFrame(gameLoop);
        }

        gameLoop();
    </script>
</body>
</html>
"""

HTML(pong_game_code)

