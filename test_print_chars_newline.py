import subprocess

def run_test(input_string):
    # Run the compiled program with input
    process = subprocess.run(['./print_chars_newline'], input=input_string, capture_output=True, text=True, encoding='utf-8')
    output = process.stdout.strip()
    expected_output = "\n".join(input_string)
    assert output == expected_output, f"Failed for input '{input_string}'. Expected output:\n{expected_output}\nGot:\n{output}"

def compile_program():
    # Compile the C program
    compile_process = subprocess.run(['gcc', 'print_chars_newline.c', '-o', 'print_chars_newline'], capture_output=True, text=True)
    if compile_process.returncode != 0:
        print("Compilation failed.")
        print(compile_process.stderr)
        exit(1)

def test_print_chars_newline():
    compile_program()
    
    # Define test case: input string
    test_input_string = "hello"
    
    run_test(test_input_string)
    
    print("Test passed. Each character of the string was correctly printed on a new line.")

if __name__ == "__main__":
    test_print_chars_newline()
