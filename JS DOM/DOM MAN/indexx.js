document.addEventListener("DOMContentLoaded", () => {
  // DECLARATIONS
  const root = document.querySelector("#root");
  //Main
  const ulTodoMain = document.querySelector("#ul-todo-main");

  //Others
  //button
  const btnAddMain = document.querySelector("#btn-add-main");
  //input
  const inputAddMain = document.querySelector("#input-add-main");

  //END OF DECLARATIONS

  //Abstractions
  //inserted in handle fucntion
  //const currentTodo = ulTodoMain.innerHTML;

  //SHOW
  //console.log(currentTodo);

  //FUNCTIONS

  //F-CREATE
  function createTodoItem(todo) {
    return `<li>${todo}</li>`;
  }

  //Add in Main List
  //ulTodoMain.innerHTML = currentTodo + `<li>New Item</li>`;
  //ulTodoMain.innerHTML = currentTodo + createTodo("CodeHutPH");

  //F-ADD
  function handleAddTodoItem() {
    const inputAddMainItem = inputAddMain.value;
    ulTodoMain.innerHTML =
      ulTodoMain.innerHTML + createTodoItem(inputAddMainItem);
    inputAddMain.value = "";
  }

  //F-ADD-BUTTON
  btnAddMain.addEventListener("click", handleAddTodoItem);
});
