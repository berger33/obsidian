---
id: software.seguranca.tranche04.000358
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

# ProjectDiscovery `httpx`: Controle de Concorrência (`-t`, `-rl`, `-rlm`), Retries, Timeout e Resiliência a WAF

## Em uma frase
O `httpx` ajusta finamente a pressão de rede sobre os alvos através do número de threads (`-t`, padrão 50), taxa máxima por segundo (`-rl`, padrão 150) ou por minuto (`-rlm`), número de retentativas (`-retries`), timeout (`-timeout`) e leitura máxima do corpo (`-mrs`).

## Por que importa
Sondagens agressivas sem controle de taxa contra balanceadores corporativos acionam bloqueios de IP ou geram falsos negativos por exaustão de sockets locais (*ephemeral ports*) e timeouts de handshake TLS.

## Como funciona
Para ambientes sensíveis, reduzir `-t 20 -rl 30 -timeout 10 -retries 2` estabiliza a coleta sem perda de pacotes. Além disso, a flag `-random-agent` (ativa por padrão) rotaciona `User-Agent`, `-http2` testa negociação HTTP/2 e `-ztls` permite alternar para a biblioteca `ztls` ao sondar servidores legados que requerem cifras TLS antigas.

## Exemplo
```bash
# Executar probing conservador com limite de 30 req/s, 2 retries e cabeçalho de identificação da equipe de segurança
httpx -l internal-targets.txt \
  -H "X-Security-Scanner: secops-easm-authorized" \
  -t 15 -rl 30 -timeout 10 -retries 2 \
  -sc -title -td -json -o internal-probing.jsonl
```

## Limites e trade-offs
Em sistemas Linux que realizam *probing* de dezenas de milhares de hosts com `-t` alto, o limite padrão de descritores de arquivos abertos (`ulimit -n 1024`) esgota rapidamente; eleve `ulimit -n 65535` antes da execução.

## Como verificar
Monitore a execução com `-stats -si 5` para acompanhar a taxa real de requisições por segundo e o percentual de conclusão em tempo real.

## Conexões
- [[httpxpd-extratores-customizados-er-ep-body-preview-redirect-chain]] — Veja também: ProjectDiscovery `httpx`: Extratores Regex (`-er`, `-ep`), Body Preview (`-bp`) e Cadeia de Redirecionamento (`-fr` / `- follow-redirects`).
- [[httpxpd-armazenamento-respostas-srd-irh-csv-sqlite-dbs]] — Veja também: ProjectDiscovery `httpx`: Arquivamento Forense de Respostas (`-srd`, `-irh`, `-irb`) e Relatórios CSV/JSONL.
- [[httpxpd-arquitetura-probing-http-retryablehttp-multipurpose-toolkit]] — Referência cruzada direta com httpxpd-arquitetura-probing-http-retryablehttp-multipurpose-toolkit.
- [[ffuf-rate-limiting-threads-delay-stop-flags-sa-sf-se-interativo]] — Referência cruzada direta com ffuf-rate-limiting-threads-delay-stop-flags-sa-sf-se-interativo.
- [[subfinder-rate-limiting-por-provedor-rls-rl-timeouts-otimizacao]] — Referência cruzada direta com subfinder-rate-limiting-por-provedor-rls-rl-timeouts-otimizacao.

## Fontes
- [ProjectDiscovery httpx GitHub — README.md (Multi-Purpose HTTP Toolkit, Supported Probes, Headless Screenshots, Matchers, Filters & Extractors)](https://raw.githubusercontent.com/projectdiscovery/httpx/main/README.md) — README oficial do projectdiscovery/httpx documentando a tabela de probes padrão e opcionais, flags de matchers/filters e captura headless; consultado em 2026-10-03.
- [ProjectDiscovery Official Documentation — httpx Overview (Architecture, Smart HTTPS-to-HTTP Fallback, WAF Retries & Pipeline Usage)](https://docs.projectdiscovery.io/opensource/httpx/overview) — Documentação oficial do httpx explicando o papel da ferramenta na transição entre descoberta de ativos e enriquecimento tecnológico; consultado em 2026-10-03.
- [ProjectDiscovery retryablehttp-go GitHub — README.md](https://github.com/projectdiscovery/retryablehttp-go/blob/main/README.md) — Biblioteca HTTP resiliente subjacente ao ProjectDiscovery httpx; consultado em 2026-10-03.
