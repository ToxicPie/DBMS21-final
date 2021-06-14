document.getElementById('search').addEventListener('keydown', e => {
    if (e.keyCode === 13) {
        let query = document.getElementById('search').value,
            params = {query: query},
            urlparams = new URLSearchParams(params).toString();

        if (query === '') {
            url = '/api/bazaar/products';
        } else {
            url = '/api/bazaar/search?' + urlparams;
        }

        fetch(url)
            .then(response => response.json())
            .then(data => {
                links_container = document.getElementById('links-container');
                // obliterate
                while (links_container.lastChild) {
                    links_container.removeChild(links_container.lastChild);
                }

                ids = [];
                for (var i = 0; i < data.length; i++) {
                    ids.push('product_id=' + data[i].product_id);
                }

                var statuses = [];
                fetch('/api/bazaar/status?' + ids.join('&'))
                    .then(response => response.json())
                    .then(data => {
                        for (var i = 0; i < data.result.length; i++) {
                            statuses.push(data.result[i]);
                        }
                        return statuses;
                    }).then(statuses => {
                        for (var i = 0; i < data.length; i++) {
                            let newdiv = document.createElement('div');

                            let link1 = document.createElement('a');
                            link1.innerHTML = data[i].name;
                            link1.href = '/history/' + data[i].product_id;

                            let link2 = document.createElement('a');
                            link2.innerHTML = '(stock chart - sell)';
                            link2.href = '/stock/' + data[i].product_id;

                            let link3 = document.createElement('a');
                            link3.innerHTML = '(stock chart - buy)';
                            link3.href = '/stock2/' + data[i].product_id;

                            let {
                                product_id,
                                product_name,
                                buy_price,
                                buy_volume,
                                sell_price,
                                sell_volume
                            } = statuses[i];
                            let desc = document.createElement('p');
                            desc.innerHTML = `Buy price: ${buy_price} / ` +
                                             `Buy volume: ${buy_volume} / ` +
                                             `Sell price: ${sell_price} / ` +
                                             `Sell volume: ${sell_volume}`;

                            newdiv.appendChild(link1);
                            newdiv.appendChild(link2);
                            newdiv.appendChild(link3);
                            newdiv.appendChild(desc);
                            links_container.appendChild(newdiv);
                        }
                    })
        });
    }
});
