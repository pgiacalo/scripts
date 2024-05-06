#!/usr/bin/env python3
import re
import sys
import shutil  # For file backup


format_replacements = {
    #the Printf must look like this: printf("Minimum free heap size: %" PRIu32 " bytes\n", esp_get_minimum_free_heap_size());
    #e.g., ESP_LOGI(BT_HF_TAG, "--connection state %s, peer feats 0x%"PRIx32", chld_feats 0x%"PRIx32,...
    "0x%x": "%\" PRIx32 \"",
    "0x%d": "%\" PRIu32 \"",
    "0x%u": "%\" PRIu32 \"",
    "0x%i": "%\" PRIi32 \"",
    "0x%o": "%\" PRIo32 \"",
    "0x%p": "%\" PRIx32 \"",
}

def replace_formats(text):
    for old_format, new_format in format_replacements.items():
        pattern = re.compile(r'(["\'])([^"\']*?' + re.escape(old_format) + r'[^"\']*?)\1')
        matches = pattern.finditer(text)
        for match in matches:
            text = text[:match.start(2)] + match.group(2).replace(old_format, new_format) + text[match.end(2):]
    return text

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: format_replace.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    # Create a backup of the original file
    backup_filename = filename + ".bak"
    shutil.copy2(filename, backup_filename)

    with open(filename, "r") as f:
        text = f.read()

    new_text = replace_formats(text)

    with open(filename, "w") as f:
        f.write(new_text)

    print("Replaced formats in", filename)
