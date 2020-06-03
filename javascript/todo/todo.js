let list = document.querySelector('ul');
let tasks = [];
let todoItem = document.querySelector('.js-form');

function addTask(taskText) {
    const task = {
        text,
        crossedOut: false,
        id: Date.now(),
    };
    tasks.push(task);
};

todoItem.addEventListener('submit', event => {
    event.preventDefault();
    let input = document.querySelector('.js-task-input');
    let taskText = input.value();
    if (input === '') {
        alert("You must enter a task.")
    }
    else {
        addTask(taskText);
    };
});

list.addEventListener('click', event => {
    if (event.target.tagName === 'LI') {
        event.target.classList.toggle('crossedOut')
    };
}, false);   
