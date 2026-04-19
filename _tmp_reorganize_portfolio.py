from pathlib import Path
import shutil
import re

ROOT = Path(__file__).resolve().parent

ASSETS_DIR = ROOT / "assets"
CSS_DIR = ASSETS_DIR / "css"
JS_DIR = ASSETS_DIR / "js"
IMAGES_DIR = ASSETS_DIR / "images"
VENDOR_DIR = ASSETS_DIR / "vendor"
PAGES_DIR = ROOT / "pages"
PROJECTS_DIR = PAGES_DIR / "projects"

for directory in [CSS_DIR, JS_DIR, IMAGES_DIR, VENDOR_DIR, PAGES_DIR, PROJECTS_DIR]:
    directory.mkdir(parents=True, exist_ok=True)


def move_file(src_rel: str, dst_rel: str):
    src = ROOT / src_rel
    dst = ROOT / dst_rel
    dst.parent.mkdir(parents=True, exist_ok=True)
    if src.exists():
        if dst.exists():
            src.unlink()
        else:
            shutil.move(str(src), str(dst))


# Move shared assets
move_file("style.css", "assets/css/style.css")
move_file("yes.css", "assets/css/yes.css")
move_file("script.js", "assets/js/script.js")
move_file("projects.js", "assets/js/projects.js")
move_file("font-awesome.min.css", "assets/vendor/font-awesome.min.css")

# Move main pages
move_file("aboutMe.html", "pages/about.html")
move_file("socials.html", "pages/socials.html")
move_file("gallery.html", "pages/gallery.html")
move_file("projects.html", "pages/projects/index.html")

# Move project pages
for name in [
    "project_9.html",
    "project_10.html",
    "project_13.html",
    "project_14.html",
    "project_15.html",
    "project_16.html",
    "project_18.html",
    "project_19.html",
    "project_shopStart.html",
]:
    move_file(name, f"pages/projects/{name}")

# Move media assets
for pattern in ("*.jpg", "*.jpeg", "*.png", "*.gif", "*.webp", "*.svg"):
    for file_path in ROOT.glob(pattern):
        target = IMAGES_DIR / file_path.name
        if file_path.exists():
            if target.exists():
                file_path.unlink()
            else:
                shutil.move(str(file_path), str(target))


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, content: str):
    path.write_text(content, encoding="utf-8")


def replace_many(content: str, replacements):
    for old, new in replacements:
        content = content.replace(old, new)
    return content


def update_root_index():
    path = ROOT / "index.html"
    if not path.exists():
        return

    content = read_text(path)

    content = replace_many(content, [
        ('href="style.css"', 'href="assets/css/style.css"'),
        ("href='style.css'", "href='assets/css/style.css'"),
        ('href="yes.css"', 'href="assets/css/yes.css"'),
        ("href='yes.css'", "href='assets/css/yes.css'"),
        ('href="font-awesome.min.css"', 'href="assets/vendor/font-awesome.min.css"'),
        ('href="aboutMe.html"', 'href="pages/about.html"'),
        ('href="projects.html"', 'href="pages/projects/index.html"'),
        ('href="socials.html"', 'href="pages/socials.html"'),
        ('href="gallery.html"', 'href="pages/gallery.html"'),
        ('src="bg.jpg"', 'src="assets/images/bg.jpg"'),
        ('src="script.js"', 'src="assets/js/script.js"'),
        ('href="http://https://mark-eugene-barasu.github.io/food-ecommerce/"', 'href="https://mark-eugene-barasu.github.io/food-ecommerce/"'),
        ('target="_blank" href="socials.html"', 'target="_blank" href="pages/socials.html"'),
    ])

    # Fix invalid body placement inside head
    content = content.replace(
        "    </style>\n    <body class=\"yes-light-grey\">",
        "    </style>\n</head>\n<body class=\"yes-light-grey\">",
    )

    write_text(path, content)


