function test2() {
    $.ajax({
        type: "GET",
        url: "/test",
        dataType: "html",
        success: function(msg) {
            console.log(msg);
            $("#announcementdiv").text(msg);
        },
        error: function (xhr, status, error) {
            console.log(error);
        }
    });
}