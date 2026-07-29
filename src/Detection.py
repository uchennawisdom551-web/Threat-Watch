import json
from pydroid1 import woo


def show_suspicious():

    Variable = woo()
    failed_attempts = {}
    report_data = []

    # Count failed attempts
    for event in Variable:
        status = event["Status"]

        if "FAILED" in status:
            ip = event["Ip"]

            if ip in failed_attempts:
                failed_attempts[ip] += 1
            else:
                failed_attempts[ip] = 1

    # Menu
    while True:

        print()
        print("======= ThreatWatch =========")
        print("1. Show Risk Level")
        print("2. Show Threat Report")
        print("3. Exit")

        choice = int(input("Enter a Number: "))

        if choice == 3:
            break

        # Build JSON report
        report_data = []

        for ip, failures in failed_attempts.items():

            if failures >= 3:
                severity = "High"
                threat = "Possible Brute Force Attack"
            else:
                severity = "Low"
                threat = "Negligible"

            report = {
                "Ip": ip,
                "Failed_Attempts": failures,
                "Severity": severity,
                "Threat": threat
            }

            report_data.append(report)

        with open("../reports/threat_report.json", "w") as file:
            json.dump(report_data, file, indent=4)

        if choice == 1:

            for ip, failures in failed_attempts.items():

                if failures >= 3:
                    print("=" * 40)
                    print("THREAT DETECTED!\n")
                    print(f"IP Address       : {ip}")
                    print(f"Failed Attempts  : {failures}")
                    print("Severity         : High")
                    print("Threat           : Possible Brute Force Attack")
                    print("=" * 40)

                else:
                    print("=" * 40)
                    print("SUSPICIOUS\n")
                    print(f"IP Address       : {ip}")
                    print(f"Failed Attempts  : {failures}")
                    print("Threat           : Negligible")
                    print("=" * 40)

        elif choice == 2:

            critical = 0
            high = 0
            low = 0

            for ip, failures in failed_attempts.items():

                if failures >= 6:
                    critical += 1
                elif failures == 3:
                    high += 1
                else:
                    low += 1

            print("======= Threat-Watch Alert Report =======\n")
            print(f"Suspicious IPs : {low}")
            print(f"Medium Threats : {high}")
            print(f"High Threats   : {critical}")


show_suspicious()
