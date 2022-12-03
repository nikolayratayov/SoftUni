export function getUserData(){
    let data = JSON.parse(sessionStorage.getItem('userData'));
    return data;
}

export function setUserData(data){
    sessionStorage.setItem('userData', JSON.stringify(data));
}

export function clearUserData(){
    sessionStorage.removeItem('userData');
}

export function createSubmitHandler(callabck){
    return function (event){
        event.preventDefault();
        let formData = new FormData(event.target);
        let data = Object.fromEntries(formData);
        callabck(data);

    }
}