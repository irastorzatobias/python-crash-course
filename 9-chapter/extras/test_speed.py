import speedtest_cli

test = speedtest_cli.Speedtest()

down = test.download()
upload = test.upload()
print(f'Download speed: {down}')
print(f'Upload speed: {upload}')