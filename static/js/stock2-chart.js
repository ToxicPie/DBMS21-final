async function get_data() {
    let query = new URLSearchParams({product_id: product_id});
    let resp = await fetch('/api/bazaar/history?' + query.toString());
    let ret = await resp.json();
    console.log(ret)
    return ret;
}

async function draw_chart() {
    const data = await get_data();

    if (data.error) {
        alert(data.error);
    } else {
        // split the data set into ohlc and volume
        let ohlc = [],
            volume = [],
            len = data.timestamps.length;

        const group = 6;

        for (var i = 0; i < len; i += group) {
            let min_price = Infinity,
                max_price = -Infinity,
                total_volume = 0,
                j = i;

            for (j = i; j < i + group && j < len; j++) {
                min_price = Math.min(min_price, data.buy_prices[j]);
                max_price = Math.max(max_price, data.buy_prices[j]);
                total_volume += data.buy_volumes[j];
            }

            ohlc.push([
                data.timestamps[i],
                data.buy_prices[i],
                max_price,
                min_price,
                data.buy_prices[j - 1]
            ]);

            volume.push([
                data.timestamps[i],
                total_volume
            ]);
        }

        console.log(ohlc)

        const groupingUnits = [[
            'week',                         // unit name
            [1]                             // allowed multiples
        ], [
            'month',
            [1, 2, 3, 4, 6]
        ]];

        // create the chart
        Highcharts.stockChart('chart-container', {

            rangeSelector: {
                selected: 1
            },

            title: {
                text: `${product_id} Historical Sell Prices`
            },

            yAxis: [{
                labels: {
                    align: 'right',
                    x: -3
                },
                title: {
                    text: 'OHLC'
                },
                height: '60%',
                lineWidth: 2,
                resize: {
                    enabled: true
                }
            }, {
                labels: {
                    align: 'right',
                    x: -3
                },
                title: {
                    text: 'Volume'
                },
                top: '65%',
                height: '35%',
                offset: 0,
                lineWidth: 2
            }],

            tooltip: {
                split: true
            },

            series: [{
                type: 'candlestick',
                name: product_id,
                data: ohlc,
                dataGrouping: {
                    units: groupingUnits
                }
            }, {
                type: 'column',
                name: 'Volume',
                data: volume,
                yAxis: 1,
                dataGrouping: {
                    units: groupingUnits
                }
            }]
        });
    }
}

await draw_chart();
