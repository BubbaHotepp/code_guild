let list = document.querySelector('#taskList');
let todoItem = document.querySelector('.task-form');
let btn = document.querySelector('#button-addon2');
let btn2 = document.querySelector('#button-addon3');


btn.addEventListener('click', function() {
    let input = document.querySelector('.task-input');
    let crossedOut = false;
    let taskText = input.value;

    if (input === '') {
        alert("You must enter a task.")
    }
    else {
        let liNode = document.createElement('LI');
        let liText = document.createTextNode(taskText);
        liNode.appendChild(liText);
        liNode.innerHTML = liNode.innerHTML + '<button class="btn2 btn-primary" onClick="delTask()" type="button" id="button-addon3">Delete</button>';
        document.getElementById('taskList').appendChild(liNode);
    };
});

list.addEventListener('click', function(event) {
    if (event.target.tagName === 'LI') {
        console.log('L1 works')
        event.target.classList.toggle('crossedOut')
        }
    }, false);  

function delTask() {
    console.log('function works')
    list.addEventListener('click', function(event) {
        console.log('still working')
        item = event.target.parentElement
        item.remove()
        
    })}

