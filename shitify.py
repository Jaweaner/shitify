import os
import time
import subprocess
from flask import Flask, jsonify, send_from_directory, render_template

app = Flask(__name__)

SONG_DIR = os.path.join(os.path.dirname(__file__), 'songs')

def open_brave_app():
    time.sleep(1)
    subprocess.Popen([
        'brave',
        '--new-window',
        '--app=http://127.0.0.1:8696',
        '--window-size=240,800',
        '--disable-features=TranslateUI'
    ])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/songs_list')
def songs_list():
    files = [f for f in os.listdir(SONG_DIR) if f.lower().endswith('.mp3')]
    return jsonify(sorted(files))

@app.route('/songs/<path:filename>')
def serve_song(filename):
    return send_from_directory(SONG_DIR, filename)

if __name__ == '__main__':
    # Open Brave app after server starts (non-blocking)
    from threading import Thread
    Thread(target=open_brave_app).start()

    # Run Flask
    app.run(port=8696, host='127.0.0.1', debug=False, use_reloader=False)
