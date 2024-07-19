import time

def pomodoro_timer(study_time, break_time):
    while True:
        print(f"Study for {study_time} minutes.")
        time.sleep(study_time * 60)
        print("Break time!")
        time.sleep(break_time * 60)

def main():
    mode = input("Select mode: 1) 25 min study and 5 min break 2) 50 min study and 10 min break: ")
    if mode == '1':
        pomodoro_timer(25, 5)
    elif mode == '2':
        pomodoro_timer(50, 10)
    else:
        print("Invalid mode selected.")

if __name__ == "__main__":
    main()
