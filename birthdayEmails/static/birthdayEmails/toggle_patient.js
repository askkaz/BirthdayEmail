current_patient="";
$(".active-table").click(function() {
    $("#emailBody").parent().removeClass("hidden");
    $("#emailSubject").parent().removeClass("hidden");
    current_patient = $(this).children(".patient-id").text();
    patient_name = $(this).children(".patient-name").text();
    patient_birthday = $(this).children(".patient-birthday").text();
    $("#patientName").val(patient_name);
    subject_text = $(this).children(".patient-email-subject").text()
    $("#emailSubject").val(subject_text);
    body_text = $(this).children(".patient-email-body").text()
    $("#emailBody").val(body_text);
    $("#patientId").val(current_patient);
    $("#patientBirthday").val(patient_birthday);
    if (body_text === "") {
        $(".delete-btn").addClass("hidden");
    } else {
        $(".delete-btn").removeClass("hidden");
    }
    if ($(this).children(".patient-email-sent").text() == "") {
        $(".save-btn").removeClass("hidden");
    } else {
        $(".save-btn").addClass("hidden");
    }
    

});