def update_page(path: Path, depth_to_root: str):
    if not path.exists():
        return

    content = read_text(path)

    content = replace_many(content, [
        ('href="font-awesome.min.css"', f'href="{depth_to_root}assets/vendor/font-awesome.min.css"'),
        ("href='font-awesome.min.css'", f"href='{depth_to_root}assets/vendor/font-awesome.min.css'"),
        ('href="style.css"', f'href="{depth_to_root}assets/css/style.css"'),
        ("href='style.css'", f"href='{depth_to_root}assets/css/style.css'"),
        ('href="yes.css"', f'href="{depth_to_root}assets/css/yes.css"'),
        ("href='yes.css'", f"href='{depth_to_root}assets/css/yes.css'"),
        ('src="script.js"', f'src="{depth_to_root}assets/js/script.js"'),
        ("src='script.js'", f"src='{depth_to_root}assets/js/script.js'"),
        ('src="projects.js"', f'src="{depth_to_root}assets/js/projects.js"'),
        ("src='projects.js'", f"src='{depth_to_root}assets/js/projects.js'"),

        ('href="index.html"', f'href="{depth_to_root}index.html"'),
        ("href='index.html'", f"href='{depth_to_root}index.html'"),
        ('href="socials.html"', f'href="{depth_to_root}pages/socials.html"' if depth_to_root == "" else ('href="socials.html"' if depth_to_root == "../../" else f'href="{depth_to_root}socials.html"')),
        ('href="gallery.html"', f'href="{depth_to_root}pages/gallery.html"' if depth_to_root == "" else ('href="gallery.html"' if depth_to_root == "../../" else f'href="{depth_to_root}gallery.html"')),
        ('href="aboutMe.html"', f'href="{depth_to_root}pages/about.html"' if depth_to_root == "" else ('href="about.html"' if depth_to_root == "../../" else f'href="{depth_to_root}about.html"')),
        ('href="projects.html"', f'href="{depth_to_root}pages/projects/index.html"' if depth_to_root == "" else ('href="index.html"' if depth_to_root == "../../" else f'href="{depth_to_root}projects/index.html"')),
    ])

    # Project pages live beside each other in pages/projects/
    if depth_to_root == "../../":
        content = replace_many(content, [
            ('href="about.html"', 'href="../about.html"'),
            ('href="socials.html"', 'href="../socials.html"'),
            ('href="gallery.html"', 'href="../gallery.html"'),
            ('href="projects/index.html"', 'href="index.html"'),
        ])

    # Replace plain media references used in src/href/url()
    image_files = sorted([p.name for p in IMAGES_DIR.iterdir() if p.is_file()])
    for image_name in image_files:
        content = replace_many(content, [
            (f'src="{image_name}"', f'src="{depth_to_root}assets/images/{image_name}"'),
            (f"src='{image_name}'", f"src='{depth_to_root}assets/images/{image_name}'"),
            (f'href="{image_name}"', f'href="{depth_to_root}assets/images/{image_name}"'),
            (f"href='{image_name}'", f"href='{depth_to_root}assets/images/{image_name}'"),
            (f'url("{image_name}")', f'url("{depth_to_root}assets/images/{image_name}")'),
            (f"url('{image_name}')", f"url('{depth_to_root}assets/images/{image_name}')"),
            (f"url({image_name})", f"url({depth_to_root}assets/images/{image_name})"),
        ])

    write_text(path, content)


def rewrite_projects_js():
    path = JS_DIR / "projects.js"
    if not path.exists():
        return

    content = """const footer = document.getElementById("foot01");
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
"""
    write_text(path, content)


def patch_gallery_missing_video():
    path = PAGES_DIR / "gallery.html"
    if not path.exists():
        return

    content = read_text(path)
    if 'src="../assets/images/20210306_152952.mp4"' in content or 'src="20210306_152952.mp4"' in content:
        content = re.sub(
            r'<video style="border: 3px solid #009688;outline: none;border-radius: 5px;" width="90%" controls>\s*<source src="[^"]*20210306_152952\.mp4" type="video/mp4">\s*Your browser does not support HTML5 video\.\s*</video>',
            '<div style="border: 3px solid #009688; border-radius: 5px; width: 90%; margin: 0 auto; padding: 24px; color: white;">Academic awards video is currently unavailable in this repository.</div>',
            content,
            flags=re.S,
        )
    write_text(path, content)


update_root_index()

for path in [
    PAGES_DIR / "about.html",
    PAGES_DIR / "socials.html",
    PAGES_DIR / "gallery.html",
]:
    update_page(path, "../")

for path in PROJECTS_DIR.glob("*.html"):
    update_page(path, "../../")

rewrite_projects_js()
patch_gallery_missing_video()

print("Portfolio structure reorganized successfully.")
