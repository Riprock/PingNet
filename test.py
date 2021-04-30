import subprocess as sp
result = sp.run("whoami", capture_output=True)
if result.check_returncode() is None:
    print(result.stdout.decode().strip())