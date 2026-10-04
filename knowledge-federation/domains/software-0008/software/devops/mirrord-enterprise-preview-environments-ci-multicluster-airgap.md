---
id: software.devops.tranche09.000899
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

# MetalBear mirrord: mirrord for CI, Preview Environments, Multi-cluster e operação Air-gapped (Enterprise)

## Em uma frase
O mesmo modelo arquitetural do `mirrord` alimenta o **mirrord for CI** (rodando testes de integração/e2e em CI contra um cluster de staging compartilhado sem criar ambientes efêmeros inteiros) e os recursos **Enterprise** como **Preview Environments**, **Multi-cluster** e **License Server Air-gapped**.

## Por que importa
Em pipelines de CI/CD de grandes empresas, subir um cluster Kubernetes inteiro com 40 microsserviços a cada Pull Request para rodar testes end-to-end demora 20 minutos e custa caro em nuvem; usar `mirrord for CI` permite rodar apenas o serviço alterado no runner de CI (ou um pod efêmero leve em `Preview Environments`) conectado ao cluster de staging compartilhado. A página oficial `What is mirrord?` detalha essas capacidades.

## Como funciona
Conforme documentado nas seções `mirrord for CI` e `mirrord for Enterprise`: (1) **mirrord for CI**: o job de CI inicia o serviço sob teste no próprio runner do GitHub Actions/GitLab CI usando `mirrord` conectado ao cluster de staging compartilhado (com filtros de tráfego/filas e DB branching para não afetar outros PRs) e roda os testes e2e contra ele sem fazer deploy da imagem; (2) **Preview Environments**: implanta apenas pods efêmeros isolados dos serviços modificados no cluster para revisão assíncrona e QA, compartilhando o restante do cluster; (3) **Multi-cluster**: intercepta tráfego através de múltiplos clusters Kubernetes em uma única sessão do `mirrord`; e (4) **Air-gapped operation & HA**: executa o `License Server` on-prem sem enviar telemetria externa e roda o Operator em modo de alta disponibilidade (HA).

## Exemplo
```bash
# Executar o binário do serviço e a suíte de testes e2e em um runner de CI conectado ao cluster de staging via mirrord
mirrord ci start --target deployment/orders-api -f .mirrord/mirrord-ci.json -- ./bin/orders-api
```

## Limites e trade-offs
Ao utilizar o **mirrord for CI** contra um cluster de staging compartilhado em múltiplos Pull Requests concorrentes, certifique-se de que os testes de integração enviem o cabeçalho HTTP de correlação daquele job de CI (configurado em `header_filter`) para que cada execução de CI alcance apenas a sua própria instância do serviço sob teste.

## Como verificar
Verifique a conclusão dos testes de integração no pipeline de CI usando `mirrord` sem que o Deployment oficial do cluster de staging tenha sofrido alteração de imagem (`kubectl get deployment <nome> -o wide`).

## Conexões
- [[mirrord-multiplas-sessoes-concorrentes-mirrord-up]] — Veja também: MetalBear mirrord: execução simultânea de múltiplos microsserviços locais conectados ao cluster com mirrord up.
- [[mirrord-alvos-execucao-targetless-pod-deployment-rollout-job]] — Veja também: MetalBear mirrord: tipos de alvos suportados (--target pod, deployment, statefulset, job, argoproj Rollout) e modo targetless.
- [[mirrord-execucao-processos-locais-contexto-cluster-kubernetes]] — Referência cruzada direta com mirrord-execucao-processos-locais-contexto-cluster-kubernetes.
- [[mirrord-operador-teams-queue-splitting-db-branching-policies]] — Referência cruzada direta com mirrord-operador-teams-queue-splitting-db-branching-policies.
- [[mirrord-agentes-ia-claude-code-cursor-codex-testes-cluster]] — Referência cruzada direta com mirrord-agentes-ia-claude-code-cursor-codex-testes-cluster.

## Fontes
- [MetalBear mirrord GitHub — README.md (mirrord exec, IDE Extensions, AI Coding Agents, mirrord-layer/agent & Linux Capabilities)](https://raw.githubusercontent.com/metalbear-co/mirrord/main/README.md) — README oficial do mirrord documentando mirrord exec, extensões VS Code e IntelliJ, uso com agentes de IA (Claude Code, Cursor, Codex), mirrord-layer, mirrord-agent e capabilities CAP_NET_ADMIN/CAP_NET_RAW/CAP_SYS_PTRACE/CAP_SYS_ADMIN; consultado em 2026-10-03.
- [MetalBear mirrord Documentation — What is mirrord? (Mirror vs Steal, File/Env Hooking, mirrord up, Operator Teams, CI & Enterprise)](https://metalbear.com/mirrord/docs/getting-started/what-is-mirrord) — Documentação oficial What is mirrord? detalhando espelhamento/roubo de tráfego, interceptação de arquivos e variáveis no processo, mirrord up, Operator for Teams (Queue splitting, DB branching, Traffic filtering) e mirrord for CI/Enterprise; consultado em 2026-10-03.
- [MetalBear mirrord — Official GitHub Repository](https://github.com/metalbear-co/mirrord) — Repositório oficial MIT do MetalBear mirrord; consultado em 2026-10-03.
