---
id: software.devops.tranche09.000897
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

# MetalBear mirrord: mirrord Operator (Teams), uso concorrente, Queue Splitting, DB Branching e Políticas

## Em uma frase
O plano **mirrord for Teams** adiciona o **mirrord Operator** no cluster Kubernetes como um plano de controle centralizado que habilita uso concorrente no mesmo alvo, **Traffic filtering**, **Queue splitting** (divisão de filas Kafka/SQS/RMQ), **DB branching** (branches efêmeros de banco por sessão) e políticas RBAC.

## Por que importa
No modo open-source básico (sem operador), o `mirrord` gerencia apenas conexões TCP/HTTP diretas; porém, em arquiteturas orientadas a eventos (onde o serviço consome de uma fila Kafka, SQS ou RabbitMQ) ou quando dois desenvolvedores precisam alterar dados no banco durante uma sessão de debug, é necessário dividir mensagens da fila por filtro e isolar o banco de dados por sessão. A seção `mirrord for Teams` em `What is mirrord?` detalha essas seis capacidades do Operator.

## Como funciona
Instalado no cluster Kubernetes, o **mirrord Operator** coordena todas as sessões ativas sem que os clientes precisem de permissões RBAC para criar pods `mirrord-agent` diretamente: (1) **Concurrent usage**: múltiplos desenvolvedores podem trabalhar no mesmo pod/deployment simultaneamente sem conflitos; (2) **Traffic filtering**: roteia apenas requisições HTTP específicas (por header, path ou método) para cada processo local; (3) **Queue splitting**: divide o tráfego de filas de mensagens (Kafka, SQS, RabbitMQ) para que cada desenvolvedor receba em sua máquina apenas as mensagens que casam com seus filtros; (4) **DB branching**: cria branches efêmeros de banco de dados (MySQL, Postgres, MongoDB) por sessão do mirrord para isolar escritas; (5) **Policies and profiles** (`MirrordPolicy`); e (6) **Session management**.

## Exemplo
```bash
# Inspecionar todas as sessões ativas gerenciadas pelo mirrord Operator no cluster e encerrar sessões se necessário
mirrord operator status
```

## Limites e trade-offs
Enquanto o núcleo open-source do `mirrord` funciona de forma 100% client-side sem precisar instalar nada previamente no cluster (criando o pod `mirrord-agent` sob demanda via API do Kubernetes), os recursos marcados com **`[Teams]`** (uso concorrente no mesmo alvo, Queue splitting, DB branching e `MirrordPolicy`) exigem o **mirrord Operator** instalado no cluster com licença ativa (ou trial).

## Como verificar
Em um cluster com o mirrord Operator instalado, execute `mirrord operator status` para verificar a versão do operador, as sessões concorrentes ativas e as políticas aplicadas.

## Conexões
- [[mirrord-agentes-ia-claude-code-cursor-codex-testes-cluster]] — Veja também: MetalBear mirrord: desenvolvimento e verificação end-to-end para agentes de codificação de IA (Claude Code, Cursor, Codex).
- [[mirrord-multiplas-sessoes-concorrentes-mirrord-up]] — Veja também: MetalBear mirrord: execução simultânea de múltiplos microsserviços locais conectados ao cluster com mirrord up.
- [[mirrord-execucao-processos-locais-contexto-cluster-kubernetes]] — Referência cruzada direta com mirrord-execucao-processos-locais-contexto-cluster-kubernetes.
- [[mirrord-modos-trafego-mirror-vs-steal-filtragem-http]] — Referência cruzada direta com mirrord-modos-trafego-mirror-vs-steal-filtragem-http.
- [[mirrord-enterprise-preview-environments-ci-multicluster-airgap]] — Referência cruzada direta com mirrord-enterprise-preview-environments-ci-multicluster-airgap.

## Fontes
- [MetalBear mirrord GitHub — README.md (mirrord exec, IDE Extensions, AI Coding Agents, mirrord-layer/agent & Linux Capabilities)](https://raw.githubusercontent.com/metalbear-co/mirrord/main/README.md) — README oficial do mirrord documentando mirrord exec, extensões VS Code e IntelliJ, uso com agentes de IA (Claude Code, Cursor, Codex), mirrord-layer, mirrord-agent e capabilities CAP_NET_ADMIN/CAP_NET_RAW/CAP_SYS_PTRACE/CAP_SYS_ADMIN; consultado em 2026-10-03.
- [MetalBear mirrord Documentation — What is mirrord? (Mirror vs Steal, File/Env Hooking, mirrord up, Operator Teams, CI & Enterprise)](https://metalbear.com/mirrord/docs/getting-started/what-is-mirrord) — Documentação oficial What is mirrord? detalhando espelhamento/roubo de tráfego, interceptação de arquivos e variáveis no processo, mirrord up, Operator for Teams (Queue splitting, DB branching, Traffic filtering) e mirrord for CI/Enterprise; consultado em 2026-10-03.
- [MetalBear mirrord — Official GitHub Repository](https://github.com/metalbear-co/mirrord) — Repositório oficial MIT do MetalBear mirrord; consultado em 2026-10-03.
