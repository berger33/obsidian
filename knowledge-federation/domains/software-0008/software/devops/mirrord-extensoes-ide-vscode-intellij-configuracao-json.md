---
id: software.devops.tranche09.000895
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

# MetalBear mirrord: integração nativa com debuggers de IDEs (VS Code e IntelliJ) e arquivo .mirrord/mirrord.json

## Em uma frase
O `mirrord` é distribuído tanto como ferramenta CLI quanto como extensão oficial do **VS Code** (`MetalBear.mirrord`) e plugin do **IntelliJ / JetBrains IDEs** (`plugin 19772`), acoplando-se diretamente ao botão "Start Debugging" da IDE e lendo configurações de `.mirrord/mirrord.json`.

## Por que importa
Desenvolvedores passam a maior parte do tempo dentro da IDE colocando breakpoints visuais, inspecionando variáveis na pilha de execução e recarregando código; se conectar o processo ao cluster exigisse sair da IDE e montar comandos complexos de terminal a cada execução de debug, a fricção reduziria a adoção pela equipe. As seções `VS Code Extension` e `IntelliJ Plugin` do README oficial demonstram o fluxo de um clique.

## Como funciona
(1) **VS Code Extension**: adiciona o botão `"Enable mirrord"` na barra de status inferior do VS Code; quando ativado, clicar em *Start Debugging* (`F5`) abre um seletor rápido de namespace e pod/deployment para impersonar (ou usa o alvo já definido em **`.mirrord/mirrord.json`**) e injeta a `mirrord-layer` automaticamente no processo depurado; (2) **IntelliJ Plugin**: adiciona o ícone do `mirrord` na Navigation Toolbar das IDEs JetBrains (IntelliJ IDEA, GoLand, PyCharm, WebStorm, Rider, RustRover), funcionando com qualquer Run/Debug Configuration existente; e (3) **`.mirrord/mirrord.json` (ou `.toml`/`.yaml`)**: arquivo versionável no repositório que padroniza o alvo (`target`), modo de rede (`mirror`/`steal`), filtros HTTP, regras de arquivos e variáveis de ambiente para toda a equipe.

## Exemplo
```json
{
  "$schema": "https://raw.githubusercontent.com/metalbear-co/mirrord/main/mirrord-schema.json",
  "target": {
    "path": "deployment/payment-api",
    "namespace": "staging"
  },
  "feature": {
    "env": true,
    "fs": "read",
    "network": true
  }
}
```

## Limites e trade-offs
Ao versionar o arquivo `.mirrord/mirrord.json` no Git para compartilhamento da equipe, utilize expressões de template ou variáveis de ambiente (como `"header_filter": "x-user: {{ get_env(name=\"USER\", default=\"dev\") }}"`) para que dois desenvolvedores usando a mesma configuração no VS Code/IntelliJ não tentem roubar (`steal`) exatamente o mesmo cabeçalho estático ao mesmo tempo.

## Como verificar
Adicione a propriedade `"$schema": "https://raw.githubusercontent.com/metalbear-co/mirrord/main/mirrord-schema.json"` no topo do arquivo `.mirrord/mirrord.json` e verifique o autocompletar e a validação de campos na IDE.

## Conexões
- [[mirrord-interceptacao-sistema-arquivos-variaveis-ambiente-libc]] — Veja também: MetalBear mirrord: interceptação de leituras/escritas de arquivos e variáveis de ambiente sem montar volumes no host.
- [[mirrord-agentes-ia-claude-code-cursor-codex-testes-cluster]] — Veja também: MetalBear mirrord: desenvolvimento e verificação end-to-end para agentes de codificação de IA (Claude Code, Cursor, Codex).
- [[mirrord-execucao-processos-locais-contexto-cluster-kubernetes]] — Referência cruzada direta com mirrord-execucao-processos-locais-contexto-cluster-kubernetes.
- [[mirrord-modos-trafego-mirror-vs-steal-filtragem-http]] — Referência cruzada direta com mirrord-modos-trafego-mirror-vs-steal-filtragem-http.
- [[mirrord-multiplas-sessoes-concorrentes-mirrord-up]] — Referência cruzada direta com mirrord-multiplas-sessoes-concorrentes-mirrord-up.

## Fontes
- [MetalBear mirrord GitHub — README.md (mirrord exec, IDE Extensions, AI Coding Agents, mirrord-layer/agent & Linux Capabilities)](https://raw.githubusercontent.com/metalbear-co/mirrord/main/README.md) — README oficial do mirrord documentando mirrord exec, extensões VS Code e IntelliJ, uso com agentes de IA (Claude Code, Cursor, Codex), mirrord-layer, mirrord-agent e capabilities CAP_NET_ADMIN/CAP_NET_RAW/CAP_SYS_PTRACE/CAP_SYS_ADMIN; consultado em 2026-10-03.
- [MetalBear mirrord Documentation — What is mirrord? (Mirror vs Steal, File/Env Hooking, mirrord up, Operator Teams, CI & Enterprise)](https://metalbear.com/mirrord/docs/getting-started/what-is-mirrord) — Documentação oficial What is mirrord? detalhando espelhamento/roubo de tráfego, interceptação de arquivos e variáveis no processo, mirrord up, Operator for Teams (Queue splitting, DB branching, Traffic filtering) e mirrord for CI/Enterprise; consultado em 2026-10-03.
- [MetalBear mirrord — Official GitHub Repository](https://github.com/metalbear-co/mirrord) — Repositório oficial MIT do MetalBear mirrord; consultado em 2026-10-03.
