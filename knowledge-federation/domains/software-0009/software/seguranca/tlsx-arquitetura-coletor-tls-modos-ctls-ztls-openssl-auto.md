---
id: software.seguranca.tranche09.000831
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

# ProjectDiscovery **`tlsx`**: Arquitetura do Coletor e Analisador TLS e os 4 Motores de Conexão (**`ctls`**, **`ztls`**, **`openssl`** e **`auto`**)

## Em uma frase
**`tlsx`** (`projectdiscovery/tlsx`, licença MIT, escrito em Go sobre `crypto/tls`, `zmap/zcrypto`, `cloudflare/cfssl` e `hdm/jarm-go`) é o toolkit de alta velocidade da ProjectDiscovery dedicado à coleta de dados TLS, inspeção em massa de certificados X.509 e detecção de falhas de configuração criptográfica.

## Por que importa
Um problema clássico ao varrer milhares de servidores heterogêneos usando apenas a biblioteca padrão `crypto/tls` do Go moderno é que o Go desabilita por segurança protocolos legados (`SSLv3`, `TLS 1.0`, `TLS 1.1`) e cifras antigas (`RC4`, `3DES`, `RSA_EXPORT`), fazendo a conexão falhar justamente nos servidores legados mais vulneráveis que você precisava descobrir!

## Como funciona
Para resolver isso, conforme documentado no `README.md` oficial, o `tlsx` integra **três motores TLS complementares** selecionáveis via **`-sm` / `-scan-mode`**: **(1) `ctls`** (`crypto/tls` padrão do Go, suporte total a TLS 1.3 moderno), **(2) `ztls`** (`zmap/zcrypto`, suporta TLS 1.0–1.2, extração de `ClientHello`/`ServerHello`, `--pre-handshake` e `JA3`), **(3) `openssl`** (invoca o binário OpenSSL para suportar até `SSLv3` e cifras arcaicas) e **(4) `auto`** (padrão: faz **fallback automático** entre os motores se o servidor exigir TLS legado!)!

## Exemplo
```bash
# Verificar a versao do tlsx e inspecionar a versao TLS, a cifra negociada e o status da sonda em modo auto-fallback
tlsx -version
tlsx -l /cases/easm/live_hosts.txt -tv -cipher -tps -sm auto -o /cases/easm/tls_summary.txt
```

## Limites e trade-offs
Graças ao modo padrão **`-sm auto`**, você nunca perde a visibilidade de um equipamento antigo que só fala `TLS 1.0`: se o handshake `ctls` falhar por incompatibilidade de protocolo, o `tlsx` refaz a tentativa automaticamente com `ztls`/`openssl`!

## Como verificar
Execute `tlsx -hc` (`-health-check`) para verificar a disponibilidade dos motores e do binário OpenSSL no sistema.

## Conexões
- [[tlsx-descoberta-subdominios-certificados-san-cn-dns-cidr-asn]] — Veja também: `tlsx`: Descoberta Ativa de Subdomínios e Ativos via **Campos `SAN` (`-san`) e `CN` (`-cn`)** sobre Blocos **CIDR e ASNs** e Modo **`-pre-handshake` (`-ps`)**.
- [[tlsx-deteccao-misconfigurations-expired-self-signed-mismatched-revoked]] — Referência cruzada direta com tlsx-deteccao-misconfigurations-expired-self-signed-mismatched-revoked.

## Fontes
- [ProjectDiscovery tlsx Official GitHub — Fast and Configurable TLS Grabber Focused on TLS Data Collection](https://raw.githubusercontent.com/projectdiscovery/tlsx/main/README.md) — repositório oficial do ProjectDiscovery tlsx cobrindo os 4 motores TLS, extração SAN/CN, auditoria de certificados/cifras e hashes JA3/JARM; consultado em 2026-10-03.
- [ProjectDiscovery tlsx Official Documentation — Scan Modes & Certificate Analysis](https://raw.githubusercontent.com/projectdiscovery/tlsx/main/go.mod) — documentação oficial do tlsx na plataforma ProjectDiscovery Docs; consultado em 2026-10-03.
- [Go Package Documentation — github.com/projectdiscovery/tlsx](https://docs.projectdiscovery.io/tools/tlsx/overview) — referência técnica do pacote Go `projectdiscovery/tlsx`; consultado em 2026-10-03.
