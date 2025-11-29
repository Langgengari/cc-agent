from google.adk.agents.invocation_context import InvocationContext
import json

def normalize_json_inputs(callback_context: InvocationContext):
    """
    Convert JSON file attachments in user content to formatted text.

    Iterates through `callback_context.user_content.parts`, detects JSON files,
    pretty-prints their contents, and replaces the file attachment with the 
    formatted text in `part.text`. Non-JSON files are ignored, and errors are logged.
    """  
    user_content = callback_context.user_content
    if not user_content:
        return
    
    for part in user_content.parts:
        #🔹Check if there is any type of file
        if hasattr(part, "inline_data") and part.inline_data:
            blob = part.inline_data
            
            if blob.mime_type != "application/json":
                continue

            print(f"Detected file to be converted to text: {blob.display_name}")
            try:
                content_str = blob.data.decode("utf-8")
                content_json = json.loads(content_str)

                #🔹Convert the JSON back to a formatted string
                json_text = json.dumps(content_json, indent=2)

                #🔹Replace the file with the text
                part.inline_data = None
                part.text = f"File content {blob.display_name}:\n{json_text}"
            except Exception as e:
                print(f"ERROR: Error processing JSON {blob.display_name}: {e}")
       
    return