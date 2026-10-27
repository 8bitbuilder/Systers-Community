"""Open the Systers Member Garden desktop display."""

import json
import random
import tkinter as tk
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MEMBERS_FILE = ROOT / "community" / "members.json"

BG = "#fff7fb"
INK = "#56344d"
FLOWER_COLORS = ["#e8a6c8", "#b9a7e8", "#f5c76b", "#9dcfc0", "#f3a99b"]
DECORATIONS = ["✿", "✦", "❀", "★", "✧", "♡"]


def load_members():
    """Read member names from the shared JSON file."""
    with MEMBERS_FILE.open(encoding="utf-8") as file:
        members = json.load(file)
    return members


def main():
    members = load_members()
    random.seed(8)

    window = tk.Tk()
    window.title("Systers Member Garden")
    window.configure(bg=BG)
    window.geometry("760x560")
    window.minsize(480, 400)

    title = tk.Label(
        window,
        text="🌷 The Systers Garden 🌷",
        font=("Arial", 25, "bold"),
        bg=BG,
        fg=INK,
        pady=12,
    )
    title.pack()

    subtitle = tk.Label(
        window,
        text="A little space for everyone to grow ✨",
        font=("Arial", 12),
        bg=BG,
        fg=INK,
    )
    subtitle.pack(pady=(0, 10))

    garden = tk.Frame(window, bg="#e8f4e8", highlightthickness=2,
                      highlightbackground="#c5dfc9")
    garden.pack(fill="both", expand=True, padx=24, pady=12)

    if not members:
        tk.Label(
            garden,
            text="The garden is waiting for its first member! 🌱",
            font=("Arial", 15),
            bg="#e8f4e8",
            fg=INK,
        ).pack(expand=True)
    
    else:
        # Scatter member cards around the garden
        garden.update_idletasks()
        width = max(garden.winfo_width(), 650)
        height = max(garden.winfo_height(), 350)

        # Randomize the positions each time the app runs
        positions = []
        card_width = 150
        card_height = 90

        for member in members:
            # Try a few positions to reduce overlap
            for attempt in range(50):
                x = random.randint(85, max(85, width - 85))
                y = random.randint(55, max(55, height - 55))

                overlaps = any(
                    abs(x - old_x) < card_width
                    and abs(y - old_y) < card_height
                    for old_x, old_y in positions
                )

                if not overlaps:
                    break

            positions.append((x, y))

            color = random.choice(FLOWER_COLORS)
            decoration = random.choice(DECORATIONS)

            card = tk.Frame(garden, bg="#e8f4e8", padx=5, pady=4)
            card.place(x=x, y=y, anchor="center")

            tk.Label(
                card,
                text=decoration,
                font=("Arial", 27),
                bg="#e8f4e8",
                fg=color,
            ).pack()

            tk.Label(
                card,
                text=member["name"],
                font=("Arial", 11, "bold"),
                bg=color,
                fg=INK,
                padx=10,
                pady=5,
                wraplength=card_width,
            ).pack()


    footer = tk.Label(
        window,
        text=f"{len(members)} member{'s' if len(members) != 1 else ''} and growing 💜",
        font=("Arial", 11),
        bg=BG,
        fg=INK,
        pady=8,
    )
    footer.pack()

    window.mainloop()


if __name__ == "__main__":
    main()
