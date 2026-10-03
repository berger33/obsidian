---
id: software.seguranca.tranche08.000774
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-08.md"
fontes: ["https://raw.githubusercontent.com/robertdavidgraham/masscan/master/README.md", "https://raw.githubusercontent.com/robertdavidgraham/masscan/master/doc/masscan.8.markdown", "https://github.com/robertdavidgraham/masscan"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Masscan: Arquivos de Configuração (`-c`), Pausa e Retomada Exata (**`paused.conf` / `--resume`**) e Distribuição em Cluster (**`--shards`**)

## Em uma frase
Durante uma varredura de longa duração sobre milhões de endereços IP e dezenas de portas, se o operador pressionar **`Ctrl+C`**, o Masscan **não perde o trabalho já realizado**: ele salva instantaneamente o estado exato do índice da cifra Feistel BlackRock, a semente (`seed`) e todos os parâmetros da varredura no arquivo **`paused.conf`**!

## Por que importa
Para retomar a varredura exatamente do pacote onde ela foi interrompida horas ou dias depois, basta executar **`sudo masscan --resume paused.conf`**!

## Como funciona
Além disso, passar **`--echo`** ao final de qualquer comando do Masscan faz a ferramenta imprimir na tela um arquivo de configuração limpo e estruturado (sem executar o scan), que pode ser salvo em `scan.conf`, versionado em Git e executado com **`sudo masscan -c scan.conf`**, ou dividido entre $M$ máquinas trabalhadoras usando **`--shards 1/4`**, **`--shards 2/4`**, etc.!

## Exemplo
```bash
# Exportar os parametros de linha de comando para um arquivo de configuracao reutilizavel (--echo) e dividir em 4 shards
masscan 10.0.0.0/8 -p80,443,8080,8443 --rate 10000 --excludefile /cases/easm/exclude_critical.txt --shards 1/4 --echo > /cases/easm/shard1.conf
```

## Limites e trade-offs
Quando distribuir uma varredura entre múltiplas máquinas usando **`--shards <x>/<total>`** (ex.: `1/4`, `2/4`, `3/4`, `4/4`), garanta que todos os nós compartilhem a **mesma `--seed <inteiro>`** na configuração: assim, a bijeção matemática BlackRock particiona o espaço de busca sem que dois nós enviem pacotes para o mesmo par `(IP, porta)`!

## Como verificar
Teste interromper uma varredura de laboratório com `Ctrl+C`, inspecione o campo `resume-index` dentro de `paused.conf` e retome com `masscan --resume paused.conf`.

## Conexões
- [[masscan-controle-taxa-rate-pf-ring-excludefile-protecao-rede]] — Veja também: Masscan: Dimensionamento de Taxa (`--rate`), Exclusão Obrigatória de Sub-redes Críticas (**`--excludefile`**) e Aceleração **`PF_RING` DNA**.
- [[masscan-formatos-saida-binaria-ob-readscan-conversao-ox-oj-ol-og]] — Veja também: Masscan: Gravação em Formato Binário Nativo (**`-oB`**) e Conversão Offline Instantânea (**`--readscan`**) para XML Nmap (`-oX`), JSON (`-oJ`), Grepable (`-oG`) e List (`-oL`).
- [[masscan-arquitetura-assincrona-pilha-tcp-ip-userspace-blackrock-syn-cookies]] — Referência cruzada direta com masscan-arquitetura-assincrona-pilha-tcp-ip-userspace-blackrock-syn-cookies.
- [[zmap-boas-praticas-varredura-etica-sinalizacao-rdns-opt-out-shards]] — Referência cruzada direta com zmap-boas-praticas-varredura-etica-sinalizacao-rdns-opt-out-shards.

## Fontes
- [Masscan Official GitHub — Mass IP Port Scanner Architecture & Banner Checking](https://raw.githubusercontent.com/robertdavidgraham/masscan/master/README.md) — documentação oficial do Masscan cobrindo transmissão assíncrona, cifra BlackRock, captura de banners, prevenção de TCP RST e PF_RING; consultado em 2026-10-03.
- [Masscan Official Manual Page — masscan(8) Complete CLI & Configuration Reference](https://raw.githubusercontent.com/robertdavidgraham/masscan/master/doc/masscan.8.markdown) — manual oficial masscan(8) cobrindo taxas, excludefile, paused.conf, shards, formatos binários/JSON/XML e payloads UDP/HTTP; consultado em 2026-10-03.
- [Masscan Project Repository — robertdavidgraham/masscan](https://github.com/robertdavidgraham/masscan) — repositório oficial do código-fonte do Masscan; consultado em 2026-10-03.
