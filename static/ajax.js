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
        console.log(data.rating_list1);
        // myvar = '{{data.rating_dict1|tojson}}';
        let rating1 = data.rating_list1;
        let rating2 = data.rating_list2;

        
        var margin = {top: 20, right: 20, bottom: 70, left: 40},
            width = 600 - margin.left - margin.right,
            height = 300 - margin.top - margin.bottom;
        var x = d3.scale.ordinal().rangeRoundBands([0, width], .05);
        var y = d3.scale.linear().range([height, 0]);
        var yAxis = d3.svg.axis()
            .scale(y)
            .orient("left")
            .ticks(10);

        var svg = d3.select("body").append("svg")
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom)
          .append("g")
            .attr("transform", 
                  "translate(" + margin.left + "," + margin.top + ")");
        y.domain([0, d3.max(rating1, function(d) { return d.count; })]);
        x.domain(rating1.map(function(d) { return d.name; }));
        svg.selectAll("whatever")
            .data(rating1)
            .enter().append("rect")
            .style("fill", "steelblue")
            .attr("x", function(d) { return x(d.name); })
            .attr("width", x.rangeBand())
            .attr("y", function(d) { return y(d.count); })
            .attr("height", function(d) { return height - y(d.count); });
        svg.selectAll("whatever")
            .data(rating2)
            .enter().append("rect")
            .style("fill", "purple")
            .attr("x", function(d) { return x(d.name); })
            .attr("width", x.rangeBand())
            .attr("y", function(d) { return y(d.count); })
            .attr("height", function(d) { return height - y(d.count); });
  

        // $('#funny1').text(data.Funny1);
        // $('#funny2').text(data.Funny2);     

    });
}

$("#get-talks").on('submit', showTalk);

