function showTalk(evt){
    evt.preventDefault();
 
    const selectedId1 = $('#ted_talk1').val();
    const selectedId2 = $('#ted_talk2').val();
    let url = `/compare/${selectedId1}/${selectedId2}`;

    $.get(url, (data) => {
        $('#talk_name1').text(data.talk_name1);
        $('#talk_name2').text(data.talk_name2);
        $('#comments1').text(data.num_comments1);
        $('#comments2').text(data.num_comments2);
        $('#views1').text(data.num_views1);
        $('#views2').text(data.num_views2);
        $('#duration1').text(data.duration1);
        $('#duration2').text(data.duration2);
    });
}

$("#get-talks").on('submit', showTalk);