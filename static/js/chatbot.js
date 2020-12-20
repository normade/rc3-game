
reset_tracking_session().then(() => {
    track_event("pageload")
});

const addBotAnswerToLog = (botResponse) => {
    emptyChatContainer();
    const botContainer = document.querySelector("#chat");
    const tag = document.createElement("p");
    const containerRow = document.createElement("div");
    const containerCol = document.createElement("div");
    const text = document.createTextNode(botResponse);
    containerRow.classList.add("row");
    containerCol.classList.add("col-7");
    tag.classList.add("bubble-left");

    tag.appendChild(text);
    containerCol.appendChild(tag);
    containerRow.appendChild(containerCol);
    botContainer.appendChild(containerRow);
}

const emptyInputField = () => {
    document.querySelector("#user-input").value = "";
}

const emptyChatContainer = () => {
    const container = document.querySelector("#chat");
    container.textContent = '';
}

async function sendUserInput(event) {
    event.preventDefault();
    const inputValue = document.querySelector("#user-input").value;
    if (inputValue === "") {
        return;
    }
    emptyInputField();
    const url = window.location.origin + postMessageUrl;
    await fetch(url, {
        method: 'POST',
        credentials: 'same-origin',
        headers: {
            "Content-Type": 'application/json',
            "X-CSRFToken": csrftoken
        },
        redirect: 'follow',
        referrerPolicy: 'same-origin',
        body: JSON.stringify(
            {
                "text": inputValue
            }
        )
    }).then(response => response.json()).then(data => {
        addBotAnswerToLog(data.text + " " + data.isSolution);
    }).catch((error) => {
        console.error(error);
    });
}

const addEventListenerToForm = () => {
    const chatForm = document.querySelector("#chat-form");
    chatForm.addEventListener("submit", sendUserInput, false);
}

setInterval(function() {
tp.classList.remove("animate");
}, 60000); // remove after 60s

setInterval(function() {
tp.classList.add("animate");
}, 120000); // animate every 2min


window.onload = (event) => {
    addEventListenerToForm();
};

const tp = document.getElementById("flying-toiletpaper");
tp.addEventListener("click", function(){
    track_event("flying-toiletpaper")
    alert("Yay! Achievement received!");
});

