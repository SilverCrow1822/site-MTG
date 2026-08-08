// Gera um campo de estrelas leve usando box-shadow em vez de centenas de
// elementos DOM — cada camada (.stars, .stars2, .stars3) simula uma
// profundidade diferente da nebulosa, criando um efeito parallax sutil.

(function () {
    function randomShadows(count, maxWidth, maxHeight) {
        const shadows = [];
        for (let i = 0; i < count; i++) {
            const x = Math.floor(Math.random() * maxWidth);
            const y = Math.floor(Math.random() * maxHeight);
            shadows.push(`${x}px ${y}px #fff`);
        }
        return shadows.join(", ");
    }

    function buildStarLayer(selector, count, size) {
        const el = document.querySelector(selector);
        if (!el) return;

        const width = Math.max(document.documentElement.scrollWidth, window.innerWidth);
        const height = Math.max(document.documentElement.scrollHeight, window.innerHeight) + 1200;

        const shadowValue = randomShadows(count, width, height);
        el.style.width = size + "px";
        el.style.height = size + "px";
        el.style.background = "transparent";
        el.style.borderRadius = "50%";
        el.style.boxShadow = shadowValue;
    }

    function init() {
        buildStarLayer(".stars", 140, 1);
        buildStarLayer(".stars2", 90, 2);
        buildStarLayer(".stars3", 60, 3);
    }

    document.addEventListener("DOMContentLoaded", init);
    window.addEventListener("resize", () => {
        clearTimeout(window.__starResizeTimer);
        window.__starResizeTimer = setTimeout(init, 250);
    });
})();
