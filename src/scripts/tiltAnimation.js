import VanillaTilt from "vanilla-tilt";

export default function initTiltAnimation() {
  const canHover = window.matchMedia("(hover: hover) and (pointer: fine)").matches;
  if (!canHover) return;

  const elements = document.querySelectorAll(".js-tilt");
  VanillaTilt.init(elements);
}
