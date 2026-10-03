---
id: software.testes.tranche24.001815
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

# Quanto custa reproduzir: de minutos a uma hora

## Em uma frase
A doc de uso quantifica a espera: "The process of reproducing one crash may take from a few minutes up to an hour depending on whether the crash is easily reproducible or non-reproducible at all" — e admite que como "this process is not perfect", há um caminho de reprodução manual documentado à parte.

## Por que importa
Planejar a infraestrutura de fuzzing de kernel exige dimensionar a contenção: cada crash em retrabalho ocupa VMs por até uma hora, e uma rajada de relatórios numa noite pode consumir o parque inteiro em reprodução em vez de descoberta.

## Como funciona
Ao montar o laboratório, reserve VMs de reprodução além do mínimo de 4 para picos, e trate o intervalo de uma hora como orçamento padrão ao escrever a rotina de triagem (quem espera o quê, com qual timeout de atenção).

## Exemplo
Numa campanha noturna com 8 VMs totais, três crashes difíceis em série podem deixar a descoberta ociosa por uma janela inteira — dimensionar separando pool de fuzz de pool de repro é a mitigação no modelo descrito.

## Limites e trade-offs
O intervalo é a qualificação da doc para o processo padrão; casos degenerados (crash não reprodutível de fato) consomem o teto sem garantia de saída, o que a própria nota "not perfect" admite.

## Como verificar
A frase de timing e a ressalva de imperfeição estão na seção Crashes de docs/usage.md oficial.

## Conexões
- [[syzkaller-repro-forms]] — Veja também: Dois formulários de reproduzor: programa syzkaller ou C.
- [[syzkaller-hub]] — Veja também: Hub: vários syz-managers trocando achados.

## Fontes
- [syzkaller — How to use syzkaller (docs/usage.md)](https://raw.githubusercontent.com/google/syzkaller/master/docs/usage.md) — Guia oficial docs/usage.md do syzkaller sobre execução do syz-manager, painel HTTP, reprodução automática em VMs, reproducers C/syzkaller e hub.; consultado em 2026-10-03.
- [syzkaller — README oficial](https://raw.githubusercontent.com/google/syzkaller/master/README.md) — README oficial do syzkaller com definição, sistemas operacionais suportados, mapa da documentação por kernel, found_bugs e badges.; consultado em 2026-10-03.
