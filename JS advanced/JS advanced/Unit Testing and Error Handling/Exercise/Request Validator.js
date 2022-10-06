function solve(obj){
    let methods = ['GET', 'POST', 'DELETE', 'CONNECT'];
    let method_t_f = methods.includes(obj.method);
    let re_uni = /[A-Za-z0-9]?\.[A-Za-z0-9]+/;
    let uni_t_f = re_uni.test(obj.uri);
    let versions = ['HTTP/0.9', 'HTTP/1.0', 'HTTP/1.1', 'HTTP/2.0'];
    let version_t_f = versions.includes(obj.version);
    if (!method_t_f){throw new Error('Invalid request header: Invalid Method')}

    if (!uni_t_f && obj.uri !== '*'){throw new Error('Invalid request header: Invalid URI')}

    if (!version_t_f){throw new Error('Invalid request header: Invalid Version')}
    if (obj.message == undefined){ throw new Error('Invalid request header: Invalid Message')}
    if (obj.message.includes('<') || obj.message.includes('>') || obj.message.includes('\\') || obj.message.includes('&') || obj.message.includes('\'') || obj.message.includes('\"')){
        throw new Error('Invalid request header: Invalid Message')
    }  
    return obj;
}
