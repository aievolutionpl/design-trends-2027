# Three additional visual directions

These are editorial additions, not claims from the video. They are grounded in existing platform or technical examples, not proof of future market dominance. See [sources](sources.md).

## 8. Dynamic materials and controlled transparency
**Why include:** Apple's Liquid Glass demonstrates an adaptive translucent interface material; one platform example does not establish a web-wide trend.
**Look:** subtle translucent floating navigation, restrained highlights, depth and a foreground surface that remains distinct over changing content. Use solid surfaces for primary reading areas.
**Use:** navigation or floating controls where layering clarifies spatial hierarchy; avoid where dense content needs stable contrast.
**Implement:** start with an opaque surface; progressively enhance with CSS `backdrop-filter` where supported, add a tint and border, and provide a solid alternative. Check light, dark and moving backgrounds, contrast, rendering cost and keyboard focus.
**Avoid:** stacking blur on every card or copying a platform's aesthetic when it conflicts with brand and readability.

## 9. Expressive geometry and brand-led UI
**Why include:** Google's Material 3 Expressive describes the use of color, shape, scale and movement in a design system; its producer-reported studies do not prove arbitrary expressive design performs better.
**Look:** two or three distinctive rules for silhouette, proportion and accent color; differentiate primary actions without turning every control into a unique shape.
**Use:** brand-led websites, onboarding and selected dashboard navigation, especially when a neutral competitor set makes recognition difficult.
**Implement:** define shape, spacing and semantic color tokens, then apply consistently to buttons, cards and states. Preserve native semantics, labels, focus visibility and adequate touch targets; compare task completion with a restrained alternative.
**Avoid:** novelty shapes that look clickable but aren't, color-only state indicators, or abandoning familiar controls.

## 10. Motion as information and narrative
**Why include:** existing CSS scroll-driven animations and reduced-motion media preferences make this an implementable visual behavior; support varies and adoption is not measured here.
**Look:** purposeful transitions that orient, acknowledge an action or reveal a narrative. Use one motion vocabulary and let static composition carry the message.
**Use:** state changes, editorial storytelling, transitions between steps—not essential content hidden behind scrolling.
**Implement:** establish a complete static baseline; use progressive enhancement and feature detection for scroll-linked effects. Respect `prefers-reduced-motion`, offer an equivalent static outcome, and test keyboard, browser support and lower-powered devices.
**Avoid:** continuous decorative motion, scroll hijacking and motion required to understand or access content.
