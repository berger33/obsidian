---
id: software.testes.tranche24.001818
tipo: tecnica
dominio: software
subdominio: testes
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-24.md"
fontes: ["https://raw.githubusercontent.com/google/syzkaller/master/README.md", "https://github.com/google/syzkaller/blob/master/docs/setup.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Onde reportar: found_bugs por SO e o guia Linux

## Em uma frase
O README mantém a política de reporte e o histórico lado a lado: cada plataforma com suporte tem seu documento "Found bugs" (Darwin/XNU, FreeBSD, NetBSD, OpenBSD, Windows, além do Linux com found_bugs.md na pasta própria) e há uma página dedicada para "How to report Linux kernel bugs" (docs/linux/reporting_kernel_bugs.md); a lista de discussão oficial é syzkaller@googlegroups.com.

## Por que importa
Em kernel, a forma de reportar é parte do efeito: um crash sem o protocolo pedido pelo maintainers do alvo vira issue fechada; a doc de reporte linkada pelo próprio fuzzer codifica o formato que a comunidade do kernel aceita — e os found_bugs por SO mostram o que já foi reportado, evitando duplicata.

## Como funciona
Antes de reportar, siga o documento de reporting da sua plataforma (o Linux tem guia próprio); para triagem de "já conhecido?", consulte o found_bugs.md da pasta do SO — ambos linkados na página do README.

## Exemplo
O report de um bug de NetBSD segue a trilha da pasta netbsd/; o de Linux inclui a checklist da doc oficial — reproduzor em C, config do kernel e relatórios KMSAN/lockdep conforme o guia do projeto.

## Limites e trade-offs
A nota descreve a existência e o destino das políticas; o conteúdo detalhado de cada guia de reporte (tags, listas de discussão do kernel-alvo) deve ser lido no documento próprio, que pode mudar sem tocar o README.

## Como verificar
A lista de links found-bugs, a linha de reporting e a mailing list constam da abertura do README oficial.

## Conexões
- [[syzkaller-docs-map]] — Veja também: O mapa da documentação por sistema operacional.
- [[syzkaller-disclaimer-status]] — Veja também: Badges públicos e o disclaimer de que não é produto Google.

## Fontes
- [syzkaller — README oficial](https://raw.githubusercontent.com/google/syzkaller/master/README.md) — README oficial do syzkaller com definição, sistemas operacionais suportados, mapa da documentação por kernel, found_bugs e badges.; consultado em 2026-10-03.
- [syzkaller — How to install syzkaller (docs/setup.md)](https://github.com/google/syzkaller/blob/master/docs/setup.md) — Guia oficial de configuração e instalação do syzkaller por sistema operacional.; consultado em 2026-10-03.
