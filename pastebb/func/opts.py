# TODO: add more filetypes
file_types = [
    ["All supprted file types", ""],
    ("Plain text", "*.txt"),
    ("Bash script", "*.sh"),
    ("Batch script", "*.bat"),
    ("C file", "*.c"),
    ("C++ file", "*.cpp"),
    ("Python file", "*.py"),
    ("R script file", "*.R")
]
for name, extension in file_types:
    file_types[0][1] += extension + " "

# TODO: add more syntax
paste_syntax = {
    "None": "text",
    "Bash" : "bash",
    "Batch" : "dos",
    "C" : "c",
    "C++" : "cpp",
    "Python" : "python",
    "R" : "rsplus"
}

paste_expiry = {
    "Never" : "N",
    "10 minutes" : "10M",
    "1 hour" : "1H",
    "1 day" : "1D",
    "1 week" : "1W",
    "2 weeks" : "2W",
    "1 month" : "1M",
    "6 months" : "6M",
    "1 year" : "1Y"
}

paste_privacy = {
    "Unlisted" : "1",
    "Public" : "0"
}
