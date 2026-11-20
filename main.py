from modules.cpu_scheduling import run_cpu_menu
from modules.memory_management import run_memory_menu
from modules.deadlock import run_deadlock_menu
from modules.disk_scheduling import run_disk_menu
from modules.reporting import show_report_menu
from modules.common import pause, print_header, log_activity

def main():
    while True:
        print_header("OS RESOURCE MANAGER")
        print("Integrated Operating System Resource-Management Simulator")
        print("\n1. CPU Process Scheduling")
        print("2. Memory Management")
        print("3. Deadlock Management")
        print("4. Disk Scheduling")
        print("5. Performance Analysis / Reports")
        print("6. Exit")
        choice = input("\nEnter your choice: ").strip()
        try:
            if choice == "1":
                run_cpu_menu()
            elif choice == "2":
                run_memory_menu()
            elif choice == "3":
                run_deadlock_menu()
            elif choice == "4":
                run_disk_menu()
            elif choice == "5":
                show_report_menu()
            elif choice == "6":
                log_activity("Application closed")
                print("\nThank you for using OS Resource Manager.")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 6.")
                pause()
        except (ValueError, IndexError) as exc:
            print(f"Input error: {exc}")
            log_activity(f"Input error: {exc}")
            pause()
        except Exception as exc:
            print(f"Unexpected error: {exc}")
            log_activity(f"Unexpected error: {exc}")
            pause()

if __name__ == "__main__":
    main()
