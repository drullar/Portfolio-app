function openNav() {
    document.getElementById("mySidebar").style.width = "150px";
    document.getElementById("mySidebar").style.marginTop = document.getElementById("main").style.marginTop;
    document.getElementById("main").style.visibility = 'hidden';
}

function closeNav() {
    document.getElementById("mySidebar").style.width = "0";
    document.getElementById("main").style.marginLeft = "0";
    document.getElementById("main").style.visibility = 'visible';
}