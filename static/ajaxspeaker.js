function showSpeaker(evt){
    evt.preventDefault();
 
    const selectedId = $('#speaker').val();
    let url = `/find_speaker/${selectedId}`;
    console.log(Hi)

    $.get(url, (data) => {
        $('#speaker-id').text(data.speaker_id);
        $('#speaker-job').text(data.speaker_job);
        $('#talks').text(data.talks);
        $('#message').text(data.message);
        console.log(Hi)
    })
};
$("#get-speaker").on('submit', showSpeaker);


