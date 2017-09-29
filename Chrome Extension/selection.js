var genMSM = function(info) {
    message = convert(info.selectionText)
    copyToClipboard(message)
}

chrome.contextMenus.create({
    title: "Generate Meme",
    contexts: ["selection"],
    onclick: genMSM
});

function convert(message) {
    output = ""
    for(var i = 0; i < message.length; i++){
        output += i % 2 == 0 ? message.charAt(i).toLowerCase():message.charAt(i).toUpperCase();
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
