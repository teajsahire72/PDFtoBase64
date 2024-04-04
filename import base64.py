import base64
import os
import time

def convert_to_base64_and_pdf(source_path, destination_folder):
    """
    This function takes a source file path and a destination folder path.
    - Reads the file content.
    - Converts the content to base64 encoded string.
    - Prints the base64 string.
    - Decodes the base64 string back to binary data.
    - Saves the decoded data as a PDF in the destination folder.
    """
    # Get the filename from the source path
    filename = os.path.basename(source_path)

    # Read the file content in binary mode
    with open(source_path, "rb") as f:
        file_content = f.read()

    # Encode the file content as base64
    start_time = time.time()
    base64_encoded_data = base64.b64encode(file_content).decode('utf-8')
    end_time = time.time()

    # Print the base64 encoded data
    # print("Base64 Encoded Data:", base64_encoded_data)

    # Print the time taken
    print("Time taken for conversion:", end_time - start_time, "seconds")

    # Decode the base64 string back to binary data
    decoded_data = base64.b64decode(base64_encoded_data)

    # Check if destination folder exists, create it if not
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Create the destination file path with the same filename and .pdf extension
    destination_file_path = os.path.join(destination_folder, filename + ".pdf")

    # Save the decoded data as a PDF file
    with open(destination_file_path, "wb") as f:
        f.write(decoded_data)

    print(f"Converted file saved to: {destination_file_path}")

# Define source and destination paths
source_path = r"E:\PDFtobase64\Source\sample-50-MB-pdf-file.pdf"
destination_folder = r"E:\PDFtobase64"

# Call the function to perform conversion
convert_to_base64_and_pdf(source_path, destination_folder)
