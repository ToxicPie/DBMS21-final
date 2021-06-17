document.addEventListener("DOMContentLoaded", event => {
    document.getElementById("Search_btn").addEventListener('click',event => {
        var url = new URL('http://localhost/api/bazaar/search');
        input = document.getElementById("Search").value;
        var params = {query: input};
        url.search = new URLSearchParams(params).toString();

        fetch(url)
            .then(function(response) {
                return response.json();
            })
            .then(function(data) {
                if (data.hasOwnProperty('error') !== true && data !== []) {
                    console.log(data);
                    window.location.replace(`/summary/${data[0].product_id}`);
                }
            })
    }, false);
});
