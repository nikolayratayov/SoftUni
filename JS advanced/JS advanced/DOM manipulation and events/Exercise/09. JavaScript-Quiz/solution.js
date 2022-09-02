function solve() {
  function next(trg){
    if(trg.target.innerHTML == 'onclick' || trg.target.innerHTML == 'JSON.stringify()' || trg.target.innerHTML == 'A programming API for HTML and XML documents'){
      correct_ans += 1
    }
    len += 1;
    sections[len - 1].setAttribute('style', 'display:none');
    if (len < 3){
      sections[len].setAttribute('style', 'display:block');
    }
    if (len == 3){
      document.getElementById('results').setAttribute('style', 'display: block')
      if (correct_ans == 3){
        document.getElementsByTagName('h1')[1].innerHTML = 'You are recognized as top JavaScript fan!'
      }
      else{
        document.getElementsByTagName('h1')[1].innerHTML = `You have ${correct_ans} right answers`
      }
    }
  }
  let len = 0
  let correct_ans = 0
  let sections = document.getElementsByTagName('section');
  let answers = document.getElementsByClassName('answer-text');
  for(let i = 0; i < answers.length; i++){
    answers[i].addEventListener('click', next)
  }
}
