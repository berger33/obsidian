---
id: software.devops.tranche10.000996
tipo: tecnica
dominio: software
subdominio: devops
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-10.md"
fontes: ["https://raw.githubusercontent.com/stern/stern/master/README.md", "https://raw.githubusercontent.com/stern/stern/master/CONTRIBUTING.md", "https://github.com/stern/stern"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Stern: controle de concorrência e proteção do API Server (--max-log-requests, --qps, --burst e --verbosity)

## Em uma frase
Para evitar sobrecarregar o API Server do Kubernetes e os `kubelet`s ao observar dezenas de pods simultaneamente, o Stern controla o número máximo de streams concorrentes com **`--max-log-requests`** (padrão 50) e a taxa de chamadas à API com **`--qps`** e **`--burst`**.

## Por que importa
Em um cluster de produção onde um `Deployment` escalou para 120 pods (com 2 containers cada = 240 streams de log), abrir 240 conexões HTTP de streaming simultâneas contra o API Server causaria throttling severo no cliente (`client-go`) ou sobrecarga no control plane; por outro lado, quando o operador realmente precisa observar mais de 50 containers, ele precisa saber ajustar `--max-log-requests`.

## Como funciona
Conforme documenta a tabela de flags e a seção `Log level verbosity` do README oficial: (1) **`--max-log-requests`**: define o número máximo de streams de log concorrentes que o Stern abrirá simultaneamente (padrão **`50`** em modo follow e **`5`** quando `--no-follow` é especificado); (2) **`--qps`** e **`--burst`**: controlam o rate limiter client-side para o API Server do Kubernetes (padrão `0`, que usa os defaults do `client-go`; passar `--qps=-1` desabilita o throttling client-side); e (3) **`--verbosity`**: aumenta o nível de detalhe dos logs internos do próprio Stern para inspecionar como ele está interagindo com o API Server do Kubernetes durante troubleshooting.

## Exemplo
```bash
# Aumentar o limite de streams simultâneos (--max-log-requests) e a taxa de QPS/Burst ao observar um deployment grande
stern deployment/high-scale-worker --max-log-requests 150 --qps 50 --burst 100 --tail 10
```

## Limites e trade-offs
Embora seja possível colocar `max-log-requests: 999` no arquivo `~/.config/stern/config.yaml` (como mostrado no próprio exemplo de configuração da documentação oficial), em clusters compartilhados combine limites altos de `max-log-requests` sempre com `--tail 10` ou `--since 1m` para que abrir centenas de streams não transfira gigabytes de logs históricos de 48 horas de uma só vez pelo API Server.

## Como verificar
Execute `stern . -n kube-system --tail 1 --verbosity 6` para observar nos logs de diagnóstico as requisições `GET` feitas pelo Stern ao API Server do Kubernetes.

## Conexões
- [[stern-processamento-logs-locais-stdin-no-follow-condition]] — Veja também: Stern: leitura de logs via entrada padrão (--stdin), execução única (--no-follow) e filtro por condição (--condition).
- [[stern-configuracao-persistente-config-yaml-cores-prompt]] — Veja também: Stern: arquivo de configuração persistente (~/.config/stern/config.yaml), customização de cores SGR e modo --prompt.
- [[stern-tail-logs-multi-pod-multi-container-kubernetes]] — Referência cruzada direta com stern-tail-logs-multi-pod-multi-container-kubernetes.

## Fontes
- [Stern GitHub — README.md (Multi-Pod & Container Log Tailing, CLI Flags Table, ~/.config/stern/config.yaml & Go Templates/JSON Functions)](https://raw.githubusercontent.com/stern/stern/master/README.md) — README oficial do stern/stern (Apache-2.0) detalhando pod-query por regex ou <resource>/<name>, tabela completa de flags da CLI, arquivo ~/.config/stern/config.yaml, modos --output e funções de template Go/JSON; consultado em 2026-10-03.
- [Stern GitHub — CONTRIBUTING.md & Official Repository Guidelines](https://raw.githubusercontent.com/stern/stern/master/CONTRIBUTING.md) — Diretrizes oficiais do repositório stern/stern; consultado em 2026-10-03.
- [Stern — Official GitHub Repository](https://github.com/stern/stern) — Repositório oficial do Stern; consultado em 2026-10-03.
