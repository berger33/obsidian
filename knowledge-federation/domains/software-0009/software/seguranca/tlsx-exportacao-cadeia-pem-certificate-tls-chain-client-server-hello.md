---
id: software.seguranca.tranche09.000837
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

# `tlsx`: Exportação Completa da **Cadeia de Certificados em PEM (`-cert`, `-tls-chain`)** e Transcrição **`-client-hello` / `-server-hello`**

## Em uma frase
Durante auditorias de PKI interna ou investigações forenses de incidentes, apenas ler o `CN` e a data de expiração não basta: o engenheiro precisa do **certificado X.509 completo codificado em PEM** (`-----BEGIN CERTIFICATE-----`), de todos os certificados intermediários entregues pelo servidor e do dump completo das mensagens `ClientHello` e `ServerHello`.

## Por que importa
No `tlsx`, adicionar **`-cert` (`-certificate`)** e **`-tc` (`-tls-chain`)** junto com `-json` embute no JSON de saída o certificado folha e a cadeia inteira de certificados intermediários em formato PEM padrão, prontos para inspeção com `openssl x509` ou `cfssl-certinfo`!

## Como funciona
E no modo `-sm ztls`, as flags **`-ch` (`-client-hello`)** e **`-sh` (`-server-hello`)** incluem no JSON a estrutura dissecada completa dos pacotes `ClientHello` e `ServerHello` (extensões, curvas suportadas, formatos de ponto, compressão e sessão)!

## Exemplo
```bash
# Exportar o certificado folha (-cert), a cadeia intermediaria (-tc) em PEM e o ServerHello completo (-sh) em JSONL
tlsx -u https://app.internal.corp:443 \
  -cert -tls-chain -server-hello \
  -sm ztls \
  -json -o /cases/easm/full_tls_transcript.jsonl
```

## Limites e trade-offs
Para validar certificados emitidos por uma **Autoridade Certificadora (CA) Privada Interna** (ex.: Vault PKI, Step-CA ou Active Directory CS) sem que eles sejam marcados como `untrusted`, passe o arquivo PEM da CA raiz corporativa via **`-cc` / `-cacert /etc/secops/corp-root-ca.pem`** junto com **`-vc` (`-verify-cert`)**!

## Como verificar
Extraia o certificado PEM de um host específico do JSONL com `jq -r '.certificate' /cases/easm/full_tls_transcript.jsonl | openssl x509 -text -noout`.

## Conexões
- [[tlsx-customizacao-sni-random-sni-rev-ptr-sni-virtual-hosts]] — Veja também: `tlsx`: Manipulação Avançada de **TLS SNI (`-sni`, `-random-sni`, `-rev-ptr-sni`)** para Descoberta de *Virtual Hosts* e Bypass de Roteamento.
- [[tlsx-auditoria-certificados-wildcard-wc-escopo-blast-radius]] — Veja também: `tlsx` **`-wc` (`-wildcard-cert`)**: Mapeamento de **Certificados Wildcard (`*.dominio`)** e Redução do *Blast Radius* de Chaves Privadas.
- [[tlsx-arquitetura-coletor-tls-modos-ctls-ztls-openssl-auto]] — Referência cruzada direta com tlsx-arquitetura-coletor-tls-modos-ctls-ztls-openssl-auto.
- [[tlsx-deteccao-misconfigurations-expired-self-signed-mismatched-revoked]] — Referência cruzada direta com tlsx-deteccao-misconfigurations-expired-self-signed-mismatched-revoked.
- [[zmap-pipeline-dois-estagios-zmap-l4-zgrab2-l7-handshakes]] — Referência cruzada direta com zmap-pipeline-dois-estagios-zmap-l4-zgrab2-l7-handshakes.

## Fontes
- [ProjectDiscovery tlsx Official GitHub — Fast and Configurable TLS Grabber Focused on TLS Data Collection](https://raw.githubusercontent.com/projectdiscovery/tlsx/main/README.md) — repositório oficial do ProjectDiscovery tlsx cobrindo os 4 motores TLS, extração SAN/CN, auditoria de certificados/cifras e hashes JA3/JARM; consultado em 2026-10-03.
- [ProjectDiscovery tlsx Official Documentation — Scan Modes & Certificate Analysis](https://raw.githubusercontent.com/projectdiscovery/tlsx/main/go.mod) — documentação oficial do tlsx na plataforma ProjectDiscovery Docs; consultado em 2026-10-03.
- [Go Package Documentation — github.com/projectdiscovery/tlsx](https://docs.projectdiscovery.io/tools/tlsx/overview) — referência técnica do pacote Go `projectdiscovery/tlsx`; consultado em 2026-10-03.
