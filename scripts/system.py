import tools as to
import time
import json
import os

candidates = to.load_data()

to.clear_screen()
to.write_menu("-- ELECTIONS 2026 --", skip_line=False)
time.sleep(0.4)
to.write_slow(" By @dlv.gonzalezz")

to.write_slow("\n⚠️  NOTICE: This project is currently under development. In the future, "
"this system will be updated to allow voting by candidate number.")

time.sleep(1.5)
print("=" * 10)

input("Press ENTER to continue:")
print("Starting...")
time.sleep(0.6)
to.clear_screen()

available_votes = 1

while True:
    if available_votes <= 0:
        print("\n=== VOTING CLOSED (Vote limit reached) ===")
        for t, c in enumerate(candidates, start=1):
            print(f"{t} - {c['candidate']:<14} | Number of votes: {c['votes']}")
        to.exit_program()
        break

    print(f"\n== HOME SCREEN == {to.show_time()} - Brasília Time")

    try:
        menu = int(input("\n1 - Vote \n2 - Exit \n - CHOOSE AN OPTION: ").strip())
        to.clear_screen()

        if menu == 1:
            while True:
                print("\n-- Candidate Options --")
                for t, c in enumerate(candidates, start=1):
                    print(f"{t} - {c['candidate']:<14} | Number of votes: {c['votes']}")
                print("=" * 10)

                vote_option = input("Enter the candidate's NAME: ").strip().upper()
                found = False

                for c in candidates:
                    if vote_option == c['candidate']:
                        c['votes'] += 1
                        available_votes -= 1
                        found = True

                        to.save_data(candidates)

                        print("\nVote successfully cast and recorded.")
                        time.sleep(1)
                        to.clear_screen()
                        break

                if found:
                    break

                print("\n[ERROR] Invalid name. Please try again.")
                time.sleep(2)
                to.clear_screen()

        elif menu == 2:
            to.exit_program()
            break

        else:
            print("[ERROR] Please enter a valid option (1 or 2).")
            time.sleep(1)
            to.clear_screen()

    except ValueError:
        print("[ERROR] Invalid input. Please enter an integer.")
        time.sleep(1)
        to.clear_screen()
