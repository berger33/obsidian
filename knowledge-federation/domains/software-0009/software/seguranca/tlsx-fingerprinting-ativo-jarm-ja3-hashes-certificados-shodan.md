---
id: software.seguranca.tranche09.000834
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

# `tlsx`: Fingerprinting Criptográfico **`-jarm`**, **`-ja3`**, Serial (`-se`) e Hashes de Certificado (**`-hash md5,sha1,sha256`**) para Threat Hunting

## Em uma frase
Ao investigar servidores suspeitos de **Command & Control (C2)** ou procurar réplicas da infraestrutura de um atacante/alvo na internet (via Shodan/Censys), os nomes de domínio mudam constantemente, mas a pilha TLS e o certificado costumam deixar impressões digitais únicas.

## Por que importa
O `tlsx` calcula nativamente três categorias de fingerprints criptográficos em lote: **(1) `-jarm`** (envia 10 pacotes `ClientHello` especialmente construídos usando `hdm/jarm-go` e gera o hash JARM de 62 caracteres da pilha TLS do servidor!), **(2) `-ja3`** (no modo `ztls`, calcula o hash MD5 JA3 da negociação TLS) e **(3) `-hash md5,sha1,sha256` + `-se` (`-serial`)** (calcula os hashes e o número de série do certificado X.509)!

## Como funciona
Com o hash `sha256` ou `serial` do certificado TLS de uma aplicação interna vazado em um IP direto, você descobre se existem outros servidores na internet apresentando exatamente o mesmo certificado (`ssl.cert.fingerprint` no Shodan/Censys)!

## Exemplo
```bash
# Calcular fingerprints ativos JARM, JA3, numero de serie (-se) e hashes SHA-256 dos certificados X.509 de uma lista de servidores
tlsx -l /cases/easm/suspect_servers.txt \
  -jarm -ja3 \
  -hash sha256 -serial \
  -sm ztls \
  -json -o /cases/easm/tls_fingerprints.jsonl
```

## Limites e trade-offs
Lembre-se de que o cálculo do fingerprint **`-jarm`** envia **10 conexões TLS adicionais por alvo** (testando combinações de TLS 1.2, TLS 1.3, ordens de cifras e extensões ALPN); portanto, ative `-jarm` de forma seletiva sobre os hosts vivos em vez de rodá-lo cegamente sobre milhões de IPs fechados.

## Como verificar
Compare o campo `"jarm_hash"` do JSONL contra assinaturas conhecidas de servidores Cobalt Strike, Mythic, Sliver e Burp Collaborator.

## Conexões
- [[tlsx-deteccao-misconfigurations-expired-self-signed-mismatched-revoked]] — Veja também: `tlsx`: Auditoria Contínua de **Misconfigurations de Certificados X.509** (`-ex` Expirado, `-ss` Auto-Assinado, `-mm` Mismatched, `-re` Revogado e `-un` Untrusted).
- [[tlsx-enumeracao-versoes-tls-version-enum-cipher-enum-cipher-type]] — Veja também: `tlsx`: Enumeração de **Versões TLS Suportadas (`-ve` / `-version-enum`)** e Auditoria de **Cifras Fracas/Inseguras (`-ce` / `-cipher-enum`, `-ct`)**.
- [[tlsx-arquitetura-coletor-tls-modos-ctls-ztls-openssl-auto]] — Referência cruzada direta com tlsx-arquitetura-coletor-tls-modos-ctls-ztls-openssl-auto.
- [[zmap-auditoria-protocolos-industriais-ot-ics-scada-zgrab2-modbus-siemens-dnp3]] — Referência cruzada direta com zmap-auditoria-protocolos-industriais-ot-ics-scada-zgrab2-modbus-siemens-dnp3.

## Fontes
- [ProjectDiscovery tlsx Official GitHub — Fast and Configurable TLS Grabber Focused on TLS Data Collection](https://raw.githubusercontent.com/projectdiscovery/tlsx/main/README.md) — repositório oficial do ProjectDiscovery tlsx cobrindo os 4 motores TLS, extração SAN/CN, auditoria de certificados/cifras e hashes JA3/JARM; consultado em 2026-10-03.
- [ProjectDiscovery tlsx Official Documentation — Scan Modes & Certificate Analysis](https://raw.githubusercontent.com/projectdiscovery/tlsx/main/go.mod) — documentação oficial do tlsx na plataforma ProjectDiscovery Docs; consultado em 2026-10-03.
- [Go Package Documentation — github.com/projectdiscovery/tlsx](https://docs.projectdiscovery.io/tools/tlsx/overview) — referência técnica do pacote Go `projectdiscovery/tlsx`; consultado em 2026-10-03.
