---
id: software.seguranca.tranche04.000360
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

# ProjectDiscovery `httpx`: Papel de Filtro e Enriquecimento Entre `subfinder`, `katana` e `nuclei`

## Em uma frase
Em arquiteturas modernas de automação de segurança (DAST/EASM), o `httpx` atua como o estágio intermediário obrigatório de filtragem e enriquecimento entre a descoberta de hosts (`subfinder`/`dnsx`) e a exploração profunda de rotas (`katana`) ou varredura de vulnerabilidades (`nuclei`).

## Por que importa
Alimentar o `nuclei` ou o `katana` diretamente com milhares de subdomínios mortos ou sem servidor HTTP desperdiça horas de *timeouts* de conexão TCP; o `httpx` reduz a lista apenas às URLs HTTP/HTTPS vivas e identifica a tecnologia exata (`-td`) para selecionar templates pertinentes.

## Como funciona
Ao emitir o arquivo JSONL do `httpx` (com `-tech-detect`), pipelines subsequentes podem alimentar o `nuclei` usando mapeamento automático de tecnologias (`nuclei -l httpx.jsonl -as`) ou filtrar URLs por tecnologia (ex.: extrair apenas servidores Spring Boot, GitLab ou WordPress) antes de acionar crawlers e scanners específicos.

## Exemplo
```bash
# Filtrar subdomínios vivos com httpx e acionar varredura automática por tecnologia no nuclei
subfinder -d example.corp -silent -duc \
  | httpx -silent -duc -td -sc -json -o live-httpx.jsonl

jq -r '.url' live-httpx.jsonl \
  | katana -silent -duc -d 3 -jc -o discovered-urls.txt
```

## Limites e trade-offs
Passar a saída padrão do `httpx` com flags visuais (`-sc -title -td` sem `-json`) diretamente via pipe para ferramentas que esperam apenas URLs puras quebrará o parser do consumidor devido aos colchetes `[200] [Title]`; ao usar pipes de texto, mantenha o `httpx` sem flags decorativas ou filtre `.url` via `jq -r`.

## Como verificar
Valide que todas as linhas de `discovered-urls.txt` começam com `http://` ou `https://` sem colchetes de status misturados.

## Conexões
- [[httpxpd-armazenamento-respostas-srd-irh-csv-sqlite-dbs]] — Veja também: ProjectDiscovery `httpx`: Arquivamento Forense de Respostas (`-srd`, `-irh`, `-irb`) e Relatórios CSV/JSONL.
- [[httpxpd-arquitetura-probing-http-retryablehttp-multipurpose-toolkit]] — Referência cruzada direta com httpxpd-arquitetura-probing-http-retryablehttp-multipurpose-toolkit.
- [[subfinder-encadeamento-pipelines-easm-stdin-stdout-httpx-nuclei]] — Referência cruzada direta com subfinder-encadeamento-pipelines-easm-stdin-stdout-httpx-nuclei.
- [[katana-arquitetura-crawler-padrao-vs-headless-chrome-dast]] — Referência cruzada direta com katana-arquitetura-crawler-padrao-vs-headless-chrome-dast.

## Fontes
- [ProjectDiscovery httpx GitHub — README.md (Multi-Purpose HTTP Toolkit, Supported Probes, Headless Screenshots, Matchers, Filters & Extractors)](https://raw.githubusercontent.com/projectdiscovery/httpx/main/README.md) — README oficial do projectdiscovery/httpx documentando a tabela de probes padrão e opcionais, flags de matchers/filters e captura headless; consultado em 2026-10-03.
- [ProjectDiscovery Official Documentation — httpx Overview (Architecture, Smart HTTPS-to-HTTP Fallback, WAF Retries & Pipeline Usage)](https://docs.projectdiscovery.io/opensource/httpx/overview) — Documentação oficial do httpx explicando o papel da ferramenta na transição entre descoberta de ativos e enriquecimento tecnológico; consultado em 2026-10-03.
- [ProjectDiscovery retryablehttp-go GitHub — README.md](https://github.com/projectdiscovery/retryablehttp-go/blob/main/README.md) — Biblioteca HTTP resiliente subjacente ao ProjectDiscovery httpx; consultado em 2026-10-03.
