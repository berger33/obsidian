---
id: software.devops.tranche09.000891
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

# MetalBear mirrord: execução de processos locais no contexto de um cluster Kubernetes em tempo real

## Em uma frase
O `mirrord` (`metalbear-co/mirrord`, licenciado sob MIT) executa o processo local da máquina do desenvolvedor (ou de um agente de IA) diretamente no contexto de um cluster Kubernetes ao vivo, roteando tráfego, leituras/escritas de arquivos e variáveis de ambiente através de um pod alvo sem VPN, sem root local e sem deploy.

## Por que importa
Ferramentas tradicionais de túnel de rede exigem privilégios de `root` na máquina do desenvolvedor para criar interfaces VPN (`tun`) e alteram o roteamento de toda a estação de trabalho, além de não interceptarem chamadas de sistema de arquivos no nível do processo. Segundo o README oficial e a página `What is mirrord?` (`metalbear.com/mirrord/docs/getting-started/what-is-mirrord`), o `mirrord` atua exclusivamente sobre o processo iniciado (`mirrord exec`), entregando o feedback de um deploy em segundos sem afetar o resto da máquina nem o cluster.

## Como funciona
Quando o usuário inicia seu processo com **`mirrord exec <comando> --target <alvo>`** (ou através das extensões oficiais para **VS Code** e **IntelliJ**), o `mirrord` atua em dois pontos: (1) injeta uma camada fina chamada **`mirrord-layer`** dentro do processo local (via `LD_PRELOAD` no Linux ou `DYLD_INSERT_LIBRARIES` no macOS) que intercepta chamadas de sistema de baixo nível (`libc` para sockets de rede, abertura/leitura/gravação de arquivos e variáveis de ambiente); e (2) lança um pod efêmero chamado **`mirrord-agent`** no mesmo nó Kubernetes onde roda o pod alvo (`pod/my-pod` ou `deployment/my-app`), conectando a `mirrord-layer` ao `mirrord-agent` para espelhar/roubar tráfego de entrada, enviar tráfego de saída pelo pod remoto, ler/gravar arquivos remotos e importar variáveis de ambiente.

## Exemplo
```bash
# Executar um processo Node.js local no contexto do pod/my-pod no cluster Kubernetes usando mirrord exec
mirrord exec --target pod/my-pod -- node app.js
```

## Limites e trade-offs
Como a `mirrord-layer` intercepta chamadas de sistema na máquina local usando injeção de biblioteca dinâmica (`DYLD_INSERT_LIBRARIES` no macOS), binários protegidos pelo System Integrity Protection (SIP) do macOS (como binários em `/bin` ou `/usr/bin`) removem variáveis `DYLD_*` por segurança; o `mirrord` contorna isso automaticamente copiando/assinando binários temporários quando necessário no macOS, mas em binários Linux 100% estáticos que fazem syscalls diretas sem passar pela `libc` (exceto Go, que o mirrord suporta enganchando o runtime Go), deve-se verificar a matriz de suporte de linguagens.

## Como verificar
Instale o `mirrord` (`brew install metalbear-co/mirrord/mirrord` ou script `install.sh`), execute `mirrord --version` e rode `mirrord exec --target deployment/meu-app -- env` para confirmar a importação imediata das variáveis de ambiente do pod remoto.

## Conexões
- [[mirrord-arquitetura-mirrord-layer-mirrord-agent-capabilities]] — Veja também: MetalBear mirrord: arquitetura mirrord-layer e mirrord-agent e gerenciamento de Linux Capabilities.
- [[mirrord-modos-trafego-mirror-vs-steal-filtragem-http]] — Referência cruzada direta com mirrord-modos-trafego-mirror-vs-steal-filtragem-http.
- [[telepresence-desenvolvimento-local-remoto-kubernetes-arquitetura]] — Referência cruzada direta com telepresence-desenvolvimento-local-remoto-kubernetes-arquitetura.

## Fontes
- [MetalBear mirrord GitHub — README.md (mirrord exec, IDE Extensions, AI Coding Agents, mirrord-layer/agent & Linux Capabilities)](https://raw.githubusercontent.com/metalbear-co/mirrord/main/README.md) — README oficial do mirrord documentando mirrord exec, extensões VS Code e IntelliJ, uso com agentes de IA (Claude Code, Cursor, Codex), mirrord-layer, mirrord-agent e capabilities CAP_NET_ADMIN/CAP_NET_RAW/CAP_SYS_PTRACE/CAP_SYS_ADMIN; consultado em 2026-10-03.
- [MetalBear mirrord Documentation — What is mirrord? (Mirror vs Steal, File/Env Hooking, mirrord up, Operator Teams, CI & Enterprise)](https://metalbear.com/mirrord/docs/getting-started/what-is-mirrord) — Documentação oficial What is mirrord? detalhando espelhamento/roubo de tráfego, interceptação de arquivos e variáveis no processo, mirrord up, Operator for Teams (Queue splitting, DB branching, Traffic filtering) e mirrord for CI/Enterprise; consultado em 2026-10-03.
- [MetalBear mirrord — Official GitHub Repository](https://github.com/metalbear-co/mirrord) — Repositório oficial MIT do MetalBear mirrord; consultado em 2026-10-03.
