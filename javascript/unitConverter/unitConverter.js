function meter(distance){
    let meters = distance * 0.3048
    return(meters)
} 

function main(){
    let rl = require('readline');

    let prompts = rl.createInterface(process.stdin, process.stdout);

    prompts.question("Please enter the distance in feet to convert to meters: ", function(distance){
        let meters = meter(distance)
        console.log(distance,"feet = ", meters, "meters.")
        process.exit();
    });
}
main()