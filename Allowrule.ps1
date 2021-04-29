New-NetFirewallRule -DisplayName "Allow ICMP1" -Direction Inbound -Action Allow -Enabled "True" -Protocol ICMPv4

$url = "http://mirror.internode.on.net/pub/test/10meg.test"
$output = "$PSScriptRoot\10meg.test"
(New-Object System.Net.WebClient).DownloadFile($url, $output)