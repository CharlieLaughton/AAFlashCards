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
    document.querySelector('#timer').textContent = time;
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
    document.querySelector('#timer').textContent = time;
};

function setScore(value) {
    document.querySelector('#score').textContent = value;
}

function processChoice(choice) {
    stopTimer(timer);
    deactivateChoosing();
    const optionboxes = document.querySelectorAll('.optionbox');
    optionboxes.forEach( (optionbox) => {
        if (optionbox.id === choice) {
            if (choice == correctChoice) {
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
    if (choice == correctChoice) {
        score += time;
    }
    setScore(score);
    round += 1
    if (round % gamesPerRound === 0) {
        gameType += 1;
        gameTime = 5;
    } else {
        gameTime = 5;
    }
    if (gameType > 7) {
        let hiScore = getCookie("hiScore");
        hiScore = (hiScore === '') ? 0 : Number(hiScore);
        if (hiScore > score) {
            alert(`GAME OVER!\nYou scored ${score}\nBest score: ${hiScore}`)
        } else {
            setCookie("hiScore", score, 365);
            alert(`GAME OVER\nYou scored ${score}\nNEW PERSONAL BEST!`)
        }
    } else {
    defer(2);
    };
};

function resetOptionBoxBackgrounds () {
    const optionboxes = document.querySelectorAll('.optionbox');
    optionboxes.forEach( (optionbox) => {
        optionbox.style.background = 'white';
    });
};

function fillOptionBoxes (aas) {
    optionboxes = document.querySelectorAll('.optionbox');
    let i = 0;
    optionboxes.forEach((optionbox) => {
        const text = aas[i];
        if (text.search('.png') > -1) {
            element = imageElement(text);
        } else {
            element = textElement(text);
        }
        optionbox.appendChild(element);
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

function newGame () {
    
    let r = Math.floor(Math.random() * aaSets.length);
    let aaSet = aaSets[r];
    correctChoice = Math.floor(Math.random() * 4);
    let correctValue = aaSet[correctChoice];
    let query = '';
    let options = [];
    if (gameType === 0) {
        query = `AAFlashCards/${longName(correctValue)}.png`;
        for (let i=0; i < aaSet.length; i++) {
            options[options.length] = longName(aaSet[i]);
        };
    } else if (gameType === 1) {
        query = `AAFlashCards/${longName(correctValue)}.png`;
        options = aaSet;
    } else if (gameType === 2) {
        query = longName(correctValue);
        for (let i=0; i < aaSet.length; i++) {
            options[options.length] = `AAFlashCards/${longName(aaSet[i])}.png`;
        };
    } else if (gameType === 3) {
        query = aaSet[correctChoice];
        for (let i=0; i < aaSet.length; i++) {
            options[options.length] = `AAFlashCards/${longName(aaSet[i])}.png`;
        };
    } else if (gameType === 4) {
        query = `AAFlashCards/${correctValue}.png`;
        for (let i=0; i < aaSet.length; i++) {
            options[options.length] = longName(aaSet[i]);
        };
    } else if (gameType === 5) {
        query = `AAFlashCards/${correctValue}.png`;
        options = aaSet;
    } else if (gameType === 6) {
        query = longName(correctValue);
        for (let i=0; i < aaSet.length; i++) {
            options[options.length] = `AAFlashCards/${aaSet[i]}.png`;
        };
    } else if (gameType === 7) {
        query = aaSet[correctChoice];
        for (let i=0; i < aaSet.length; i++) {
            options[options.length] = `AAFlashCards/${aaSet[i]}.png`;
        };
    }
    if (query.search('.png') > -1) {
        setupImageQuery(query);
    } else {
        setupTextQuery(query);
    }

    if (options[0].search('.png') > -1) {
        setupImageOptions(options);
    } else {
        setupTextOptions(options);
    }

    if (round % gamesPerRound === 0) {
        text = `Round ${gameType + 1}:\n`;
        switch (gameType) {
            case 0:
                text += 'Pick the 3-letter code that matches the 2D structure';
                break;
            case 1:
                text += 'Pick the 1-letter code that matches the 2D structure';
                break;
            case 2:
                text += 'Pick the 2D structure that matches the 3-letter code';
                break;
            case 3:
                text += 'Pick the 2D structure that matches the 1-letter code';
                break;
            case 4:
                text += 'Pick the 3-letter code that matches the 3D structure (highlighted in grey)';
                break;
            case 5:
                text += 'Pick the 1-letter code that matches the 3D structure (highlighted in grey)';
                break;
            case 6:
                text += 'Pick the 3D structure that matches the 3-letter code';
                break;
            case 7:
                text += 'Pick the 3D structure that matches the 1-letter code';
                break;
        }
        alert(text);
        setTimer(gameTime);
        timer = startTimer();
        resetOptionBoxBackgrounds();
        activateChoosing();
    } else {
        setTimer(gameTime);
        timer = startTimer();
        resetOptionBoxBackgrounds();
        activateChoosing();
    };
};

function removeChildren (node) {
    while (node.firstChild) {
        node.removeChild(node.lastChild);
    };
};

function createImageBox (path) {
    const img = document.createElement('img');
    img.setAttribute('src', path);
    return img;
};

function createTextBox (text) {
    const textbox = document.createElement('div');
    textbox.classList.add('textcontent');
    textbox.textContent = text;
    return textbox;
};

function setupImageQuery (path) {
    const querybox = document.querySelector('.querybox');
    removeChildren(querybox);
    imagebox = createImageBox(path);
    querybox.appendChild(imagebox);
};

function setupTextQuery (text) {
    const querybox = document.querySelector('.querybox');
    removeChildren(querybox);
    textbox = createTextBox(text);
    querybox.appendChild(textbox);
};

function setupTextOptions (texts) {
    const optionboxes = document.querySelectorAll('.optionbox');
    let i = 0;
    optionboxes.forEach((optionbox) => {
        removeChildren(optionbox);
        textbox = createTextBox(texts[i]);
        optionbox.appendChild(textbox);
        i++;
    });
};

function setupImageOptions (paths) {
    const optionboxes = document.querySelectorAll('.optionbox');
    let i = 0;
    optionboxes.forEach((optionbox) => {
        removeChildren(optionbox);
        imagebox = createImageBox(paths[i]);
        optionbox.appendChild(imagebox);
        i++;
    });
};

function hideOptions () {
    const optionboxes = document.querySelectorAll('.optionbox');
    optionboxes.forEach((optionbox) => {
        optionbox.firstChild.style.visibility = 'hidden';
    });
};

function showOptions () {
    const optionboxes = document.querySelectorAll('.optionbox');
    optionboxes.forEach((optionbox) => {
        optionbox.firstChild.style.visibility = 'visible';
    });
};

function longName (aa) {
    const longNames = [
        'ala', 'cys', 'asp', 'glu', 'phe', 'gly', 'his', 'ile', 'lys', 'leu',
        'met', 'asn', 'pro', 'gln', 'arg', 'ser', 'thr', 'val', 'trp', 'tyr',
    ]
    const shortNames = ['a','c','d','e','f','g','h','i','k','l','m','n','p','q','r','s','t','v','w','y'];
    return longNames[shortNames.indexOf(aa)];
};

function setCookie(cname, cvalue, exdays) {
    const d = new Date();
    d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
    let expires = "expires="+d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
  }
  
  function getCookie(cname) {
    let name = cname + "=";
    let ca = document.cookie.split(';');
    for(let i = 0; i < ca.length; i++) {
      let c = ca[i];
      while (c.charAt(0) == ' ') {
        c = c.substring(1);
      }
      if (c.indexOf(name) == 0) {
        return c.substring(name.length, c.length);
      }
    }
    return "";
  }
  
  
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
];

let timer = null;
let time = 0;
let score = 0;
let gameTime = 5;
let correctChoice = 2;
let gameType = 0;
let round = 0;
const gamesPerRound = 3;
setScore(score)
newGame();