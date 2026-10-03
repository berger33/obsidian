---
id: software.seguranca.tranche04.000353
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

# ProjectDiscovery `httpx`: Probes de Infraestrutura (`-ip`, `-cname`, `-asn`, `-cdn`), Portas (`-p`) e Virtual Hosts (`-vhost`)

## Em uma frase
O `httpx` correlaciona a camada de aplicação HTTP com a camada de infraestrutura de rede extraindo endereço IP (`-ip`), registro `CNAME` (`-cname`), número de Sistema Autônomo (`-asn`), provedor de CDN/WAF (`-cdn`), teste de Virtual Host (`-vhost`) e portas customizadas (`-p`).

## Por que importa
Permite distinguir rapidamente quais domínios estão protegidos atrás de Cloudflare/CloudFront/Akamai (`-cdn`) e quais expõem o IP de origem da nuvem diretamente ou apontam para `CNAMEs` de terceiros.

## Como funciona
A opção `-p` aceita listas e faixas nomeadas de portas (ex.: `-p http:80,8080,8000,https:443,8443,9443`), multiplicando os alvos pelas portas indicadas. Já `-cdn` compara o IP resolvido e cabeçalhos contra faixas conhecidas de CDNs/WAFs (via biblioteca `cdncheck`), permitindo filtrar ou excluir ativos atrás de CDN com `-mcdn` ou `-fcdn`.

## Exemplo
```bash
# Sondar portas web alternativas identificando IP, CNAME, ASN e provedor de CDN/WAF
httpx -l subdomains.txt \
  -p http:80,8080,https:443,8443 \
  -ip -cname -asn -cdn -vhost \
  -json -o infra-web-map.jsonl
```

## Limites e trade-offs
Sondar dezenas de portas (`-p`) em milhares de hosts atrás de uma mesma CDN gera bloqueio rápido do IP do scanner; use `-exclude-cdn` quando o objetivo for testar portas altas diretamente em servidores de origem.

## Como verificar
Execute `jq -c 'select(.cdn == false) | {url, host, port, cname, asn}' infra-web-map.jsonl` para listar servidores que respondem diretamente sem camada de CDN.

## Conexões
- [[httpxpd-deteccao-tecnologias-wappalyzer-favicon-hash-jarm-tls]] — Veja também: ProjectDiscovery `httpx`: Fingerprinting de Tecnologias (`-td`), Favicon Hash (`-favicon`), Body Hash e JARM (`-jarm`).
- [[httpxpd-inspecao-certificados-tls-csp-extract-fqdn-san]] — Veja também: ProjectDiscovery `httpx`: Inspeção de Certificados TLS (`tls-grab`), Header CSP (`-csp-probe`) e Extração de FQDNs (`-efqdn`).
- [[httpxpd-arquitetura-probing-http-retryablehttp-multipurpose-toolkit]] — Referência cruzada direta com httpxpd-arquitetura-probing-http-retryablehttp-multipurpose-toolkit.
- [[subfinder-monitoramento-continuo-diff-novos-subdominios-alertas]] — Referência cruzada direta com subfinder-monitoramento-continuo-diff-novos-subdominios-alertas.
- [[httpxpd-matchers-filters-status-length-string-regex-cdn-time]] — Referência cruzada direta com httpxpd-matchers-filters-status-length-string-regex-cdn-time.

## Fontes
- [ProjectDiscovery httpx GitHub — README.md (Multi-Purpose HTTP Toolkit, Supported Probes, Headless Screenshots, Matchers, Filters & Extractors)](https://raw.githubusercontent.com/projectdiscovery/httpx/main/README.md) — README oficial do projectdiscovery/httpx documentando a tabela de probes padrão e opcionais, flags de matchers/filters e captura headless; consultado em 2026-10-03.
- [ProjectDiscovery Official Documentation — httpx Overview (Architecture, Smart HTTPS-to-HTTP Fallback, WAF Retries & Pipeline Usage)](https://docs.projectdiscovery.io/opensource/httpx/overview) — Documentação oficial do httpx explicando o papel da ferramenta na transição entre descoberta de ativos e enriquecimento tecnológico; consultado em 2026-10-03.
- [ProjectDiscovery retryablehttp-go GitHub — README.md](https://github.com/projectdiscovery/retryablehttp-go/blob/main/README.md) — Biblioteca HTTP resiliente subjacente ao ProjectDiscovery httpx; consultado em 2026-10-03.
