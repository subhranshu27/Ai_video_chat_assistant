from sarvamai import SarvamAI

client = SarvamAI(
    api_subscription_key="sk_bpjelsgg_xblPNnZyV39R4KlNSPHN7OlQ",
)

with open("downloads/Sailendra Mashup_converted.wav", "rb") as f:
    response = client.speech_to_text.transcribe(
        file=f,
        model="saaras:v4",
        language_code="en-IN",
        mode="transcribe",
        
    )

print(response.transcript)









#     st.markdown("""
#     <style>
#     .chat-container { background: #ffffff; border-radius: 12px; padding: 1rem; }
#     .chat-msg { display:flex; flex-direction:column; margin-bottom:0.9rem; }
#     .chat-label { font-size:0.72rem; font-weight:700; margin-bottom:0.25rem; opacity:0.75; }
#     .user-label { color:#7c3aed; }
#     .bot-label { color:#0891b2; }
#     .chat-bubble { padding:0.6rem 0.9rem; border-radius:14px; max-width:75%; font-size:0.9rem; line-height:1.5; }
#     .user-bubble { background:#f3e8ff; color:#3b0764; border:1px solid #d8b4fe; }
#     .bot-bubble { background:#e0f7fa; color:#083344; border:1px solid #a5f3fc; }
#     .card { background:#ffffff; border:1px solid #f0f0f0; border-radius:12px; }
#     .badge { padding:0.3rem 0.8rem; border-radius:999px; font-size:0.75rem; font-weight:600; }
#     .badge-purple { background:#f3e8ff; color:#7c3aed; }
#     .badge-cyan { background:#cffafe; color:#0891b2; }
#     .badge-green { background:#dcfce7; color:#16a34a; }
#     </style>
#     """, unsafe_allow_html=True)

#     st.markdown('<div style="font-family:\'Syne\',sans-serif;font-size:1.2rem;font-weight:700;margin-bottom:1rem;color:#111827">💬 Chat with your Meeting</div>', unsafe_allow_html=True)

#     # Chat history display
#     if st.session_state.chat_history:
#         chat_html = '<div class="chat-container">'
#         for msg in st.session_state.chat_history:
#             if msg["role"] == "user":
#                 chat_html += f"""
#                 <div class="chat-msg" style="align-items:flex-end">
#                     <span class="chat-label user-label">You</span>
#                     <div class="chat-bubble user-bubble">{msg['content']}</div>
#                 </div>"""
#             else:
#                 chat_html += f"""
#                 <div class="chat-msg" style="align-items:flex-start">
#                     <span class="chat-label bot-label">🤖 Assistant</span>
#                     <div class="chat-bubble bot-bubble">{msg['content']}</div>
#                 </div>"""
#         chat_html += '</div>'
#         st.markdown(chat_html, unsafe_allow_html=True)
#     else:
#         st.markdown("""
#         <div class="card" style="text-align:center;padding:2rem">
#             <div style="font-size:2rem;margin-bottom:0.5rem">💬</div>
#             <div style="color:#6b7280;font-size:0.85rem">Ask anything about your meeting transcript</div>
#         </div>""", unsafe_allow_html=True)

#     # Chat input
#     chat_col1, chat_col2 = st.columns([5, 1], gap="small")
#     with chat_col1:
#         user_input = st.text_input("Your question", placeholder="What were the main decisions made?", label_visibility="collapsed")
#     with chat_col2:
#         send_btn = st.button("Send →", use_container_width=True)

#     if send_btn and user_input.strip():
#         with st.spinner("Thinking…"):
#             answer = ask_question(r["rag_chain"], user_input.strip())
#         st.session_state.chat_history.append({"role": "user",      "content": user_input.strip()})
#         st.session_state.chat_history.append({"role": "assistant", "content": answer})
#         st.rerun()

#     if st.session_state.chat_history:
#         if st.button("🗑️ Clear Chat", type="secondary"):
#             st.session_state.chat_history = []
#             st.rerun()

# else:
#     # Empty state
#     st.markdown("""
#     <div style="display:flex;flex-direction:column;align-items:center;justify-content:center;padding:5rem 2rem;text-align:center">
#         <div style="font-size:4rem;margin-bottom:1rem">🎬</div>
#         <div style="font-family:'Syne',sans-serif;font-size:1.5rem;font-weight:700;color:#111827;margin-bottom:0.5rem">
#             Ready to Analyse
#         </div>
#         <div style="color:#6b7280;font-size:0.85rem;max-width:380px;line-height:1.7">
#             Paste a YouTube URL or local file path in the sidebar, choose your language, and hit <strong>Analyse</strong> to get started.
#         </div>
#         <div style="margin-top:2rem;display:flex;gap:1rem;flex-wrap:wrap;justify-content:center">
#             <span class="badge badge-purple">Transcription</span>
#             <span class="badge badge-cyan">Summarisation</span>
#             <span class="badge badge-green">RAG Chat</span>
#         </div>
#     </div>""", unsafe_allow_html=True)