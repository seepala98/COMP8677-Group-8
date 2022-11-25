$TTL 3D
@       IN      SOA   ns.attacker.com. admin.attacker.com. (
                2008111001
                8H
                2H
                4W
                1D)

@       IN      NS    ns.attacker.com.

@       IN      A     10.9.0.180
www     IN      A     10.9.0.180
ns      IN      A     10.9.0.153
*       IN      A     10.9.0.100
