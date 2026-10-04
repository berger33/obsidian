---
id: software.devops.tranche10.000992
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

# Stern: seleção granular de pods e containers (--selector, --field-selector, --node, --container e --container-state)

## Em uma frase
Conforme a tabela oficial de flags da CLI no README do Stern, além da `pod-query`, é possível filtrar alvos por label selector (`-l`), field selector (`--field-selector`), nó (`--node`), expressões regulares de inclusão/exclusão de containers (`-c` / `-E`), exclusão de pods (`--exclude-pod`) e estado do container (`--container-state`).

## Por que importa
Em clusters com service mesh (Istio/Linkerd) ou agentes de coleta de logs, cada pod possui um container sidecar `istio-proxy` que emite centenas de linhas de access log por segundo; durante a investigação de um bug de negócio, você frequentemente quer ver os logs de todos os pods com a label `app=orders`, mas **excluindo** o container `istio-proxy` ou filtrando apenas containers que terminaram com erro (`terminated`).

## Como funciona
As flags de seleção de alvos do Stern combinam-se de forma flexível: (1) **Seletores sem pod-query**: ao passar **`--selector` (`-l`)** ou **`--field-selector`**, a `pod-query` assume automaticamente o padrão `".*"` (não sendo necessário digitar `.` na linha de comando); (2) **Filtro por nó (`--node`)**: acompanha apenas os pods agendados em um nó worker específico; (3) **Filtros de Container**: `--container` (`-c`, regex, padrão `.*`), `--exclude-container` (`-E`, regex para ignorar sidecars como `-E istio-proxy`), `--init-containers=true|false` e `--ephemeral-containers=true|false`; e (4) **Estado do Container (`--container-state`)**: aceita `running`, `waiting`, `terminated` ou `all` (padrão `all`, podendo passar múltiplos estados separados por vírgula).

## Exemplo
```bash
# Acompanhar pods pelo label selector (-l) em todos os namespaces (-A), excluindo o container sidecar istio-proxy (-E)
stern -A -l app.kubernetes.io/part-of=payments -E "istio-proxy|envoy" --tail 20
```

## Limites e trade-offs
Quando você passa a flag **`--all-namespaces` (`-A`)**, conforme documenta a tabela oficial de flags da CLI do Stern, qualquer namespace específico que tenha sido passado junto na flag `--namespace` (`-n`) é ignorado; se você quiser acompanhar apenas 2 ou 3 namespaces específicos sem buscar no cluster inteiro, repita a flag `-n` ou passe os nomes separados por vírgula (**`-n staging,production`**).

## Como verificar
Execute `stern -l k8s-app=kube-dns -n kube-system --tail 10` (sem passar `pod-query` posicional) e confirme que o Stern assume `.*` automaticamente quando `-l` está presente.

## Conexões
- [[stern-tail-logs-multi-pod-multi-container-kubernetes]] — Veja também: Stern: tailing dinâmico de logs de múltiplos pods e múltiplos containers no Kubernetes com codificação por cores.
- [[stern-filtragem-linhas-include-exclude-highlight-timestamps]] — Veja também: Stern: filtragem e destaque de conteúdo de logs por Regex (--include, --exclude, --highlight) e formatação de timestamps (-t).
- [[stern-formatos-saida-output-templates-go-funcoes-json]] — Referência cruzada direta com stern-formatos-saida-output-templates-go-funcoes-json.

## Fontes
- [Stern GitHub — README.md (Multi-Pod & Container Log Tailing, CLI Flags Table, ~/.config/stern/config.yaml & Go Templates/JSON Functions)](https://raw.githubusercontent.com/stern/stern/master/README.md) — README oficial do stern/stern (Apache-2.0) detalhando pod-query por regex ou <resource>/<name>, tabela completa de flags da CLI, arquivo ~/.config/stern/config.yaml, modos --output e funções de template Go/JSON; consultado em 2026-10-03.
- [Stern GitHub — CONTRIBUTING.md & Official Repository Guidelines](https://raw.githubusercontent.com/stern/stern/master/CONTRIBUTING.md) — Diretrizes oficiais do repositório stern/stern; consultado em 2026-10-03.
- [Stern — Official GitHub Repository](https://github.com/stern/stern) — Repositório oficial do Stern; consultado em 2026-10-03.
