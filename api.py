from flask import Flask, request, Response
import edge_tts

app = Flask(__name__)

@app.route('/tts', methods=['GET'])
async def tts():
    text = request.args.get('text')
    voice = request.args.get('voice')
    result = []
    communicate = edge_tts.Communicate(text, voice)
    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            result.append(chunk["data"])

    return Response(b''.join(result), mimetype="audio/mpeg")

if __name__ == "__main__":
    app.run()
