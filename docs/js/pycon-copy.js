document$.subscribe(function () {
  document.querySelectorAll(".language-pycon").forEach(function (block) {
    const code = block.querySelector("code");
    const button = block.querySelector("[data-clipboard-target]");

    if (!code || !button) {
      return;
    }

    const clone = code.cloneNode(true);

    // Remove the >>> prompt.
    clone.querySelectorAll(".gp").forEach(function (element) {
      element.remove();
    });

    // Remove Python REPL output (.go).
    clone.querySelectorAll(".go").forEach(function (element) {
      element.remove();
    });

    button.setAttribute(
      "data-clipboard-text",
      clone.textContent.trim()
    );

    // data-clipboard-target takes precedence.
    button.removeAttribute("data-clipboard-target");
  });
});