# gemini_processor.py

import os
import time
import google.generativeai as genai
from dotenv import load_dotenv
import uuid
import tempfile

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def upload_to_gemini(path, mime_type=None):
    """
    Upload a file to Gemini API.
    """
    try:
        file = genai.upload_file(path, mime_type=mime_type)
        print(f"Uploaded file '{file.display_name}' as: {file.uri}")
        return file
    except Exception as e:
        print(f"Error uploading file to Gemini API: {e}")
        return None

def wait_for_files_active(files):
    """
    Wait until all uploaded files are in ACTIVE state.
    """
    print("Waiting for file processing...")
    for name in (file.name for file in files):
        file = genai.get_file(name)
        while file.state.name == "PROCESSING":
            print(".", end="", flush=True)
            time.sleep(10)
            file = genai.get_file(name)
        if file.state.name != "ACTIVE":
            raise Exception(f"File {file.name} failed to process")
    print("...all files ready\n")

def process_content(username, content, task_id, tasks):
    """
    Process the scraped content through Gemini API and update the tasks dict with progress.
    """
    try:
        generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 8192,
            "response_mime_type": "text/plain",
        }

        tasks[task_id]['progress'] = 'Initializing Gemini model...'
        model = genai.GenerativeModel(
            model_name="gemini-exp-1206",  # Replace with actual model name if different
            generation_config=generation_config,
        )

        # Create a unique temporary file
        temp_dir = tempfile.gettempdir()
        unique_id = uuid.uuid4().hex
        temp_input_file = os.path.join(temp_dir, f"{username}_{unique_id}_reddit_full_data.md")

        # Write content to the temporary input file
        with open(temp_input_file, "w", encoding="utf-8") as f:
            f.write(content)

        tasks[task_id]['progress'] = 'Uploading file to Gemini API...'
        # Upload the file
        uploaded_file = upload_to_gemini(temp_input_file, mime_type="text/markdown")
        if not uploaded_file:
            tasks[task_id]['status'] = 'Failed'
            tasks[task_id]['progress'] = 'Failed to upload file to Gemini API.'
            os.remove(temp_input_file)  # Clean up
            return None

        tasks[task_id]['progress'] = 'Waiting for Gemini to process the file...'
        # Wait for the file to be active
        wait_for_files_active([uploaded_file])

        tasks[task_id]['progress'] = 'Generating analysis report...'
        # Start chat session with the designed prompt
        chat_session = model.start_chat(
            history=[
                {
                    "role": "user",
                    "parts": [
                        uploaded_file,
                        "You are an advanced AI linguist, psychologist, and behavior analyst trained to analyze digital personas. The attached file contains publicly scraped data of a Reddit account, including their posts and comments. Your task is to create a highly detailed and objective report analyzing the personality, behavior, and potential real-life characteristics of the individual behind this account. Be thorough, no sugarcoating, and support every conclusion with evidence from their posts or comments. You have to be in detail as much as possible breakdown everything. The analysis should be structured as follows:\n\n### 1. **General Overview**\n   - Summarize their overall Reddit activity.\n   - Identify the primary subreddits they engage with and their interaction patterns.\n   - Highlight any notable quirks or unique behaviors.\n\n### 2. **Personality Traits**\n   - Writing Style:\n     - Do they use a lot of slang, swear words, or formal language?\n     - Are they concise or verbose? How articulate are they?\n   - Emotional Tone:\n     - Do they appear sarcastic, angry, empathetic, or neutral or what?\n     - Identify recurring emotional patterns (e.g., consistent frustration, humor, kindness, etc).\n   - Recurring Themes:\n     - What topics are they obsessed with (e.g., tech, politics, cats)?\n     - Any peculiar or niche interests that stand out?\n\n### 3. **Behavioral Red Flags**\n   - Problematic Behavior:\n     - Are there indications of toxic traits (e.g., misogyny, racism, trolling etc)?\n     - Provide evidence from specific posts/comments.\n   - Controversial Topics:\n     - Have they engaged in heated debates or controversial discussions? If so, which ones?\n   - Ethical Concerns:\n     - Any signs of stalking, harassment, or unethical behavior? Cite examples.\n\n### 4. **Psychological Insights**\n   - Infer potential personality disorders or quirks based on their patterns (e.g., narcissism, obsessive tendencies, etc).\n   - Are there signs of insecurity, overconfidence, or attention-seeking behavior or any other similar?\n   - Any traits that suggest leadership qualities, creativity, or empathy?\n\n### 5. **Social Dynamics**\n   - Interaction Style:\n     - Do they seek validation? Argue a lot? Or mostly observe?\n     - How do they respond to criticism—defensive, open-minded, dismissive?\n   - Relationship Indicators:\n     - Can you infer how they might interact with friends, colleagues, or family based on their tone and topics?\n\n### 6. **Real-Life Details (Deep Dive)**\n   - **Personal Information Extraction**:\n     - Extract any real-life details the user may have inadvertently shared (e.g., full name, location, city, state, country).\n     - Did they mention where they live or any specific places related to them (e.g., city, neighborhood)?\n   - **Family and Relationships**:\n     - If the user shared any information about their family (e.g., parents, siblings, children), include it.\n     - Look for any references to close relationships or social groups (e.g., friends, colleagues, romantic partners).\n     - Note if they referenced any personal struggles, relationships with family, or any other intimate details they’ve discussed.\n   - **Detailed Analysis of Real-Life Connections**:\n     - Does the person mention any specific events or people in their personal life? (E.g., family holidays, relationships, problems with peers, etc.)\n     - What can be inferred about their social circles or living environment based on the information shared?\n\n### 7. **Judgment and Prediction**\n   - Is this person likely a positive or negative influence in real life? Why?\n   - What kind of individual might they be in real-world settings (e.g., introvert, extrovert, leader, loner)?\n   - Predict their personality in real life with evidence-backed reasoning.\n\n### 8. **Detailed Proofs**\n   - For every conclusion you make, cite specific posts, comments, or patterns from the data. Use quotes or direct references for clarity.\n   - Example: \n     - \"The user exhibits signs of trolling. In [this comment](https://reddit.com/comment_id), they mocked someone’s opinion without adding value.\"\n     - \"Evidence of recurring sarcasm: 'Yeah, sure, because *that’s* going to solve the world’s problems' [Post in r/sarcasm].\"\n     - \"Signs of toxic masculinity in [this post](https://reddit.com/post_id): 'Women these days just want...'\"\n\n### 9. **Report Structure**\n   - **Concise Headings:** Use bullet points, headers, and sub-headers for readability.\n   - **Language Style:** Be sharp, direct, and unapologetic, as if preparing a psychological profile for an investigation. \n   - **Tone:** Maintain professionalism, but don’t shy away from brutally honest insights.\n\n### Example Outputs:\n- *\"Bro, you're essentially Reddit's poster child for trolling. Here’s the proof: [links to comments]. Your obsession with debating flat-earthers in r/science suggests an inferiority complex and a need to assert intellectual dominance.\"*\n- *\"Based on [this post](https://reddit.com/post_id) in r/MGTOW, your comments reveal a pattern of misogynistic tendencies and anger issues. This is consistent across multiple threads.\"*\n- *\"You’ve replied 'LOL cringe' to 37 people in r/memes. This indicates dismissive behavior and likely a lack of constructive engagement in real life.\"*\n\nFinally, ensure your report is brutally honest, free of bias, and as comprehensive as possible.\n"
                    ],},
                        {
                        "role": "model",
                        "parts": [
                            "Yes, I will do it.",
                        ],
                    },
                ]
        )

        try:
            response = chat_session.send_message("Yes Do IT!!!!")
        except Exception as e:
            print(f"Error during chat session: {e}")
            os.remove(temp_input_file)  # Clean up
            tasks[task_id]['progress'] = 'Failed during Gemini processing.'
            tasks[task_id]['status'] = 'Failed'
            return None

        # Save the response to a unique .md file
        unique_id = uuid.uuid4().hex
        output_filename = f"response_output_{username}_{unique_id}.md"
        output_path = os.path.join(temp_dir, output_filename)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(response.text)

        print(f"Response saved to {output_path}")
        tasks[task_id]['progress'] = 'Report generated successfully.'
        tasks[task_id]['status'] = 'Completed'
        tasks[task_id]['report_path'] = output_path
        return output_path

    except Exception as e:
        pass
