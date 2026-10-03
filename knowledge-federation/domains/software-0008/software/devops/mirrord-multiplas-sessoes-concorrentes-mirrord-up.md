---
id: software.devops.tranche09.000898
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

# MetalBear mirrord: execução simultânea de múltiplos microsserviços locais conectados ao cluster com mirrord up

## Em uma frase
Para desenvolvedores que estão alterando vários microsserviços ao mesmo tempo, o comando **`mirrord up`** inicia e gerencia múltiplas sessões concorrentes do `mirrord` a partir de um único arquivo de configuração (funcionando como um `docker compose` para sessões `mirrord`).

## Por que importa
Quando uma funcionalidade nova exige modificar simultaneamente o `api-gateway` (em Go) e o `pricing-service` (em Python) enquanto os outros 30 microsserviços continuam rodando no cluster Kubernetes, abrir vários terminais manuais de `mirrord exec` e coordenar seus logs e encerramentos torna-se trabalhoso. A documentação oficial `What is mirrord?` destaca o comando **`mirrord up`** para esse fluxo multi-serviço.

## Como funciona
O desenvolvedor define um arquivo de composição declarando cada serviço local que deseja subir, seu comando de inicialização, diretório de trabalho, alvo (`target`) no cluster Kubernetes e configurações específicas de rede/ambiente. Ao executar **`mirrord up`**, a CLI inicia todas as sessões do `mirrord` em conjunto, conecta cada processo local ao seu respectivo deployment no cluster (de modo que quando o `api-gateway` local chama o DNS `pricing-service` do cluster, a requisição filtrada no cluster é roteada automaticamente para o `pricing-service` também rodando localmente!) e agrega o ciclo de vida de todas as sessões em um único comando.

## Exemplo
```bash
# Iniciar múltiplas sessões locais de microsserviços conectadas ao cluster a partir de um arquivo de configuração unificado
mirrord up -f mirrord-compose.json
```

## Limites e trade-offs
Ao rodar múltiplos processos pesados localmente com `mirrord up` (especialmente com compiladores em modo watch/hot-reload para 3 ou 4 serviços simultâneos), cada sessão mantém sua própria conexão de agente com o cluster; limite o arquivo do `mirrord up` apenas aos 2 ou 3 serviços nos quais você está ativamente editando código naquela tarefa, deixando todos os demais serviços intocados rodando remotamente no cluster.

## Como verificar
Durante a execução de `mirrord up`, envie uma requisição para o primeiro serviço local que faz uma chamada HTTP interna para o segundo serviço e confirme nos logs unificados que ambos os processos locais atenderam à cadeia da requisição.

## Conexões
- [[mirrord-operador-teams-queue-splitting-db-branching-policies]] — Veja também: MetalBear mirrord: mirrord Operator (Teams), uso concorrente, Queue Splitting, DB Branching e Políticas.
- [[mirrord-enterprise-preview-environments-ci-multicluster-airgap]] — Veja também: MetalBear mirrord: mirrord for CI, Preview Environments, Multi-cluster e operação Air-gapped (Enterprise).
- [[mirrord-execucao-processos-locais-contexto-cluster-kubernetes]] — Referência cruzada direta com mirrord-execucao-processos-locais-contexto-cluster-kubernetes.
- [[mirrord-extensoes-ide-vscode-intellij-configuracao-json]] — Referência cruzada direta com mirrord-extensoes-ide-vscode-intellij-configuracao-json.

## Fontes
- [MetalBear mirrord GitHub — README.md (mirrord exec, IDE Extensions, AI Coding Agents, mirrord-layer/agent & Linux Capabilities)](https://raw.githubusercontent.com/metalbear-co/mirrord/main/README.md) — README oficial do mirrord documentando mirrord exec, extensões VS Code e IntelliJ, uso com agentes de IA (Claude Code, Cursor, Codex), mirrord-layer, mirrord-agent e capabilities CAP_NET_ADMIN/CAP_NET_RAW/CAP_SYS_PTRACE/CAP_SYS_ADMIN; consultado em 2026-10-03.
- [MetalBear mirrord Documentation — What is mirrord? (Mirror vs Steal, File/Env Hooking, mirrord up, Operator Teams, CI & Enterprise)](https://metalbear.com/mirrord/docs/getting-started/what-is-mirrord) — Documentação oficial What is mirrord? detalhando espelhamento/roubo de tráfego, interceptação de arquivos e variáveis no processo, mirrord up, Operator for Teams (Queue splitting, DB branching, Traffic filtering) e mirrord for CI/Enterprise; consultado em 2026-10-03.
- [MetalBear mirrord — Official GitHub Repository](https://github.com/metalbear-co/mirrord) — Repositório oficial MIT do MetalBear mirrord; consultado em 2026-10-03.
