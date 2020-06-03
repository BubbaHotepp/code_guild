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
    
    let span = document.createElement("SPAN");

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
    let list = document.querySelector('ul');
    let tasks = [];
    let todoItem = document.querySelector('.js-form');
    
    list.addEventListener('click', function(event) {
        if (event.target.tagName === 'LI') {
            event.target.classList.toggle('crossedOut');
        }
    }, false);

    todoItem.addEventListener('submit', event => {
        event.preventDefault();
        let item = document.querySelector('.js-todo-item');
        let itemText = item.value();
        addTodo(itemText, tasks);

    })
}
main()