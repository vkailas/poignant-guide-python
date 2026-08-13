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
    background: url(../assets/2007-cover-pale.jpg);
    text-align: center;
    font-family: verdana, arial, sans-serif;
    margin: 0; padding: 0;
  }
  a img {
    border: none;
  }
  #cover {
    margin: 0 auto;
    padding: 20px 150px 20px 0px;
    background: url(../assets/2007-cover-spacer.jpg);
    z-index: 1;
    overflow: hidden;
  }
  #cover img {
    margin-bottom: -90px;
  }
  #menu { font-size: 12px; color: gray }
  #menu a { color: #009 }
  #menu p:last-child a { color: inherit }
  #news {
    margin: 0 auto;
    text-align: center;
    font-size: 14px;
    width: 240px;
    padding-left: 500px;
    padding-right: -150px;
    padding-bottom: 20px;
  }
  #news a {
    color: #FF3;
  }
  </style>

  <script>
  function openBook() {
    document.getElementById("cover-image").src = "../assets/2007-cover-open.jpg";
  }
  function shutBook() {
    document.getElementById("cover-image").src = "../assets/2007-cover-shut.jpg";
  }
  </script>

  <div id="cover">
    <a href="../chapter-1/" onmouseover="openBook()" onmouseout="shutBook()"><img id="cover-image" src="../assets/2007-cover-shut.jpg" /></a>
    <div align="right">
      Now for Python
    </div>
  </div>

  <div id="menu">
    <p>
    <strong><a href="../chapter-1">open the book</a></strong>
    &#0164;
    <a href="ttps://poignant.guide/">the Ruby book??</a>
    &#0164;
    <a href="https://poignant.guide/soundtrack/">but the soundtrack??!</a>
    </p>

    <p class=vcard>
    Tenderly written and illustrated by
    <strong rel=author class=fn>Why the Lucky Stiff</strong> and updated for Python.
    <br>
    <a href="https://github.com/mislav/poignant-guide">Source on GitHub</a>
    </p>
  </div>
