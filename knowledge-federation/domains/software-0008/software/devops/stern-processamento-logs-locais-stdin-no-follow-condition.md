---
id: software.devops.tranche10.000995
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

# Stern: leitura de logs via entrada padrão (--stdin), execução única (--no-follow) e filtro por condição (--condition)

## Em uma frase
O Stern pode operar como um formatador e filtro de logs locais sem conectar-se ao Kubernetes usando **`--stdin`**, encerrar automaticamente após mostrar os logs atuais com **`--no-follow`** e filtrar pods por condições de status (como `Ready=false`) com **`--condition`**.

## Por que importa
Em scripts de coleta de diagnóstico de CI/CD (onde o comando precisa capturar os logs existentes e **sair** em vez de ficar bloqueado esperando novos logs eternamente), o modo `--no-follow` é obrigatório; já ao analisar arquivos de log salvos em disco, `--stdin` permite aplicar todo o poder de templates Go (`prettyJSON`, `levelColor`, `-H`, `-e`) do Stern sobre arquivos locais.

## Como funciona
Conforme especifica a tabela de flags do README oficial: (1) **`--stdin`**: faz o Stern ler e processar linhas de log vindas da entrada padrão (`cat app.log | stern --stdin -H ERROR`), ignorando todas as flags relacionadas ao Kubernetes; (2) **`--no-follow`**: imprime todos os logs encontrados nos pods selecionados e encerra o processo imediatamente com código `0`; e (3) **`--condition <condition-name>[=<condition-value>]`** (onde o valor padrão é `true`, case-insensitive): filtra pods com base em suas `status.conditions` (por exemplo, `--condition Ready=false`), sendo suportado em conjunto com `--tail=0` ou `--no-follow`.

## Exemplo
```bash
# Coletar todos os logs recentes dos pods de um job/deployment e encerrar imediatamente (--no-follow) para uso em CI
stern job/db-migration -n staging --since 15m --no-follow > /tmp/migration-logs.txt
```

## Limites e trade-offs
Conforme documenta a tabela oficial de flags da CLI para `--max-log-requests`, quando você usa **`--no-follow`** sem especificar `--max-log-requests`, o limite padrão de requisições concorrentes de log cai de `50` (no modo streaming normal) para **`5`**; se o seu comando `stern --no-follow` precisar coletar logs de 20 pods no mesmo deployment, passe explicitamente **`--max-log-requests 50`** para que ele não aborte ao atingir 5 fluxos de log!

## Como verificar
Execute `echo '{"level":"info","msg":"hello stern"}' | stern --stdin --template '{{prettyJSON .Message}}'` no terminal local (sem precisar de cluster Kubernetes) para validar o modo `--stdin`.

## Conexões
- [[stern-formatos-saida-output-templates-go-funcoes-json]] — Veja também: Stern: modos de saída (--output default, raw, json, extjson, ppextjson) e templates Go customizados (--template).
- [[stern-limites-concorrencia-max-log-requests-qps-burst-api]] — Veja também: Stern: controle de concorrência e proteção do API Server (--max-log-requests, --qps, --burst e --verbosity).
- [[stern-tail-logs-multi-pod-multi-container-kubernetes]] — Referência cruzada direta com stern-tail-logs-multi-pod-multi-container-kubernetes.

## Fontes
- [Stern GitHub — README.md (Multi-Pod & Container Log Tailing, CLI Flags Table, ~/.config/stern/config.yaml & Go Templates/JSON Functions)](https://raw.githubusercontent.com/stern/stern/master/README.md) — README oficial do stern/stern (Apache-2.0) detalhando pod-query por regex ou <resource>/<name>, tabela completa de flags da CLI, arquivo ~/.config/stern/config.yaml, modos --output e funções de template Go/JSON; consultado em 2026-10-03.
- [Stern GitHub — CONTRIBUTING.md & Official Repository Guidelines](https://raw.githubusercontent.com/stern/stern/master/CONTRIBUTING.md) — Diretrizes oficiais do repositório stern/stern; consultado em 2026-10-03.
- [Stern — Official GitHub Repository](https://github.com/stern/stern) — Repositório oficial do Stern; consultado em 2026-10-03.
