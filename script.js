function handleMouseEnter (e) {
    e.target.style.background = '#999999';
};

function handleMouseLeave (e) {
    e.target.style.background = 'white';
};

function handleChoiceClick (e) {
    choice = e.currentTarget.id;
    processChoice(choice);
};

function activateChoosing () {
    let i = 0;
    const optionboxes = document.querySelectorAll('.optionbox');
    optionboxes.forEach( (optionbox) => {
        optionbox.addEventListener('mouseenter', handleMouseEnter);
        optionbox.addEventListener('mouseleave', handleMouseLeave);
        optionbox.addEventListener('click', handleChoiceClick);
        optionbox.setAttribute('id', i);
        i += 1;
    });
};

function deactivateChoosing () {
    const optionboxes = document.querySelectorAll('.optionbox');
    optionboxes.forEach( (optionbox) => {
        optionbox.removeEventListener('mouseenter', handleMouseEnter);
        optionbox.removeEventListener('mouseleave', handleMouseLeave);
        optionbox.removeEventListener('click', handleChoiceClick);
    });
};

function decrementer () {
    time -= 1;
    document.querySelector('.timer').textContent = time;
    if (time ===  0) {
        stopTimer(timer);
        processChoice(-1);
    }
};

function startTimer() {
    let timer = setInterval(decrementer, 1000);
    return timer;
};

function stopTimer(timer) {
    clearInterval(timer);
};

function setTimer(value) {
    time = value;
    document.querySelector('.timer').textContent = time;
};

function processChoice(choice) {
    stopTimer(timer);
    deactivateChoosing();
    const optionboxes = document.querySelectorAll('.optionbox');
    optionboxes.forEach( (optionbox) => {
        if (optionbox.id === choice) {
            if (choice === correctChoice) {
                optionbox.style.background = '#99ff99';
            } else {
                optionbox.style.background = '#ff9999';
            };
        } else {
            if (choice === -1) {
                optionbox.style.background = '#ff9999';
            };
        };
        if (optionbox.id == correctChoice) {
            optionbox.style.background = '#99ff99';
        }
    });
    defer(2);
};

function resetOptionBoxes () {
    const optionboxes = document.querySelectorAll('.optionbox');
    optionboxes.forEach( (optionbox) => {
        optionbox.style.background = 'white';
    });
};

function fillOptionBoxes (aas) {
    const rightbox = document.querySelector('.rightbox');
    textboxes = rightbox.querySelectorAll('.textbox');
    let i = 0;
    textboxes.forEach((textbox) => {
        textbox.textContent = aas[i];
        i += 1;
    });
};

function defer (seconds) {
    let s = seconds;
    let x = setInterval( () => {
        s -= 1;
        if (s <= 0) {
            clearInterval(x);
            newGame();
        };
    }, 1000);
};

function setAA (a) {
    let path = `AAFlashCards/${a}.png`
    leftBox = document.querySelector('.leftbox');
    img = leftBox.querySelector('img');
    img.src = path;
};


function newGame () {
    setTimer(gameTime);
    let r = Math.floor(Math.random() * aaSets.length);
    let aaSet = aaSets[r];
    correctChoice = Math.floor(Math.random() * 4);
    resetOptionBoxes();
    let aaNames = []
    if (gameType === 0) {
        for (let i=0; i < aaSet.length; i++) {
            aaNames[aaNames.length] = aaSet[i];
        };
    } else if (gameType === 1) {
        for (let i=0; i < aaSet.length; i++) {
            aaNames[aaNames.length] = longName(aaSet[i]);
        };
    };
    
    fillOptionBoxes(aaNames);
    setAA(aaNames[correctChoice]);
    timer = startTimer();
    activateChoosing();
};

function longName (aa) {
    const longNames = [
        'ala', 'cys', 'asp', 'glu', 'phe', 'gly', 'his', 'ile', 'lys', 'leu',
        'met', 'asn', 'pro', 'gln', 'arg', 'ser', 'thr', 'val', 'trp', 'tyr',
    ]
    const shortNames = ['a','c','d','e','f','g','h','i','k','l','m','n','p','q','r','s','t','v','w','y'];
    console.log(aa);
    return longNames[shortNames.indexOf(aa)];
};

const aaSets = [
    ['a', 'v', 'c', 'g'],
    ['c', 's', 't', 'm'],
    ['d', 'e', 'n', 'q'],
    ['f', 'y', 'w', 'h'],
    ['g', 'e', 'k', 'l'],
    ['h', 'f', 'r', 'n'],
    ['i', 'l', 'v', 't'],
    ['k', 'r', 'm', 'l'],
    ['l', 'k', 'g', 'i'],
    ['m', 'a', 'c', 's'],
    ['p', 'f', 'g', 'a'],
    ['s', 't', 'c', 'v'],
    ['w', 'r', 'y', 'q'],
]
let timer = null;
let correctChoice = 2;
const gameTime = 5;
const gameType = 1;
newGame();