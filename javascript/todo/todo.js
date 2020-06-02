function addTodo() {
    let li = document.createElement("li");
    let addTask = document.getElementById("addTask").value;
    let taskText = document.createTextNode(addTask);
    li.appendChild(taskText);
    if (addTask === "") {
        alert("Please enter task details!")
    }
    else {
        document.getElementById("taskUL").appendChild(li);
    }
    document.getElementById("addTask").value = "";   
}

function delTodo() {
    let remove = document.getElementsByClassName("remove");
    const item;
    for (item = 0, i < remove.length; item++) {
        remove[item].onclick = function() {
            let div = this.parentElement;
            div.style.display = "none";
        }
    }
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