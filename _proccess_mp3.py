# we will convert and translate the audio mp3 to the json format
import json
import os
from faster_whisper import WhisperModel
# model = whisper.load_model("large-v2").to("cuda")
model = WhisperModel("medium",device="cuda",compute_type="float16")

files = os.listdir("audio")
for file in files:
    title = file.split('.')[0]
    audio = os.path.join("audio",file)
    print(f'result for {file}')
    result,info = model.transcribe(audio,language = "hi",task ="translate",
                              word_timestamps=False,
                              )




# audio = "audio/＊HEATED ＊ MESSI WORLD CUP OR RONALDO 1000 GOALS!.mp3"
# result,info = model.transcribe(audio,language="hi",task="translate",word_timestamps=False)

    chunk_text = ""
    chunk_start = None
    chunks = []
    for segment in result:
        if chunk_start is None:
            chunk_start=segment.start
        chunk_text+=segment.text +" "
        
        if len(chunk_text)>700:
            chunks.append({
            "start":chunk_start,
            "end":segment.end,
            "text":chunk_text.strip()
            })
            # print(segment_json1)
            chunk_text = ""
            chunk_start = None


    if chunk_text:
        chunks.append({
            "start":chunk_start,
            "end":segment.end,
            "text":chunk_text.strip()
        })
    
        #print(segment_json2)


# merged = segment_json1+segment_json2
    chunk_with_metadata = {'chunk':chunks,'text':chunk_text.strip()}
    
    with open(f"jsons/{title}.json", "w") as f:
        json.dump(chunk_with_metadata, f)