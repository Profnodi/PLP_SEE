def read_and_modify_file():
    """
    Reads a file, modifies its content, and writes to a new file.
    Handles various file-related errors gracefully.
    """
    
    # Get filename from user with error handling
    while True:
        try:
            filename = input("Enter the filename to read: ")
            
            # Try to open and read the file
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # If we get here, file was read successfully
            break
            
        except FileNotFoundError:
            print(f"Error: The file '{filename}' was not found. Please try again.")
        except PermissionError:
            print(f"Error: Permission denied to read '{filename}'. Please check file permissions.")
        except UnicodeDecodeError:
            print(f"Error: Unable to decode '{filename}'. Please ensure it's a text file.")
            try:
                # Try with different encoding
                with open(filename, 'r', encoding='latin-1') as file:
                    content = file.read()
                print("File read successfully with alternative encoding.")
                break
            except:
                print("Still unable to read the file. Please try another file.")
        except IsADirectoryError:
            print(f"Error: '{filename}' is a directory, not a file. Please enter a filename.")
        except Exception as e:
            print(f"Unexpected error: {e}. Please try again.")
    
    # Modify the content (example: convert to uppercase and add line numbers)
    modified_lines = []
    lines = content.split('\n')
    
    for i, line in enumerate(lines, 1):
        modified_line = f"{i:3d}. {line.upper()}"
        modified_lines.append(modified_line)
    
    modified_content = '\n'.join(modified_lines)
    
    # Get output filename from user
    while True:
        try:
            output_filename = input("Enter the output filename: ")
            
            # Check if file already exists
            try:
                with open(output_filename, 'r'):
                    overwrite = input(f"File '{output_filename}' already exists. Overwrite? (y/n): ").lower()
                    if overwrite != 'y':
                        print("Please choose a different filename.")
                        continue
            except FileNotFoundError:
                pass  # File doesn't exist, which is good
            
            # Write to the new file
            with open(output_filename, 'w', encoding='utf-8') as file:
                file.write(modified_content)
            
            print(f"Success! Modified content written to '{output_filename}'")
            break
            
        except PermissionError:
            print(f"Error: Permission denied to write to '{output_filename}'. Please choose a different filename.")
        except Exception as e:
            print(f"Error writing to file: {e}. Please try again.")

def display_file_preview(filename, num_lines=5):
    """Display a preview of the file content."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        print(f"\nPreview of '{filename}':")
        print("─" * 50)
        for i, line in enumerate(lines[:num_lines], 1):
            print(f"{i}: {line.rstrip()}")
        if len(lines) > num_lines:
            print(f"... and {len(lines) - num_lines} more lines")
        print("─" * 50)
        
    except Exception as e:
        print(f"Could not display preview: {e}")

def main():
    """Main program function."""
    print("📁 File Read & Write Program 📁")
    print("This program reads a file, modifies it, and saves a new version.")
    print("=" * 60)
    
    try:
        read_and_modify_file()
        
        # Optional: Ask if user wants to see a preview
        preview = input("\nWould you like to see a preview of the output file? (y/n): ").lower()
        if preview == 'y':
            output_filename = input("Enter the output filename to preview: ")
            display_file_preview(output_filename)
            
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user. Goodbye!")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
    finally:
        print("\nThank you for using the File Read & Write Program! 📝")

# Run the program
if __name__ == "__main__":
    main()