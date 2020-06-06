let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;

let user_dif;
let comp_dif;

// Write your code below:

function generateTarget() {
    let num = Math.floor(Math.random() * 9);
    return num;
    
}

function compareGuesses(user_guess, comp_guess, target_number){
    if(user_guess == target_number){
        return true;
    }
    else if(user_guess != target_number && comp_guess == target_number){
        return false;
    }
    else{
        if(user_guess < target_number){
            user_dif = target_number - user_guess;
        }
        else if(user_guess > target_number){
            user_dif = user_guess - target_number;
        }

        if(comp_guess < target_number){
            comp_dif = target_number - comp_guess;
        }
        else if(comp_guess > target_number){
            comp_dif = comp_guess - target_number;
        }

    if(user_dif < comp_dif){
        return true;
    }
    else if(user_dif > comp_dif){
        return false;
    }
    else if(user_dif == comp_dif){
        return true;
    }
console.log(user_dif);
console.log(comp_dif);

    }
}

function updateScore(winner) {
    if(winner == "human"){
        humanScore++;
    }
    else if(winner =="computer"){
        computerScore++;
    }
}

function advanceRound() {
    currentRoundNumber++;
}