import csv
from datetime import datetime

class SaveData:
    def txt_file(self, result):
        with open(f"result_{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.txt", "w") as f:
            f.write(",".join(str(port) for port in result))

    def csv_file(self, result):
        with open(f"result_{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(result)

    def html_file(self, result):
        with open(f"result_{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.html", "w") as f:
            f.write("<html><head><title>Open ports</title></head><body><table><tr>")
            f.write("".join(f"<td>{port}</td>" for port in result))
            f.write("</tr></table></body></html>")