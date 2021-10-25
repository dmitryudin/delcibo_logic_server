

class RestCard{
    constructor() {
    }
    renderView(obj){
        var div = document.createElement("div");
        div.id = "main-rest-div";
        var hr = document.createElement("hr"); div.appendChild(hr);
         var hr = document.createElement("hr"); div.appendChild(hr);
        var caption = document.createElement("h2");
        caption.id = "rest-caption";
        caption.className = "rest-caption";
        caption.textContent= obj.name;
        div.appendChild(caption);
        ///////////////////////////////////
        var hr = document.createElement("hr"); div.appendChild(hr);
        var caption = document.createElement("h2");
        caption.id = "rest-description";
        caption.className = "rest-description";
        caption.textContent= obj.description;
        div.appendChild(caption);
        var hr = document.createElement("hr"); div.appendChild(hr);
        //////////////////////////////
        var img = document.createElement("img");
        img.src=obj.icon
        img.className = "img"
        div.appendChild(img);
        return div;
    }
}



function getRestList(){
    const request = new XMLHttpRequest();
    const url = "/grl";

    request.open("POST", url, true);
    request.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

    request.addEventListener("readystatechange", () => {

    if(request.readyState === 4 && request.status === 200) {




        for (let i = 0; i < 10; i++) {
		let div = new RestCard().renderView(JSON.parse(request.responseText).value[0]);
		document.body.appendChild(div);}
    }
});

//	Вот здесь мы и передаем строку с данными, которую формировали выше. И собственно выполняем запрос.
    request.send();



}

getRestList();