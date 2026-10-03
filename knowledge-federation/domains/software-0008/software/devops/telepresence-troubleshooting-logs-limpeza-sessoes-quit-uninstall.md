---
id: software.devops.tranche09.000890
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-09.md"
fontes: ["https://raw.githubusercontent.com/telepresenceio/telepresence/release/v2/README.md", "https://telepresence.io/docs/concepts/architecture", "https://github.com/telepresenceio/telepresence"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Telepresence: diagnóstico de conectividade (gather-logs, loglevel) e limpeza de agentes e daemons (leave, uninstall, quit)

## Em uma frase
O Telepresence disponibiliza comandos estruturados para encerrar anexações (`telepresence leave`), remover sidecars injetados (`telepresence uninstall`), desconectar e parar daemons locais (`telepresence quit -s`) e coletar pacotes de diagnóstico (`telepresence gather-logs`).

## Por que importa
Se um desenvolvedor fechar o laptop abruptamente ou tiver problemas de firewall/VPN bloqueando o túnel para o `Traffic Manager`, saber como limpar o estado dos daemons locais (`User-Daemon` e `Root-Daemon`), reverter o pod remoto ao estado original e exportar os logs unificados dos daemons e agentes resolve rapidamente problemas operacionais.

## Como funciona
O ciclo de limpeza e diagnóstico possui níveis graduais: (1) **`telepresence leave <workload>`**: encerra uma interceptação/wiretap/replace/ingest ativa, fazendo o `Traffic Agent` voltar a repassar 100% do tráfego para o container original no pod; (2) **`telepresence uninstall <workload>`** (ou `--all-agents`): remove a anotação/sidecar `traffic-agent` do Deployment para que o pod volte a rodar sem o container sidecar; (3) **`telepresence disconnect`** vs **`telepresence quit -s`**: `disconnect` encerra a sessão com o cluster atual, enquanto `quit -s` encerra completamente os processos `User-Daemon` e `Root-Daemon` na estação de trabalho e remove a interface `VIF`; e (4) **`telepresence gather-logs`**: coleta em um único arquivo `.zip` os logs do `User-Daemon`, do `Root-Daemon`, do `Traffic Manager` e de todos os `Traffic Agents` no cluster.

## Exemplo
```bash
# Coletar todos os logs locais e do cluster em um arquivo zip para diagnóstico e encerrar os daemons locais
telepresence gather-logs --output-file /tmp/tp-diagnostico.zip
telepresence quit -s
```

## Limites e trade-offs
Caso a estação de trabalho do desenvolvedor perca completamente a conexão de internet ou entre em suspensão profunda no meio de um `telepresence intercept` sem ter conseguido enviar o comando `telepresence leave`, o `Traffic Manager` no cluster detecta a perda de heartbeat da sessão após o timeout configurado e desativa automaticamente o intercept órfão para restaurar o tráfego do serviço no cluster.

## Como verificar
Após executar `telepresence quit -s`, rode `telepresence status` para confirmar que tanto o `User Daemon` quanto o `Root Daemon` reportam `Not running` e que as rotas virtuais da VIF foram removidas do host.

## Conexões
- [[telepresence-modos-nao-intrusivos-wiretap-ingest-producao-staging]] — Veja também: Telepresence: depuração não-intrusiva com wiretap (cópia de tráfego) e ingest (apenas variáveis/volumes).
- [[telepresence-desenvolvimento-local-remoto-kubernetes-arquitetura]] — Referência cruzada direta com telepresence-desenvolvimento-local-remoto-kubernetes-arquitetura.
- [[telepresence-quatro-modos-anexacao-replace-intercept-wiretap-ingest]] — Referência cruzada direta com telepresence-quatro-modos-anexacao-replace-intercept-wiretap-ingest.
- [[telepresence-gerenciamento-traffic-manager-helm-namespaces-rbac]] — Referência cruzada direta com telepresence-gerenciamento-traffic-manager-helm-namespaces-rbac.

## Fontes
- [Telepresence GitHub — README.md (CNCF Local-to-Cluster Development, 4 Attachment Modes & Traffic Filtering)](https://raw.githubusercontent.com/telepresenceio/telepresence/release/v2/README.md) — README oficial do Telepresence (v2) detalhando eliminação do ciclo build/push/deploy, modos replace/intercept/wiretap/ingest, filtragem HTTP para equipes e importação de ambiente/volumes; consultado em 2026-10-03.
- [Telepresence Official Documentation — Architecture (User-Daemon, Root-Daemon VIF, Traffic Manager & Sidecar vs Node-Agent)](https://telepresence.io/docs/concepts/architecture) — Documentação oficial de arquitetura do Telepresence v2.32 explicando User-Daemon, Root-Daemon (Virtual Network Device VIF), Traffic Manager (telepresence helm install) e Traffic Agent como sidecar ou node-agent sem restart; consultado em 2026-10-03.
- [Telepresence — Official GitHub Repository](https://github.com/telepresenceio/telepresence) — Repositório oficial Apache-2.0 do Telepresence na CNCF; consultado em 2026-10-03.
