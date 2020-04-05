import subprocess as sp


result = sp.run(["powershell", "Get-LocalUser"], capture_output=True)
print(result.check_returncode() == None)
