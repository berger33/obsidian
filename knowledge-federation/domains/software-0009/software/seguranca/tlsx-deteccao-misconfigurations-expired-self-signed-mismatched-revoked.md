---
id: software.seguranca.tranche09.000833
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-09.md"
fontes: ["https://raw.githubusercontent.com/projectdiscovery/tlsx/main/README.md", "https://raw.githubusercontent.com/projectdiscovery/tlsx/main/go.mod", "https://docs.projectdiscovery.io/tools/tlsx/overview"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `tlsx`: Auditoria Contínua de **Misconfigurations de Certificados X.509** (`-ex` Expirado, `-ss` Auto-Assinado, `-mm` Mismatched, `-re` Revogado e `-un` Untrusted)

## Em uma frase
Em infraestruturas com centenas de microsserviços, ingress controllers e balanceadores, um certificado TLS expirado derruba integrações em produção, enquanto certificados auto-assinados (`self-signed`), revogados (`revoked`) ou emitidos para outro domínio (`mismatched`) indicam ambientes de homologação esquecidos ou ataques de interceptação.

## Por que importa
O `tlsx` possui cinco flags dedicadas de detecção de **Misconfigurations X.509**: **`-ex` / `-expired`** (certificado com `not_after` vencido), **`-ss` / `-self-signed`** (certificado auto-assinado), **`-mm` / `-mismatched`** (o hostname conectado não bate com nenhum `SAN`/`CN` do certificado!), **`-re` / `-revoked`** (certificado revogado via OCSP/CRL!) e **`-un` / `-untrusted`** (cadeia não confiável)!

## Como funciona
Além disso, no modo JSON (`-json`), o `tlsx` calcula e exporta campos preciosos como `not_before`, `not_after` e quantos dias faltam para cada certificado expirar, permitindo criar alertas preventivos de renovação!

## Exemplo
```bash
# Auditar toda a superficie HTTPS em busca de certificados expirados (-ex), auto-assinados (-ss), incompativeis (-mm) ou revogados (-re)
tlsx -l /cases/easm/live_web_assets.txt \
  -ex -ss -mm -re -un \
  -json -o /cases/easm/tls_misconfigurations.jsonl
```

## Limites e trade-offs
Note um insight ofensivo/EASM importante sobre **`-mm` (`mismatched`)** e **`-ss` (`self-signed`)**: quando um subdomínio aponta para um IP cujo certificado é `mismatched` (ex.: apresenta o certificado padrão `*.cloudprovider.com` ou `Kubernetes Ingress Controller Fake Certificate`), isso frequentemente revela o **IP de origem real** sem proteção de CDN ou um Ingress recém-provisionado!

## Como verificar
Filtre no `tls_misconfigurations.jsonl` qualquer ativo com `"expired": true` ou `"revoked": true` para acionar a renovação via **Certbot / ACME**.

## Conexões
- [[tlsx-descoberta-subdominios-certificados-san-cn-dns-cidr-asn]] — Veja também: `tlsx`: Descoberta Ativa de Subdomínios e Ativos via **Campos `SAN` (`-san`) e `CN` (`-cn`)** sobre Blocos **CIDR e ASNs** e Modo **`-pre-handshake` (`-ps`)**.
- [[tlsx-fingerprinting-ativo-jarm-ja3-hashes-certificados-shodan]] — Veja também: `tlsx`: Fingerprinting Criptográfico **`-jarm`**, **`-ja3`**, Serial (`-se`) e Hashes de Certificado (**`-hash md5,sha1,sha256`**) para Threat Hunting.
- [[tlsx-arquitetura-coletor-tls-modos-ctls-ztls-openssl-auto]] — Referência cruzada direta com tlsx-arquitetura-coletor-tls-modos-ctls-ztls-openssl-auto.

## Fontes
- [ProjectDiscovery tlsx Official GitHub — Fast and Configurable TLS Grabber Focused on TLS Data Collection](https://raw.githubusercontent.com/projectdiscovery/tlsx/main/README.md) — repositório oficial do ProjectDiscovery tlsx cobrindo os 4 motores TLS, extração SAN/CN, auditoria de certificados/cifras e hashes JA3/JARM; consultado em 2026-10-03.
- [ProjectDiscovery tlsx Official Documentation — Scan Modes & Certificate Analysis](https://raw.githubusercontent.com/projectdiscovery/tlsx/main/go.mod) — documentação oficial do tlsx na plataforma ProjectDiscovery Docs; consultado em 2026-10-03.
- [Go Package Documentation — github.com/projectdiscovery/tlsx](https://docs.projectdiscovery.io/tools/tlsx/overview) — referência técnica do pacote Go `projectdiscovery/tlsx`; consultado em 2026-10-03.
