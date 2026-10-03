---
id: software.seguranca.tranche04.000352
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

# ProjectDiscovery `httpx`: Fingerprinting de Tecnologias (`-td`), Favicon Hash (`-favicon`), Body Hash e JARM (`-jarm`)

## Em uma frase
O `httpx` identifica a pilha tecnológica de servidores web combinando o dataset Wappalyzer (`-td` / `-tech-detect`), *fingerprints* customizados (`-cff`), hash MurmurHash3 (`mmh3`) de `/favicon.ico` (`-favicon`), hashes de corpo/cabeçalho (`-hash`) e impressões digitais TLS ativas JARM (`-jarm`).

## Por que importa
Mesmo quando um painel administrativo ou servidor C2 remove banners `Server` e altera o título HTML, o hash `mmh3` do favicon e o fingerprint TLS `JARM` permanecem idênticos aos da aplicação original.

## Como funciona
A flag `-td` inspeciona cabeçalhos HTTP, cookies, meta tags HTML e caminhos de scripts JavaScript contra assinaturas Wappalyzer; `-favicon` calcula o hash `mmh3` compatível com buscas Shodan (`http.favicon.hash:<valor>`); e `-jarm` envia 10 pacotes `ClientHello` TLS especificamente formatados para gerar um hash de 62 caracteres da pilha TLS do servidor.

## Exemplo
```bash
# Enriquecer ativos web com detecção de tecnologias, hash mmh3 de favicon, SHA-256 do body e JARM
httpx -l live-hosts.txt \
  -td -favicon -jarm \
  -hash sha256 \
  -json -o tech-fingerprints.jsonl
```

## Limites e trade-offs
O cálculo de `-jarm` exige 10 conexões TCP/TLS adicionais por host sondado; habilite `-jarm` apenas em subconjuntos priorizados de ativos para não multiplicar por 10 o tráfego de rede e o tempo de varredura.

## Como verificar
Inspecione `jq -c '{url, tech, favicon, jarm}' tech-fingerprints.jsonl` e filtre ativos que compartilham o mesmo hash de favicon com `-mfc <hash>`.

## Conexões
- [[httpxpd-arquitetura-probing-http-retryablehttp-multipurpose-toolkit]] — Veja também: ProjectDiscovery `httpx`: Arquitetura de Probing HTTP Multi-Propósito com `retryablehttp-go`.
- [[httpxpd-probes-rede-ip-cname-asn-cdn-waf-vhost-ports]] — Veja também: ProjectDiscovery `httpx`: Probes de Infraestrutura (`-ip`, `-cname`, `-asn`, `-cdn`), Portas (`-p`) e Virtual Hosts (`-vhost`).
- [[httpxpd-inspecao-certificados-tls-csp-extract-fqdn-san]] — Referência cruzada direta com httpxpd-inspecao-certificados-tls-csp-extract-fqdn-san.
- [[httpxpd-matchers-filters-status-length-string-regex-cdn-time]] — Referência cruzada direta com httpxpd-matchers-filters-status-length-string-regex-cdn-time.

## Fontes
- [ProjectDiscovery httpx GitHub — README.md (Multi-Purpose HTTP Toolkit, Supported Probes, Headless Screenshots, Matchers, Filters & Extractors)](https://raw.githubusercontent.com/projectdiscovery/httpx/main/README.md) — README oficial do projectdiscovery/httpx documentando a tabela de probes padrão e opcionais, flags de matchers/filters e captura headless; consultado em 2026-10-03.
- [ProjectDiscovery Official Documentation — httpx Overview (Architecture, Smart HTTPS-to-HTTP Fallback, WAF Retries & Pipeline Usage)](https://docs.projectdiscovery.io/opensource/httpx/overview) — Documentação oficial do httpx explicando o papel da ferramenta na transição entre descoberta de ativos e enriquecimento tecnológico; consultado em 2026-10-03.
- [ProjectDiscovery retryablehttp-go GitHub — README.md](https://github.com/projectdiscovery/retryablehttp-go/blob/main/README.md) — Biblioteca HTTP resiliente subjacente ao ProjectDiscovery httpx; consultado em 2026-10-03.
