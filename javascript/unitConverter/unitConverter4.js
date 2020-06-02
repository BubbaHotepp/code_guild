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

} // Converts inputed unit to meters

function main(){

    let rl = require('readline');
    let unit = "";
    let distance = "";
    const miles = (meters) => meters / 1609.34;
    const yards = (meters) => meters / 0.9144;
    const inches = (meters) => meters / 0.0254;
    const feet = (meters) => meters / 0.3048;
    const kilometers = (meters) => meters / 1000;

    const ops = {
        'mi': miles,
        'yd': yards,
        'in': inches,
        'ft': feet,
        'km': kilometers,
    };

    let prompts = rl.createInterface(process.stdin, process.stdout);

    prompts.question("Please enter the unit to convert from'\n'(Kilometers = 'km', Miles = 'mi', Meters = 'm', Yard = 'yd', Feet = 'ft', Inches = 'in'):", function(unit_from){

        prompts.question("Please enter the unit to convert to'\n'(Kilometers = 'km', Miles = 'mi', Meters = 'm', Yard = 'yd', Feet = 'ft', Inches = 'in'):",function(unit_to){

            prompts.question("Please enter the distance: ", function(distance){

                let interim = meter(unit_from, distance)
                console.log(distance, unit_from, "=", ops[unit_to](interim), ",", unit_to)
                process.exit()
            });
        });
    });
}

main()