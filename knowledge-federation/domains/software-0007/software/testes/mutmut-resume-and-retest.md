---
id: software.testes.tranche21.001522
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-21.md"
fontes: ["https://github.com/boxed/mutmut", "https://github.com/boxed/mutmut/blob/main/README.rst"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# mutmut: interromper, retomar e retestar

## Em uma frase
O mutmut lembra do trabalho já feito, permitindo parar a corrida a qualquer momento e continuar de onde parou, e o browse retesta mutantes depois de você mexer nos testes.

## Por que importa
Rodar a mutação inteira de uma vez trava a máquina; trabalhar por fatias com retomada encaixa o esforço no ritmo normal do time.

## Como funciona
Interrompa com Ctrl-C no meio da corrida, escreva os testes faltantes e retome: o browse mostra os mutantes e retesta na hora.

## Exemplo
Após matar dez sobreviventes, a reexecução só testa o que faltou, não o inventário inteiro de novo.

## Limites e trade-offs
A memória incremental depende do estado local da corrida; limpar o cache força recomeço completo, e CI volátil perde o benefício.

## Como verificar
Pare uma corrida no meio, retome e confirme que o contador prossegue de onde parou.

## Conexões
- [[mutmut-install-first-run]] — Veja também: mutmut: instalar e rodar sem setup.
- [[mutmut-browse-tui]] — Veja também: mutmut: explorar mutantes no browse.

## Fontes
- [mutmut — README oficial](https://github.com/boxed/mutmut) — instalação, browse, configuração e filtros; consultado em 2026-10-03.
- [mutmut — repositório oficial](https://github.com/boxed/mutmut/blob/main/README.rst) — material-fonte do README e das releases; consultado em 2026-10-03.
