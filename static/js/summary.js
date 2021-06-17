console.log(product_id)

async function get_data() {
    let url = new URL('http://localhost/api/bazaar/history'),
        params = {product_id: product_id};

    url.search = new URLSearchParams(params).toString();

    let resp = await fetch(url);
    let data = await resp.json();

    let buy_prices = [],
        buy_volumes = [],
        sell_prices = [],
        sell_volumes = [];

    for (var i = 0; i < data.timestamps.length; i++) {
        buy_prices.push([data.timestamps[i], data.buy_prices[i]]);
        buy_volumes.push([data.timestamps[i], data.buy_volumes[i]]);
        sell_prices.push([data.timestamps[i], data.sell_prices[i]]);
        sell_volumes.push([data.timestamps[i], data.sell_volumes[i]]);
    }
    return { buy_prices, buy_volumes, sell_prices, sell_volumes };
}

async function plot_chart(){
    const {
        buy_prices, buy_volumes, sell_prices, sell_volumes
    } = await get_data();

    let chart = Highcharts.stockChart('container', {
        chart: {
            backgroundColor: '#353535'
        },

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

plot_chart();
