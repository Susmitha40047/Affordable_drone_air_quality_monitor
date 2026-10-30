from __future__ import annotations

from flask import Flask, jsonify, render_template, request

from simulator import DroneMissionSimulator


app = Flask(__name__)
simulator = DroneMissionSimulator()


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/api/state")
def api_state():
    return jsonify(simulator.get_state())


@app.get("/api/history")
def api_history():
    return jsonify({"history": simulator.get_history()})


@app.post("/api/mission/start")
def start_mission():
    payload = request.get_json(silent=True) or {}
    interval = payload.get("interval_seconds")
    simulator.start(interval_seconds=interval)
    return jsonify(
        {
            "message": "Mission simulation started",
            "state": simulator.get_state(),
        }
    )


@app.post("/api/mission/stop")
def stop_mission():
    simulator.stop()
    return jsonify(
        {
            "message": "Mission simulation stopped",
            "state": simulator.get_state(),
        }
    )


@app.post("/api/mission/reset")
def reset_mission():
    simulator.reset()
    return jsonify(
        {
            "message": "Mission simulation reset",
            "state": simulator.get_state(),
        }
    )


if __name__ == "__main__":
    app.run(debug=True)
