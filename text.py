from core.transcriber import transcribe_all
from utils.audio_processor import process_input
from core.summarizer import get_summary,generate_title
from core.extractor import extract_action_items,extract_key_decisions,extract_questions
from dotenv import load_dotenv
load_dotenv()


data="https://youtu.be/UabBYexBD4k"
lang="english"


chunks=process_input(data)
transcript = transcribe_all(chunks, language=lang)
print("\n" + "=" * 60)
print("📝 TRANSCRIPT")
print("=" * 60)
print(transcript[:500] + "..." if len(transcript) > 500 else transcript)

title=generate_title(transcript)
summary=get_summary(transcript)


print("\n" + "=" * 60)
print(f"📌 TITLE: {title}")
print("=" * 60)
print("\n📋 SUMMARY")
print("-" * 60)
print(summary)

action_items=extract_action_items(transcript)
decisions=extract_key_decisions(transcript)
questions=extract_questions(transcript)


print("\n" + "=" * 60)
print("✅ ACTION ITEMS")
print("=" * 60)
print(action_items)

print("\n" + "=" * 60)
print("🔑 KEY DECISIONS")
print("=" * 60)
print(decisions)

print("\n" + "=" * 60)
print("❓ OPEN QUESTIONS")
print("=" * 60)
print(questions)