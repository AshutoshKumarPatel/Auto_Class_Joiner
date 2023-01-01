# Sleep for laptop to wake up properly
nircmd.exe sendkeypress ctrl
Start-Sleep -s 120

# Run the Teams App
Set-Location "F:\Useful_Projects\Auto_Class_Joiner\"
explorer shell:appsFolder\com.squirrel.Teams.Teams

# Sleep for the App to open properly
Start-Sleep -s 30

#Start main.py

python main.py