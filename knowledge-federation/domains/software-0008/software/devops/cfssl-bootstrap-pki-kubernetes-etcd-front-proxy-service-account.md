---
id: software.devops.tranche20.001930
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

# CFSSL para Kubernetes "The Hard Way": automação completa das CAs de cluster (`kubernetes-ca`, `etcd-ca` e `front-proxy-ca`)

## Em uma frase
O par `cfssl` + `cfssljson` é a ferramenta padrão consagrada (inclusive no guia *Kubernetes The Hard Way*) para provisionar as três hierarquias de PKI exigidas por um control plane Kubernetes: **`kubernetes-ca`** (API Server, Kubelets, Controller Manager, Scheduler), **`etcd-ca`** (peers e clientes do etcd) e **`front-proxy-ca`** (aggregation layer).

## Por que importa
Misturar os certificados de peer do `etcd` e do `front-proxy` na mesma CA geral do cluster permitiria que qualquer componente com certificado de cliente ou proxy forjasse identidades na camada de agregação da API.

## Como funciona
Em um script reprodutível com CFSSL, você gera três CAs independentes (`ca`, `etcd-ca`, `front-proxy-ca`), emite os certificados dos nós kubelet com `CN: system:node:<nodeName>` e `O: system:nodes` (para o autorizador `Node`), e emite o certificado do `admin` com `O: system:masters`.

## Exemplo
```json
{
  "CN": "system:node:worker-1",
  "key": {
    "algo": "ecdsa",
    "size": 256
  },
  "names": [
    {
      "O": "system:nodes",
      "OU": "Kubernetes The Hard Way"
    }
  ]
}
```

## Limites e trade-offs
No Kubernetes, o campo `"O"` (*Organization*) no array `"names"` do JSON do CFSSL mapeia diretamente para os **Groups RBAC** do usuário autenticado via mTLS; portanto, restrinja estritamente quem recebe certificados com `"O": "system:masters"`.

## Como verificar
Valide o `Subject` (`CN` e `O`) e os `SANs` de cada certificado do control plane executando `cfssl certinfo -cert <arquivo>.pem`.

## Conexões
- [[cfssl-ocsp-responder-certdb-revogacao-ocspserve-ocspsign]] — Veja também: CFSSL OCSP e Banco de Certificados (`certdb`): rastreamento de certificados emitidos, revogação e servidor `ocspserve`.

## Fontes
- [Cloudflare CFSSL GitHub — README.md (PKI/TLS Swiss Army Knife, CLI Tools, Signing Profiles, CSR Generation, Bundle Flavors & Multirootca)](https://raw.githubusercontent.com/cloudflare/cfssl/master/README.md) — README oficial do cloudflare/cfssl detalhando a suíte de binários, perfis de assinatura, geração de CA/certificados, flavors de bundle e servidor API; consultado em 2026-10-03.
- [Cloudflare CFSSL Official CLI Reference — doc/cmd/cfssl.txt (Subcommands: bundle, certinfo, gencert, gencsr, ocsprefresh, ocspserve, scan & serve)](https://raw.githubusercontent.com/cloudflare/cfssl/master/doc/cmd/cfssl.txt) — Referência oficial de subcomandos e flags da CLI cfssl; consultado em 2026-10-03.
- [Cloudflare CFSSL — Official GitHub Repository](https://github.com/cloudflare/cfssl) — Repositório oficial BSD-2-Clause do Cloudflare CFSSL; consultado em 2026-10-03.
