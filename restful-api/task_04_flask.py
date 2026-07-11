#!/usr/bin/python3
"""A simple API built using Flask."""

from flask import Flask, jsonify, request


app = Flask(__name__)

users = {}


@app.route("/", methods=["GET"])
def home():
    """Return the welcome message."""
    return "Welcome to the Flask API!"


@app.route("/data", methods=["GET"])
def get_data():
    """Return a list containing all stored usernames."""
    return jsonify(list(users.keys()))


@app.route("/status", methods=["GET"])
def status():
    """Return the current API status."""
    return "OK"


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """Return the user associated with the supplied username."""
    if username not in users:
        return jsonify({"error": "User not found"}), 404

    return jsonify(users[username])


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user to the in-memory users dictionary."""
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = data

    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201


if __name__ == "__main__":
    app.run()
