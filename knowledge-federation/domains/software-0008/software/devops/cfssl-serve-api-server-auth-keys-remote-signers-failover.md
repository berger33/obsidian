---
id: software.devops.tranche20.001925
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
fontes: ["https://raw.githubusercontent.com/cloudflare/cfssl/master/doc/cmd/cfssl.txt", "https://raw.githubusercontent.com/cloudflare/cfssl/master/README.md", "https://github.com/cloudflare/cfssl"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# CFSSL API Server (`cfssl serve`), `auth_keys` e `remotes`: assinatura remota autenticada por HMAC e failover de CAs

## Em uma frase
O subcomando **`cfssl serve`** inicia um servidor HTTP REST de Autoridade Certificadora que protege os endpoints de assinatura com autenticação HMAC (**`auth_keys`** do tipo `standard`) e permite que instâncias locais do `cfssl` encaminhem pedidos para servidores CA remotos com failover automático (**`remotes`** e **`auth_remote`**).

## Por que importa
Copiar o arquivo da chave privada da CA (`ca-key.pem`) para cada servidor web ou worker node que precisa emitir um certificado viola a segurança elementar de qualquer PKI.

## Como funciona
Conforme detalhado em `doc/cmd/cfssl.txt`, a chave privada permanece exclusivamente no servidor central rodando `cfssl serve`. Nos servidores de aplicação, o `cfssl` local configura `"remotes": {"prod_ca": "ca1.example.org:8888, ca2.example.org:8888"}` e `"auth_keys"` com a chave hexadecimal compartilhada: cada requisição `cfssl gencert -remote=...` gera um token autenticado e tenta `ca1` primeiro, fazendo failover automático para `ca2` se `ca1` estiver indisponível.

## Exemplo
```json
{
  "signing": {
    "default": {
      "usages": ["signing", "key encipherment", "client auth"],
      "expiry": "720h",
      "auth_remote": {
        "remote": "caserver",
        "auth_key": "primary"
      }
    }
  },
  "auth_keys": {
    "primary": {
      "type": "standard",
      "key": "0123456789ABCDEF0123456789ABCDEF"
    }
  },
  "remotes": {
    "caserver": "ca1.corp.internal:8888,ca2.corp.internal:8888"
  }
}
```

## Limites e trade-offs
Nunca exponha o endpoint `/api/v1/cfssl/sign` de um `cfssl serve` na rede sem configurar `auth_keys` nos perfis de assinatura (ou use exclusivamente os endpoints autenticados `/api/v1/cfssl/authsign`).

## Como verificar
Inicie um servidor local de teste com `cfssl serve -ca=ca.pem -ca-key=ca-key.pem -config=ca-config.json -port=8888` e consulte `curl -s http://127.0.0.1:8888/api/v1/cfssl/info -d '{"label":"default"}'`.

## Conexões
- [[cfssl-gencert-csr-json-san-hosts-ecdsa-rsa-override-hostname]] — Veja também: CFSSL Emissão de Certificados (`cfssl gencert` e `cfssl sign`): definição de SANs (`hosts`), algoritmos `ecdsa`/`rsa` e `-hostname`.
- [[cfssl-bundle-flavors-optimal-ubiquitous-force-cfssl-trust]] — Veja também: CFSSL Certificate Bundling (`cfssl bundle` e `mkbundle`): montagem de cadeias TLS nos modos `optimal`, `ubiquitous` e `force`.

## Fontes
- [Cloudflare CFSSL GitHub — README.md (PKI/TLS Swiss Army Knife, CLI Tools, Signing Profiles, CSR Generation, Bundle Flavors & Multirootca)](https://raw.githubusercontent.com/cloudflare/cfssl/master/doc/cmd/cfssl.txt) — README oficial do cloudflare/cfssl detalhando a suíte de binários, perfis de assinatura, geração de CA/certificados, flavors de bundle e servidor API; consultado em 2026-10-03.
- [Cloudflare CFSSL Official CLI Reference — doc/cmd/cfssl.txt (Subcommands: bundle, certinfo, gencert, gencsr, ocsprefresh, ocspserve, scan & serve)](https://raw.githubusercontent.com/cloudflare/cfssl/master/README.md) — Referência oficial de subcomandos e flags da CLI cfssl; consultado em 2026-10-03.
- [Cloudflare CFSSL — Official GitHub Repository](https://github.com/cloudflare/cfssl) — Repositório oficial BSD-2-Clause do Cloudflare CFSSL; consultado em 2026-10-03.
