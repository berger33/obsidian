---
id: software.testes.tranche21.001525
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

# mutmut: requisito de fork e plataformas

## Em uma frase
O mutmut exige suporte a fork no sistema operacional, o que na prática significa rodar no Windows dentro do WSL.

## Por que importa
A arquitetura de teste por processo filho vem da velocidade: copiar via fork barateia o processo-por-mutante que o mutmut usa.

## Como funciona
Planeje a máquina de execução sabendo disso: Linux e macOS nativos, Windows via WSL, contêiner de CI padrão.

## Exemplo
Um job de CI em runner Linux roda a mutação sem nenhuma adaptação adicional.

## Limites e trade-offs
WSL adiciona latência de sistema de arquivos se o projeto residir fora do sistema de arquivos Linux, multiplicando o custo por mutante.

## Como verificar
Rode a mesma corrida dentro e fora do ambiente esperado e confirme o comportamento consistente do runner de mutantes.

## Conexões
- [[mutmut-apply-mutant]] — Veja também: mutmut: aplicar o mutante no disco.
- [[mutmut-config-paths]] — Veja também: mutmut: configuração em setup.cfg ou pyproject.

## Fontes
- [mutmut — README oficial](https://github.com/boxed/mutmut) — instalação, browse, configuração e filtros; consultado em 2026-10-03.
- [mutmut — repositório oficial](https://github.com/boxed/mutmut/blob/main/README.rst) — material-fonte do README e das releases; consultado em 2026-10-03.
