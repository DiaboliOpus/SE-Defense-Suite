
import argparse, time, json, os, sys
from core_utils import run_ml, run_url, run_logs, run_sim, run_defense, run_pdf
from colors import *

def menu():
    print(BLUE + "\n=====================================================")
    print("   S E   D E F E N S E   S U I T E  -  C O R E")
    print("=====================================================" + RESET)
    print(GREEN + "1) ML Phishing Detector")
    print("2) URL Analyzer")
    print("3) Log Monitor")
    print("4) Social Engineering Simulator")
    print("5) Defense Framework Generator")
    print("6) PDF Report Generator")
    print("7) Exit" + RESET)
    return input("\nSelect an option: ")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--module", type=str)
    parser.add_argument("--file", type=str)
    args = parser.parse_args()

    if args.module:
        if args.module=="ml": run_ml(args.file)
        elif args.module=="url": run_url(args.file)
        elif args.module=="logs": run_logs(args.file)
        elif args.module=="sim": run_sim()
        elif args.module=="defense": run_defense()
        elif args.module=="pdf": run_pdf()
        else: print(RED+"Unknown module"+RESET)
        sys.exit()

    while True:
        choice = menu()
        if choice=="1": run_ml(None)
        elif choice=="2": run_url(None)
        elif choice=="3": run_logs(None)
        elif choice=="4": run_sim()
        elif choice=="5": run_defense()
        elif choice=="6": run_pdf()
        elif choice=="7":
            print(YELLOW+"Exiting..."+RESET)
            break
        else:
            print(RED+"Invalid option"+RESET)

if __name__=="__main__":
    main()
