long_text = 3000 * "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
COMPREHEND_LIMIT = 5000


lines = long_text.split(".")
current_text = ""

for line in lines:
    if len(current_text + line) > COMPREHEND_LIMIT:
        # EXECUTE COMPREHEND
        print(f"Executing Comprehend on {len(current_text)} characters")
        current_text = ""
    current_text = current_text + line

if current_text != "":
    # EXECUTE COMPREHEND
    print(f"Executing Comprehend on {len(current_text)} characters)")

