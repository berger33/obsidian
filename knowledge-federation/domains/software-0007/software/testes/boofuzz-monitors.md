---
id: software.testes.tranche23.001727
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-23.md"
fontes: ["https://github.com/jtpereyda/boofuzz/blob/master/README.rst", "https://github.com/jtpereyda/boofuzz"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Monitores fora do processo: os scripts de processo e rede no root

## Em uma frase
O repositório oficial carrega os monitores como arquivos de topo nomeados: process_monitor.py e process_monitor_unix.py (watchdog de processo-alvo, com variante unix) e network_monitor.py — correspondendo ao par de capacidades que o README lista como elementos críticos de um fuzzer: "Instrumentation – AKA failure detection" e "Target reset after failure".

## Por que importa
Monitorar o alvo de fora é o modelo para serviços que somem quando crasham: o processo monitor detecta a morte e permite o reset; o network monitor cobre o caso em que o crash não mata o host inteiro mas some com a conectividade — o design do boofuzz trata detecção como extensão (frase "Extensible instrumentation/failure detection" no README).

## Como funciona
Os scripts vivem no root do repositório, passados à Session como objetos de monitor (a classe base citada é ITargetConnection para conexão; os monitores entram como observadores independentes), e a existência dos três arquivos é verificável na árvore pública sem instalar nada.

## Exemplo
Liste a raiz do repositório no GitHub e abra os três arquivos citados; confirme que são standalone (docstring no topo) — é o ponto de partida para passá-los a uma Session customizada.

## Limites e trade-offs
Os nomes de arquivo são âncoras verificáveis; a receita completa de integração (parâmetros, loop de restart, ssh) mora nos exemplos do repositório — a página de quickstart consultada não documenta os monitores em si, e a doc do readthedocs tem página de instrumentation que a versão estável não resolve (404 no snapshot atual), o que pede cuidado extra ao citar.

## Como verificar
Confirme na página do repositório os três nomes de monitor no tree raiz e os bullets de instrumentation e target reset na seção Features do README.rst.

## Conexões
- [[boofuzz-callbacks]] — Veja também: post_test_case_callbacks e ProtocolSessionReference: resposta que alimenta a próxima requisição.
- [[boofuzz-install-python]] — Veja também: Instalação por pip e o modelo de script Python.

## Fontes
- [boofuzz — README.rst oficial](https://github.com/jtpereyda/boofuzz/blob/master/README.rst) — sucessão ao Sulley, features, instalação e comunidade; consultado em 2026-10-03.
- [boofuzz — repositório oficial](https://github.com/jtpereyda/boofuzz) — árvore do repositório com monitores, examples e request_definitions; consultado em 2026-10-03.
