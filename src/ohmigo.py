import serial


class Ohmigo:
    def __init__(self, device):
        self.ser = serial.Serial(device, timeout=1)

    def __del__(self):
        self.ser.close()

    def response(self):
        s = None
        r = []
        while s != b"":
            s = self.ser.read(128)
            r.append(s.decode("utf-8").strip())

        return r[:1]

    def write(self, str):
        self.ser.write(str.encode("utf-8") + b"\n")

    def atr(self, r):
        self.write(f"ATR={r:.2f},ACK")
        res = self.response()
        if res[0].split(",")[1] == "OK":
            return True
        print(f"E: {res}", flush=True)
        return False
