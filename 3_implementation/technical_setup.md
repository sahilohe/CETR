# Technical Setup: The Offline-First Learning Environment

To practice CETR effectively, we must solve the **Digital Distraction Crisis.** Traditional internet is optimized for engagement (passive consumption), while CETR requires deep focus (active creation).

---

## 1. The "CETR Box" (Portable Knowledge Server)
We recommend setting up a local server (Mini-PC or Raspberry Pi) that provides a "Safe Harbor" for learning without internet access.

### Core Components:
1.  **Kiwix (The Encyclopedia):**
    *   Wikipedia (Full copy, ~90GB)
    *   Khan Academy (Full courses)
    *   Project Gutenberg (70,000+ books)
2.  **Curated Video Library:**
    *   Download YouTube channels like *3Blue1Brown*, *Kurzgesagt*, and *Veritasium* using `yt-dlp`.
    *   Serve them locally so there are no algorithms, ads, or "Recommended" sidebars.
3.  **Local Socratic AI:**
    *   Use **Ollama** to run a local LLM (like Llama 3 or Mistral).
    *   **The Socratic Prompt:** Program the AI to never give direct answers. It must only ask questions that push the child to conjecture and refine.

---

## 2. Why Offline-First?

| Traditional Internet | CETR Digital Library |
| :--- | :--- |
| Infinite feeds (Distraction) | Finite, curated content (Focus) |
| Algorithmic recommendations | Intentional browsing |
| Passive consumption | Active exploration |
| Ads and Tracking | Total Privacy |

---

## 3. Integration with Edventures Studio (ES)

### The "Conjecture Pitch"
In the Maker Studio, every project starts with a 5-minute pitch. 
*   *Before:* "I'm building a bridge." 
*   *After:* "My **Conjecture** is that this triangle structure will support 5kg because [Explanation]."

### Friday Adventures as "Epistemic Expeditions"
Before any field trip, children use the **CETR Box** to form a theory about what they will see.
*   *Action:* During the trip, their goal is to find evidence that **refutes** their theory. 
*   *Example:* "If these stilts are only for floods, why are they so high in the dry season?"

### The Refinement Fair
Replace "Show and Tell" with a session where children present their **most interesting failure**. They explain the test that refuted their initial conjecture and how they **Refined** their theory.

---

## 4. Hardware Recommendations
*   **The Server:** Raspberry Pi 5 (8GB) or a used Intel NUC.
*   **Storage:** 2TB External SSD (to hold Wikipedia and Video Archives).
*   **Software:** Kiwix-Serve, Ollama, Docker.

**The goal of the tech is to get out of the way of the thinking.**
