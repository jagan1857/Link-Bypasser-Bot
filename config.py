Vars = [
    # Bot API Token
    "5478011283:AAF8wL2dZIeh2p7j-ocz5TtydqowKtRQZ90",
    # GdToT Crypt
    "",
    # Laravel Session
    "",
    # XSRF_TOKEN 
    "",
    # KOLOP_CRYPT
    "",
    # DRIVEFIRE_CRYPT
    "",
    # HUBDRIVE_CRYPT
    "",
    # KATDRIVE_CRYPT
    "",
    # UPTOBOX_TOKEN
    ""
]

if not Vars[0]:
	raise ValueError('Bot API Token cannot be empty!')
elif not Vars[1]:
	Vars.insert(1,'b0lDek5LSCt6ZjVRR2EwZnY4T1EvVndqeDRtbCtTWmMwcGNuKy8wYWpDaz0%3D')
else:
	pass
