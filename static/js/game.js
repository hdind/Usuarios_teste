const canvas = document.querySelector('canvas');
const ctx = canvas.getContext('2d');

const scoreElement = document.querySelector('.score--value');
const timerElement = document.querySelector('.timer--value');
const finalScore = document.querySelector('.final-score > span');
const menu = document.querySelector('.menu-screen');
const buttonPlay = document.getElementById('btn-play');

var timerRunning = false;

// SUPP LAYER
const randomNumber = (min, max) => {
    return Math.round(Math.random() * (max - min) + min)
}

const randomPosition = () => {
    return randomNumber(0, canvas.width-1)
}

const randomColor = () => {
    const red = randomNumber(0, 255)
    const green = randomNumber(0, 255)
    const blue = randomNumber(0, 255)

    return `rgb(${red}, ${green}, ${blue})`
}

// RULES LAYER
function checkColision() {
    if (game.player.x === game.fruit.x) {
        if (game.player.y === game.fruit.y) {
            replaceFruit();
            plusScore();
        }
    }
}

function checkMapLimit() {
    return {
    'ArrowUp': function() { return game.player.y - 1 >= 0 },
    'ArrowDown': function() { return game.player.y + 1 < canvas.height },
    'ArrowRight': function() { return game.player.x + 1 < canvas.width },
    'ArrowLeft': function() { return game.player.x - 1 >= 0 },
    }
}

// INPUT LAYER
buttonPlay.addEventListener('click', handleClick);

function handleClick() {
    buttonPlay.style.display = 'none';
    canvas.style.filter = 'none';
    menu.style.display = 'none';
  
    timerRunning = true;

    game.player.score = 0;

    startTimer(game.timer);

    renderCanvas();
}

document.addEventListener('keydown', handleKeyDown);

function handleKeyDown(event) {
    const keyPressed = event.key;
    console.log(keyPressed);
    movePlayer(keyPressed);
}

// GAME LAYER
const game =  {
    player: {
        x: randomPosition(), 
        y: randomPosition(), 
        score: 0
    },
    fruit: {
        x: randomPosition(), 
        y: randomPosition(), 
        color: randomColor() 
    },
    timer: 5
}

function plusScore() {
    return game.player.score += 1;
}

function gameOver() {
    menu.style.display = 'flex'
    finalScore.innerText = game.player.score
    canvas.style.filter = 'blur(2px)'
    buttonPlay.style.display = 'flex';
    buttonPlay.style.marginTop = '150px';
}

function movePlayer(keyPressed) {
    const canMove = checkMapLimit()[keyPressed]()

    const moves = {
        'ArrowUp' : function() { return game.player.y -= 1 },
        'ArrowDown' : function() { return game.player.y += 1 },
        'ArrowRight' : function() { return game.player.x += 1 },
        'ArrowLeft' : function() { return game.player.x -= 1 },
    }

    if (canMove) {
        if (timerRunning) {
            moves[keyPressed]();
            checkColision();
            console.log(`Player -> x: ${game.player.x}, y: ${game.player.y}`);
        }             
    }
}

function replaceFruit() {
    game.fruit.x = randomPosition()
    game.fruit.y = randomPosition() 
    game.fruit.color = randomColor() 
    console.log(`Fruit -> x: ${game.fruit.x}, y: ${game.fruit.y}`)
}

function startTimer(secondsRemaining) {
    const intervalId = setInterval(() => {
        timerElement.textContent = secondsRemaining;

        if (secondsRemaining <= 0) {
            timerRunning = false;
            clearInterval(intervalId);
            gameOver()
        }

        secondsRemaining -= 1;
    }, 1000);
}

// PRESENTATION LAYER
renderCanvas()
timerElement.innerText = game.timer

function renderCanvas() {
    ctx.clearRect(0,0,15,15);

    ctx.fillStyle = '#ddd';
    ctx.fillRect(game.player.x, game.player.y, 1, 1);


    ctx.fillStyle = game.fruit.color;
    ctx.fillRect(game.fruit.x, game.fruit.y, 1, 1);

    scoreElement.innerText = game.player.score

    requestAnimationFrame(renderCanvas);
}
