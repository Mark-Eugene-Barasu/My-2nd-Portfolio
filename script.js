function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
    document.getElementById("pageContainer").style.opacity = "0.5";
    document.getElementById("navButton").style.width = "0px";
  }
  
  function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("pageContainer").style.opacity = "1";
    document.getElementById("navButton").style.width = "50px";
  }