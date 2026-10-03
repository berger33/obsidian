---
id: software.testes.tranche24.001813
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

# Reprodução automática: 4 VMs e minimização

## Em uma frase
O contrato de crash do syzkaller, em docs/usage.md: detectado um crash do kernel numa VM, começa automaticamente o processo de reproduzi-lo (a menos que "reproduce": false conste no config); por padrão a ferramenta usa 4 VMs para reproduzir e depois minimiza o programa causador — e isso "may stop the fuzzing, since all of the VMs might be busy reproducing detected crashes".

## Por que importa
Um crash não reproduzível não entra no kernel: a reprodução e a minimização automáticas são o que separa o fuzzador de um gerador de ruído — o relatório chega com um programa mínimo que derruba o kernel previsivelmente.

## Como funciona
Mantenha reproduce habilitado e dimensione o pool de VMs considerando a contenção: com poucas VMs, uma rajada de crashes pausa a descoberta enquanto o retrabalho de reprodução consome o parque; quem precisa de throughput máximo pode desligar a reprodução e tratar os relatórios manualmente.

## Exemplo
Cenário observado: campanha com muitas falhas num kernel experimental para de gerar programa novo porque as 4 VMs de reprodução estão todas ocupadas — comportamento documentado, não bug.

## Limites e trade-offs
A nota usa o default documentado (4 VMs) e o trade-off descrito no parágrafo; tuning fino de reprodução (limites de tempo, retry) vive na página de reproducing crashes e no config.

## Como verificar
Todo o comportamento da seção Crashes de docs/usage.md oficial sustenta a nota.

## Conexões
- [[syzkaller-http-dashboard]] — Veja também: HTTP de serviço: crashes e estatísticas expostos.
- [[syzkaller-repro-forms]] — Veja também: Dois formulários de reproduzor: programa syzkaller ou C.

## Fontes
- [syzkaller — How to use syzkaller (docs/usage.md)](https://raw.githubusercontent.com/google/syzkaller/master/docs/usage.md) — Guia oficial docs/usage.md do syzkaller sobre execução do syz-manager, painel HTTP, reprodução automática em VMs, reproducers C/syzkaller e hub.; consultado em 2026-10-03.
- [syzkaller — README oficial](https://raw.githubusercontent.com/google/syzkaller/master/README.md) — README oficial do syzkaller com definição, sistemas operacionais suportados, mapa da documentação por kernel, found_bugs e badges.; consultado em 2026-10-03.
