export default function initScrollReveal(targetElements, defaultProps) {
  if (!targetElements.length) return;

  // Sideways motion clips text once the layout stacks.
  const compact = window.matchMedia("(max-width: 991px)").matches;

  ScrollReveal({ reset: false });

  targetElements.forEach(({ element, animation }) => {
    const resolved = Object.assign({}, animation);
    if (compact && resolved.origin && resolved.origin !== "bottom") {
      resolved.origin = "bottom";
      resolved.distance = "16px";
    }
    ScrollReveal().reveal(element, Object.assign({}, defaultProps, resolved));
  });
}
