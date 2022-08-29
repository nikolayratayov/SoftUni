/* function solve() {
   document.querySelector('#btnSend').addEventListener('click', onClick);

   function onClick () {
      let text_lst = JSON.parse(document.getElementsByTagName('textarea')[0].value);
      let obj = {
         best_rest: '',
         average_salary: 0,
         best_salary: 0,
         restaurants: {}
      };
      let rest;
      for(let item of text_lst){
         let rest_workers = item.split(' - ');
         rest = rest_workers[0];
         if (!(rest in obj['restaurants'])){
            obj['restaurants'][rest] = {};
         }
         let zaplati = [];
         let workers_salaries_lst = rest_workers[1].split(', ');
         for (let iter of workers_salaries_lst){
            work_sal = iter.split(' ');
            obj['restaurants'][rest][work_sal[0]] = parseFloat(work_sal[1]);
         }
         for(const key in obj['restaurants'][rest]){
            zaplati.push(obj['restaurants'][rest][key]);
         }
         let sum = zaplati.reduce((partialSum, a) => partialSum + a, 0);
         let ave = sum / zaplati.length;
         let max_sal = Math.max(...zaplati);
         if (ave > obj['average_salary']){
            obj['best_rest'] = rest;
            obj['average_salary'] = ave;
            obj['best_salary'] = max_sal;
         }
      }
      let sorted_workers = [];
      for(const key in obj['restaurants'][obj['best_rest']]){
         sorted_workers.push([key, obj['restaurants'][obj['best_rest']][key]]);
      }
      sorted_workers.sort(function(a, b){return b[1] - a[1]})
      document.getElementById('bestRestaurant').getElementsByTagName('p')[0].innerHTML = `Name: ${obj['best_rest']} Average Salary: ${(obj['average_salary']).toFixed(2)} Best Salary: ${(obj['best_salary']).toFixed(2)}`
      let str_workers = '';
      for(let element of sorted_workers){
         str_workers += `Name: ${element[0]} With Salary: ${element[1]} `;
      }
      document.getElementById('workers').getElementsByTagName('p')[0].innerHTML = str_workers;
   }
} */
function solve() {
   document.querySelector('#btnSend').addEventListener('click', onClick);

   function onClick() {
       let arr = JSON.parse(document.querySelector('#inputs textarea').value);
       let objWinner = findBestRestaurant(arr);
       document.querySelector('#bestRestaurant>p').textContent = getMsgRest(objWinner);
       document.querySelector('#workers>p').textContent = getMsgEmp(objWinner.workers);
   }

   function getMsgRest(objWinner) {
       return `Name: ${objWinner.name} Average Salary: ${objWinner.avgSalary.toFixed(2)} Best Salary: ${objWinner.maxSalary.toFixed(2)}`;
   }

   function getMsgEmp(workers) {
       return workers.map(w => `Name: ${w.worker} With Salary: ${w.salary}`).join(' ');
   }

   function findBestRestaurant(arr) {
       let resultRestaurants = arr.reduce((acc, e) => {
           let [restaurant, ...workers] = e.split(/(?: - )|(?:, )/g);
           workers = workers.map(w => {
               let [worker, salary] = w.split(' ');
               return {
                   worker: worker,
                   salary: +salary
               };
           });
           let foundRestraunt = acc.find(r => r.name === restaurant);
           if (foundRestraunt) {
               foundRestraunt.workers = foundRestraunt.workers.concat(workers);
           } else {
               acc.push({
                   name: restaurant,
                   workers: workers
               });
           }
           return acc;
       }, []);

       resultRestaurants.forEach((el, idx) => {
           el.inputOrder = idx;
           el.avgSalary = el.workers.reduce((acc, el) => acc + el.salary, 0) / el.workers.length;
           el.maxSalary = Math.max(...el.workers.map(w => w.salary));
       });

       resultRestaurants.sort((a, b) => b.avgSalary - a.avgSalary || a.inputOrder - b.inputOrder);
       let bestRestaurant = resultRestaurants[0];
       bestRestaurant.workers.sort((a, b) => b.salary - a.salary);

       return bestRestaurant;
   }
}