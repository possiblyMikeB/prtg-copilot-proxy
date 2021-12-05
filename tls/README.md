# Create client & server certificates with CFSSL

This directory contains the bare essentials required to create a one-off `CA` and use it to 
create a sufficiently secure client/server certificate pair. 


## Make the `CA`: 
Fundamentally, we don't care about the `CA`; the only relavent piece of information we are
going to eventually keep is it's public certificate. However, we'll need it in tact long enough 
for us to issuse what we're really after. 

Using the `CSR` parameters from `csr/ca.json` (feel free to modify) we generate the `CA` by running,

```bash
$ cfssl gencert -initca "csr/ca.json" > obj.json
$ cfssl -bare -f obj.json "ca"
```

Once run, you will find `ca.pem`, `ca-key.pem`, and `ca.csr` in the directory you 
ran the commands from; they are (in order) you `CA`'s public certificate, private key, and 
originating `CSR`.

## Issue the `server` certificate:

To generate the `server` certificate, we should modify the `hosts` & `CN` fields from `csr/server.json` 
so that they accurately refect the deployment environment. Alternatively, we can pass `cfssl gencert` the `-hostname` 
argment; this argumnet expects a comma seperated list of ip-addresses and hostnames to be added to the resulting certificate as `SAN` entries. 

In this case, running the following,

```bash
$ cfssl gencert -config "cfssl.json" -ca "ca.pem" -ca-key "ca-key.json" -hostname "localhost,127.0.0.1,metrics.davidson.edu" -profile "server" "csr/server.json" > obj.json 
$ cfssl -bare -f obj.json "cert"
```

will produce similar files as before, only this time prefixed with `cert` instead of `ca`; in addition 
looking at the output from `openssl x509 -in cert.pem -text -noout` we should have something similar to:

```
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            55:96:f7:11:25:4a:7f:db:28:9b:c3:44:9b:10:3c:20:fb:19:4b:bd
        Signature Algorithm: ecdsa-with-SHA256
        Issuer: C = US, CN = PRTG Shim CA
        Validity
            Not Before: Dec  4 23:22:00 2021 GMT
            Not After : Dec  4 23:22:00 2022 GMT
        Subject: C = US, CN = metrics-host
        Subject Public Key Info:
            Public Key Algorithm: id-ecPublicKey
                Public-Key: (256 bit)
                pub:
                    04:94:19:0a:22:34:41:a0:5e:b3:d1:ad:b9:5a:d0:
                    04:12:6f:02:82:6f:08:63:39:b7:21:e1:b9:ab:8e:
                    f1:a2:ea:b6:63:9b:e2:8c:83:5f:b7:34:7d:bd:49:
                    cb:58:16:08:3e:a6:f4:f1:76:6c:45:e7:79:b0:30:
                    49:38:45:25:ac
                ASN1 OID: prime256v1
                NIST CURVE: P-256
        X509v3 extensions:
            X509v3 Key Usage: critical
                Digital Signature, Key Encipherment
            X509v3 Extended Key Usage: 
                TLS Web Server Authentication
            X509v3 Basic Constraints: critical
                CA:FALSE
            X509v3 Subject Key Identifier: 
                89:C8:68:D4:DE:04:22:68:7B:8C:FE:AB:1B:D7:A2:57:0E:CA:61:99
            X509v3 Authority Key Identifier: 
                keyid:FD:D9:9D:37:1C:C3:3A:45:8B:50:CE:A3:4F:17:00:D6:EC:1C:DC:C0

            X509v3 Subject Alternative Name: 
                DNS:localhost, DNS:metrics.davidson.edu, IP Address:127.0.0.1
				
    Signature Algorithm: ecdsa-with-SHA256
         30:45:02:21:00:82:59:24:89:f9:01:81:46:ad:a3:ad:5d:11:
         cb:48:40:de:30:47:f2:48:12:6c:91:45:4f:e7:64:45:83:ee:
         58:02:20:2b:f3:f0:73:b0:e1:6f:7d:61:0e:ca:de:cd:7f:ed:
         74:16:f6:6c:11:a7:55:47:76:0e:8e:54:53:6e:a8:1c:4f
```

where the fields "X509v3 Subject Alternative Name" and "X509v3 Extended Key Usage" contain (respectively) the hostnames we passed to `cfssl` and contain the appropriate role we expect to use the certificate for (i.e. `TLS Web Server Authentication` in this case).


## Issue one (or more) `client` certificate:

The `CN` is the only field really useful (aside from the private key) when creating the kind of "only works as a client send" certificates we will generate; looking at `csr/client.json`, you can see we only used the `CN` to vaguely label the context in which that certificate should have originated from.

```json
{
    "CN": "PRTG-Service",
    "hosts": [],
    "key": {
        "algo": "ecdsa",
        "size": 256
    },
    "names": [
        {
            "C": "US"
        }
    ]
}
```

Finding that it fits with what we want, let's create the client certificates. Making the assumption that the forgoing instructions for the `CA` and `server` certificates have been done on `metrics-host`, we will do the following 


 1. Run `openssl rand -hex 16` and use the output to replace the `key` field under `client_key` in the files `cfssl.json` & `remote.json`.
 2. Copy `remote.json` and `csr/client.json` to `PRTG`, or the end-point you are going to upload the client certificates from.
 3. Once done, begin the `cfssl` remote signing service on `metrics-host`:

```
$ cfssl serve -config "cfssl.json" -ca "ca.pem" -ca-key "ca-key.pem" -port 8889 -address metrics-host
```
 4. From where the copies of `remote.json` & `client.json` reside, run the following,
```
$ cfssl genkey client.json | cfssljson -bare client
$ cfssl sign  -config "remote.json" -profile=client "client.csr" | cfssljson -bare client
```
 5. Stop the `cfssl` remote signing server on `metrics-host`


You should now have `client.pem`, `client-key.pem`, and `client.csr` on (or adjacent to) the client server; in addition, since the private-key was locally generated and likely exists nowhere else on earth, we can be confident when this client verifies themselves with the service. 

Repeat with as many trusted clients as you require.
