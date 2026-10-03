---
id: software.devops.tranche09.000894
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

# MetalBear mirrord: interceptação de leituras/escritas de arquivos e variáveis de ambiente sem montar volumes no host

## Em uma frase
Em vez de montar volumes de rede no sistema operacional da máquina do desenvolvedor, a `mirrord-layer` intercepta chamadas de abertura, leitura e escrita de arquivos (`open`, `read`, `write`, `stat`) diretamente dentro do processo local e as executa no sistema de arquivos do pod remoto.

## Por que importa
Montar volumes remotos via FUSE/SSHFS/NFS no macOS ou Windows exige instalar drivers de sistema no host e não permite montar caminhos na raiz como `/etc/certs` ou `/var/run/secrets/kubernetes.io/serviceaccount` sem alterar o código da aplicação para ler um prefixo de diretório diferente. Como o `mirrord` intercepta as chamadas `open("/var/run/secrets/...")` dentro do próprio processo, nenhuma linha de código precisa ser alterada e nenhum volume precisa ser montado no SO host.

## Como funciona
Quando o processo iniciado sob `mirrord exec` chama funções de sistema de arquivos ou de ambiente: (1) **File system (`feature.fs`)**: a `mirrord-layer` avalia o caminho solicitado contra as regras configuradas (`mode`: `read`, `write` ou `local`, mais padrões regex `read_only`, `read_write`, `local` e `not_found`). Caminhos de código e bibliotecas locais (como `node_modules` ou `.py`) são lidos localmente para performance máxima, enquanto caminhos de configuração, segredos do Kubernetes e volumes do container são encaminhados ao `mirrord-agent` e lidos/gravados diretamente no filesystem do pod alvo; e (2) **Environment variables (`feature.env`)**: importa todas as variáveis do pod remoto (permitindo incluir/excluir ou sobrescrever variáveis específicas em `override`).

## Exemplo
```bash
# Testar leitura direta do token de ServiceAccount do pod remoto como se o arquivo existisse na máquina local
mirrord exec --target deployment/my-app -- cat /var/run/secrets/kubernetes.io/serviceaccount/namespace
```

## Limites e trade-offs
Se uma aplicação em Node.js, Python ou PHP faz milhares de chamadas `stat`/`open` no boot para carregar pacotes locais em caminhos incomuns que não estejam nas listas padrão de leitura local do `mirrord`, encaminhar essas leituras pela rede até o pod remoto deixará a inicialização lenta; nesses casos, adicione o padrão do diretório local na lista `feature.fs.local` do `.mirrord/mirrord.json`.

## Como verificar
Execute o comando `mirrord exec --target deployment/<seu-app> -- cat /var/run/secrets/kubernetes.io/serviceaccount/namespace` na sua máquina local (onde `/var/run/secrets/kubernetes.io` não existe) e confirme que ele imprime o nome do namespace do pod no cluster.

## Conexões
- [[mirrord-modos-trafego-mirror-vs-steal-filtragem-http]] — Veja também: MetalBear mirrord: modos de tráfego de entrada (mirror padrão vs steal) e roteamento de saída pelo pod remoto.
- [[mirrord-extensoes-ide-vscode-intellij-configuracao-json]] — Veja também: MetalBear mirrord: integração nativa com debuggers de IDEs (VS Code e IntelliJ) e arquivo .mirrord/mirrord.json.
- [[mirrord-execucao-processos-locais-contexto-cluster-kubernetes]] — Referência cruzada direta com mirrord-execucao-processos-locais-contexto-cluster-kubernetes.
- [[mirrord-arquitetura-mirrord-layer-mirrord-agent-capabilities]] — Referência cruzada direta com mirrord-arquitetura-mirrord-layer-mirrord-agent-capabilities.
- [[telepresence-ambiente-remoto-variaveis-montagem-volumes-locais]] — Referência cruzada direta com telepresence-ambiente-remoto-variaveis-montagem-volumes-locais.

## Fontes
- [MetalBear mirrord GitHub — README.md (mirrord exec, IDE Extensions, AI Coding Agents, mirrord-layer/agent & Linux Capabilities)](https://raw.githubusercontent.com/metalbear-co/mirrord/main/README.md) — README oficial do mirrord documentando mirrord exec, extensões VS Code e IntelliJ, uso com agentes de IA (Claude Code, Cursor, Codex), mirrord-layer, mirrord-agent e capabilities CAP_NET_ADMIN/CAP_NET_RAW/CAP_SYS_PTRACE/CAP_SYS_ADMIN; consultado em 2026-10-03.
- [MetalBear mirrord Documentation — What is mirrord? (Mirror vs Steal, File/Env Hooking, mirrord up, Operator Teams, CI & Enterprise)](https://metalbear.com/mirrord/docs/getting-started/what-is-mirrord) — Documentação oficial What is mirrord? detalhando espelhamento/roubo de tráfego, interceptação de arquivos e variáveis no processo, mirrord up, Operator for Teams (Queue splitting, DB branching, Traffic filtering) e mirrord for CI/Enterprise; consultado em 2026-10-03.
- [MetalBear mirrord — Official GitHub Repository](https://github.com/metalbear-co/mirrord) — Repositório oficial MIT do MetalBear mirrord; consultado em 2026-10-03.
