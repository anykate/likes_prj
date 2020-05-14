window.setTimeout(function () {
  $(".alert")
    .fadeTo(500, 0)
    .slideUp(500, function () {
      $(this).remove();
    });
}, 1000);

$(document).ready(function () {
  var count = 0;
  $("#genbutton").on("click", function (e) {
    e.preventDefault();
    count++;
    $.ajax({
      url: "",
      type: "POST",
      data: {
        button_text: count,
        csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
      },
      dataType: "json",
      success: function (response) {
        $(".likes_val").text(response.response_text);
      },
      error: function (e) {
        console.error(e.statusText);
      },
    });
  });
});
