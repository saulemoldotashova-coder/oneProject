# 13 задание 

def ips_between(start, end):
    def ip_to_int(ip):
        parts = list(map(int, ip.split(".")))
        
        return (
            parts[0] * 256**3 +
            parts[1] * 256**2 +
            parts[2] * 256 +
            parts[3]
        )
    
    return ip_to_int(end) - ip_to_int(start)  
