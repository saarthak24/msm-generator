chrome.commands.onCommand.addListener(function(command) {
    if (command == "generate") {
        text = window.getSelection().toString()
        console.log(text)
        message = convert(text)
        copyToClipboard(message)
    }
});

function convert(message) {
    output = ""
    for (var i = 0; i < message.length; i++) {
        output += i % 2 == 0 ? message.charAt(i).toLowerCase() : message.charAt(i).toUpperCase();
    }
    return output
}

function copyToClipboard(text) {
    var temp = document.createElement("textarea");
    temp.textContent = text;
    var body = document.getElementsByTagName('body')[0];
    body.appendChild(temp);
    temp.select();
    document.execCommand('copy');
    body.removeChild(temp);
}
