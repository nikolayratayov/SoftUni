function solve(a){
    arr = []
    for (let i = 1; i < a.length; i++){
        let text = a[i].slice(2, -2);
        let [town, lat, long] = text.split(' | ');
        lat = parseFloat(lat).toFixed(2);
        long = parseFloat(long).toFixed(2);
        lat = parseFloat(lat);
        long = parseFloat(long);
        arr.push({Town: town, Latitude: lat, Longitude:long})
    }
    console.log(JSON.stringify(arr));
}