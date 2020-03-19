function showTalk(evt){
    evt.preventDefault();
 
    const selectedId1 = $('#ted_talk1').val();
    const selectedId2 = $('#ted_talk2').val();
    const url = `/compare/${selectedId1}/${selectedId2}`;

    $.get(url, (data) => {
        $('#talk_name1').text(data.talk_name1);
        $('#talk_name2').text(data.talk_name2);
        $('#comments1').text(data.num_comments1);
        $('#comments2').text(data.num_comments2);
        $('#views1').text(data.num_views1);
        $('#views2').text(data.num_views2);
        duration1=data.duration1[0]+" min "+data.duration1[1]+" sec"
        duration2=data.duration2[0]+" min "+data.duration2[1]+" sec"
        $('#duration1').text(duration1);
        $('#duration2').text(duration2);
 
 
        const ratingList = data.rating_list;

        const createObj = () => {
            const dataObj = [];
            for(let i = 0; i < 14; i++){
                let newObj = {
                    "rating": ratingList[0].values[i].rating,
                    "values": [
                        {
                            "count": ratingList[0].values[i].count,
                            "name": ratingList[0].name
                        },
                        {
                            "count": ratingList[1].values[i].count,
                            "name": ratingList[1].name
                        }
                             ]
                    }
                    dataObj.push(newObj);
            }

        return dataObj;
        }

        const ratingListMapped = createObj();

        let talkNames = ratingListMapped[0].values.map(function(d){ return d.name ;});
        let ratingNames = ratingListMapped.map(function(d){ return d.rating; });


        document.querySelector("#Area1").innerHTML = "";
        const margin = {top: 20, right: 30, bottom: 50, left: 40},
            width = 700 - margin.left - margin.right,
            height = 400 - margin.top - margin.bottom;
        let x1 = d3.scale.ordinal();

        let x0 = d3.scale.ordinal()
        .rangeRoundBands([0, width], .1);

        let y = d3.scaleLinear()
                .range([height, 0]);

        var yAxis = d3.axisLeft()
            .scale(y);
        
        var xAxis = d3.axisBottom()
            .scale(x0)
            .tickSize(0);
        
        var color = d3.scale.ordinal()
            .range(["#ca0020","#f4a582"]);
        

        let svg = d3.select("#Area1").append("svg")
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom)
        .append("g")
            .attr("transform", 
                  "translate(" + margin.left + "," + margin.top + ")");

        
        x0.domain(ratingNames);
        x1.domain(talkNames).rangeRoundBands([0, x0.rangeBand()]);
        y.domain([0, d3.max(ratingListMapped, function(rating){return d3.max(rating.values, function(d) {return d.count; }); })]);
    


        
        svg.append("g")
            .attr("class", "x axis")
            .attr("transform", "translate(0," + height + ")")
            .call(xAxis)
            .selectAll("text")
                .style("text-anchor", "end")
                .attr("transform", function(d) {
                    return "rotate(-45)" 
                    });
        svg.append("g")
            .attr("class", "y axis")
            .call(yAxis)
          .append("text")
            .attr("transform", "rotate(-90)")
            .attr("y", 6)
            .attr("dy", ".71em")
            .style("text-anchor", "end")
            .text("Count");

        let slice = svg.selectAll(".slice")
            .data(ratingListMapped)
            .enter().append("g")
            .attr("class", "g")
            .attr("transform",function(d) { return "translate(" + x0(d.rating) + ",0)"; });
      
        slice.selectAll("rect")
            .data(function(d) { return d.values; })
        .enter().append("rect")
            .attr("width", x1.rangeBand())
            .attr("x", function(d) { return x1(d.name); })
            .style("fill", function(d) { return color(d.name) })
            .attr("y", function(d) { return y(d.count); })
            .attr("height", function(d) { return height - y(d.count); })
            .on("mouseover", onMouseOver)
            .on("mouseout", onMouseout);
        
        function onMouseOver(d){
            svg.append("text")
            .attr('class', 'val')
            .style('font-size', '10px') 
            .attr('x', 10)
            .attr('y', 20)
            .text(function() {
             return ['Count: '+ d.count];  // Value of the bar
            });
        }
        function onMouseout(){
            d3.selectAll('.val')
            .remove()
        }
        
        //Legend
        const legend = svg.selectAll(".legend")
            .data(ratingListMapped[0].values.map(function(d) { return d.name; }).reverse())
            .enter().append("g")
            .attr("class", "legend")
            .attr("transform", function(d,i) { return "translate(0," + i * 20 + ")"; })
            .style("opacity","0");

        legend.append("rect")
            .attr("x", width - 18)
            .attr("width", 18)
            .attr("height", 18)
            .style("fill", function(d) { return color(d); });

        legend.append("text")
            .attr("x", width - 24)
            .attr("y", 9)
            .attr("dy", ".35em")
            .style("text-anchor", "end")
            .style("font-size", "10px")
            .text(function(d) {return d; });

        legend.transition().duration(500).delay(function(d,i){ return 1300 + 100 * i; }).style("opacity","1");

                });

}


$("#get-talks").on('submit', showTalk);

