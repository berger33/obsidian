---
id: software.devops.tranche07.000650
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-07.md"
fontes: ["https://raw.githubusercontent.com/kubescape/kubescape/master/README.md", "https://kubescape.io/docs/operator/", "https://github.com/kubescape/kubescape"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Kubescape: filtragem de escopo por namespaces, execução de controles individuais e gerenciamento de cache

## Em uma frase
A CLI do Kubescape permite restringir varreduras por inclusão/exclusão de namespaces (`--include-namespaces` / `--exclude-namespaces`), auditar controles isolados (`kubescape scan control`) e gerenciar configurações em cache (`kubescape config`).

## Por que importa
Em clusters Kubernetes compartilhados de grande porte, escanear todos os namespaces (incluindo `kube-system`, `kube-public` e operadores de terceiros) quando uma equipe de produto deseja validar apenas seus ambientes `staging` e `production` desperdiça tempo e mistura alertas de infraestrutura com problemas da aplicação. O README oficial do Kubescape detalha as flags de escopo, seleção de controles e gerenciamento de cache local.

## Como funciona
Durante uma varredura de cluster, as flags `--include-namespaces production,staging` ou `--exclude-namespaces kube-system,kube-public` filtram os recursos coletados da API do Kubernetes (usando o contexto padrão ou um arquivo alternativo via `--kubeconfig /path/to/kubeconfig`). Quando o objetivo é verificar rapidamente a correção de uma única falha apontada anteriormente, o comando `kubescape scan control <ID-ou-nome> -v` (por exemplo, `C-0005`) avalia apenas aquela regra Rego em vez de rodar um framework inteiro. Já o subcomando `kubescape config` (`view`, `set`, `delete`) gerencia as configurações persistidas localmente em cache pelo cliente CLI.

## Exemplo
```bash
# Escanear apenas namespaces de aplicação excluindo componentes de sistema e focar em um controle específico
kubescape scan control C-0005 -v \
  --include-namespaces production,staging \
  --kubeconfig ~/.kube/config

# Visualizar e limpar a configuração em cache da CLI do Kubescape
kubescape config view
kubescape config delete
```

## Limites e trade-offs
Excluir o namespace `kube-system` com `--exclude-namespaces kube-system` é útil para relatórios voltados a equipes de desenvolvimento de aplicações, mas oculta problemas críticos de segurança de infraestrutura (como configurações permissivas do CoreDNS, proxies ou DaemonSets privilegiados); portanto, auditorias de segurança de plataforma devem sempre incluir o `kube-system` em uma execução separada.

## Como verificar
Execute `kubescape list controls --format json | jq '.[0]'` para identificar o ID de um controle e rode `kubescape scan control <ID> --include-namespaces default -v` para inspecionar a avaliação detalhada recurso por recurso.

## Conexões
- [[kubescape-integracao-cicd-github-actions-gitlab-megalinter-sarif]] — Veja também: Kubescape: integração em pipelines CI/CD com GitHub Actions, GitLab CI, Jenkins, MegaLinter e relatórios SARIF/JUnit.
- [[kubescape-plataforma-seguranca-kubernetes-opa-regolibrary]] — Referência cruzada direta com kubescape-plataforma-seguranca-kubernetes-opa-regolibrary.
- [[kubescape-execucao-offline-air-gapped-protecao-metadados]] — Referência cruzada direta com kubescape-execucao-offline-air-gapped-protecao-metadados.

## Fontes
- [Kubescape GitHub — README.md (OPA/Regolibrary, Grype, Copacetic, VAP, Operator & MCP)](https://raw.githubusercontent.com/kubescape/kubescape/master/README.md) — README oficial do Kubescape documentando varredura de postura com OPA/Regolibrary, CVEs de imagens com Grype, auto-fix, patching com Copacetic, Validating Admission Policies (CEL) e MCP server; consultado em 2026-10-03.
- [Kubescape Official Documentation — In-Cluster Operator & Runtime Security](https://kubescape.io/docs/operator/) — Documentação oficial do operador in-cluster do Kubescape com monitoramento contínuo e detecção de ameaças em runtime via eBPF (Inspektor Gadget); consultado em 2026-10-03.
- [Kubescape — Official GitHub Repository](https://github.com/kubescape/kubescape) — Repositório oficial Apache-2.0 do Kubescape (CNCF Incubating); consultado em 2026-10-03.
