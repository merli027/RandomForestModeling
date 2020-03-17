function showSpeaker(evt){
    evt.preventDefault();
 
    let speakerName = $('#speaker').val().replace(/\s+/g, '-');
    let url = `/find_speaker/${speakerName}`;
    console.log(speakerName);

    $.get(url, (data) => {
        $('#speaker-id').text(data.speaker_id);
        $('#speaker-job').text(data.speaker_job);
        
        document.querySelector("#talks").innerHTML = "";
        const list = document.createElement("ul");
        for(let talk of data.talks){
            const listText = document.createTextNode(talk);
            const listEl = document.createElement("li");
            listEl.appendChild(listText);
            list.appendChild(listEl);
        }

        document.getElementById("talks").appendChild(list);
        console.log("Hi");
    })
};
$("#get-speaker").on('submit', showSpeaker);




