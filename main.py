from fastapi import FastAPI, UploadFile, File
from chatbot import chatbot_response
from document_processor import extract_text_from_pdf, summarize_text, extract_keywords
from badwords import check_bad_language
from auth import generate_otp, verify_otp

app = FastAPI()

logged_users = set()

# ---------- AUTH ----------

@app.post("/login")

def login(email:str):

    return generate_otp(email)


@app.post("/verify")

def verify(email:str, otp:int):

    if verify_otp(email, otp):

        logged_users.add(email)

        return {"message":"Login successful"}

    return {"message":"Invalid OTP"}


# ---------- CHATBOT ----------

@app.post("/chat")

def chat(email:str, message:str):

    if email not in logged_users:
        return {"error":"User not authenticated"}

    if check_bad_language(message):
        return {"response":"Please avoid inappropriate language."}

    reply = chatbot_response(message)

    return {"response":reply}


# ---------- DOCUMENT UPLOAD ----------

@app.post("/upload")

async def upload(email:str, file:UploadFile = File(...)):

    if email not in logged_users:
        return {"error":"User not authenticated"}

    text = extract_text_from_pdf(file.file)

    summary = summarize_text(text)

    keywords = extract_keywords(text)

    return {
        "summary":summary,
        "keywords":keywords
    }