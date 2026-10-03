---
id: software.devops.tranche09.000892
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

# MetalBear mirrord: arquitetura mirrord-layer e mirrord-agent e gerenciamento de Linux Capabilities

## Em uma frase
No modo open-source sem operador, o `mirrord` agenda um pod efêmero `mirrord-agent` no mesmo nó do pod alvo utilizando as capabilities Linux `CAP_NET_ADMIN`, `CAP_NET_RAW`, `CAP_SYS_PTRACE` e `CAP_SYS_ADMIN` (desativáveis via `MIRRORD_AGENT_DISABLED_CAPABILITIES`).

## Por que importa
Diferentemente de ferramentas que exigem instalar previamente um servidor no cluster ou injetar um sidecar permanente que reinicia o Deployment da aplicação, o `mirrord` cria o `mirrord-agent` sob demanda no mesmo nó do pod alvo e o destrói assim que o processo local termina. Porém, administradores de clusters com políticas estritas de Pod Security Standards precisam saber exatamente quais capabilities o `mirrord-agent` usa e como restringi-las. A seção `How It Works -> Additional capabilities` do README oficial detalha cada uma.

## Como funciona
Quando `mirrord exec --target pod/my-pod` inicia, ele usa o `kubeconfig` padrão da máquina para criar o pod efêmero **`mirrord-agent`** agendado no mesmo `nodeName` de `my-pod`. Por padrão, o container do `mirrord-agent` solicita quatro Linux capabilities específicas para acessar o contexto do pod alvo sem modificá-lo: (1) **`CAP_NET_ADMIN`** e **`CAP_NET_RAW`**: para modificar tabelas de roteamento e capturar pacotes de rede; (2) **`CAP_SYS_PTRACE`**: para ler o ambiente e descritores do processo do pod alvo; e (3) **`CAP_SYS_ADMIN`**: para entrar no namespace de rede e mount do pod alvo. Caso a política de segurança do cluster proíba alguma dessas capabilities, o usuário pode desabilitá-las via configuração ou variável **`MIRRORD_AGENT_DISABLED_CAPABILITIES`**.

## Exemplo
```bash
# Executar mirrord exec desabilitando capabilities específicas no container do mirrord-agent conforme o README oficial
MIRRORD_AGENT_DISABLED_CAPABILITIES=CAP_NET_RAW,CAP_SYS_PTRACE mirrord exec --target pod/my-pod -- node app.js
```

## Limites e trade-offs
Conforme adverte a seção `Additional capabilities` do README oficial do `mirrord`, desabilitar um subconjunto dessas capabilities com `MIRRORD_AGENT_DISABLED_CAPABILITIES` permite rodar em clusters mais restritivos, mas limitará as funcionalidades correspondentes do `mirrord` (por exemplo, sem `CAP_NET_RAW`/`CAP_NET_ADMIN` o agente não poderá capturar ou redirecionar tráfego de entrada do pod alvo) ou pode torná-lo inutilizável em determinados setups.

## Como verificar
Durante a execução de `mirrord exec`, abra outro terminal e rode `kubectl get pods` para observar o pod efêmero `mirrord-agent-*` em execução no mesmo nó do alvo, e confirme que ele desaparece automaticamente ao encerrar o processo local (`Ctrl+C`).

## Conexões
- [[mirrord-execucao-processos-locais-contexto-cluster-kubernetes]] — Veja também: MetalBear mirrord: execução de processos locais no contexto de um cluster Kubernetes em tempo real.
- [[mirrord-modos-trafego-mirror-vs-steal-filtragem-http]] — Veja também: MetalBear mirrord: modos de tráfego de entrada (mirror padrão vs steal) e roteamento de saída pelo pod remoto.
- [[youki-inspecao-capacidades-kernel-bpf-checkpoint-restore-info]] — Referência cruzada direta com youki-inspecao-capacidades-kernel-bpf-checkpoint-restore-info.

## Fontes
- [MetalBear mirrord GitHub — README.md (mirrord exec, IDE Extensions, AI Coding Agents, mirrord-layer/agent & Linux Capabilities)](https://raw.githubusercontent.com/metalbear-co/mirrord/main/README.md) — README oficial do mirrord documentando mirrord exec, extensões VS Code e IntelliJ, uso com agentes de IA (Claude Code, Cursor, Codex), mirrord-layer, mirrord-agent e capabilities CAP_NET_ADMIN/CAP_NET_RAW/CAP_SYS_PTRACE/CAP_SYS_ADMIN; consultado em 2026-10-03.
- [MetalBear mirrord Documentation — What is mirrord? (Mirror vs Steal, File/Env Hooking, mirrord up, Operator Teams, CI & Enterprise)](https://metalbear.com/mirrord/docs/getting-started/what-is-mirrord) — Documentação oficial What is mirrord? detalhando espelhamento/roubo de tráfego, interceptação de arquivos e variáveis no processo, mirrord up, Operator for Teams (Queue splitting, DB branching, Traffic filtering) e mirrord for CI/Enterprise; consultado em 2026-10-03.
- [MetalBear mirrord — Official GitHub Repository](https://github.com/metalbear-co/mirrord) — Repositório oficial MIT do MetalBear mirrord; consultado em 2026-10-03.
