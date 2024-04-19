fetch("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1")
    .then((response) => {
        return response.json();
    })
    .then( (response) => {
        console.log(response);
    })
    .catch((error) => {
        console.log("error");
    })