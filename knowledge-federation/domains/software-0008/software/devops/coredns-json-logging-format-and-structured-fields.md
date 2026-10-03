---
id: software.devops.tranche03.000287
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-03.md"
fontes: ["https://raw.githubusercontent.com/coredns/coredns/master/README.md", "https://github.com/coredns/coredns"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Logging operacional estruturado em JSON com -log-format=json e campos time, level, msg e plugin

## Em uma frase
A subseção `JSON Logging` em `Examples` do README explica que iniciar o CoreDNS com `./coredns -conf Corefile -log-format=json` faz o processo emitir logs operacionais como JSON de linha única (enquanto o padrão `-log-format=text` mantém a saída textual): o formato aplica-se a todo o processo, persiste através de recargas do `Corefile` e gera registros contendo `time` (RFC3339 com frações de segundo), `level` (`DEBUG`, `INFO`, `WARN`, `ERROR` ou `FATAL`), `msg` e, para loggers de plugins nomeados, o campo `plugin`.

## Por que importa
Quando coletores como Grafana Alloy, Fluent Bit ou Vector ingerem logs do CoreDNS para enviá-los ao Loki, fazer parsing de texto livre com quebras de linha embutidas e escapes DNS é frágil; usar `-log-format=json` garante codificação JSON segura e campos tipados sem precisar de expressões regulares complexas.

## Como funciona
Adicione a flag `-log-format=json` ao comando de inicialização do CoreDNS em ambientes integrados a pipelines de observabilidade estruturada (como Loki, Fluent Bit ou Vector) e consulte `plugin/log/README.md#json-output` para campos tipados de consultas.

## Exemplo
O DaemonSet do Fluent Bit coleta os logs em JSON de linha única do CoreDNS e indexa automaticamente por nível de severidade (`WARN`, `ERROR`) no Grafana Loki.

## Limites e trade-offs
O README esclarece que o logging de consultas ainda exige habilitar o plugin `log`, a saída de debug exige o plugin `debug`, e que loggers de terceiros configurados independentemente, escritas diretas em stdout/stderr, diagnósticos do runtime Go e flags de ajuda (`-version`, `-plugins`) não são interceptados pelo formato JSON.

## Como verificar
Conferi a subseção JSON Logging no README oficial de coredns/coredns.

## Conexões
- [[coredns-source-and-docker-compilation-coredns-plugins-env]] — Veja também: Compilação a partir do código-fonte (Go 1.26.0+), variável COREDNS_PLUGINS e build via Docker.
- [[coredns-default-whoami-behavior-and-dns-port-override]] — Veja também: Comportamento padrão sem Corefile (plugins whoami e log na porta 53) e substituição com -dns.port.

## Fontes
- [CoreDNS — GitHub README](https://raw.githubusercontent.com/coredns/coredns/master/README.md) — Visão geral do CoreDNS (servidor DNS em Go graduado na CNCF baseado em cadeia de plugins, protocolos UDP/TCP/DoT/DoH/DoH3/DoQ/gRPC, 18 capacidades/plugins, compilação com COREDNS_PLUGINS, -log-format=json e regras do Corefile).; consultado em 2026-10-03.
- [CoreDNS — Repositório Oficial no GitHub](https://github.com/coredns/coredns) — Repositório oficial do CoreDNS na CNCF com código-fonte Go, plugin.cfg e documentação por plugin.; consultado em 2026-10-03.
