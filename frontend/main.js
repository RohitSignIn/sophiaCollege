$(document).ready(function () {
  let count = 0;
  let todos = [];

  $.ajax({
    type: "get",
    url: "http://localhost:9090/api/v1/todos",
    success: function (response) {
      //   console.log(response["res"]);
      for (let i = 0; i < response["res"].length; i++) {
        todos.push(response["res"][i][1]);
      }
      handleRepaint(todos);
    },
  });

  function handleDelete(btn) {
    todos[btn.attr("value")] = null;
    handleRepaint(todos);
  }

  function handleEdit(btn) {
    btnType = $(btn).text();

    if (btnType == "Edit") {
      $(btn).text("Save");

      const inputNode = $(
        `<input type="text" value="${$(btn).parent().prev().text()}"  />`
      );
      $(btn).parent().prev().html(inputNode);
    } else {
      $(btn).text("Edit");

      const text = $(btn).parent().prev().children().val();
      $(btn).parent().prev().html(text);
    }

    $(btn).parent().prev().text();
  }

  $("#rowCount").on("click");

  $("#todoSubmit").on("click", () => {
    const task = $("#todoInput").val();
    todos.push(task);
    handleRepaint(todos);
  });

  function handleRepaint(todos) {
    $("#rowCont").html("");
    let count = 0;
    for (let indx = 0; indx < todos.length; indx++) {
      const val = todos[indx];
      if (val == null) continue;

      const task = $("#todoInput").val();
      const tableRow = $("<tr></tr>");
      const tableHead = $(`<th scope="row">${++count}</th>`);
      const tableData = $(`<td>${val}</td>`);
      const editTd = $("<td></td>");
      const editBtn = $('<button class="btn btn-warning">Edit</button>');
      const deleteBtn = $(
        `<td value=${indx}><button btnVal=${indx} class="btn btn-danger todoDelete">Delete</button></td>`
      );

      deleteBtn.on("click", () => {
        handleDelete(deleteBtn);
      });

      editBtn.on("click", () => {
        handleEdit(editBtn);
      });

      editTd.append(editBtn);

      tableRow.append(tableHead);
      tableRow.append(tableData);
      tableRow.append(editTd);
      tableRow.append(deleteBtn);

      $("#rowCont").append(tableRow);
    }
  }
});
