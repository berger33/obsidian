---
id: software.testes.tranche24.001817
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

# O mapa da documentação por sistema operacional

## Em uma frase
O README organiza a doc em dois eixos: um núcleo temático — How to install, How to use, How syzkaller works (internals.md), How to install syzbot, How to contribute, How to report Linux kernel bugs, Talks e Research — e um eixo por kernel, com pastas próprias para Darwin/XNU, FreeBSD, Fuchsia, NetBSD, OpenBSD, Starnix, Windows, gVisor e Akaros, anotando que "most of the documentation at this moment is related to the Linux kernel".

## Por que importa
Saber onde cada pergunta tem resposta oficial evita adivinhação: setup por SO mora na pasta do SO, a teoria de operação em internals.md, e a automação de bot (syzbot) tem seu guia próprio de instalação — três perguntas que todo avaliador faz na primeira semana.

## Como funciona
Comece por setup.md e usage.md para Linux; para outro kernel, leia primeiro o README da pasta correspondente; para entender o porquê do design (por que VMs, por que minimização), internals.md é o documento declarado.

## Exemplo
Um time que quer fuzzar NetBSD vai direto a docs/netbsd/setup.md e à found_bugs.md da plataforma, em vez de adaptar prescrições da documentação Linux — a separação por pastas torna isso possível.

## Limites e trade-offs
O próprio README declara o desequilíbrio (maioria da doc sobre Linux); para SOs menos cobertos, o estado de suporte pode estar mais nos fontes e issues do que em guias.

## Como verificar
O índice de links e a nota Linux-first constam da seção Documentation do README oficial.

## Conexões
- [[syzkaller-hub]] — Veja também: Hub: vários syz-managers trocando achados.
- [[syzkaller-bug-reporting]] — Veja também: Onde reportar: found_bugs por SO e o guia Linux.

## Fontes
- [syzkaller — README oficial](https://raw.githubusercontent.com/google/syzkaller/master/README.md) — README oficial do syzkaller com definição, sistemas operacionais suportados, mapa da documentação por kernel, found_bugs e badges.; consultado em 2026-10-03.
- [syzkaller — How to install syzkaller (docs/setup.md)](https://github.com/google/syzkaller/blob/master/docs/setup.md) — Guia oficial de configuração e instalação do syzkaller por sistema operacional.; consultado em 2026-10-03.
