$(".active-table").click(function() {
    // Unhide email text
    $("#emailBody").parent().removeClass("hidden");
    $("#emailSubject").parent().removeClass("hidden");

    //Move all the existing patient info over to the form
    $("#patientEmailAddress").val($(this).children(".patient-email-address").text());
    $("#patientName").val($(this).children(".patient-name").text());
    $("#emailSubject").val($(this).children(".patient-email-subject").text());
    body_text=$(this).children(".patient-email-body").text();
    $("#emailBody").val(body_text);
    $("#patientId").val($(this).children(".patient-id").text());
    $("#patientBirthday").val($(this).children(".patient-birthday").text());
    //Remove delete button for empty emails
    if (body_text === "") {
        $(".delete-btn").addClass("hidden");
    } else {
        $(".delete-btn").removeClass("hidden");
    }
    //Remove save button for emails that have been sent
    if ($(this).children(".patient-email-sent").text() == "") {
        $(".save-btn").removeClass("hidden");
    } else {
        $(".save-btn").addClass("hidden");
    }
});