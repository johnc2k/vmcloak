:: Win7: Disable ISATAP, Teredo, and 6to4
netsh int ipv6 isatap set state disabled
netsh int ipv6 6to4 set state disabled
netsh interface teredo set state disable
:: Win7: Disable Windows Firewall
netsh advfirewall set allprofiles state off