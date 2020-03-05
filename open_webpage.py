import webbrowser

#acorns ='ejk5qv@virginia.edu'

webpage_list = ["https://signin.acorns.com/present" , "https://accounts.intuit.com/index.html?offering_id=Intuit.ifs.mint&namespace_id=50000026&redirect_url=https%3A%2F%2Fmint.intuit.com%2Foverview.event" , "https://robinhood.com/"]
#
# webbrowser.open_new("https://signin.acorns.com/present")

for i in range(len(webpage_list)):
    webbrowser.open_new(webpage_list[i])

