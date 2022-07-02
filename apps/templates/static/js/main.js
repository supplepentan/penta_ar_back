document.querySelector("#toggle-btn").onclick = function () {
    bootstrap.Button.getOrCreateInstance(this).toggle();
    this.innerHTML = "起動中";
    message = prompt("起動しますか？", "起動");
    alert(message)
}