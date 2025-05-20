<p align="center">
  <img src="banner.png" alt="EchoFlowAI Banner" width="100%" />
</p>

<h1 align="center">EchoFlowAI 🎙️</h1>
<p align="center">
  <b>AI-Powered Voice Sales Agent • Twilio + Vocode + Deepgram + GPT-4o + ElevenLabs</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/OpenAI-GPT4o-orange?style=for-the-badge" />
</p>

---

## 🚀 Overview

**EchoFlowAI** is an enterprise-grade AI Voice Agent that conducts real-time, multi-turn sales conversations over the phone using state-of-the-art voice and language technologies.

Built for seamless customer engagement, it combines:
- **Vocode** for real-time voice interactivity
- **Twilio** for telephony
- **Deepgram** for rapid transcription
- **GPT-4o Mini** for intelligent sales dialogue
- **ElevenLabs** for natural, human-like speech synthesis

---

## 🎯 Features

- 🤖 Human-like AI Sales Agent
- 📞 Inbound & Outbound Call Support (Twilio)
- 🧠 Multi-Turn Conversational Memory (GPT-4o)
- 🗣️ Real-Time Transcription (Deepgram)
- 🔊 High-Fidelity TTS (ElevenLabs)
- 📊 Conversation Logging (JSON with Timestamps, Metadata)
- 🧪 7–8 Turn Sample Demo Included

---

## 🧱 Architecture

```mermaid
graph TD
    A[Incoming/Outgoing Call (Twilio)] -->|Voice Signal| B[Vocode Gateway]
    B -->|Audio Stream| C[Deepgram STT]
    C -->|Transcribed Text| D[GPT-4o Mini (Dialogue Engine)]
    D -->|Response Text| E[ElevenLabs TTS]
    E -->|Synthesized Voice| F[Vocode Gateway]
    F -->|Voice Signal| G[Twilio → User]
    D -->|Conversation Data| H[Logger → JSON/Database]
```

## 🛠️ Setup Instructions

### 1. Clone the Repo
```bash
git clone https://github.com/your-username/echoflowai.git
cd echoflowai
```

### 2. Install Dependencies

📝 Logs Example

```json
{
  "call_sid": "CAxxxxxxxxxxxx",
  "start_time": "2025-05-18T12:30:45Z",
  "log": [
    { "timestamp": "12:30:46", "speaker": "user", "text": "Hello, who is this?" },
    { "timestamp": "12:30:48", "speaker": "agent", "text": "Hi! I'm Alex from Jivus AI. How can I help you today?" },
    ...
  ]
}
```

## 📊 Dashboard (Optional UI)
Live Preview — coming soon!

## 📚 Tech Stack
| Component          | Tech Used         |
|---------------------|-------------------|
| Voice Gateway      | Vocode            |
| Telephony          | Twilio            |
| Speech-to-Text     | Deepgram          |
| Dialogue Engine    | OpenAI GPT-4o     |
| Text-to-Speech     | ElevenLabs        |
| Backend Framework  | Python (FastAPI)  |

### 📝 Logs Example
<p align="center"> <img src="https://img.shields.io/badge/Built%20with-Vocode,%20Twilio,%20GPT4o,%20ElevenLabs-blueviolet?style=for-the-badge"/> </p> ```