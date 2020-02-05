document.head.appendChild(
  Object.assign(document.createElement("script"), {
    src: "//cdnjs.cloudflare.com/ajax/libs/socket.io/1.3.6/socket.io.min.js"
  })
);

var socket = io.connect("http://" + document.domain + ":" + location.port);

socket.on("playlist_channel", function(msg) {
  console.log(msg);
});
