function solve(a){
    function escape(text){
        return text.toString().replace(/&/g, '&amp;').replace(/>/g, '&gt;').replace(/</g, '&lt;').replace(/'/g, '&#39;').replace(/"/g, '&quot;');
    }
    let niki = JSON.parse(a);
    let cols = [];
    for(const k in niki[0]){
        if(cols.indexOf(k) === -1){
            cols.push('<th>' + escape(k) + '</th>');
        }
    }
    console.log('<table>');
    console.log('   <tr>' + cols.join('') + '</tr>');
    for(let i = 0; i < niki.length; i++){
        let cells = [];
        for(const k in niki[i]){
            let proba = parseFloat(niki[i][k])
            if (k != 'Name' && typeof(proba) === 'NaN'){
                cells.push('<td></td>')
            }
            else{
                cells.push('<td>' + escape(niki[i][k]) + '</td>')
            }
        }
        console.log('   <tr>' + cells.join('') + '</tr>')
    }
    console.log('</table>')
};