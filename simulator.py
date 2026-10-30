from __future__ import annotations

import csv
import math
import random
import threading
import time
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path


BASE_LAT = 17.385044
BASE_LON = 78.486671
DEFAULT_INTERVAL_SECONDS = 1.0
MISSION_POINTS = 48
DATA_DIR = Path(__file__).resolve().parent / "data"
CSV_PATH = DATA_DIR / "air_quality_data.csv"


@dataclass
class Reading:
    step: int
    timestamp: str
    latitude: float
    longitude: float
    altitude_m: float
    speed_mps: float
    pm25: int
    pm10: int
    co2: int
    temperature_c: float
    humidity_pct: float
    gas_index: int
    aqi_label: str
    alert: bool


class DroneMissionSimulator:
    def __init__(self) -> None:
        DATA_DIR.mkdir(exist_ok=True)
        self._lock = threading.Lock()
        self._thread: threading.Thread | None = None
        self._running = False
        self._interval_seconds = DEFAULT_INTERVAL_SECONDS
        self._route = self._build_route()
        self._step_index = 0
        self._history: list[Reading] = []
        self._write_csv_header()

    def _build_route(self) -> list[tuple[float, float]]:
        route = []
        for index in range(MISSION_POINTS):
            angle = (2 * math.pi * index) / MISSION_POINTS
            lat = BASE_LAT + 0.0040 * math.sin(angle)
            lon = BASE_LON + 0.0060 * math.cos(angle)
            route.append((round(lat, 6), round(lon, 6)))
        return route

    def _write_csv_header(self) -> None:
        with CSV_PATH.open("w", newline="", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(
                [
                    "step",
                    "timestamp",
                    "latitude",
                    "longitude",
                    "altitude_m",
                    "speed_mps",
                    "pm25",
                    "pm10",
                    "co2",
                    "temperature_c",
                    "humidity_pct",
                    "gas_index",
                    "aqi_label",
                    "alert",
                ]
            )

    def _append_csv_row(self, reading: Reading) -> None:
        with CSV_PATH.open("a", newline="", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(
                [
                    reading.step,
                    reading.timestamp,
                    reading.latitude,
                    reading.longitude,
                    reading.altitude_m,
                    reading.speed_mps,
                    reading.pm25,
                    reading.pm10,
                    reading.co2,
                    reading.temperature_c,
                    reading.humidity_pct,
                    reading.gas_index,
                    reading.aqi_label,
                    reading.alert,
                ]
            )

    def _aqi_label(self, pm25: int) -> str:
        if pm25 <= 30:
            return "Good"
        if pm25 <= 60:
            return "Moderate"
        if pm25 <= 90:
            return "Unhealthy for Sensitive Groups"
        return "Poor"

    def _generate_reading(self, step: int) -> Reading:
        latitude, longitude = self._route[step % len(self._route)]
        wave = math.sin(step / 4)
        hotspot = math.exp(-((step - 18) ** 2) / 85)

        pm25 = max(18, int(28 + 18 * wave + 55 * hotspot + random.randint(-5, 5)))
        pm10 = max(pm25 + 8, int(pm25 * 1.55 + random.randint(-8, 12)))
        co2 = max(380, int(430 + 35 * wave + 220 * hotspot + random.randint(-20, 20)))
        temperature_c = round(28 + 2.3 * math.sin(step / 6) + random.uniform(-0.4, 0.4), 1)
        humidity_pct = round(56 - 6 * math.sin(step / 7) + random.uniform(-1.5, 1.5), 1)
        gas_index = max(80, int(120 + pm25 * 0.9 + random.randint(-12, 12)))
        altitude_m = round(18 + 5 * math.sin(step / 5), 1)
        speed_mps = round(4.5 + 0.8 * math.cos(step / 6), 1)

        aqi_label = self._aqi_label(pm25)
        alert = pm25 >= 80 or co2 >= 750

        return Reading(
            step=step + 1,
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            latitude=latitude,
            longitude=longitude,
            altitude_m=altitude_m,
            speed_mps=speed_mps,
            pm25=pm25,
            pm10=pm10,
            co2=co2,
            temperature_c=temperature_c,
            humidity_pct=humidity_pct,
            gas_index=gas_index,
            aqi_label=aqi_label,
            alert=alert,
        )

    def _run_loop(self) -> None:
        while self._running:
            with self._lock:
                reading = self._generate_reading(self._step_index)
                self._history.append(reading)
                self._append_csv_row(reading)
                self._step_index = (self._step_index + 1) % len(self._route)
            time.sleep(self._interval_seconds)

    def start(self, interval_seconds: float | None = None) -> None:
        with self._lock:
            if interval_seconds is not None:
                self._interval_seconds = max(0.5, float(interval_seconds))
            if self._running:
                return
            self._running = True

        self._thread = threading.Thread(target=self._run_loop, daemon=True)
        self._thread.start()

    def stop(self) -> None:
        self._running = False
        if self._thread and self._thread.is_alive():
            self._thread.join(timeout=1.5)

    def reset(self) -> None:
        self.stop()
        with self._lock:
            self._step_index = 0
            self._history.clear()
            self._interval_seconds = DEFAULT_INTERVAL_SECONDS
            self._write_csv_header()

    def get_history(self) -> list[dict]:
        with self._lock:
            return [asdict(item) for item in self._history]

    def get_state(self) -> dict:
        with self._lock:
            current = asdict(self._history[-1]) if self._history else None
            alerts = [asdict(item) for item in self._history if item.alert][-5:]
            return {
                "running": self._running,
                "interval_seconds": self._interval_seconds,
                "mission_points": len(self._route),
                "completed_points": len(self._history),
                "current": current,
                "history": [asdict(item) for item in self._history],
                "recent_alerts": alerts,
                "csv_path": str(CSV_PATH),
            }
