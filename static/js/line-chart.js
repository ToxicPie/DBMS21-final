let query = new URLSearchParams({product_id: product_id});

async function get_data() {
    let query = new URLSearchParams({product_id: product_id});
    let resp = await fetch('/api/bazaar/history?' + query.toString());
    let ret = await resp.json();

    let buy_prices = [],
        buy_volumes = [],
        sell_prices = [],
        sell_volumes = [];

    for (var i = 0; i < ret.timestamps.length; i++) {
        buy_prices.push([ret.timestamps[i], ret.buy_prices[i]]);
        buy_volumes.push([ret.timestamps[i], ret.buy_volumes[i]]);
        sell_prices.push([ret.timestamps[i], ret.sell_prices[i]]);
        sell_volumes.push([ret.timestamps[i], ret.sell_volumes[i]]);
    }
    return { buy_prices, buy_volumes, sell_prices, sell_volumes };
}

async function draw_chart() {

    const {
        buy_prices, buy_volumes, sell_prices, sell_volumes
    } = await get_data();

    let chart = Highcharts.stockChart('chart-container', {
        rangeSelector: {
            selected: 1
        },
        yAxis: [{
            labels: {
                align: 'left'
            },
            height: '80%',
            resize: {
                enabled: true
            }
        }, {
            labels: {
                align: 'left'
            },
            top: '80%',
            height: '20%',
            offset: 0
        }],
        plotOptions: {
            column: {
                stacking: 'normal'
            }
        },
        series: [
            {
                name: 'Buy price',
                data: buy_prices,
                tooltip: {
                    valueDecimals: 1
                }
            },
            {
                name: 'Buy volume',
                type: 'column',
                yAxis: 1,
                data: buy_volumes,
                tooltip: {
                    valueDecimals: 0
                }
            },
            {
                name: 'Sell price',
                data: sell_prices,
                tooltip: {
                    valueDecimals: 1
                }
            },
            {
                name: 'Sell volume',
                type: 'column',
                yAxis: 1,
                data: sell_volumes,
                tooltip: {
                    valueDecimals: 0
                }
            },
        ]
    });
}

await draw_chart();
