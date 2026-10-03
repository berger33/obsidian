---
id: software.seguranca.tranche04.000354
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-04.md"
fontes: ["https://raw.githubusercontent.com/projectdiscovery/httpx/main/README.md", "https://docs.projectdiscovery.io/opensource/httpx/overview", "https://github.com/projectdiscovery/retryablehttp-go/blob/main/README.md"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# ProjectDiscovery `httpx`: Inspeção de Certificados TLS (`tls-grab`), Header CSP (`-csp-probe`) e Extração de FQDNs (`-efqdn`)

## Em uma frase
Durante o handshake HTTPS, o `httpx` extrai os metadados completos do certificado X.509 do servidor (`tls`), analisa políticas `Content-Security-Policy` (`-csp-probe`) e coleta novos domínios e subdomínios presentes no corpo e nos cabeçalhos HTTP (`-efqdn` / `-extract-fqdn`).

## Por que importa
A lista de `Subject Alternative Names` (SAN) de um certificado TLS e as diretivas `connect-src` / `script-src` do cabeçalho CSP frequentemente revelam subdomínios internos, APIs de backend e buckets de armazenamento que não constam em dicionários de DNS.

## Como funciona
No output JSON (`-json`), o objeto `.tls` reporta `subject_cn`, `subject_an` (SANs), `issuer_cn`, `not_before`, `not_after`, `tls_version`, `cipher` e `fingerprint_hash`. Combinado com `-csp-probe` e `-efqdn`, o `httpx` alimenta recursivamente o inventário de superfície de ataque com os novos FQDNs descobertos.

## Exemplo
```bash
# Extrair certificados TLS, domínios da política CSP e FQDNs embutidos no corpo/headers
httpx -l live-https.txt \
  -csp-probe -efqdn \
  -json -o tls-csp-discovery.jsonl

# Listar certificados que expiram nos próximos 30 dias ou usam TLS legado
jq -c '{url, tls_version: .tls.tls_version, not_after: .tls.not_after, san: .tls.subject_an}' tls-csp-discovery.jsonl
```

## Limites e trade-offs
Servidores mal configurados que exigem SNI estrito podem apresentar um certificado *fallback* genérico do balanceador se sondados pelo endereço IP bruto em vez do hostname; passe sempre o FQDN na entrada ou configure `-sni-name`.

## Como verificar
Verifique que o campo `.tls.subject_an` e `.csp.domains` estão preenchidos nos registros JSONL gerados.

## Conexões
- [[httpxpd-probes-rede-ip-cname-asn-cdn-waf-vhost-ports]] — Veja também: ProjectDiscovery `httpx`: Probes de Infraestrutura (`-ip`, `-cname`, `-asn`, `-cdn`), Portas (`-p`) e Virtual Hosts (`-vhost`).
- [[httpxpd-captura-screenshots-headless-chrome-system-chrome-js]] — Veja também: ProjectDiscovery `httpx`: Triagem Visual em Escala com Screenshots Headless (`-ss`, `-system-chrome` e `-jsc`).
- [[httpxpd-arquitetura-probing-http-retryablehttp-multipurpose-toolkit]] — Referência cruzada direta com httpxpd-arquitetura-probing-http-retryablehttp-multipurpose-toolkit.
- [[httpxpd-deteccao-tecnologias-wappalyzer-favicon-hash-jarm-tls]] — Referência cruzada direta com httpxpd-deteccao-tecnologias-wappalyzer-favicon-hash-jarm-tls.
- [[subfinder-arquitetura-enumeracao-passiva-subdominios-fontes-curadas]] — Referência cruzada direta com subfinder-arquitetura-enumeracao-passiva-subdominios-fontes-curadas.

## Fontes
- [ProjectDiscovery httpx GitHub — README.md (Multi-Purpose HTTP Toolkit, Supported Probes, Headless Screenshots, Matchers, Filters & Extractors)](https://raw.githubusercontent.com/projectdiscovery/httpx/main/README.md) — README oficial do projectdiscovery/httpx documentando a tabela de probes padrão e opcionais, flags de matchers/filters e captura headless; consultado em 2026-10-03.
- [ProjectDiscovery Official Documentation — httpx Overview (Architecture, Smart HTTPS-to-HTTP Fallback, WAF Retries & Pipeline Usage)](https://docs.projectdiscovery.io/opensource/httpx/overview) — Documentação oficial do httpx explicando o papel da ferramenta na transição entre descoberta de ativos e enriquecimento tecnológico; consultado em 2026-10-03.
- [ProjectDiscovery retryablehttp-go GitHub — README.md](https://github.com/projectdiscovery/retryablehttp-go/blob/main/README.md) — Biblioteca HTTP resiliente subjacente ao ProjectDiscovery httpx; consultado em 2026-10-03.
