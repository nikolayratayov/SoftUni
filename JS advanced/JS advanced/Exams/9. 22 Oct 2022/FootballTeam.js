class footballTeam{
    constructor(n, coun){
        this.clubName = n;
        this.country = coun;
        this.invitedPlayers = [];
    }

    newAdditions(fplayers){
        let players_to_return = [];
        for (let i of fplayers){
            let [ime, god, st] = i.split('/')
            if (!players_to_return.includes(ime)){
                players_to_return.push(ime)
            }
            god = Number(god);
            st = Number(st);
            let not_present = true;
            for (let player of this.invitedPlayers){
                if (player.name == ime){
                    not_present = false
                    if (st > player.playerValue){
                        player.playerValue = st;
                    }
                }
            }
            if (not_present){
                this.invitedPlayers.push({'name': ime, 'age': god, 'playerValue': st});
            }

        }
        let res = `You successfully invite ${players_to_return.join(', ')}.`;
        return res
    }

    signContract(selplayer){
        let [ime, offer] = selplayer.split('/');
        for (let player of this.invitedPlayers){
            if (player.name == ime){
                if (offer < player.playerValue){
                    let difference = player.playerValue - offer
                    throw new Error(`The manager's offer is not enough to sign a contract with ${ime}, ${difference} million more are needed to sign the contract!`)
                }
                else{
                    player.playerValue = 'Bought';
                    return `Congratulations! You sign a contract with ${ime} for ${offer} million dollars.`
                }
            }
        }
        throw new Error(`${ime} is not invited to the selection list!`)
    }

    ageLimit(n, a){
        for (let player of this.invitedPlayers){
            if (player.name == n){
                if (player.age < a){
                    let diff = a - player.age;
                    if (diff < 5){
                        return `${n} will sign a contract for ${diff} years with ${this.clubName} in ${this.country}!`
                    }
                    else{
                        return `${n} will sign a full 5 years contract for ${this.clubName} in ${this.country}!`
                    }
                }
                else{
                    return `${n} is above age limit!`
                }
            }
        }
        throw new Error(`${n} is not invited to the selection list!`)
    }

    transferWindowResult(){
        let res = 'Players list:\n'
        let sorted = this.invitedPlayers.sort((a, b) => a.name.localeCompare(b.name));
        for (let player of sorted){
            res += `Player ${player.name}-${player.playerValue}\n`
        }
        return res.substring(0, res.length - 1)
    }
}
