document.addEventListener("DOMContentLoaded", () => {
  const root = document.querySelector("#root");
  const ulTodoMain = document.querySelector("#ul-todo-main");
  const btnAddMain = document.querySelector("#btn-add-main");
  const inputAddMain = document.querySelector("#input-add-main");

  function createTodoItem(todo) {
    return `<li>${todo}</li>`;
  }

  function handleAddTodoItem() {
    const inputAddMainItem = inputAddMain.value;
    ulTodoMain.innerHTML =
      ulTodoMain.innerHTML + createTodoItem(inputAddMainItem);
    inputAddMain.value = "";
  }

  btnAddMain.addEventListener("click", handleAddTodoItem);
});
