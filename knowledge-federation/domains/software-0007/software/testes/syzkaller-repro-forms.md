---
id: software.testes.tranche24.001814
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
fontes: ["https://raw.githubusercontent.com/google/syzkaller/master/docs/usage.md", "https://raw.githubusercontent.com/google/syzkaller/master/README.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Dois formulários de reproduzor: programa syzkaller ou C

## Em uma frase
Quando a reprodução tem sucesso, o programa pode ser gerado "in one of the two forms: syzkaller program or C program"; a ferramenta "always tries to generate a more user-friendly C reproducer", mas "sometimes fails for various reasons (for example slightly different timings)", e nesse caso existe caminho para executar o programa syzkaller manualmente a fim de reproduzir e debugar o crash (docs/reproducing_crashes.md).

## Por que importa
A dupla forma reflete dois públicos: o mantenedor de kernel quer um .c autocontido para colar no report, e o caçador do bug quer o programa de syscalls da ferramenta — mais fiel à geração e debugável com as opções próprias de execução.

## Como funciona
Recebido um report sem C reproducer, rode o programa syzkaller pela via manual documentada antes de assumir não-reprodutibilidade; a diferença de timings citada é razão listada para o gerador de C ter falhado, não para o bug ter sumido.

## Exemplo
Fluxo real de laboratório: syzkaller program reproduz o KMSAN report de forma confiável; a tentativa de C reproducer falhou por timing — o programa nativo continua o caminho do debug.

## Limites e trade-offs
A doc de uso descreve o comportamento e os exemplos de motivo; o formato exato do programa syzkaller (syscall description language) não está no trecho lido — o documento de uso de programas vive em outro arquivo da pasta docs.

## Como verificar
A seção Crashes de docs/usage.md oficial define os dois formulários e a preferência declarada.

## Conexões
- [[syzkaller-auto-repro]] — Veja também: Reprodução automática: 4 VMs e minimização.
- [[syzkaller-repro-timing]] — Veja também: Quanto custa reproduzir: de minutos a uma hora.

## Fontes
- [syzkaller — How to use syzkaller (docs/usage.md)](https://raw.githubusercontent.com/google/syzkaller/master/docs/usage.md) — Guia oficial docs/usage.md do syzkaller sobre execução do syz-manager, painel HTTP, reprodução automática em VMs, reproducers C/syzkaller e hub.; consultado em 2026-10-03.
- [syzkaller — README oficial](https://raw.githubusercontent.com/google/syzkaller/master/README.md) — README oficial do syzkaller com definição, sistemas operacionais suportados, mapa da documentação por kernel, found_bugs e badges.; consultado em 2026-10-03.
