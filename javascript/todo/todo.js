function addTodo(text, tasks){
    let item = {
        text,
        checked: false,
        id: Date.now()
    };

    tasks.push(item);
    console.log(tasks);
}

function delTodo(text){
    // have to remove items by value
}


function main(){
    let tasks = [];
    let todoItem = document.querySelector('.js-form');
    todoItem.addEventListener('', event => {
        event.preventDefault();
        let item = document.querySelector('.js-todo-item');
        let itemText = item.value();
        addTodo(itemText, tasks);

    })
}