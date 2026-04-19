const footer = document.getElementById("foot01");
if (footer) {
  footer.innerHTML = `<p>&copy; ${new Date().getFullYear()} Eugene Mark Korku Barasu. All rights reserved.</p>`;
}

const nav = document.getElementById("nav01");

if (nav) {
  const links = [
    { href: "../../index.html", label: "Home", icon: '<i class="fa fa-home"></i>' },
    { href: "index.html", label: "Projects Overview" },
    { href: "project_9.html", label: "Super-Calculator Project" },
    { href: "project_10.html", label: "Word Replacement Game" },
    { href: "project_13.html", label: "Wish List" },
    { href: "project_14.html", label: "JavaScript Pizzaria" },
    { href: "project_15.html", label: "Activity of the Day Calendar" },
    { href: "project_16.html", label: "Adventure Game" },
    { href: "project_18.html", label: "Lunch Game" },
    { href: "project_19.html", label: "Lemonade Game" },
    { href: "project_shopStart.html", label: "Shop-Start" }
  ];

  const currentFile = window.location.pathname.split("/").pop() || "index.html";

  nav.innerHTML = `<ul id="menu">${links
    .map((link) => {
      const isActive =
        currentFile === link.href ||
        (currentFile === "" && link.href === "index.html");

      const style = isActive
        ? ' style="color:white;background-color:#009688;"'
        : "";

      return `<li><a${style} href="${link.href}">${link.icon ? link.icon + " " : ""}${link.label}</a></li>`;
    })
    .join("")}</ul>`;
}
