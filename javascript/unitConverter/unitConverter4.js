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

function mi(meters){
    convert = meters / 1609.34
    return(convert)
} // Converts meters to miles

function yd(meters){
    convert = meters / 0.9144
    return(convert)
} // Converts meters to yards

function in(meters){
    convert = meters / 0.0254
    return(convert)
} // Converts meters to inches

function ft(meters){
    convert = meters / 0.3048
    return(convert)
} // Converts meters to feet

function km(meters){
    convert = meters / 1000
    return(convert) 
} // Converts meters to kilometers

function main(){

    let rl = require('readline');
    let unit = "";
    let distance = "";

    let prompts = rl.createInterface(process.stdin, process.stdout);
    prompts.question("Please enter the unit to convert from'\n'(Kilometers = 'km', Miles = 'mi', Meters = 'm', Yard = 'yd', Feet = 'ft', Inches = 'in'):", function(unit_from){
        
        prompts.question("Please enter the unit to convert to'\n'(Kilometers = 'km', Miles = 'mi', Meters = 'm', Yard = 'yd', Feet = 'ft', Inches = 'in'):",function(unit_to){

            prompts.question("Please enter the distance in", unit_from,"to convert to", unit_to,": ", function(distance){
                let meters = meter(unit_from, distance)
                let distance_ouput = (meters)
                console.log(distance, unit_from, "=", distance_ouput, unit_to)
                process.exit();
            });
        });
    });
}

main()