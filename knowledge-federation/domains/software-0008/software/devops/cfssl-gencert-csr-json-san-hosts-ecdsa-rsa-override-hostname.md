---
id: software.devops.tranche20.001924
tipo: tecnica
dominio: software
subdominio: devops
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-20.md"
fontes: ["https://raw.githubusercontent.com/cloudflare/cfssl/master/README.md", "https://raw.githubusercontent.com/cloudflare/cfssl/master/doc/cmd/cfssl.txt", "https://github.com/cloudflare/cfssl"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# CFSSL Emissão de Certificados (`cfssl gencert` e `cfssl sign`): definição de SANs (`hosts`), algoritmos `ecdsa`/`rsa` e `-hostname`

## Em uma frase
O comando **`cfssl gencert`** gera em um único passo uma nova chave privada, um CSR e o certificado assinado pela CA local (`-ca` / `-ca-key`) ou remota (`-remote`), lendo os parâmetros de algoritmo (`key.algo`: `ecdsa` ou `rsa`, `key.size`: `256`, `384`, `2048`, `4096`), `CN`, `names` e `hosts` (SANs DNS, IP, URI e e-mail) de um arquivo JSON.

## Por que importa
Certificados TLS modernos exigem que todos os nomes DNS e endereços IP do serviço constem na extensão *Subject Alternative Name (SAN)*; depender apenas do campo *Common Name (CN)* é rejeitado por navegadores e clientes Go/gRPC atuais.

## Como funciona
No arquivo `csr.json`, a lista `"hosts"` define todos os SANs do certificado. Além disso, passar a flag `-hostname="api.corp.internal,10.0.0.10,127.0.0.1"` na linha de comando do `cfssl gencert` ou `cfssl sign` sobrescreve dinamicamente a lista de SANs do JSON, permitindo reutilizar o mesmo template JSON em scripts de automação.

## Exemplo
```bash
cfssl gencert \
  -ca=ca.pem \
  -ca-key=ca-key.pem \
  -config=ca-config.json \
  -profile=server \
  -hostname="kube-apiserver,10.96.0.1,127.0.0.1,kubernetes.default.svc" \
  apiserver-csr.json | cfssljson -bare apiserver
```

## Limites e trade-offs
Para menor tamanho de handshake e menor custo de CPU, prefira chaves `"algo": "ecdsa"` com `"size": 256` (curva P-256) em vez de chaves RSA de 2048/4096 bits, a menos que um cliente legado específico exija RSA.

## Como verificar
Execute `cfssl-certinfo -cert apiserver.pem` para inspecionar a lista `sans` e o algoritmo de chave pública do certificado gerado.

## Conexões
- [[cfssl-signing-profiles-usages-expiry-server-client-peer-kubernetes]] — Veja também: CFSSL Signing Profiles (`signing.profiles`): configuração de `usages`, `expiry`, `backdate` e `name_whitelist` para mTLS e Kubernetes.
- [[cfssl-serve-api-server-auth-keys-remote-signers-failover]] — Veja também: CFSSL API Server (`cfssl serve`), `auth_keys` e `remotes`: assinatura remota autenticada por HMAC e failover de CAs.

## Fontes
- [Cloudflare CFSSL GitHub — README.md (PKI/TLS Swiss Army Knife, CLI Tools, Signing Profiles, CSR Generation, Bundle Flavors & Multirootca)](https://raw.githubusercontent.com/cloudflare/cfssl/master/README.md) — README oficial do cloudflare/cfssl detalhando a suíte de binários, perfis de assinatura, geração de CA/certificados, flavors de bundle e servidor API; consultado em 2026-10-03.
- [Cloudflare CFSSL Official CLI Reference — doc/cmd/cfssl.txt (Subcommands: bundle, certinfo, gencert, gencsr, ocsprefresh, ocspserve, scan & serve)](https://raw.githubusercontent.com/cloudflare/cfssl/master/doc/cmd/cfssl.txt) — Referência oficial de subcomandos e flags da CLI cfssl; consultado em 2026-10-03.
- [Cloudflare CFSSL — Official GitHub Repository](https://github.com/cloudflare/cfssl) — Repositório oficial BSD-2-Clause do Cloudflare CFSSL; consultado em 2026-10-03.
