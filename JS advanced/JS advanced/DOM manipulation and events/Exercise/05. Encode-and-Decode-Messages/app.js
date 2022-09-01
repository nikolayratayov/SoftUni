function encodeAndDecodeMessages() {
    function encode(){
        let text = document.getElementsByTagName('textarea')[0].value;
        let encoded_text = '';
        let res;
        for (let i = 0; i < text.length; i++){
            res = text.charCodeAt(i);
            res ++;
            encoded_text += String.fromCharCode(res);
        }
        document.getElementsByTagName('textarea')[0].value = '';
        document.getElementsByTagName('textarea')[1].value = encoded_text;
    }
    function decode(){
        let text_to_decode = document.getElementsByTagName('textarea')[1].value;
        let encoded = '';
        let res;
        for (let i = 0; i < text_to_decode.length; i++){
            res = text_to_decode.charCodeAt(i);
            res--;
            encoded += String.fromCharCode(res);
        }
        document.getElementsByTagName('textarea')[1].value = encoded;
    }

    let btn_encode = document.getElementsByTagName('button')[0];
    let btn_decode = document.getElementsByTagName('button')[1];
    btn_encode.addEventListener('click', encode);
    btn_decode.addEventListener('click', decode);
}