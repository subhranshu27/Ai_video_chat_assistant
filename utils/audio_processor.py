import yt_dlp
from pydub import AudioSegment
import os


Download_dir='downloads'
os.makedirs(Download_dir,exist_ok=True)
def download_youtube_audio(url :str) ->str:
    output_path = os.path.join(Download_dir, "%(title)s.%(ext)s")
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": output_path,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "wav",
                "preferredquality": "192",
            }
        ],
        "quiet": True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info).replace(".webm", ".wav").replace(".m4a", ".wav")
    return filename





def convert_to_wav(input_path: str) -> str:
    """Convert any audio/video file to WAV format using pydub."""
    output_path = os.path.splitext(input_path)[0] + "_converted.wav"
    audio = AudioSegment.from_file(input_path)
    audio = audio.set_channels(1).set_frame_rate(16000) #16khz
    audio.export(output_path, format="wav")
    return output_path





def chunk_audio(path:str,chunk_min:int=10) ->list:
    audio =AudioSegment.from_wav(path)
    chunk_ms= chunk_min *60 *1000

    chunks =[]
    for i,start in enumerate(range(0,len(audio),chunk_ms)):
        chunk= audio[start:start+chunk_ms]
        chunk_path=f"{path}_chunk_{i}.wav"
        chunk.export(chunk_path,format="wav")

        chunks.append(chunk_path)

    return chunks

def process_input(source:str)-> list:
    if source.startswith("http://")  or source.startswith("https://"):
        print("Youtube video detected and downloading ...")
        vid=download_youtube_audio(source)
        wav_path=convert_to_wav(vid)


    else:
        print("local file detected")
        wav_path=convert_to_wav(source)

    print('chunking the audio')
    chunks=chunk_audio(wav_path)
    print(f"{len(chunks)} chunks are created")
    return chunks

