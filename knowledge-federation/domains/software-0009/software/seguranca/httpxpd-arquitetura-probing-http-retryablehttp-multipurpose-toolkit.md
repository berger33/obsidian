---
id: software.seguranca.tranche04.000351
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

# ProjectDiscovery `httpx`: Arquitetura de Probing HTTP Multi-Propósito com `retryablehttp-go`

## Em uma frase
O `httpx` da ProjectDiscovery (MIT, distinto da biblioteca cliente Python de mesmo nome) é um toolkit de *probing* HTTP rápido escrito em Go sobre a biblioteca `retryablehttp-go` para validar e enriquecer listas massivas de hosts, URLs e blocos CIDR.

## Por que importa
Transforma listas brutas de nomes DNS ou IPs em um inventário vivo de serviços web, realizando *auto-fallback* inteligente de `https://` para `http://`, retentativas com *backoff* contra WAFs e extração simultânea de dezenas de metadados em uma única requisição.

## Como funciona
Para cada alvo recebido via `-l hosts.txt`, `-u` ou `stdin`, o `httpx` estabelece conexões reutilizáveis com pool de goroutines configurável (`-t`), negocia TLS/HTTP2, coleta os *probes* habilitados (status code, título, tamanho, servidor, certificado TLS, hashes e tecnologias) e emite resultados filtrados em texto ou JSONL (`-json`).

## Exemplo
```bash
# Sondar uma lista de hosts extraindo status, tamanho, título, servidor web e tempo de resposta
httpx -l discovered-hosts.txt \
  -sc -cl -title -server -rt \
  -threads 50 -silent \
  -json -o httpx-inventory.jsonl
```

## Limites e trade-offs
Confundir o binário `httpx` do Python (`pip install httpx`) com o `httpx` da ProjectDiscovery em imagens Docker baseadas em Debian/Ubuntu/Kali é um erro operacional comum; invoque o caminho explícito (`pdtm` / `/root/go/bin/httpx`) ou verifique `httpx -version`.

## Como verificar
Execute `httpx -version` e valide o schema de saída de `httpx-inventory.jsonl` com `jq -e '.url and .status_code'`.

## Conexões
- [[httpxpd-deteccao-tecnologias-wappalyzer-favicon-hash-jarm-tls]] — Veja também: ProjectDiscovery `httpx`: Fingerprinting de Tecnologias (`-td`), Favicon Hash (`-favicon`), Body Hash e JARM (`-jarm`).
- [[httpxpd-probes-rede-ip-cname-asn-cdn-waf-vhost-ports]] — Referência cruzada direta com httpxpd-probes-rede-ip-cname-asn-cdn-waf-vhost-ports.
- [[subfinder-arquitetura-enumeracao-passiva-subdominios-fontes-curadas]] — Referência cruzada direta com subfinder-arquitetura-enumeracao-passiva-subdominios-fontes-curadas.

## Fontes
- [ProjectDiscovery httpx GitHub — README.md (Multi-Purpose HTTP Toolkit, Supported Probes, Headless Screenshots, Matchers, Filters & Extractors)](https://raw.githubusercontent.com/projectdiscovery/httpx/main/README.md) — README oficial do projectdiscovery/httpx documentando a tabela de probes padrão e opcionais, flags de matchers/filters e captura headless; consultado em 2026-10-03.
- [ProjectDiscovery Official Documentation — httpx Overview (Architecture, Smart HTTPS-to-HTTP Fallback, WAF Retries & Pipeline Usage)](https://docs.projectdiscovery.io/opensource/httpx/overview) — Documentação oficial do httpx explicando o papel da ferramenta na transição entre descoberta de ativos e enriquecimento tecnológico; consultado em 2026-10-03.
- [ProjectDiscovery retryablehttp-go GitHub — README.md](https://github.com/projectdiscovery/retryablehttp-go/blob/main/README.md) — Biblioteca HTTP resiliente subjacente ao ProjectDiscovery httpx; consultado em 2026-10-03.
