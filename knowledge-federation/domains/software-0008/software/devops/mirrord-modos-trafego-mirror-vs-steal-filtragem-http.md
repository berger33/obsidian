---
id: software.devops.tranche09.000893
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

# MetalBear mirrord: modos de tráfego de entrada (mirror padrão vs steal) e roteamento de saída pelo pod remoto

## Em uma frase
Para o tráfego de entrada (`incoming`), o `mirrord` suporta dois modos — **mirror** (espelha uma cópia das requisições sem afetar o pod remoto) e **steal** (intercepta as requisições fazendo o processo local responder aos clientes do cluster) — enquanto o tráfego de saída (`outgoing`) e o DNS passam transparentemente pelo pod alvo.

## Por que importa
Quando um desenvolvedor começa a testar seu código local contra um cluster compartilhado, o comportamento mais seguro por padrão é **espelhar (`mirror`)** o tráfego de entrada: o código local recebe as requisições reais para teste, mas o pod remoto continua respondendo normalmente aos clientes sem risco de quebrar o ambiente. Quando o desenvolvedor precisa que a resposta do seu código local seja devolvida ao chamador no cluster, ele ativa o modo **`steal`**.

## Como funciona
Na configuração de rede (`feature.network`) do `mirrord`: (1) **Incoming `mirror` (padrão no OSS)**: o `mirrord-agent` captura os pacotes TCP/HTTP que chegam à porta escutada pelo pod alvo e envia uma cópia para a `mirrord-layer` na máquina local, descartando a resposta gerada localmente; (2) **Incoming `steal` (`--steal` ou `"mode": "steal"` no arquivo `.mirrord/mirrord.json`)**: o `mirrord-agent` redireciona a conexão de entrada para o processo local e devolve a resposta do processo local para o cliente no cluster (suportando também `http_filter` por header, path ou método para roubar apenas requisições específicas); e (3) **Outgoing (`TCP` e `UDP`) + DNS**: todas as conexões abertas pelo processo local saem de dentro do namespace de rede do pod alvo no cluster.

## Exemplo
```json
{
  "target": "deployment/orders-service",
  "feature": {
    "network": {
      "incoming": {
        "mode": "steal",
        "http_filter": {
          "header_filter": "x-developer: alice"
        }
      },
      "outgoing": true
    }
  }
}
```

## Limites e trade-offs
Assim como em qualquer ferramenta de espelhamento de tráfego, quando você roda em modo **`mirror`** com `outgoing: true`, o seu processo local recebe uma cópia da requisição que o pod remoto **também** está processando; se aquela requisição fizer um `INSERT` no banco de dados do cluster ou cobrar um cartão de crédito, a operação de saída será executada duas vezes (uma pelo pod remoto e outra pelo seu processo local), sendo recomendável usar `steal` com `http_filter` (ou DB branching) para rotas mutantes.

## Como verificar
Execute `mirrord exec --steal -f .mirrord/mirrord.json -- go run ./cmd/server` e envie uma requisição com o header `x-developer: alice` ao serviço no cluster, confirmando que a resposta recebida veio do seu código local.

## Conexões
- [[mirrord-arquitetura-mirrord-layer-mirrord-agent-capabilities]] — Veja também: MetalBear mirrord: arquitetura mirrord-layer e mirrord-agent e gerenciamento de Linux Capabilities.
- [[mirrord-interceptacao-sistema-arquivos-variaveis-ambiente-libc]] — Veja também: MetalBear mirrord: interceptação de leituras/escritas de arquivos e variáveis de ambiente sem montar volumes no host.
- [[mirrord-execucao-processos-locais-contexto-cluster-kubernetes]] — Referência cruzada direta com mirrord-execucao-processos-locais-contexto-cluster-kubernetes.
- [[telepresence-modos-nao-intrusivos-wiretap-ingest-producao-staging]] — Referência cruzada direta com telepresence-modos-nao-intrusivos-wiretap-ingest-producao-staging.

## Fontes
- [MetalBear mirrord GitHub — README.md (mirrord exec, IDE Extensions, AI Coding Agents, mirrord-layer/agent & Linux Capabilities)](https://raw.githubusercontent.com/metalbear-co/mirrord/main/README.md) — README oficial do mirrord documentando mirrord exec, extensões VS Code e IntelliJ, uso com agentes de IA (Claude Code, Cursor, Codex), mirrord-layer, mirrord-agent e capabilities CAP_NET_ADMIN/CAP_NET_RAW/CAP_SYS_PTRACE/CAP_SYS_ADMIN; consultado em 2026-10-03.
- [MetalBear mirrord Documentation — What is mirrord? (Mirror vs Steal, File/Env Hooking, mirrord up, Operator Teams, CI & Enterprise)](https://metalbear.com/mirrord/docs/getting-started/what-is-mirrord) — Documentação oficial What is mirrord? detalhando espelhamento/roubo de tráfego, interceptação de arquivos e variáveis no processo, mirrord up, Operator for Teams (Queue splitting, DB branching, Traffic filtering) e mirrord for CI/Enterprise; consultado em 2026-10-03.
- [MetalBear mirrord — Official GitHub Repository](https://github.com/metalbear-co/mirrord) — Repositório oficial MIT do MetalBear mirrord; consultado em 2026-10-03.
