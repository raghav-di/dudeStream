🎥 DudeStream – Real-Time Video Streaming Web App

DudeStream is a real-time video streaming and collaboration web application built using WebRTC, Django Channels, and Firebase Authentication.
It allows users to securely log in, create or join rooms, and stream video directly between peers with low latency.

🚀 Features

🔐 Authentication

Email & Password login

Google Sign-In

Persistent login state using Firebase Auth

🎬 Real-Time Video Streaming

Peer-to-peer video streaming using WebRTC

Low-latency media transmission

🧑‍🤝‍🧑 Room System

Create rooms with unique room codes

Join existing rooms

Role-based streaming (Streamer ↔ Viewer)

🔄 WebSocket Signaling

Real-time signaling using Django Channels

Exchange of SDP offers/answers and ICE candidates

🌐 Deployment

Hosted on Render (free plan)

Publicly accessible for testing and demos

🧠 Tech Stack
Frontend

HTML, CSS, JavaScript

WebRTC APIs

Firebase Authentication (Web SDK)

Backend

Django

Django Channels (WebSockets)

ASGI server

Real-Time Communication

WebRTC (Audio/Video + DataChannels)

STUN (Google STUN server)

TURN (planned / future enhancement)

Authentication

Firebase Auth (Google & Email/Password)

🔁 Application Flow (High-Level)
1️⃣ User Authentication

Users log in or register using Firebase Authentication.

Firebase manages session persistence.

Login state is reflected instantly in the UI.

2️⃣ Room Creation / Joining

Logged-in users can:

Create a new room

Join an existing room using a room code

Each room corresponds to a WebSocket group in Django Channels.

3️⃣ Signaling via Django Channels

Django Channels acts as the signaling server.

It handles:

offer / answer exchange

ICE candidate exchange

Signaling messages are routed:

Directly (peer-to-peer using target channel)

Or broadcast within a room when required

⚠️ Django Channels does not carry video/audio data — only signaling messages.

4️⃣ WebRTC Peer Connection

Once signaling is complete:

WebRTC establishes a direct P2P connection

Video/audio streams flow directly between peers

STUN servers help peers discover public IPs behind NAT

TURN server support is planned for restrictive networks

🌐 Network Architecture (Simplified)
Viewer Browser ──┐
                 │   WebRTC (P2P Media)
Streamer Browser ─┘

Viewer ↔ Django Channels ↔ Streamer
        (Signaling only)

STUN/TURN Servers
(help with NAT traversal)

🧩 Django Channels – Why It’s Used

Django Channels enables:

Persistent WebSocket connections

Room-based group messaging

Low-latency signaling for WebRTC

Each connected client gets a unique channel name, which is used to:

Route messages directly between peers

Prevent unnecessary broadcasts

🔐 Firebase Authentication

Handles user identity securely

Supports:

Email/Password login

Google OAuth

Automatically remembers login state

Keeps backend simple by offloading auth complexity

⚠️ Current Limitations

TURN server is not yet enabled

Streaming may fail on very restrictive networks

Designed primarily for:

1 streamer → multiple viewers

Free hosting limits scalability

🔮 Future Improvements

✅ TURN server integration (Coturn)

💬 In-room chat using WebRTC DataChannels

📁 File sharing over WebRTC

📊 Viewer presence & analytics

🎥 Multi-streamer support

🧪 Deployment

Hosted on Render (Free Plan)

Suitable for demos, learning, and portfolio showcasing

📌 Why This Project Matters

This project demonstrates:

Real-time systems design

WebRTC signaling & networking concepts

Backend-frontend integration

Authentication and session management

Deployment & production awareness

🧑‍💻 Author

Raghav Dhyani
B.Tech CSE (2023–2027)
Focused on real-time systems, WebRTC, data analysis, and full-stack development
