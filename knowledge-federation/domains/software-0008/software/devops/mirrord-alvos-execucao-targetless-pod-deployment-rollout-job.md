---
id: software.devops.tranche09.000900
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
fontes: ["https://raw.githubusercontent.com/metalbear-co/mirrord/main/README.md", "https://metalbear.com/mirrord/docs/getting-started/what-is-mirrord", "https://github.com/metalbear-co/mirrord"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# MetalBear mirrord: tipos de alvos suportados (--target pod, deployment, statefulset, job, argoproj Rollout) e modo targetless

## Em uma frase
O `mirrord` pode se conectar a múltiplos tipos de recursos Kubernetes como alvo (`pod`, `deployment`, `statefulset`, `job`, `cronjob` e `rollout` do Argo Rollouts, selecionando inclusive um `container` específico) ou rodar em modo **targetless** para apenas acessar serviços internos do cluster sem impersonar nenhum pod existente.

## Por que importa
Nem sempre o desenvolvedor quer impersonar um `Deployment` existente: às vezes ele quer depurar um `StatefulSet`, um `Rollout` gerenciado pelo Argo Rollouts ou apenas rodar um script de migração/consulta local que precisa acessar o banco de dados e o DNS interno do cluster sem se atrelar a nenhum pod de aplicação (**targetless mode**).

## Como funciona
Na flag **`--target`** (ou campo `"target"` no `.mirrord/mirrord.json`), o usuário pode especificar a sintaxe `<tipo>/<nome>[/container/<container-name>]`, suportando: (1) `pod/<nome>`; (2) `deployment/<nome>` (onde o `mirrord` seleciona automaticamente um pod saudável do Deployment ou coordena todas as réplicas quando usado com o Operator); (3) `statefulset/<nome>`, `job/<nome>`, `cronjob/<nome>` e `rollout/<nome>` (Argo Rollouts); e (4) **Modo Targetless** (omitindo `--target` ou definindo `"target": "targetless"`): o `mirrord` cria um pod `mirrord-agent` autônomo no namespace selecionado sem se anexar a nenhum pod existente, permitindo que o processo local resolva DNS e faça conexões de saída (`outgoing`) para qualquer Service/Pod do cluster.

## Exemplo
```bash
# Executar um comando local em modo targetless (sem impersonar nenhum pod) apenas para acessar um Service interno do cluster
mirrord exec -n staging -- curl -sSf http://internal-catalog-api.staging.svc.cluster.local:8080/healthz
```

## Limites e trade-offs
Quando você executa o `mirrord` em modo **targetless** (sem um pod alvo), como não há um container de aplicação existente sendo impersonado, o processo local não herda variáveis de ambiente nem sistema de arquivos de nenhum pod específico e não pode receber tráfego de entrada (`incoming`); o modo targetless destina-se exclusivamente ao tráfego de saída (`outgoing`) e resolução DNS para dentro do cluster.

## Como verificar
Execute `mirrord ls` (ou `mirrord ls -n <namespace>`) para listar todos os alvos disponíveis (`pod/...`, `deployment/...`, `rollout/...`) no namespace antes de iniciar `mirrord exec`.

## Conexões
- [[mirrord-enterprise-preview-environments-ci-multicluster-airgap]] — Veja também: MetalBear mirrord: mirrord for CI, Preview Environments, Multi-cluster e operação Air-gapped (Enterprise).
- [[mirrord-execucao-processos-locais-contexto-cluster-kubernetes]] — Referência cruzada direta com mirrord-execucao-processos-locais-contexto-cluster-kubernetes.
- [[mirrord-arquitetura-mirrord-layer-mirrord-agent-capabilities]] — Referência cruzada direta com mirrord-arquitetura-mirrord-layer-mirrord-agent-capabilities.

## Fontes
- [MetalBear mirrord GitHub — README.md (mirrord exec, IDE Extensions, AI Coding Agents, mirrord-layer/agent & Linux Capabilities)](https://raw.githubusercontent.com/metalbear-co/mirrord/main/README.md) — README oficial do mirrord documentando mirrord exec, extensões VS Code e IntelliJ, uso com agentes de IA (Claude Code, Cursor, Codex), mirrord-layer, mirrord-agent e capabilities CAP_NET_ADMIN/CAP_NET_RAW/CAP_SYS_PTRACE/CAP_SYS_ADMIN; consultado em 2026-10-03.
- [MetalBear mirrord Documentation — What is mirrord? (Mirror vs Steal, File/Env Hooking, mirrord up, Operator Teams, CI & Enterprise)](https://metalbear.com/mirrord/docs/getting-started/what-is-mirrord) — Documentação oficial What is mirrord? detalhando espelhamento/roubo de tráfego, interceptação de arquivos e variáveis no processo, mirrord up, Operator for Teams (Queue splitting, DB branching, Traffic filtering) e mirrord for CI/Enterprise; consultado em 2026-10-03.
- [MetalBear mirrord — Official GitHub Repository](https://github.com/metalbear-co/mirrord) — Repositório oficial MIT do MetalBear mirrord; consultado em 2026-10-03.
