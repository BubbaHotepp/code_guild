function meter(unit, distance){
    
    if (unit === 'ft'){
    let meters = distance * 0.3048
    return(meters)
    }
    
    else if (unit === 'km'){
        let meters = distance * 1000
        return(meters)
    }
    
    else if (unit === 'mi'){
        let meters = distance * 1609.34
        return(meters)
    }

    else {
        let meters = distance * 1
        return(meters)
    }

} 

function main(){

    let rl = require('readline');
    let unit = "";
    let distance = "";

    let prompts = rl.createInterface(process.stdin, process.stdout);
    prompts.question("Please enter the unit to convert '\n'(Kilometers = 'km', Miles = 'mi', Meters = 'm', Feet = 'ft'):", function(unit){

        prompts.question("Please enter the distance in feet to convert to meters: ", function(distance){
            let meters = meter(unit, distance)
            console.log(distance,", feet = ", meters, " meters.")
            process.exit();
        });
    });
}
main()