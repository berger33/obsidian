---
id: software.seguranca.tranche04.000359
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

# ProjectDiscovery `httpx`: Arquivamento Forense de Respostas (`-srd`, `-irh`, `-irb`) e Relatórios CSV/JSONL

## Em uma frase
Para auditoria histórica e análise de *diff* entre varreduras, o `httpx` pode gravar em disco todas as requisições e respostas HTTP brutas (`-srd` / `-store-response-dir`) ou incluí-las diretamente no JSONL (`-irh` / `-include-response-header` e `-irb` / `-include-response-base64`).

## Por que importa
Quando uma vulnerabilidade ou alteração de superfície é detectada, o analista não precisa enviar novas requisições ao alvo para inspecionar cabeçalhos de segurança (`Strict-Transport-Security`, `X-Frame-Options`, `Set-Cookie`) ou o HTML retornado no instante da coleta.

## Como funciona
Com `-srd /var/lib/easm/http-responses`, o `httpx` cria uma estrutura organizada por domínio contendo o dump completo do par requisição/resposta e um índice `index.txt`. Já a exportação `-csv -o report.csv` (com `-csvo` para codificação) gera planilhas prontas para auditoria de conformidade de cabeçalhos TLS/HTTP.

## Exemplo
```bash
# Salvar cabeçalhos e corpos HTTP em diretório de evidências e exportar JSONL enriquecido
httpx -l critical-endpoints.txt \
  -sc -title -server -td \
  -srd /var/lib/easm/evidence-dump \
  -irh \
  -json -o critical-endpoints-audit.jsonl
```

## Limites e trade-offs
Habilitar `-irb` (corpo completo em Base64 dentro do JSONL) em listas grandes produz arquivos JSONL de vários gigabytes; prefira `-srd` combinado com `-mrs 1048576` para limitar o tamanho máximo armazenado por resposta.

## Como verificar
Verifique a criação dos arquivos de evidência em `/var/lib/easm/evidence-dump/` e confirme a presença do objeto de cabeçalhos no JSONL gerado com `-irh`.

## Conexões
- [[httpxpd-otimizacao-rate-limit-threads-retries-timeout-waf-bypass]] — Veja também: ProjectDiscovery `httpx`: Controle de Concorrência (`-t`, `-rl`, `-rlm`), Retries, Timeout e Resiliência a WAF.
- [[httpxpd-encadeamento-dast-subfinder-httpx-katana-nuclei]] — Veja também: ProjectDiscovery `httpx`: Papel de Filtro e Enriquecimento Entre `subfinder`, `katana` e `nuclei`.
- [[httpxpd-arquitetura-probing-http-retryablehttp-multipurpose-toolkit]] — Referência cruzada direta com httpxpd-arquitetura-probing-http-retryablehttp-multipurpose-toolkit.
- [[httpxpd-captura-screenshots-headless-chrome-system-chrome-js]] — Referência cruzada direta com httpxpd-captura-screenshots-headless-chrome-system-chrome-js.
- [[ffuf-auditoria-relatorios-json-html-csv-od-replay-proxy-ffufrc]] — Referência cruzada direta com ffuf-auditoria-relatorios-json-html-csv-od-replay-proxy-ffufrc.

## Fontes
- [ProjectDiscovery httpx GitHub — README.md (Multi-Purpose HTTP Toolkit, Supported Probes, Headless Screenshots, Matchers, Filters & Extractors)](https://raw.githubusercontent.com/projectdiscovery/httpx/main/README.md) — README oficial do projectdiscovery/httpx documentando a tabela de probes padrão e opcionais, flags de matchers/filters e captura headless; consultado em 2026-10-03.
- [ProjectDiscovery Official Documentation — httpx Overview (Architecture, Smart HTTPS-to-HTTP Fallback, WAF Retries & Pipeline Usage)](https://docs.projectdiscovery.io/opensource/httpx/overview) — Documentação oficial do httpx explicando o papel da ferramenta na transição entre descoberta de ativos e enriquecimento tecnológico; consultado em 2026-10-03.
- [ProjectDiscovery retryablehttp-go GitHub — README.md](https://github.com/projectdiscovery/retryablehttp-go/blob/main/README.md) — Biblioteca HTTP resiliente subjacente ao ProjectDiscovery httpx; consultado em 2026-10-03.
