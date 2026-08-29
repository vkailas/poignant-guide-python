---
hide:
  - navigation
  - toc
  - footer
---

# Welcome to Poignant Guide to Python

<style type="text/css">
body {
  color: white;
  background: url(assets/2007-cover-pale.jpg);
  text-align: center;
  font-family: verdana, arial, sans-serif;
  margin: 0;
  padding: 0;
}
a img {
  border: none;
}
#cover {
  margin: 0 auto;
  /* Replaced rigid 150px padding with fluid percentage bounds */
  padding: 20px 5% 20px 5%; 
  background: url(assets/2007-cover-spacer.jpg);
  z-index: 1;
  overflow: hidden;
  max-width: 648px; /* Ensures container never exceeds natural image size */
}
#cover img {
  margin-bottom: -90px;
  /* Added rules to scale down image smoothly on mobile */
  max-width: 100%;
  height: auto;
}
#menu {
  font-size: 12px;
  color: gray;
  padding: 10px;
}
#menu a {
  color: #009;
}
#menu p:last-child a {
  color: inherit;
}
#news {
  margin: 0 auto;
  text-align: center;
  font-size: 14px;
  width: 100%;
  max-width: 240px;
  padding-bottom: 20px;
}
#news a {
  color: #FF3;
}
</style>

<script>
function openBook() {
  document.getElementById("cover-image").src = "assets/2007-cover-open.jpg";
}
function shutBook() {
  document.getElementById("cover-image").src = "assets/2007-cover-shut.jpg";
}
</script>

<div id="cover" markdown="1">
[![Cover Image](assets/2007-cover-shut.jpg){: id="cover-image" onmouseover="openBook()" onmouseout="shutBook()" }](chapter-1.md)
<div align="right">
Now for Python
</div>
</div>

<div id="menu">
<p>
<strong><a href="chapter-1">open the book</a></strong> ¤ <a href="https://poignant.guide/">the Ruby book??</a> ¤ <a href="https://poignant.guide/soundtrack/">but the soundtrack??!</a>
</p>
<p class=vcard>
Tenderly written and illustrated by <strong rel=author class=fn>Why the Lucky Stiff</strong> and updated for Python.
<br>
<a href="https://github.com/vkailas/poignant-guide-python">Source on GitHub</a>
</p>
</div>