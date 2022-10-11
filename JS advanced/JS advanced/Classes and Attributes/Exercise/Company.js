class Company {
    constructor(){
        this.obj = {}
    }
    addEmployee(n, sal, pos, dep){
        if (!n || !sal || sal < 0 || !pos || !dep) {
            throw new Error('Invalid input!');
        }
        if (!this.obj[dep]){this.obj[dep] = []}
        this.obj[dep].push({name: n, salary: Number(sal), position: pos})
        
        return `New employee is hired. Name: ${n}. Position: ${pos}`
    }
    bestDepartment(){
        let best_dep = '';
        let best_sal = 0;
        for (let i in this.obj){
            let current_average = 0;
            let current_sum = 0;
            let counter = 0
            for (let j in this.obj[i]){
                current_sum += this.obj[i][j].salary;
                counter += 1
            }
            current_average = current_sum / counter;
            if (current_average > best_sal){
                best_sal = current_average;
                best_dep = i;
            }
        }
        let sorted = Object.values(this.obj[best_dep]).sort((a, b) => b.salary - a.salary || a.name.localeCompare(b.name));
        let res = '';
        res += `Best Department is: ${best_dep}\n`;
        res += `Average salary: ${best_sal.toFixed(2)}\n`;
        for (let i of sorted){
            res += `${i.name} ${i.salary} ${i.position}\n`
        }
        return res.substring(0, res.length - 1);
    }
}