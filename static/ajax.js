function showHuman(evt){
    evt.preventDefault();
 
    const selectedId = $('#ted_talk1').val();
    const selectedId = $('#ted_talk2').val();
    let url = `/compare`;

    $.get(url, (data) => {
        $('#fname').text(data.fname);
        $('#lname').text(data.lname);
        $('#email').text(data.email);
    });
}

$("#get-human").on('submit', showHuman);