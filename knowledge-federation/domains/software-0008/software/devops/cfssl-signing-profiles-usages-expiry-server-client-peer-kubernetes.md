---
id: software.devops.tranche20.001923
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

# CFSSL Signing Profiles (`signing.profiles`): configuração de `usages`, `expiry`, `backdate` e `name_whitelist` para mTLS e Kubernetes

## Em uma frase
No arquivo de configuração JSON do CFSSL (`-config ca-config.json`), o dicionário **`signing`** define um perfil `default` e múltiplos **`profiles`** nomeados (ex.: `server`, `client`, `peer`), controlando `expiry`, `usages` (*Key Usage* e *Extended Key Usage*), `backdate`, `issuer_urls`, `ocsp_url`, `crl_url` e `name_whitelist`.

## Por que importa
Em um cluster etcd ou Kubernetes, um certificado de cliente (`client auth`) não deve poder atuar como servidor TLS (`server auth`), enquanto um nó peer do etcd precisa de ambos (`server auth` e `client auth`) além de `signing` e `key encipherment`.

## Como funciona
Na referência oficial (`doc/cmd/cfssl.txt`), `expiry` usa a sintaxe de duração do pacote `time` do Go (onde a maior unidade aceita é hora, ex.: `"8760h"` para 1 ano ou `"720h"` para 30 dias), `backdate` (ex.: `"5m"`) retroage o campo `NotBefore` para evitar falhas de validação por leve *clock skew* entre servidores, e `name_whitelist` aplica uma expressão regular sobre os SANs permitidos.

## Exemplo
```json
{
  "signing": {
    "default": {
      "expiry": "8760h"
    },
    "profiles": {
      "server": {
        "usages": ["signing", "key encipherment", "server auth"],
        "expiry": "2160h",
        "backdate": "5m"
      },
      "client": {
        "usages": ["signing", "key encipherment", "client auth"],
        "expiry": "2160h"
      },
      "peer": {
        "usages": ["signing", "key encipherment", "server auth", "client auth"],
        "expiry": "2160h"
      }
    }
  }
}
```

## Limites e trade-offs
Lembre-se de que `time.ParseDuration` do Go não aceita a unidade `"d"` (dias) nem `"y"` (anos): especifique sempre `expiry` em horas (`"720h"` = 30 dias, `"8760h"` = 365 dias).

## Como verificar
Emita um certificado passando `-profile=server` no `cfssl gencert` e verifique os *Extended Key Usages* resultantes com `cfssl-certinfo -cert server.pem`.

## Conexões
- [[cfssl-inicializacao-root-ca-intermediate-ca-genkey-initca-ca-constraint]] — Veja também: CFSSL Inicialização de Root CA e Intermediate CA: uso de `cfssl gencert -initca`, `cfssljson -bare` e `ca_constraint`.
- [[cfssl-gencert-csr-json-san-hosts-ecdsa-rsa-override-hostname]] — Veja também: CFSSL Emissão de Certificados (`cfssl gencert` e `cfssl sign`): definição de SANs (`hosts`), algoritmos `ecdsa`/`rsa` e `-hostname`.

## Fontes
- [Cloudflare CFSSL GitHub — README.md (PKI/TLS Swiss Army Knife, CLI Tools, Signing Profiles, CSR Generation, Bundle Flavors & Multirootca)](https://raw.githubusercontent.com/cloudflare/cfssl/master/doc/cmd/cfssl.txt) — README oficial do cloudflare/cfssl detalhando a suíte de binários, perfis de assinatura, geração de CA/certificados, flavors de bundle e servidor API; consultado em 2026-10-03.
- [Cloudflare CFSSL Official CLI Reference — doc/cmd/cfssl.txt (Subcommands: bundle, certinfo, gencert, gencsr, ocsprefresh, ocspserve, scan & serve)](https://raw.githubusercontent.com/cloudflare/cfssl/master/README.md) — Referência oficial de subcomandos e flags da CLI cfssl; consultado em 2026-10-03.
- [Cloudflare CFSSL — Official GitHub Repository](https://github.com/cloudflare/cfssl) — Repositório oficial BSD-2-Clause do Cloudflare CFSSL; consultado em 2026-10-03.
