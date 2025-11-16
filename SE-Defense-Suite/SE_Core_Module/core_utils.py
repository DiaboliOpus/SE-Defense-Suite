
from colors import *
import time, os, json

def loading(msg):
    print(YELLOW + msg + RESET)
    for i in range(10):
        print("." , end="", flush=True)
        time.sleep(0.1)
    print()

def run_ml(f):
    loading("Running ML Phishing Detector")
    print(GREEN+"ML analysis complete (placeholder)."+RESET)

def run_url(f):
    loading("Running URL Analyzer")
    print(GREEN+"URL scan complete (placeholder)."+RESET)

def run_logs(f):
    loading("Running Log Monitor")
    print(GREEN+"Log analysis complete (placeholder)."+RESET)

def run_sim():
    loading("Running Social Engineering Simulator")
    print(GREEN+"Simulation complete (placeholder)."+RESET)

def run_defense():
    loading("Generating Defense Framework")
    print(GREEN+"Framework generated (placeholder)."+RESET)

def run_pdf():
    loading("Generating PDF Report")
    print(GREEN+"PDF generated (placeholder)."+RESET)
