---
id: software.devops.tranche20.001922
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

# CFSSL Inicialização de Root CA e Intermediate CA: uso de `cfssl gencert -initca`, `cfssljson -bare` e `ca_constraint`

## Em uma frase
Para construir uma hierarquia de PKI de duas camadas (Root CA offline + Intermediate CA emissora) com o CFSSL, utiliza-se **`cfssl gencert -initca`** (ou `cfssl genkey -initca`) em conjunto com **`cfssljson -bare`** e a restrição de caminho **`ca_constraint`** (`is_ca` e `max_path_len`) no perfil de assinatura.

## Por que importa
Assinar certificados de serviços finais diretamente com a chave da Root CA obriga a manter a chave raiz online; criar uma CA intermediária com `max_path_len: 0` garante criptograficamente que a intermediária possa emitir apenas certificados folha (*leaf certificates*) e nunca outra sub-CA.

## Como funciona
Na especificação oficial (`doc/cmd/cfssl.txt`), para emitir uma CA intermediária que não pode delegar novas CAs (`pathlen = 0`), o perfil de assinatura deve conter `"ca_constraint": {"is_ca": true, "max_path_len": 0, "max_path_len_zero": true}` — o campo booleano extra `max_path_len_zero: true` é obrigatório em Go/CFSSL para distinguir o valor `0` explícito de um campo omitido!

## Exemplo
```bash
# Gerando o par de chaves e certificado autoassinado da Root CA (ca.pem e ca-key.pem):
cfssl gencert -initca ca-csr.json | cfssljson -bare ca

# Assinando o CSR da Intermediate CA com a Root CA usando o perfil intermediate_ca:
cfssl gencert -ca ca.pem -ca-key ca-key.pem \
  -config ca-config.json -profile intermediate_ca \
  intermediate-csr.json | cfssljson -bare intermediate_ca
```

## Limites e trade-offs
Preste muita atenção ao detalhe documentado em `doc/cmd/cfssl.txt`: se você definir `"max_path_len": 0` mas esquecer de adicionar `"max_path_len_zero": true` em `ca_constraint`, o certificado intermediário será emitido **sem nenhuma restrição de pathlen**.

## Como verificar
Inspecione o certificado gerado com `cfssl-certinfo -cert intermediate_ca.pem` e confirme `Basic Constraints: CA:TRUE, pathlen:0`.

## Conexões
- [[cfssl-arquitetura-toolkit-pki-tls-cloudflare-cfssljson-multirootca]] — Veja também: CFSSL: arquitetura do toolkit de PKI e TLS da Cloudflare (`cfssl`, `cfssljson`, `mkbundle`, `multirootca` e `cfssl-scan`).
- [[cfssl-signing-profiles-usages-expiry-server-client-peer-kubernetes]] — Veja também: CFSSL Signing Profiles (`signing.profiles`): configuração de `usages`, `expiry`, `backdate` e `name_whitelist` para mTLS e Kubernetes.

## Fontes
- [Cloudflare CFSSL GitHub — README.md (PKI/TLS Swiss Army Knife, CLI Tools, Signing Profiles, CSR Generation, Bundle Flavors & Multirootca)](https://raw.githubusercontent.com/cloudflare/cfssl/master/doc/cmd/cfssl.txt) — README oficial do cloudflare/cfssl detalhando a suíte de binários, perfis de assinatura, geração de CA/certificados, flavors de bundle e servidor API; consultado em 2026-10-03.
- [Cloudflare CFSSL Official CLI Reference — doc/cmd/cfssl.txt (Subcommands: bundle, certinfo, gencert, gencsr, ocsprefresh, ocspserve, scan & serve)](https://raw.githubusercontent.com/cloudflare/cfssl/master/README.md) — Referência oficial de subcomandos e flags da CLI cfssl; consultado em 2026-10-03.
- [Cloudflare CFSSL — Official GitHub Repository](https://github.com/cloudflare/cfssl) — Repositório oficial BSD-2-Clause do Cloudflare CFSSL; consultado em 2026-10-03.
