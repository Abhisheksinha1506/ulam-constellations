# ✨ Ulam Constellations (Prime Spiral)

> "Mapping the hidden patterns of prime numbers into a digital galaxy."

### 📢 Latest Status
<!-- LATEST_STATUS_START -->
> The prime search has reached N=1551. Today, 5 new primes (celestial bodies) were discovered and added to the constellation map. The diagonal clusters characteristic of the Ulam Spiral are becoming more visible in the project's grid.
<!-- LATEST_STATUS_END -->

### 📖 The Analogy
Prime numbers (like 2, 3, 5, 7, 11...) are the "atoms" of mathematics. They seem to appear randomly, but if you write numbers in a spiral and mark only the primes, beautiful diagonal lines begin to appear, like constellations in the night sky. This is called the Ulam Spiral.

This repository is building that map, one number at a time. Each "star" (prime number) is represented by a file. Over time, you can see the galaxies of primes forming in the project's directory.

### 🌱 How it Evolves
The map-maker works daily:
1. **Counting Up**: The script checks the next set of numbers from where it [left off](state.json).
2. **Hunting for Primes**: If a number is prime, it calculates its position in the spiral.
3. **Staking a Claim**: A [new file](grid/) is created for every prime discovered.
4. **Drawing the Map**: A visual snapshot is added to the [Spiral Log](spiral-log.md).

**The hunt for primes is fully automated and infinite.**

### 🔍 Quick Links
- [The Spiral Log](spiral-log.md) — Visual snapshots of the prime constellations.
- [The Stars (Primes)](grid/) — Browse the collection of prime number files.
- [Current Progress](state.json) — See how high we've counted so far.
