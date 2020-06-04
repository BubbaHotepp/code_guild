let list = document.querySelector('#taskList');
let todoItem = document.querySelector('.js-form');
let btn = document.querySelector('#button-addon2');
let btn2 = document.querySelector('#button-addon3');


btn.addEventListener('click', function() {
    let input = document.querySelector('.js-task-input');
    let crossedOut = false;
    let taskText = input.value;

    if (input === '') {
        alert("You must enter a task.")
    }
    else {
        let liNode = document.createElement('LI');
        let liText = document.createTextNode(taskText);
        liNode.appendChild(liText);
        liNode.innerHTML = liNode.innerHTML + '<button class="btn2 btn-primary" action="delete" type="button" id="button-addon3">Delete</button>';
        document.getElementById('taskList').appendChild(liNode);
    };


});

list.addEventListener('click', function(event) {
    if (event.target.tagName === 'LI') {
        event.target.classList.toggle('crossedOut')
        }
    }, false);  

list.addEventListener('', function(event){
    if (event.target.tagName === 'LI') {
        event.target.remove()
        }
    });
