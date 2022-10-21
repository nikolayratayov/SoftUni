class SmartHike{
    constructor(u){
        this.username = u;
        this.goals = {};
        this.listOfHikes = [];
        this.resources = 100;
    }

    addGoal(p, alt){
        if (p in this.goals){
            return `${p} has already been added to your goals`
        }
        this.goals[p] = alt;
        return `You have successfully added a new goal - ${p}`
    }

    hike(p, t, difficult){
        if (p in this.goals){
            if (this.resources > 0){
                let difference = this.resources - (t * 10);
                if (difference >= 0){
                    this.resources = difference;
                    this.listOfHikes.push({'peak': p, 'time': t, 'difficultyLevel': difficult})
                    return `You hiked ${p} peak for ${t} hours and you have ${this.resources}% resources left`
                }
                return "You don't have enough resources to complete the hike"
            }
            throw new Error("You don't have enough resources to start the hike")
        }
        throw new Error(`${p} is not in your current goals`)
    }

    rest(t){
        this.resources += (t * 10);
        if (this.resources >= 100){
            this.resources = 100;
            return `Your resources are fully recharged. Time for hiking!`
        }
        return `You have rested for ${t} hours and gained ${t*10}% resources`
    }

    showRecord(crit){
        if (this.listOfHikes.length > 0){
            if (crit == 'all'){
                let res = "All hiking records:\n"
                for (let hike of this.listOfHikes){
                    res += `${this.username} hiked ${hike.peak} for ${hike.time} hours\n`
                }
                return res.substring(0, res.length - 1)
            }
            else{
                let hikes_with_crit = []
                for (let hike of this.listOfHikes){
                    if (hike.difficultyLevel == crit){
                        hikes_with_crit.push(hike)
                    }
                }
                if (hikes_with_crit > 0){
                    let sorted_hikes = hikes_with_crit.sort((a, b) => a.time - b.time)
                    return `${this.username}'s best ${crit} hike is ${sorted_hikes[0].peak} peak, for ${sorted_hikes[0].time} hours`
                }
                return `${this.username} has not done any ${crit} hiking yet`
                
            }
        }
        return `${this.username} has not done any hiking yet`
    }
}
